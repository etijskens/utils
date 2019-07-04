#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for module stopwatch
"""
#===============================================================================
import os
import sys
from time import sleep
#===============================================================================
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
from utils import StopWatch
# from utils import __version__
#===============================================================================
def test_create_StopWatch():
    tmr = StopWatch()
    assert tmr.time==0.0
#===============================================================================
def test_sleep_1():
    with StopWatch("time 'sleep(1)': ")as tmr:
        sleep(1)
    time = tmr.time
    assert time>1.00
    assert time<1.01
#===============================================================================
def test_sleep_1_iterated():
    with StopWatch("time 5 times 'sleep(1)': ",ndigits=3) as tmr:
        for i in range(5):
            sleep(1)
            time = tmr.timelapse()
            print(i,time)
            assert time>=1.00
            assert time<=1.01
    time = tmr.time
    assert time>5.00
    assert time<5.05
#===============================================================================

# ==============================================================================
# The code below is for debugging a particular test in eclipse/pydev.
# (normally all tests are run with pytest)
# ==============================================================================
if __name__ == "__main__":
    the_test_you_want_to_debug = test_create_StopWatch
    
    from utils import taskcm
    with taskcm(f"__main__ running {the_test_you_want_to_debug}"
               , "-*# finished #*-", singleline=False, combine=False):
        the_test_you_want_to_debug()
# ==============================================================================
