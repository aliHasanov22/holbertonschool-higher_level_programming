#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return None
    first = sentence[0]
    length = len(sentence)
    return length, first
