#!/usr/bin/python3
"""Creates an object from json file"""
import json


def load_from_json_file(filename):
    """load from json file"""
    with open(filename) as f:
        x = json.load(f)
    return x
