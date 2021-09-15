#!/usr/bin/env python3
"""
Author : abennett1 <abennett1@localhost>
Date   : 2021-09-14
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('numbers',
                        metavar='integers',
                        nargs='+',
                        type=int,
                        help='Sum of numbers')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    numbers = []
    sum = 0
    
    for nums in args.numbers:
        numbers.append(str(nums))
        sum += nums
    
    print('{} = {}'.format(' + '.join(numbers), sum))


# --------------------------------------------------
if __name__ == '__main__':
    main()
