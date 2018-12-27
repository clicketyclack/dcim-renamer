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

import subprocess
import re

class DcimImage(object):


    def __init__(self, absfile):
        self._exif_tags = None

        if absfile != None:
            stdout = self.get_exiv2_stdout(absfile)
            self._exif_tags = self.keyvals_from_exiv2_stdout(stdout)
            self._extract_maker_specifics()

    def get_exiv2_stdout(self, absfile):
        """
        Get raw stdout when running exiv2 on a file.

        absfile - Target file.
        returns - Raw std out.
        """
        cmd = "/usr/bin/exiv2"
        full_cmd = [cmd, '-PEkt', absfile, '-q']
        result = subprocess.run(full_cmd, stdout=subprocess.PIPE)
        toreturn = result.stdout.decode('utf-8')
        if toreturn is None:
            raise Exception("Could not get stdout from exiv2 for file '%s'" % absfile)

        return toreturn


    def keyvals_from_exiv2_stdout(self, stdout):
        """
        stdout must be passed in as a multi-line string.

        Converts exif2-style stdout into key-value dict.
        """
        if str(stdout) != stdout:
            raise TypeError("kjfdh '%s'" % stdout)
        lines = stdout.split("\n")
        lines = [l.strip() for l in lines if len(l.strip()) > 3]


        toreturn = {}
        for line in lines:
            if line in ['Exif.Image.Copyright', 'Exif.Canon.OwnerName', 'Exif.Photo.CameraOwnerName',
                        'Exif.Image.Artist', 'Exif.Photo.ComponentsConfiguration', 'Exif.CanonCs.FlashDetails',
                        'Exif.CanonCs.FocusContinuous', 'Exif.CanonPi.AFPointsUsed20D',
                        'Exif.Nikon3.FlashSetting', 'Exif.Nikon3.FlashDevice', 'Exif.Photo.UserComment',
                        'Exif.Nikon3.VariProgram', 'Exif.Image.ImageDescription', 'Exif.Photo.CameraOwnerName']:
                # These lines are valid lines without values, they only show the key.
                continue
            res = re.match('^(?P<key>[^ ]+) +(?P<val>.*)', line)
            if res is None:
                raise TypeError("Unhandled exiv2 output line '%s'" % line)
            toreturn[res.group('key').strip()] = res.group('val').strip()

        #print(toreturn)
        return toreturn


    def _extract_maker_specifics(self):
        """
        Not all camera makers put the serial number in the same tag.

        Call this method after reading exif2 tags
        """

        if self._exif_tags is None:
            raise TypeError("%._extract_maker_specifics() called without successfull exif tag read." % str(self))

        if 'Exif.Canon.SerialNumber' in self._exif_tags:
            self._exif_tags['SerialNumber'] = self._exif_tags['Exif.Canon.SerialNumber']
        elif 'Exif.Photo.BodySerialNumber' in self._exif_tags:
            self._exif_tags['SerialNumber'] = self._exif_tags['Exif.Photo.BodySerialNumber']
        else:
            raise TypeError("Could not extract SerialNumber from keys '%s'" % self._exif_tags.keys())


        if 'Exif.Image.Model' in self._exif_tags:
            self._exif_tags['Model'] = self._exif_tags['Exif.Image.Model']
        else:
            raise TypeError("Could not extract model from keys '%s'" % self._exif_tags.keys())


        if 'Exif.Photo.DateTimeOriginal' in self._exif_tags:
            self._exif_tags['DateTimeOriginal'] = self._exif_tags['Exif.Photo.DateTimeOriginal']
        else:
            raise TypeError("Could not extract DateTimeOriginal from keys '%s'" % self._exif_tags.keys())



    def get_camera_designation(self, exif_tags=None):
        """
        Return short designation for camera.
        """

        tags = exif_tags

        if tags is None:
            tags = self._exif_tags

        if tags is None:
            raise TypeError("get_camera_designation got none exif_tags")

        if 'Model' not in tags:
            keys = tags.keys()
            keys = [k for k in keys if 'odel' in k]
            msg = "%s Could not determine model from exif keys. Potential keys are '%s'" % (str(self), keys)
            raise TypeError(msg)

        model = tags['Model']

        if model == 'Canon EOS 7D':
            serial = tags['SerialNumber']
            if '3456' in serial:
                return '7Dmk1_First'
            else:
                return '7Dmk1_Second'

        if model == 'Canon EOS 80D':
            return '80Dmk1'



if __name__ == '__main__':
    pass
