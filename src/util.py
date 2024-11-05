from subprocess import Popen, PIPE
from json import JSONEncoder
from functools import cache
from pathlib import Path
from typing import List

import json

from schema import Document


@cache
def get_project_root() -> Path:
    stdout = Popen(['git', 'rev-parse', '--show-toplevel'], stdout=PIPE).communicate()
    return Path(stdout[0].rstrip().decode('utf-8'))


@cache
def avgDocLen(zone, weight):
    files = json.loads(open(get_project_root().joinpath('data/docs.json')).read())

    l = 0
    c = 0
    for s in files.keys():
        for d in files[s]:
            l += len(d[zone]) * weight
            c += 1

    return l/c


@cache
def numDocs():
    files = json.loads(open(get_project_root().joinpath('data/docs.json')).read())

    c = 0
    for s in files.keys():
        for d in files[s]:
            c += 1

    return c

class Serialize(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Document):
            return {attr: getattr(obj, attr) for attr in obj.__slots__}
        if isinstance(obj, Path):
            return str(obj)
        return super().default(obj)
