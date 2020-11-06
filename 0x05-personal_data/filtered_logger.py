#!/usr/bin/env python3
"""
================================================================================
function called filter_datum that returns the log message obfuscated:

Arguments:
fields: a list of strings representing all fields to obfuscate
redaction: a string representing by what the field will be obfuscated
message: a string representing the log line
separator: a string representing by which character is separating all fields in
the log line (message)
The function should use a regex to replace occurrences of certain field values.
filter_datum should be less than 5 lines long and use re.sub to perform the
substitution with a single regex.
================================================================================
"""

import logging
import re
from typing import List


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        :param fields: list of strings
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        :param record: logging record to be formatted
        :return: formatted record
        """

        record.msg = filter_datum(self.fields, self.REDACTION, record.msg,
                                  self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    :param fields: a list of strings representing all fields to obfuscate
    :param redaction:a string representing by what the field will be obfuscated
    :param message: a string representing the log line
    :param separator:  string representing by which character is separating
    all fields in the log line (message)
    :return: a new string replacing message string with fields
    """

    for word in fields:
        message = re.sub(rf'{word}=.+?{separator}',
                         f'{word}={redaction}{separator}', message)
    return message
