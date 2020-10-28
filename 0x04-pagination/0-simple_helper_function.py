#!/usr/bin/env python3
"""
===============================================================================
function named index_range that takes two integer arguments page and
 page_size.

The function should return a tuple of size two containing a start index and an
end index corresponding to the range of indexes to return in a list for those
particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.
===============================================================================
"""

from typing import Tuple


def index_range(page: int = 0, page_size: int = 0) -> Tuple[int, int]:
    """
        :param page: page number to calculated the starting index
        :param page_size: index size per page
        :return: a tuple with starting and end index for a particular page
    """

    start_index = (page_size * page) - page_size
    end_index = page_size * page

    return start_index, end_index
