from wordcloud import WordCloud
from nltk import download

import json
import sys

from sources import SourceNames, Sources
from util import Serialize, get_project_root


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
