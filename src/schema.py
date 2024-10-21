from dataclasses import dataclass
from typing import List, Dict
from pathlib import Path


filetypes: List[str] = [
    r'^.*\.md$'
]


blacklist: List[str] = [
    'data/raw/heap-exploitation/SUMMARY.md',
    'data/raw/heap-exploitation/README.md',
    'data/raw/heap-exploitation/CONTRIBUTING.md',
    'data/raw/heap-exploitation/author.md',
    'data/raw/heap-exploitation/introduction.md',
    'data/raw/heap-exploitation/secure_coding_guidelines.md',
    'data/raw/hacktricks-cloud/README.md',
    'data/raw/hacktricks-cloud/SUMMARY.md',
    'data/raw/hacktricks/SUMMARY.md',
    'data/raw/hacktricks/LICENSE.md',
    'data/raw/pwn-notes/LICENSE.md',
    'data/raw/pwn-notes/SUMMARY.md',
    'data/raw/pwn-notes/README.md',
    'data/raw/PayloadsAllTheThings/CONTRIBUTING.md',
    'data/raw/PayloadsAllTheThings/README.md',
    'data/raw/PayloadsAllTheThings/_LEARNING_AND_SOCIALS/YOUTUBE.md',
    'data/raw/PayloadsAllTheThings/_LEARNING_AND_SOCIALS/TWITTER.md',
    'data/raw/PayloadsAllTheThings/_LEARNING_AND_SOCIALS/BOOKS.md',
    'data/raw/PayloadsAllTheThings/_template_vuln/README.md',
    'data/raw/exploit-notes/README.md',
    'data/raw/exploit-notes/LICENSE.md',
    'data/raw/exploit-notes/SUMMARY.md',
]


@dataclass(kw_only=True, slots=True)
class Document:
    src: Dict[str, str | Path]
    title: List[str]
    description: List[str]
    tags: List[str]
    body: List[str]
