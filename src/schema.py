from dataclasses import dataclass
from typing import List, Dict
from pathlib import Path
from enum import Enum

from util import get_project_root


filetypes: List[str] = [
    '^.*\.md$'
]


blacklist: List[str] = [
    'LICENSE',
    'LICENSE.md',
    'SUMMARY.md'
]


class Sources(Enum):
    exploit_notes: Dict = {
        'url': 'https://exploit-notes.hdks.org/', 
        'dat': get_project_root().joinpath('data/raw/pwn-notes/'),
    }
    hacktricks: Dict[str, Path] = {
        'url': 'https://book.hacktricks.xyz/', 
        'dat': get_project_root().joinpath('data/raw/hacktricks/'),
    }
    hacktricks_cloud: Dict[str, Path] = {
        'url': 'https://cloud.hacktricks.xyz/', 
        'dat': get_project_root().joinpath('data/raw/hacktricks-cloud/'),
    }
    heap_exploitation: Dict[str, Path] = {
        'url': 'https://heap-exploitation.dhavalkapil.com/',
        'dat': get_project_root().joinpath('data/raw/heap-exploitation/'),
    }
    payloadallthethings: Dict[str, Path] = {
        'url': 'https://swisskyrepo.github.io/PayloadsAllTheThings/',
        'dat': get_project_root().joinpath('data/raw/PayloadsAllTheThings/'),
    }
    pwn_notes: Dict[str, Path] = {
        'url': 'https://ir0nstone.gitbook.io/',
        'dat': get_project_root().joinpath('data/raw/pwn-notes/'),
    }


@dataclass(kw_only=True, slots=True)
class Document:
    src: Sources
    title: str
    description: str
    tags: List[str]
    body: str
