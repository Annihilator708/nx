import _nx

from .audio import *
from .controllers import *
from .title import *
from .players import *


_nx.account_initialize()


p1 = Player(1)
p2 = Player(2)
p3 = Player(3)
p4 = Player(4)


class _Titles:
    def __init__(self):
        self._titles = {}

    def __getitem__(self, title_id):
        if title_id in self._titles:
            return self._titles[title_id]
        _title = Title(title_id)
        self._titles[title_id] = _title
        return _title


titles = _Titles()
