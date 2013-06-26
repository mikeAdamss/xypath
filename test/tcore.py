#!/usr/bin/env python
import sys
import unittest
sys.path.append('xypath')
import xypath
import messytables
from os.path import dirname, abspath, join, splitext


def get_extension(filename):
    """
    >>> get_extension('/foo/bar/test.xls')
    'xls'
    """
    return splitext(filename)[1].strip('.')


class TCore(unittest.TestCase):
    @classmethod
    def setup_class(cls):
        cls.wpp_filename = join(
            abspath(dirname(__file__)), '..', 'fixtures', 'wpp.xls')
        cls.messy = messytables.excel.XLSTableSet(open(cls.wpp_filename, "rb"))
        cls.table = xypath.Table.from_messy(cls.messy.tables[0])

    def setUp(self):
        pass


