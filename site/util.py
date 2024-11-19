from subprocess import Popen, PIPE
from html.parser import HTMLParser
from json import JSONEncoder
from functools import cache
from typing import Pattern
from pathlib import Path

import json
import re


@cache
def get_project_root() -> Path:
    stdout = Popen(['git', 'rev-parse', '--show-toplevel'], stdout=PIPE).communicate()
    return Path(stdout[0].rstrip().decode('utf-8'))


@cache
def get_docs():
    return json.loads(open(get_project_root().joinpath('data/docs.json')).read())

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


class ReadmeParser(HTMLParser):
    __slots__ = ("_content", "headers", "data", "_header_pattern")

    headers: list
    data: list
    _content: list
    _header_pattern: Pattern[str]
    _flag_pattern: Pattern[str]

    def __init__(self):
        HTMLParser.__init__(self)
        self.headers = []
        self.data = []
        self._content = []
        self._header_pattern = re.compile(r"</?h[0-9]+>")

    def handle_starttag(self, tag, attrs):
        self._content.append(f"<{tag}>")

    def handle_endtag(self, tag):
        self._content.append(f"</{tag}>")

    def handle_data(self, data):
        if self._header_pattern.match(self._content[-1]):
            self.headers.append(data)
        else:
            self._content.append(data)

    def parse(self):
        data = []
        builder = []

        while self._content:
            c = self._content.pop()
            if not self._header_pattern.match(c):
                builder.append(c)
            elif builder:
                data.append("".join(reversed(builder)))
                builder = []
        data.reverse()
        self.data = data
