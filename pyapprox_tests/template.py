#!/usr/bin/env python3
"""
File: template.py
Author: riley cooper
Email: rwr.cooper@gmail.com
Description:
    Template script.

Usage:
    template.py -a <arg1> -b <arg2>... [-c <arg3>]
    template.py option1 -a <arg1> -b <arg2>... [-c <arg3>]
                    

Options:
    -a <arg1>, --arg1=<arg1>
    -b <arg2>, --arg2s=<arg2>
    -c <arg3>, --arg3=<arg3>

    -h, --help
    --option=<n>
"""


# test edit
# test edit 2

# imports
from docopt import docopt


def execute_option1():
    # run some task
    for i in range(2):
    print(i)


def main(args):

    if args['option1']:
    # for example
        execute_option1()

    arg1 = args['--arg1']
    # other args...

    return


if __name__ == '__main__':
    args = docopt(__doc__)

    main(args)

