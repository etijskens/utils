# -*- coding: utf-8 -*-

"""
Module utils.stopwatch
======================

A context manager class for timing a piece of code.
"""
#===============================================================================
from timeit import default_timer as timer
#===================================================================================================
class StopWatch:
    """
    Context manager class for timing a code fragment
    :param comment: label for the print statement, if None nothing is printed.
    """
    #-----------------------------------------------------------------------------------------------
    def __init__(self,message='',ndigits=6):
        self.started = -1.0
        self.stopped = -1.0
        self.message = message
        self.ndigits = ndigits
    #-----------------------------------------------------------------------------------------------
    def __enter__(self):
        self.start()
        return self
    #-----------------------------------------------------------------------------------------------
    def __exit__(self, exception_type, exception_value, tb):
        seconds = self.stop()
        if not self.message is None:
            print(self)
    #-----------------------------------------------------------------------------------------------
    #@property
    # DO NOT use the @property decorator for functions that change the state!
    def timelapse(self):
        """
        return number of seconds since last call to timelapse (or to start if it is called for the
        first time.
        """
        now = timer()
        seconds = round(now - self.stopped,self.ndigits)
        self.stopped = now
        return seconds
    #-----------------------------------------------------------------------------------------------
    @property
    def time(self):
        """
        return number of seconds between the timer was started and stopped (for the last time)
        """
        return round(self.stopped-self.started,self.ndigits)
    #-----------------------------------------------------------------------------------------------
    def start(self):
        """
        Start or restart the timer
        """
        self.started = timer()
        self.stopped = self.started
    #-----------------------------------------------------------------------------------------------
    def stop(self):
        """
        Stop the timer and return the number of seconds since the timer was started.
        """
        self.stopped = timer()
        return self.time
    #-----------------------------------------------------------------------------------------------
    def __repr__(self):
        """

        """
        if not self.message is None:
            return self.message+'{} s'.format(self.time)
        else:
            return              '{} s'.format(self.time)
    #-----------------------------------------------------------------------------------------------

#===================================================================================================
