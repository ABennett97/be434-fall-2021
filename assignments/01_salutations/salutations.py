#!/usr/bin/env python3
"""
Author : abennett1 <abennett1@localhost>
Date   : 2021-12-07
Purpose: Print greeting
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Print greeting',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-g',
                        '--greeting',
                        help='The greeting',
                        metavar='str',
                        default='Howdy')

    parser.add_argument('-n',
                        '--name',
                        help='Who to greet',
                        metavar='str',
                        default='Stranger')

    parser.add_argument('-e',
                        '--excited',
                        help='Include an exclamation point',
                        default=False)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print("{greeting}, {name}.".format(greeting=args.greeting,
            name=args.name))


# --------------------------------------------------
if __name__ == '__main__':
    main()
