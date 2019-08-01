import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileModifiedEvent, PatternMatchingEventHandler, RegexMatchingEventHandler
from .monitor import run_tests, get_patterns
import glob, os
import argparse

def test_files():
    """
    Noted that watchdog's pattern matching event has the leading './' in the path
    """

    return glob.glob("./tests/**.py")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="verbose", type=str,  default="INFO", choices=["DEBUG", "INFO", "WARN"])
    parser.add_argument("-lf", "--log_format", help="log format", type=str,  default="%(asctime)s - %(message)s")
    parser.add_argument("-d", "--watched_folder", help="folder to watch", type=str)

    args = parser.parse_args()

    logging.basicConfig(level=getattr(logging, args.verbose), format=args.log_format)

    patterns = get_patterns(args.watched_folder)
    logging.debug("watching the following files %s"%patterns)

    p = PatternMatchingEventHandler(patterns=patterns)
    p.on_created = run_tests
    p.on_modified = run_tests
    observer = Observer()
    observer.schedule(p, '.', recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
