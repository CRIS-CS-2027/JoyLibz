'''Utility Functions'''
import os
import sys

def warn(*args, **kwargs):
    '''print args to stderr'''
    print(*args, file=sys.stderr, **kwargs)

def die(*args, **kwargs):
    '''print args to stderr and exit 1'''
    warn(*args, **kwargs)
    sys.exit(1)

def path_fname(path):
    '''returns the filename part of a path'''
    #  basename("/head/tail") returns "tail"
    return os.path.basename(path)