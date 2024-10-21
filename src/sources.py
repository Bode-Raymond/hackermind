from dataclasses import dataclass, field
from typing import Dict, Any
from pathlib import Path

from util import get_project_root
from parsers import parsers


@dataclass(frozen=True, slots=True)
class Sources():
    exploit_notes: Dict[str, str | Path | Any] = field(default_factory=lambda: {
        'url': 'https://exploit-notes.hdks.org/', 
        'dat': get_project_root().joinpath('data/raw/exploit-notes/src/'),
        'parser': parsers['exploit_notes']
    })
    hacktricks: Dict[str, str | Path | Any] = field(default_factory=lambda: {
        'url': 'https://book.hacktricks.xyz/', 
        'dat': get_project_root().joinpath('data/raw/hacktricks/'),
        'parser': parsers['hacktricks']
    })
    hacktricks_cloud: Dict[str, str | Path | Any] = field(default_factory=lambda: {
        'url': 'https://cloud.hacktricks.xyz/', 
        'dat': get_project_root().joinpath('data/raw/hacktricks-cloud/'),
        'parser': parsers['hacktricks']
    })
    heap_exploitation: Dict[str, str | Path | Any] = field(default_factory=lambda: {
        'url': 'https://heap-exploitation.dhavalkapil.com/',
        'dat': get_project_root().joinpath('data/raw/heap-exploitation/'),
        'parser': parsers['hacktricks']
    })
    payloadallthethings: Dict[str, str | Path | Any] = field(default_factory=lambda: {
        'url': 'https://swisskyrepo.github.io/PayloadsAllTheThings/',
        'dat': get_project_root().joinpath('data/raw/PayloadsAllTheThings/'),
        'parser': parsers['hacktricks']
    })
    pwn_notes: Dict[str, str | Path | Any] = field(default_factory=lambda: {
        'url': 'https://ir0nstone.gitbook.io/',
        'dat': get_project_root().joinpath('data/raw/pwn-notes/'),
        'parser': parsers['hacktricks']
    })
