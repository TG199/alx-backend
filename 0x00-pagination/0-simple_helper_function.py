#!/usr/bin/env python3
"""Simple helper function """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size

    tuple_size = (start_idx, end_idx)

    return tuple_size
