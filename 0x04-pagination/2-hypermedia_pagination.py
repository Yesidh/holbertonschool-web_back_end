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
from typing import Tuple, List, Dict, Union


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

        :param page: page number to calculated the starting index
        :param page_size: index size per page
        :return: a tuple with starting and end index for a particular page
        """

        assert isinstance(page, int) and isinstance(page_size, int)
        assert page_size > 0 and page > 0

        __dataset = self.dataset()
        data: List[List] = []
        indexes = index_range(page, page_size)
        if indexes[0] > len(__dataset):
            return []
        for i in range(indexes[0], indexes[1] + 1):
            if i <= len(__dataset) and i >= 0:
                data.append(__dataset[i])

        return data

    def get_hyper(self, page: int = 1, page_size: int = 10)\
            -> Dict[str, Union[int, List[List], None]]:
        """
            :param page: page number to calculated the starting index
            :param page_size: index size per page
            :return: a tuple with starting and end index for a particular page
        """

        # assert isinstance(page, int) and isinstance(page_size, int)
        # assert page_size > 0 and page > 0

        data = self.get_page(page, page_size)
        data_dict: Dict[str, Union[int, List[List], None]] = {}

        data_dict["page_size"] = len(data)
        data_dict["page"] = page
        data_dict["data"] = data
        len_data = len(self.__dataset)
        indexes = index_range(page, page_size)

        if (indexes[1] - len_data) >= 0:
            next_page = None
        else:
            next_page = page + 1
        data_dict["next_page"] = next_page

        if page <= 1:
            prev_page = None
        else:
            prev_page = page - 1
        data_dict["prev_page"] = prev_page

        data_dict["total_pages"] = math.ceil(len_data / page_size)

        return data_dict


def index_range(page: int = 10, page_size: int = 0) -> Tuple[int, int]:
    """
        :param page: page number to calculated the starting index
        :param page_size: index size per page
        :return: a tuple with starting and end index for a particular page
    """

    start_index = (page_size * page) - page_size
    end_index = page_size * page

    return start_index, end_index
