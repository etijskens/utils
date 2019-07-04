# -*- coding: utf-8 -*-

"""
Module utils.titleline
======================

A method for for creating title lines.

"""
#===============================================================================
def title_line(text='', width=80,char='*',start=4,above=False,below=False,cr=True):
    """
    Function for creating title lines.

    :param str text: the title text
    :param int width: width of the title line
    :param str char: character used for the line
    :param int start: start point of the title text
    :param bool above: print a line above or not
    :param bool above: print a line below or not
    :param bool cr: add a carriage return at the end of the line

    Some examples::

        >>> print(titleline.title_line("A title", 30))
        *** A title ******************
        >>> print(titleline.title_line("A title",30,start=8 ,char='-',above=True,below=True))
        ------------------------------
        ------- A title --------------
        ------------------------------
        >>> print(titleline.title_line(width=30))
        ******************************
    """
    w = int(width/len(char))
    line0 = w*char
    if cr:
        line0 += '\n'
    if text:
        text = ' '+text+' '
    n =len(text)
    line = line0[:start-1]+text+line0[n+start-1:]
    if above:
        line = line0+line
    if below:
        line = line+line0
    return line
    #---------------------------------------------------------------------------
#===============================================================================
