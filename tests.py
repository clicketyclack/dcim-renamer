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

from dcim_renamer import DcimImage

class TestDcimRunner(unittest.TestCase):
    """
    Verify Dcim output parser.
    """

    @classmethod
    def setUpClass(cls):

        cls.img_0071 = DcimImage(os.path.abspath(os.path.join('.', 'DCIM/IMG_0071.JPG')))
        cls.img_0072 = DcimImage(os.path.abspath(os.path.join('.', 'DCIM/IMG_0072.JPG')))
        cls.img_0080 = DcimImage(os.path.abspath(os.path.join('.', 'DCIM/IMG_0080.JPG')))



    def test_dcim_reader(self):
        """
        Test that we can get raw output from exif2 calls.
        """

        abspath = os.path.abspath(os.path.join('.', 'DCIM/IMG_0071.JPG'))
        er = DcimImage(abspath)
        raw_output = er.get_exiv2_stdout(abspath)
        self.assertTrue('EF24-105mm' in raw_output)



    def test_exiv2_parsing(self):
        """
        Verify parsing.
        """

        raw_output = """Exif.Photo.DateTimeOriginal                   2017:07:30 02:44:14
Exif.CanonFi.NoiseReduction                   Off
Exif.CanonSi.TargetAperture                   F1
Exif.Photo.RecommendedExposureIndex           1600
Exif.CanonFi.FilterEffect                     None
Exif.Canon.ThumbnailImageValidArea            0 159 7 112
Exif.CanonPr.ColorTemperature                 0
Exif.Photo.SubSecTimeOriginal                 00
Exif.CanonSi.ISOSpeed                         3.51844e+15
Exif.Image.Artist                             Erik Mossberg clicketyclack@users.noreply.github.com
Exif.Canon.InternalSerialNumber               S0123456A
Exif.CanonFi.RawJpgSize                       Large
Exif.CanonCs.FlashActivity                    Did not fire
Exif.CanonCs.Lens                             0 0 0
Exif.CanonSi.FlashBias                        0 EV
Exif.CanonCs.DriveMode                        Single / timer
Exif.Image.Model                              Canon EOS 7D
Exif.CanonPr.PictureStyle                     None
Exif.Canon.AFInfo                             182 2 19 19 5184 3456 5184 3456 222 222 222 222 222 222 222 222 222 222 222 222 222 222 222 222 222 222 222 266 266 266 266 266 266 266 266 266 266 266 266 266 266 266 266 266 266 266 64163 64655 64655 64655 65143 65143 65143 0 0 0 0 0 393 393 393 881 881 881 1373 0 393 0 65143 393 0 65143 743 393 0 65143 64793 393 0 65143 393 0 65143 0 8192 0 8192 0 0 0 65535
Exif.CanonSi.WhiteBalance                     Auto
Exif.Photo.BodySerialNumber                   0123456789
Exif.Photo.MakerNote                          (Binary value suppressed)
"""

        keyvals = self.img_0080.keyvals_from_exiv2_stdout(raw_output)
        self.assertEqual(keyvals['Exif.Image.Model'], "Canon EOS 7D")
        self.assertEqual(keyvals['Exif.Photo.DateTimeOriginal'], "2017:07:30 02:44:14")
        self.assertEqual(keyvals['Exif.Photo.BodySerialNumber'], "0123456789")
        self.assertEqual(keyvals['Exif.Photo.MakerNote'], "(Binary value suppressed)")


    def test_get_camera_designation(self):
        """
        Verify that we can give camera names to images depending on both model and serial number.
        """
        self.assertEqual(self.img_0071.get_camera_designation(), "7Dmk1_First")
        self.assertEqual(self.img_0072.get_camera_designation(), "7Dmk1_Second")
        self.assertEqual(self.img_0080.get_camera_designation(), "80Dmk1")
        #_set_serial_number

    def test_datetime_extraction(self):
        """
        Verify that we can extract original datetime for use in new filenames.
        """

        expected = '2017_07_30_024414'
        actual = self.img_0071.get_new_filename()
        msg = "Expected date '%s' to be in new filename '%s', but it wasn't." % (expected, actual)
        self.assertTrue(expected in actual, msg)

        self.assertTrue('2017_02_30_024414' in self.img_0072.get_new_filename())
        self.assertTrue('2018_08_30_024414' in self.img_0080.get_new_filename())

    def test_filename_mangling(self):
        """
        Verify that we can split abspaths from constructors into filepart and directory parts.
        """
        self.assertEqual(self.img_0071.get_old_filename(), "IMG_0071.JPG")

        msg = "Expected new file name to end with 'IMG_0071.jpg', got '%s'" % self.img_0071.get_new_filename()
        self.assertTrue(self.img_0071.get_new_filename().endswith('IMG_0071.jpg'), msg)

        self.assertTrue('7Dmk1_First' in self.img_0071.get_new_filename())

    def test_gen_mv_cmds(self):
        """
        Verify that we can generate move commands.
        """
        cmds = self.img_0071.generate_mv_cmds()
        dcim_abspath = os.path.abspath('./DCIM/')
        cmd0 = "cd '%s/'" % dcim_abspath
        self.assertEqual(cmd0, cmds[0])
        self.assertEqual("mv -v -n 'IMG_0071.JPG' '2017_07_30_024414_7Dmk1_First_IMG_0071.jpg'", cmds[1])


    def test_filename_exceptions(self):
        """
        Verify that we get exceptions on certain cases.
        """
        try:
            dcim_none = DcimImage(None)
        except Exception as e:
            self.fail("DcimImages should be able to handle None arguments as special cases, got '%s'." % str(e))

        try:
            dcim_dir = DcimImage(os.path.abspath('./'))
        except ValueError as e:
            self.assertTrue('s not seem to be a file' in str(e))

        try:
            dcim_inexistent_dir = DcimImage(os.path.abspath('./Vpy10RIX9AVr2MZsqFpm5SBJ/'))
        except ValueError as e:
            self.assertTrue('ich does not seem to exist.' in str(e))

        try:
            dcim_inexistent_file = DcimImage(os.path.abspath('./IMG_5555.JPG'))
        except ValueError as e:
            self.assertTrue('ich does not seem to exist.' in str(e))

        try:
            dcim_not_abspath = DcimImage('DCIM/Wedding/IMG_7003.JPG')
        except ValueError as e:
            self.assertTrue('t seem to be an absolute path.' in str(e))






if __name__ == '__main__':
    unittest.main()
