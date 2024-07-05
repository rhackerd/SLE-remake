import inspect
from classes.kons_format import consoleFormat
import datetime


def error(*args):
    filename = inspect.currentframe().f_back.f_globals['__file__'].split('/')[-1]
    time = datetime.datetime.now().strftime("%H:%M:%S")
    message = ' '.join(map(str, args))
    print(consoleFormat(f"&<black>&d[{time}]&r &<red>&l[ERROR] &<black>&l[{filename}] &<white>{message}&r").format())

def info(*args):
    filename = inspect.currentframe().f_back.f_globals['__file__'].split('/')[-1]
    time = datetime.datetime.now().strftime("%H:%M:%S")
    message = ' '.join(map(str, args))

    print(consoleFormat(f"&<black>&d[{time}]&r &<cyan>&l[INFO] &<black>&l[{filename}] &<white>{message}&r").format())


def _error(*args):
    filename = inspect.currentframe().f_back.f_globals['__file__'].split('/')[-1]
    time = datetime.datetime.now().strftime("%H:%M:%S")
    message = ' '.join(map(str, args))
    return consoleFormat(f"&<black>&d[{time}]&r &<red>&l[ERROR] &<black>&l[{filename}] &<white>{message}&r").format()

def _info(*args):
    filename = inspect.currentframe().f_back.f_globals['__file__'].split('/')[-1]
    time = datetime.datetime.now().strftime("%H:%M:%S")
    message = ' '.join(map(str, args))

    return consoleFormat(f"&<black>&d[{time}]&r &<cyan>&l[INFO] &<black>&l[{filename}] &<white>{message}&r").format()