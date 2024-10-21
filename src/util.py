from subprocess import Popen, PIPE
from functools import cache
from pathlib import Path
from typing import List

from schema import Document

import json


@cache
def get_project_root() -> Path:
    stdout = Popen(['git', 'rev-parse', '--show-toplevel'], stdout=PIPE).communicate()
    return Path(stdout[0].rstrip().decode('utf-8'))


class Serialize(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Document):
            return {attr: getattr(obj, attr) for attr in obj.__slots__}
        if isinstance(obj, Path):
            return str(obj)
        return super().default(obj)
