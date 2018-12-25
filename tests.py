#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# DCIM renamer - Renames your DCIM files.
#
# Copyright (C) 2018 Erik Mossberg
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import unittest
import os
import sys

from dcim_renamer import *

class TestDcimRunner(unittest.TestCase):
    """
    Verify Dcim output parser.
    """

    def test_dcim_reader(self):
        """
        Test that we can get raw output from exif2 calls.
        """
        er = Exiv2Reader()
        abspath = os.path.abspath(os.path.join('.', 'DCIM/IMG_0001.JPG'))
        raw_output = er.get_exiv2_stdout(abspath)
        self.assertTrue('EF24-105mm' in raw_output)


if __name__ == '__main__':
    unittest.main()
