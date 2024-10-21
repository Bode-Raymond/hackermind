from typing import Dict, List, Any
from urllib.parse import urljoin
from os.path import splitext
from pathlib import Path

import re

from parsers.parser import Parser as BaseParser
from schema import Document


class Parser(BaseParser):
    def parse(self, source: Dict[str, str | Path | Any]) -> List[Document]:
        docs = []
        files = super()._get_files(source['dat'])

        for file in files:
            src = {
                'url': urljoin(source['url'], str(splitext(file.relative_to(source['dat']))[0]).replace('README', '')),
                'dat': file,
            }

            data = file.read_text()

            title = splitext(file.name)[0]
            if title == 'README':
                title = file.parent.name
            title = super()._tokenize(title)

            tags = super()._tokenize(
                re.sub('[-_/]', ' ', str(file.relative_to(source['dat']).parent))
            )

            docs.append(Document(
                src=src,
                title=title,
                description=[],
                tags=tags,
                body=super()._tokenize(data),
            ))

        return docs
