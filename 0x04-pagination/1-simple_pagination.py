#!/usr/bin/env python3
"""
===============================================================================
Implement a method named get_page that takes two integer arguments page with
default value 1 and page_size with default value 10.

You have to use this CSV file (same as the one presented at the top of the
 project) Use assert to verify that both arguments are integers greater than 0.
Use index_range to find the correct indexes to paginate the dataset correctly
and return the appropriate page of the dataset (i.e. the correct list of rows).
If the input arguments are out of range for the dataset, an empty list should
be returned.
===============================================================================
"""

import csv
import math
from typing import Tuple, List


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
        """

        :param page:
        :param page_size:
        :return:
        """

        assert isinstance(page, int) and isinstance(page_size, int)
        assert page_size > 0 and page > 0

        __dataset = self.dataset()
        data: List[List] = []
        indexes = index_range(page, page_size)
        if indexes[0] > len(self.__dataset):
            return []
        for i in range(indexes[0], indexes[1]):
            data.append(__dataset[i])

        return data


def index_range(page: int = 10, page_size: int = 0) -> Tuple[int, int]:
    """
        :param page: page number to calculated the starting index
        :param page_size: index size per page
        :return: a tuple with starting and end index for a particular page
    """

    start_index = (page_size * page) - page_size
    end_index = page_size * page

    return start_index, end_index
