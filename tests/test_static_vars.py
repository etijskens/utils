#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `utils` package."""

import os
import sys

from click import echo

from utils import __version__

# Make sure that the current directory is the project directory.
# 'make test" and 'pytest' are generally run from the project directory.
# However, if we run/debug this file in eclipse, we end up in test
if os.getcwd().endswith('tests'):
    echo(f"Changing current working directory"
         f"\n  from '{os.getcwd()}'"
         f"\n  to   '{os.path.abspath(os.path.join(os.getcwd(),'..'))}'.\n")
    os.chdir('..')
# Make sure that we can import the module being tested. When running
# 'make test" and 'pytest' in the project directory, the current working
# directory is not automatically added to sys.path.
if not ('.' in sys.path or os.getcwd() in sys.path):
    echo(f"Adding '.' to sys.path.\n")
    sys.path.insert(0, '.')

# ==============================================================================
"""
Tests for module static_vars (using pytest)
"""
#===============================================================================
#===============================================================================
from utils import static_vars
#===============================================================================    
def test_static_vars():
    #---------------------------------------------------------------------------
    @static_vars(counter=0)
    def foo():
        foo.counter += 1
    #---------------------------------------------------------------------------
    foo()
    foo()
    assert foo.counter==2
    foo.counter = 0
    foo()
    assert foo.counter==1
#===============================================================================

# ==============================================================================
# The code below is for debugging a particular test in eclipse/pydev.
# (normally all tests are run with pytest)
# ==============================================================================
if __name__ == "__main__":
    the_test_you_want_to_debug = test_static_vars

    from utils import taskcm
    with taskcm(f"__main__ running {the_test_you_want_to_debug}",
               '-*# finished #*-', singleline=False, combine=False):
        the_test_you_want_to_debug()
# ==============================================================================
