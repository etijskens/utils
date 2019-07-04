#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for `taskcm` module.
"""
# ==============================================================================
import os
import sys
from click import echo
# ==============================================================================
# Make sure that the current directory is the project directory.
# 'make test" and 'pytest' are generally run from the project directory.
# However, if we run/debug this file in eclipse, we end up in test
if os.getcwd().endswith('tests'):
    echo(f"Changing current working directory"
         f"\n  from '{os.getcwd()}'"
         f"\n  to   '{os.path.abspath(os.path.join(os.getcwd(),'..'))}'\n")
    os.chdir('..')
# Make sure that we can import the module being tested. When running
# 'make test" and 'pytest' in the project directory, the current working
# directory is not automatically added to sys.path.
if not ('.' in sys.path or os.getcwd() in sys.path):
    echo(f"Adding '.' to sys.path.\n")
    sys.path.insert(0, '.')
# ==============================================================================
from utils import taskcm, print2stderr
# from utils import __version__
# ==============================================================================
def test_taskcm():
    import logging
    log = logging.getLogger('main')
    log.addHandler(logging.StreamHandler(sys.stderr))
    log.setLevel(logging.INFO)
    with taskcm('executing __main__','finished.',log=log):
        with taskcm('something',singleline=False):
            # we must print to the same stream, otherwise the printed lines 
            # are not in the right order
            print2stderr('hello')
            print('world')
        with taskcm('something else'):
            # we must print to the same stream, otherwise the printed lines 
            # are not in the right order
            print2stderr('hello ...',end='')
# ==============================================================================

# ==============================================================================
# The code below is for debugging a particular test in eclipse/pydev.
# (normally all tests are run with pytest)
# ==============================================================================
if __name__ == "__main__":
    the_test_you_want_to_debug = test_taskcm
    the_test_you_want_to_debug()
# ==============================================================================
