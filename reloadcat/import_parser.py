import importlib
import re, os
from . import src_to_module

class ImportParser:
    def __init__(self, src):
        self.src = src

    def module(self):
        return re.sub("(\.py$|^\./)", "", self.src).replace(os.sep, ".")

    def subclass_of(self, cls):
        m = importlib.import_module(src_to_module(self.src))

        for klass in dir(m):
            attr = getattr(m, klass)
            if self._issubclass(attr, cls):
                yield attr

    def _issubclass(self, cls, subcls):
        try:
            return issubclass(cls, subcls)
        except:
            return False
