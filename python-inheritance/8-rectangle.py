#!/usr/bin/python3
"""python class"""
BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle subclass"""
    def __init__(self, width, height):
        """Python"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
