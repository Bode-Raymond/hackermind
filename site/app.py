from flask import Flask, render_template, request
from urllib.parse import urljoin
from os.path import splitext
from pathlib import Path

import mistletoe
import re

from util import get_docs, ReadmeParser
from schema import Sources
from bm25.bm25 import BM25F


app = Flask(__name__)
app.config.from_object('config.Config')
app.config['_sources'] = Sources()
app.config['rp'] = ReadmeParser()


@app.route('/', methods=['GET'])
def index():
    return render_template('search.html')


@app.route('/', methods=['POST'])
def search():
    q = request.form['query']
    ds = get_docs()

    docscores = {}
    for s in ds.keys():
        for d in ds[s]:
            tfs = BM25F.getDocTermFreq(d, q.split())
            ntf = BM25F.normalizeTFs(tfs, d, q.split())

            score = BM25F.score(ntf, d, q.split())
            docscores[d['src']['dat']] = score

    docscores = {k: v for k, v in sorted(docscores.items(), key=lambda item: item[1])}

    results = {}

    for src in list(docscores.keys())[-10::][::-1]:
        if docscores[src] == 0:
            break

        results[src] = {}

    for src in ds.keys():
        for d in ds[src]:
            if d['src']['dat'] in list(results.keys()):
                print(d['src']['dat'])
                results[d['src']['dat']]['source'] = getattr(app.config['_sources'], src)['name']
                results[d['src']['dat']]['url'] = urljoin(
                    getattr(app.config['_sources'], src)['url'], 
                    str(splitext(Path(d['src']['dat']).relative_to(getattr(app.config['_sources'], src)['dat']))[0]).replace('README', ''))
                results[d['src']['dat']]['base'] = getattr(app.config['_sources'], src)['url']
                results[d['src']['dat']]['page'] = results[d['src']['dat']]['url'].rstrip('/').split('/')[-1]
                results[d['src']['dat']]['favicon'] = getattr(app.config['_sources'], src)['favicon']

                html = mistletoe.markdown(Path(d['src']['dat']).read_text())
                app.config['rp'].feed(html.replace("\n", ""))
                app.config['rp'].parse()
                results[d['src']['dat']]['description'] = re.sub(r'\{%[^%]*%\}', '', re.sub(r'<[^>]*>', '', app.config['rp'].data[0]))

    print(list(results.values()))

    return render_template('search.html', query=q, results=list(results.values()))


if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'])
