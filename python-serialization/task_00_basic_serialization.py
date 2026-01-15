#!?usr/bin/python
"""Python json serialization"""
import json


def serialize_and_save_to_json(data, filename):
    """Saves data as a human-readable JSON file"""
    # Note: Use "w" (text mode) instead of "wb"
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def load_and_deserialize_json(filename):
    """Loads data from a JSON file"""
    # Note: Use "r" (text mode) instead of "rb"
    with open(filename, "r") as file:
        data = json.load(file)
    print(data)
    return data
