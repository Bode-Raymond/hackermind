from wordcloud import WordCloud
from nltk import download

import json
import sys

from sources import SourceNames, Sources
from util import Serialize, get_project_root
from bm25 import BM25F


_sources = Sources()


def parse_data():
    docs = {source: None for source in _sources.__slots__}
    for source in _sources.__slots__:
        docs[source] = getattr(_sources, source)['parser'].parse(getattr(_sources, source))

    with open(get_project_root().joinpath('data/docs.json'), 'w') as f:
        f.write(json.dumps(docs, cls=Serialize))


def analyze_data():
    import numpy as np
    import matplotlib.pyplot as plt

    with open(get_project_root().joinpath('data/docs.json'), 'r') as f:
        docs = json.loads(f.read())

    dcs = {getattr(SourceNames, source).value: None for source in docs.keys()}
    for source in docs.keys():
        dcs[getattr(SourceNames, source).value] = len(docs[source])

    print(f"Total documents: {sum(dcs.values())}")
    print(f"Document counts: {dcs}")

    x = list(dcs.keys())
    y = list(dcs.values())

    f1 = plt.figure(1)
    plt.bar(x, y, color='maroon')
    plt.xlabel('Sources')
    plt.ylabel('# of Documents')
    plt.title('Number of Documents by Source')
    plt.xticks(rotation=15, ha='right')
    plt.tight_layout()
    plt.savefig(get_project_root().joinpath('static/docs_by_category.png'))


    avdls = {}
    for source in docs.keys():
        tdl = 0
        for doc in docs[source]:
            tdl += len(doc['body'])

        avdls[getattr(SourceNames, source).value] = tdl / dcs[getattr(SourceNames, source).value]

    print(f"Average document lengths: {avdls}")

    x = list(avdls.keys())
    y = list(avdls.values())

    f2 = plt.figure(2)
    plt.bar(x, y, color='maroon')
    plt.xlabel('Source')
    plt.ylabel('Avg. Document Length')
    plt.title('Average Document Length by Source')
    plt.xticks(rotation=15, ha='right')
    plt.tight_layout()
    plt.savefig(get_project_root().joinpath('static/avg_doc_len_by_source.png'))


def score():
    qs = open(get_project_root().joinpath('data/queries.txt')).read().strip().split('\n')
    ds = json.loads(open(get_project_root().joinpath('data/docs.json')).read())

    scorer = BM25F()
    for q in qs:
        docscores = {}
        for s in ds.keys():
            for d in ds[s]:
                tfs = scorer.getDocTermFreq(d, q.split())
                ntf = scorer.normalizeTFs(tfs, d, q.split())
                score = scorer.score(ntf, d, q.split())
                docscores[d['src']['url']] = score
        docscores = {k: v for k, v in sorted(docscores.items(), key=lambda item: item[1])}

        print(f'================ Query: {q} ================')
        for i in list(docscores.keys())[-5::][::-1]:
            print(docscores[i], i)
        print(f'========================={"="*len(q)}================\n\n')

"""
def create_train_data():
    qs = open(get_project_root().joinpath('data/queries.txt')).read().strip().split('\n')
    ds = json.loads(open(get_project_root().joinpath('data/docs.json')).read())

    train = {'training': []}
    for q in qs:
        q = q.split()
        matching = {'query': q, 'docs': []}
        for s in ds:
            for d in ds[s]:
                doc = {
                    'url': d['url'], 
                    'title': d['title'],
                    'title_len': len(d['title'])
                    'description': d['description'],
                    'description_len': len(d['description']),
                    'tags': len(d['tags'])
                }

        train['training'].append(matching)
"""


if __name__ == '__main__':
    download('punkt_tab')
    download('punkt')

    if len(sys.argv) > 1:
        if sys.argv[1] == 'parse':
            parse_data()
            exit()
        if sys.argv[1] == 'analyze':
            analyze_data()
            exit()
        if sys.argv[1] == 'bm25':
            score()
            exit()
        """
        if sys.argv[1] == 'gentrain':
            create_train_data()
            exit()
        """
