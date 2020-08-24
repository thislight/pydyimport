print(f"{require=}")
print(f"{require_only=}")

mod3 = require('mod2/mod3.py')
print(f"{mod3=}")
hello4, = require_only('mod2/mod4.py', 'hello4')
print(f"{hello4=}")


def hello1():
    mod3.hello3()
    hello4()
    print("Hello 1")
