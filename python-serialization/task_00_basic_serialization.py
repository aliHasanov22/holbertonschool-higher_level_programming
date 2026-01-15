#!?usr/bin/python
"""Python json serialization"""
import pickle


def serialize_and_save_to_file(data, filename):
    """Serialization"""
    with open(filename, "wb") as file:
        pickle.dump(data, file)


def load_and_deserialize(filename):
    """Deserialization"""
    with open(filename, "rb") as file:
        loaddata = pickle.load(file)
    print(loaddata)
