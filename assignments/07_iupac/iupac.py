#!/usr/bin/env python3
"""
Author : abennett1 <abennett1@localhost>
Date   : 2021-10-20
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence',
                        metavar='str',
                        help='Input sequence(s)')

    

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    


# --------------------------------------------------
if __name__ == '__main__':
    main()
