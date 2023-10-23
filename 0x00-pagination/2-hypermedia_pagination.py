#!/usr/bin/env python3
""" index range returning a tuple containging start index and end index"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> int:
    """ index range function taking in two parameters
    Return: tuple containing start index and end index """

    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ get a specific page of data from the dataset
        Args:
            page (int): The 1-indexed page number.
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list of rows from the dataset for the requested page,
            or an empty list if out of range.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0, "Both page and page_size > 0."

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)

        # Check if the start index is out of range
        if start_index >= len(dataset):
            return []

        # Return the appropriate page of the dataset
        return dataset[start_index:end_index]
