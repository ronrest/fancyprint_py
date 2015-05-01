"""====================================================
                    DESCRIPTION

=======================================================
"""
__author__ = 'Ronny Restrepo'

def printkv(key, val, sep=": ", fill=0, fill_char=" ", rounding=False):
    """
    ==========================================================================
                                                                       PRINTKV
    ==========================================================================
    Print a key value pair. You can specify that the value be positioned at a
    certain minimum column number, which can be used to line up multiple
    prinkv() function calls.
    You can also specity how the gap between the key and the value should be
    filled up, aswell as the separator.

    :param key: the content of the key
    :param val: content of the value
    :param sep: the character used to separate a key from a value.
           defaults to ": "
    :param fill: integer. The minimum number of columns to fill up before the
           separator is displayed. Use this to line values up.
    :param rounding: used for setting the number of decimal places to show (if
           val was a numeric type).
           If rounding is False (Default), then no rounding occurs.
           If rounding is an integer, then val is rounded to that many decimal
           places

    EXAMPLES
    printkv("name", "Joe", sep="= ", fill=10, fill_char=".")
    printkv("age", 34, sep="= ", fill=10, fill_char=".")
    printkv("age", 56)
    """

    # TODO: check that the inputs are of the correct data type.

    #-------------------------------------------------------------------------
    #                                 Fill with the necessary amount of spaces
    #-------------------------------------------------------------------------
    gap = fill - len(key)
    key = key + (gap*fill_char) + sep # fill the gap, and add separator


    #-------------------------------------------------------------------------
    #                                                           Value Rounding
    #-------------------------------------------------------------------------
    if (type(val) == float) and (type(rounding) == int):
        val = round(val, ndigits=rounding)

    # If user specifies round to be True instead of an integer, then round to
    # nearest whole number.
    elif (type(val) == float) and (type(rounding) == bool) and round:
        val = round(val)

    #-------------------------------------------------------------------------
    #                                                     Print out the Result
    #-------------------------------------------------------------------------
    print(key+str(val))


if __name__ == '__main__':
    print("fancyprint")


