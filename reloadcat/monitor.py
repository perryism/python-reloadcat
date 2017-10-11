import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileModifiedEvent, PatternMatchingEventHandler, RegexMatchingEventHandler
from .import_parser import ImportParser
from imp import reload
from inspect import getmodule
import importlib
import glob
import unittest
from .reloader import Reloader

def test(klass):
    suite = unittest.TestLoader().loadTestsFromTestCase( klass )
    unittest.TextTestRunner(verbosity=1,stream=sys.stderr).run( suite )

import re, os

class Patterns:
    def __init__(self, yaml_file):
        import yaml
        logging.info("reading %s"%yaml_file)
        self.yaml = yaml.load(open(yaml_file,'r').read())

    def files(self):
        flatten = lambda l: [item for sublist in l for item in sublist]
        return flatten(self._files())

    def _files(self):
        for pattern in self.yaml["patterns"]:
            yield glob.glob(pattern)

DEFAULT_PATTERN_FILE = 'reloadcat.yaml'

def get_patterns():
    if os.path.isfile(DEFAULT_PATTERN_FILE):
        patterns = Patterns(DEFAULT_PATTERN_FILE).files()
    else:
        logging.fatal("%s is not found"%DEFAULT_PATTERN_FILE)
        sys.exit(1)

    logging.debug("watching the following files %s"%patterns)

    return patterns

def find_test(src):

    files = get_patterns()
    test_file = "test_%s"%os.path.basename(src)

    found = filter(lambda x: test_file in x, files)

    return found[0] if len(found) > 0 else None

def run_tests(e):
    logging.info("%s is modified"%e.src_path)
    if e.src_path.startswith("./tests/"):
        reload_file(e.src_path)
    else:
        reload_file(e.src_path)
        test_file = find_test(e.src_path)
        if test_file:
            reload_file(test_file)

def reload_file(src_path):
    Reloader(src_path).reload()

    for klass in ImportParser(src_path).subclass_of(unittest.TestCase):
        logging.info("Testing %s"%klass)
        test(klass)
