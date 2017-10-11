import unittest
from reloader.import_parser import ImportParser

class TestImportParser(unittest.TestCase):
    def test_module(self):
        src = './tests/test_hello.py'
        self.assertEqual(ImportParser(src).module(), 'tests.test_hello')

