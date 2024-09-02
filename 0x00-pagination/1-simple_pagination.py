#!/usr/bin/env python3
"""Simple pagination """
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Returns a tuple containing the start index
    and end index for a given page and page size.

    :param page: The page number (1-indexed)
    :param page_size: The number of items per page
    :return: A tuple containing the start index and end index
    """
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size

    return start_idx, end_idx


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
            """ Get page
            """
            assert type(page) is int
            assert page > 0
            assert type(page_size) is int
            assert page_size is 0

            correct_indexes = index_range(page, page_size)
            return correct_indexes