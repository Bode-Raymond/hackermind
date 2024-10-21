from subprocess import Popen, PIPE
from functools import cache
from pathlib import Path

@cache
def get_project_root() -> Path:
    stdout = Popen(['git', 'rev-parse', '--show-toplevel'], stdout=PIPE).communicate()
    return Path(stdout[0].rstrip().decode('utf-8'))
