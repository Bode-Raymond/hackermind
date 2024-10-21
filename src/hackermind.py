from nltk import download

import json
import sys

from sources import Sources
from util import Serialize, get_project_root


_sources = Sources()


def parse_data():
    docs = {source: None for source in _sources.__slots__}
    for source in _sources.__slots__:
        docs[source] = getattr(_sources, source)['parser'].parse(getattr(_sources, source))

    with open(get_project_root().joinpath('data/docs.json'), 'w') as f:
        f.write(json.dumps(docs, cls=Serialize))


def analyze_data():
    pass


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
