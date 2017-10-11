import unittest
import mock
from mock import Mock
from reloader import Reloader

class TestReloader(unittest.TestCase):
    @mock.patch("reloader.reloader.reload_module")
    @mock.patch("reloader.reloader.importlib")
    def test_load(self, import_mock, reload_mock):
        module_mock = Mock()
        module_mock.__package__ = 'reloader'
        import_mock.import_module.return_value = module_mock
        package_mock = Mock()

        #__import__('reloader')
        #reload_mock.return_value = module_mock
        reloader = Reloader("../reloader/import_parser.py")
        def _import(self, package):
            return package_mock

        reloader._import = _import
        reloader.reload()

        #print(reload_mock.mock_calls)
        import_mock.import_module.assert_called_with('reloader.import_parser')
