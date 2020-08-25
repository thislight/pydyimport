# inject_require
from pydyimport import DynamicImport

hello_spam, = require_only('mod3.py', 'hello_spam')


def hello4():
    hello_spam()
    print("Hello 4")
