#!/usr/bin/python3
"""
Function that prints a text with 2 new lines
after each of these characters
"""


def text_indentation(text):
    """[summary]

    Arguments:
        text {[str]}

    Raises:
        TypeError: [text must be a string]
    """
    if (text):
        if type(text) is str:
            char = ['.', '?', ':']
            new_text = ""
            for words in text:
                new_text += words
                if words in char:
                    print(new_text.strip())
                    print()
                    new_text = ""
            print(new_text.strip(), end="")
        else:
            raise TypeError("text must be a string")
