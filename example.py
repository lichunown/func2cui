import sys
from func2cui import ParseFunction, ParseModule


parse = ParseModule()


@parse.sub_module('sum', help_msg=None)
def parse_sum(*args):
    return sum([float(i) for i in args])


@parse.sub_module('minus', help_msg="__doc__")
def minus(a:float, b:float):
    """minus two numbers.

        y = a - b
    """
    return a - b


@parse.sub_module('-v', help=False)
def _version():
    return 'example v1.0.0'


if __name__ == '__main__':
    print(parse(sys.argv[1:]))
