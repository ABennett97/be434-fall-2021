#!/usr/bin/env python3
"""
Author : abennett1 <abennett1@localhost>
Date   : 2021-09-20
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Do Re Mi solfege',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        nargs='+',
                        help='Solfege')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    syllable = {'Do': 'Do, A deer, a female deer', 'Re': 'Re, A drop of golden sun',
                'Mi': 'Mi, A name I call myself', 'Fa': 'Fa, A long long way to run',
                'Sol': 'Sol, A needle pulling thread', 'La': 'La, A note to follow sol',
                'Ti': 'Ti, A drink with jam and bread'}
    
    for word in args.text:
        if word in syllable:
            print(syllable.get(word))
        else:
            print("I don't know " + '"' + word + '"')

# --------------------------------------------------
if __name__ == '__main__':
    main()
