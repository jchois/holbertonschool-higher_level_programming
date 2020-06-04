#!/usr/bin/python3
"""x"""
from json import argv

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    list = load_from_json_file("add_item.json")
except:
    list = []
for i in range(1, len(argv)):
    list.append(argv[i])
save_to_json_file(lst, "add_item.json")
