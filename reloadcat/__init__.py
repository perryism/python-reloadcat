from pathlib import Path
import os

def src_to_module(src):
    execute_path = os.getcwd()
    relative = src.replace(execute_path, "")
    path = Path(relative).parent.absolute()
    fragments = str(path).split(os.sep)[1:]
    return ".".join(fragments)

from .import_parser import ImportParser
from .reloader import Reloader
