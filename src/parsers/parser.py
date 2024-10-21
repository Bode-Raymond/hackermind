from typing import List, Dict, Union, Self
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
    def parse(self, source: Dict[str, Union[str, Path, Self]]) -> List[Document]:
        pass

    def parse(self, source: Dict[str, Union[str, Path, Self]]) -> List[Document]:
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


if __name__ == '__main__':
    from util import get_project_root

    path = get_project_root().joinpath('data/raw/pwn-notes/')
    parser = Parser()

    files = parser._get_files(path)
    print(files)
    parser._tokenize(files[0])
