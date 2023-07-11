#!/usr/bin/python3

"""Defines a function to count the number of lines in a text file."""

def number_of_lines(filename=""):
    """Return the number of lines in a text file."""
    lines = 0
    with open(filename, 'r') as file:
        for line in file:
            lines += 1
    return lines
