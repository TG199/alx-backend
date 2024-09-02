#!/usr/bin/env python3
"""Simple helper function """
from typing import Tuple


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
