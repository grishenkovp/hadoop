#!/usr/bin/env python
"""mapper.py"""
import sys
import re

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''


def perform_map():
    for line in sys.stdin:
        line = line.strip()
        line = re.sub(r'[^\w\s]', '', line)
        line = line.lower()
        for x in line:
            if x in punctuations:
                line = line.replace(x, " ")
        words = line.split()
        for word in words:
            print('%s\t%s' % (word, 1))


if __name__ == '__main__':
    perform_map()
