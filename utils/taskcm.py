# -*- coding: utf-8 -*-

"""
Module utils.taskcm 
=================================================================

A module

"""
#===============================================================================
import sys
from contextlib import contextmanager
#===============================================================================
def print2stderr(*args, **kwargs):
    """
    The standard print, but print to stderr instead of to stdout.
    """
    print(*args, file=sys.stderr, **kwargs)

#===============================================================================
@contextmanager
def taskcm(begin_msg='doing',end_msg='done.',log=None,singleline=True, combine=True):
    """
    Print a start and stop message when executing a task.

    :param str begin_msg: print this before body is executed
    :param str end_msg: print this after body is executed
    :param log: if None, generates the execution trace on stderr, otherwise on
        a logger object (from the logging module)
    :param singleline: generates a single line execution trace as in
        `<begin_msg> ... <end_msg>`. Calling print2stderr may obfuscate this.
    :param combine: if True the after message recapitulates the begin message.
        This parameter is ignored when singleline is True.
    """
    if log:
        log.info(begin_msg+' ...')
        yield
        log.info(f"{begin_msg} {end_msg}")
    elif singleline:
        print2stderr(begin_msg,'... ', end='')
        yield
        print2stderr(end_msg)
    else:
        print2stderr(begin_msg,'...')
        yield
        if combine:
            print2stderr(begin_msg,end_msg,'\n')
        else:
            print2stderr(end_msg,'\n')
#===============================================================================
