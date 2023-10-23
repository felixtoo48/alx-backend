#!/usr/bin/env python3
""" index range returning a tuple containging start index and end index"""
import math


def index_range(page: int, page_size: int) -> int:
    """ index range function taking in two parameters
    Return: tuple containing start index and end index """

    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)
