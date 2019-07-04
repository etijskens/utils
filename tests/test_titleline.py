#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for module titleline.
"""
#===============================================================================
import os
import sys
from click import echo

#===============================================================================
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
#===============================================================================
from utils import title_line
#===============================================================================
# tests
#===============================================================================
def test_title_line():
    n=30
    line = title_line("A title",n)
    assert len(line)==n+1
    assert line == '*** A title ******************\n'
    
    line = title_line("A title",n,start=8 ,char='-',above=True,below=True)
    assert len(line) == 3*(n+1)
    assert line == "------------------------------\n"\
                   "------- A title --------------\n"\
                   "------------------------------\n"
                   
    line = title_line(width=30)
    assert len(line)==n+1
    assert line == '******************************\n'
    
#===============================================================================
# The code below is for debugging a particular test in eclipse/pydev.
# (normally all tests are run with pytest)
#===============================================================================
if __name__=="__main__":
    the_test_you_want_to_debug = test_title_line

    from utils import taskcm
    with taskcm(f"__main__ running {the_test_you_want_to_debug}","-*# finished #*-",singleline=False,combine=False):
        the_test_you_want_to_debug()
#===============================================================================
