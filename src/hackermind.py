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

    ### Documents by source
    x = list(dcs.keys())
    y = list(dcs.values())

    f1 = plt.figure(1)
    plt.bar(x, y, color='#f44088')
    plt.xlabel('Sources')
    plt.ylabel('# of Documents')
    plt.title('Number of Documents by Source')
    plt.xticks(rotation=15, ha='right')
    plt.tight_layout()
    plt.savefig(get_project_root().joinpath('static/docs_by_source.png'))
    ###


    ### Average document length by source
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
    plt.bar(x, y, color='#f44088')
    plt.xlabel('Source')
    plt.ylabel('Avg. Document Length')
    plt.title('Average Document Length by Source')
    plt.xticks(rotation=15, ha='right')
    plt.tight_layout()
    plt.savefig(get_project_root().joinpath('static/avg_doc_len_by_source.png'))
    ###

    ### All documents by length histogram
    #dls = {f'{i-200}-{i}': 0 for i in range(200, 12000, 200)}
    values = []
    for source in docs.keys():
        for doc in docs[source]:
            values.append(len(doc['body']))
            #nlen = int(len(doc['body']) / 200) * 200
            #dls[f'{nlen}-{nlen+200}'] = dls.get(f'{nlen}-{nlen+200}', 0) + 1

    f3 = plt.figure(3)
    #plt.bar(list(dls.keys()), list(dls.values()), color='maroon', width=0.7)
    plt.hist(values, 250, color='#00a8f7')
    plt.xlabel('Document Length')
    plt.ylabel('Document Count')
    plt.title('Documents by Length')
    #plt.xticks(rotation=90, ha='right')
    plt.tight_layout()
    plt.savefig(get_project_root().joinpath('static/docs_by_len.png'))
    ###

    ### All doc length histogram by source
    values = []
    sources = [getattr(SourceNames, s).value for s in list(docs.keys())]
    for source in docs.keys():
        values.append([])
        for doc in docs[source]:
            values[-1].append(len(doc['body']))

    f4 = plt.figure(4)
    plt.hist(values, 250, stacked=True, color=['#ffc725', '#fa8b57', '#f44088', '#00f0f7', '#00d3f6', '#00a8f7'])
    plt.legend(sources)
    plt.xlabel('Document Length')
    plt.ylabel('Document Count')
    plt.title('Document Lengths by Source')
    plt.tight_layout()
    plt.savefig(get_project_root().joinpath('static/source_docs_by_len.png'))
    ###


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
        for i in list(docscores.keys())[-10::][::-1]:
            print(docscores[i], i)
        print(f'========================={"="*len(q)}================\n\n')


def main():
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


if __name__ == '__main__':
    main()
