from typing import List, Dict, Any
from abc import ABC, abstractmethod
from nltk import word_tokenize
from pathlib import Path

import re

from schema import Document, filetypes, blacklist
from util import get_project_root


class Parser(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def parse(self, source: Dict[str, str | Path | Any]) -> List[Document]:
        pass

    def parse(self, source: Dict[str, str | Path | Any]) -> List[Document]:
        return []

    def _tokenize(self, data: str) -> List[str]:
        data = data.replace('_', ' ').replace('-', ' ').replace('.', ' ') if data else []
        return list(
            filter(
                str.isalpha, 
                map(
                    lambda s: re.sub('[^a-zA-Z0-9]', '', s), 
                    map(str.lower, word_tokenize(data))
                )
            )
        ) if data else []


    def _get_files(self, path: Path) -> List[Path]:
        def match_file(path: Path):
            for r in filetypes:
                if (
                    re.search(r, path.name) and
                    path not in map(get_project_root().joinpath, blacklist)
                ):
                    return path
            else:
                return ''

        files = list(filter(None, map(match_file, path.glob('**/*'))))
        return files
