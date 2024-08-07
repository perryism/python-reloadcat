import logging, re, os, sys
from importlib import reload as reload_module
import importlib
from . import ImportParser, src_to_module

class Reloader:
    def __init__(self, src_path):
        self.parser = ImportParser(src_path)
        self.module_name = src_to_module(src_path) 

    def reload(self):
        self._reload(self.module_name)

    def junk(self):
        logging.debug("module name: %s"%self.module_name)
        module = importlib.import_module(self.module_name)
        logging.debug("reloading %s"%module)
        reload_module(module)
        if module.__package__ is None: return

        package = importlib.import_module(module.__package__)
        #package = __import__(module.__package__)
        logging.debug("reloading %s"%package)
        reload_module(package)

    def _reload(self, name):
        if len(name) == 0: return

        try:
            module = importlib.import_module(name)
            logging.debug("reloading %s"%module)
            reload_module(module)
            self._reload('.'.join(module.__name__.split('.')[:-1]))
        except:
            logging.error(f"failed at loading {name}")
            logging.warning(sys.exc_info()[0])

