from dataclasses import dataclass, field
from typing import Dict, Any
from pathlib import Path

from util import get_project_root


@dataclass(frozen=True, slots=True)
class Sources():
    exploit_notes: Dict[str, str | Path | Any] = field(default_factory=lambda: {
        'name': 'Exploit Notes',
        'url': 'https://exploit-notes.hdks.org/', 
        'dat': get_project_root().joinpath('data/raw/exploit-notes/src/'),
        'favicon': 'https://exploit-notes.hdks.org/img/favicon.ico'
    })
    hacktricks: Dict[str, str | Path | Any] = field(default_factory=lambda: {
        'name': 'HackTricks',
        'url': 'https://book.hacktricks.xyz/', 
        'dat': get_project_root().joinpath('data/raw/hacktricks/'),
        'favicon': 'https://book.hacktricks.xyz/~gitbook/image?url=https%3A%2F%2F2783428383-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fcollections%252FmuMguNrsRx2mNyNqEox4%252Ficon%252F1qCJ0VIDlWcvGSecYCDq%252Ffondo.png%3Falt%3Dmedia%26token%3D1e721267-450f-43f3-861b-6c4f93278e93&width=32&dpr=4&quality=100&sign=61472716&sv=1'
    })
    hacktricks_cloud: Dict[str, str | Path | Any] = field(default_factory=lambda: {
        'name': 'HackTricks Cloud',
        'url': 'https://cloud.hacktricks.xyz/', 
        'dat': get_project_root().joinpath('data/raw/hacktricks-cloud/'),
        'favicon': 'https://1903070231-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/collections%2FCwO1tbNpoOUJlM2hGhoK%2Ficon%2F5f3X1nONH2UfRY8Bj39K%2FCLOUD-logo.svg?alt=media&token=fb49f498-1147-46ee-979c-07f4b02ace70'
    })
    heap_exploitation: Dict[str, str | Path | Any] = field(default_factory=lambda: {
        'name': 'Heap Exploitation',
        'url': 'https://heap-exploitation.dhavalkapil.com/',
        'dat': get_project_root().joinpath('data/raw/heap-exploitation/'),
        'favicon': 'https://3316937432-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/spaces%2F-MHeffotUnwuuxDxBYkc%2Favatar-1600593992126.png?generation=1600593992349116&alt=media'
    })
    payloadallthethings: Dict[str, str | Path | Any] = field(default_factory=lambda: {
        'name': 'PayloadsAllTheThings',
        'url': 'https://swisskyrepo.github.io/PayloadsAllTheThings/',
        'dat': get_project_root().joinpath('data/raw/PayloadsAllTheThings/'),
        'favicon': 'https://swisskyrepo.github.io/PayloadsAllTheThings/assets/images/favicon.png'
    })
    pwn_notes: Dict[str, str | Path | Any] = field(default_factory=lambda: {
        'name': 'ir0nstone',
        'url': 'https://ir0nstone.gitbook.io/',
        'dat': get_project_root().joinpath('data/raw/pwn-notes/'),
        'favicon': 'https://ir0nstone.gitbook.io/~gitbook/image?url=https%3A%2F%2F349224153-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fspaces%252F-MEwBGnjPgf263kl5vWP%252Favatar-1597679102856.png%3Fgeneration%3D1597679103137105%26alt%3Dmedia&width=32&dpr=4&quality=100&sign=2a41daa1&sv=1'
    })

