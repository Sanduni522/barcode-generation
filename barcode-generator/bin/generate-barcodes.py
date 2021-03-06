#!/usr/bin/env python

import argparse
import random
import sys
from itertools import cycle

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--length', '-l', help='length of barcode', type=int, required=True)
    parser.add_argument('--min-dist', '-d', help='minimum edit distance', type=int, required=True)
    parser.add_argument('--count', '-c', help='number of barcodes', type=int, required=True)
    parser.add_argument('--max-stretch', '-s', help='max stretch of the same nucleotide', type=int, required=False)
    parser.add_argument('--input', '-i', help='(optional) list of already-designed barcodes to extend')

    return parser.parse_args()


def hamming(a, b):
    ''' hamming distance between two strings '''
    dist = 0
    for i, j in zip(a, b):
        if i != j:
            dist += 1
    return dist

def max_stretch(s):
    ''' returns max stretch of the same letter in string '''
    max_stretch = 0
    last = None
    for n in s:
        if last == None:
            last = n
            stretch = 0
            continue
        if n == last:
            stretch += 1
            if stretch > max_stretch:
                max_stretch = stretch
        else:
            stretch = 0
        last = n
    return max_stretch


def random_nucleotide_sequence(length, alphabet = 'GATC'):
    ''' generate a random nucleotide sequence '''
    return ''.join( random.sample(alphabet, 1)[0] for i in range(0, length) )


def generate_barcodes(barcodes, **kwargs):
    ''' generate barcodes given constrains '''

    spinner = cycle('|/-\\')

    while True:
        if len(barcodes) == kwargs['count']:
            break
        
        new_barcode = random_nucleotide_sequence(kwargs['length'])

        keep = True

        if new_barcode in barcodes:
            keep = False
            break

        if kwargs.get('max_stretch', False):
            if max_stretch(new_barcode) >= kwargs['max_stretch']:
                keep = False

        if keep:
            for barcode in barcodes:
                if hamming(new_barcode, barcode) < kwargs['min_dist']:
                    keep = False
                    break

        if keep:
            sys.stderr.write(next(spinner))
            sys.stderr.flush()
            sys.stderr.write('\b')
            barcodes.append(new_barcode)

    print(sys.stderr, 'finished')

    # make sure there are no duplicates!
    assert len(set(barcodes)) == len(barcodes)

    return barcodes


def main():
    ''' the guts '''

    args = parse_args()

    barcodes = []

    # check if list of barcodes already exists
    if args.input:
        with open(args.input) as handle:
            barcodes.extend(i.strip() for i in handle)

    print(sys.stderr, 'generating barcodes...')
    barcodes = generate_barcodes(barcodes,
                                 min_dist=args.min_dist,
                                 count=args.count,
                                 length=args.length,
                                 max_stretch=args.max_stretch)

    for i, barcode in enumerate(barcodes):
        print('>%s\n%s' % (i, barcode))


if __name__ == '__main__':
    main()
