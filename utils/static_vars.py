# -*- coding: utf-8 -*-

"""
Module utils.static_vars 
========================

A decorator for adding static variables to a function.
see https://stackoverflow.com/questions/279561/what-is-the-python-equivalent-of-static-variables-inside-a-function
"""
#===============================================================================
def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate
    #---------------------------------------------------------------------------

#===============================================================================
