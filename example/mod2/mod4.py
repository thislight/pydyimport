from pydyimport import DynamicImport

hello_spam, = DynamicImport(__file__).require_only('mod3.py', 'hello_spam')


def hello4():
    hello_spam()
    print("Hello 4")
