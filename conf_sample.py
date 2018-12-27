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


def tags2shorthand(tags):
    """
    Config section that allows you to add your own model shorthands depending
    on the exif tags from a image.

    Copy this file to conf.py if you want to override it.
    """
    model = tags['Model']

    if model == 'Canon EOS 7D':
        serial = tags['SerialNumber']
        if '0123456789' in serial:
            return '7Dmk1_First'
        elif '0777776789' in serial:
            return '7Dmk1_Second'

    model_mapping = {
      'Canon EOS 5D' : '5Dmk1',
      'Canon EOS 5D Mark II' : '5Dmk2',
      'Canon EOS 5D Mark III' : '5Dmk3',
      'Canon EOS 5D Mark IV' : '5Dmk4',
      'Canon EOS 6D' : '6Dmk1',
      'Canon EOS 6D Mark II' : '6Dmk2',
      'Canon EOS 7D' : '7Dmk1',
      'Canon EOS 7D Mark II' : '7Dmk2',
      'Canon EOS 20D' : '20D',
      'Canon EOS 30D' : '30D',
      'Canon EOS 40D' : '40D',
      'Canon EOS 50D' : '50D',
      'Canon EOS 60D' : '60D',
      'Canon EOS 70D' : '70D',
      'Canon EOS 80D' : '80D',
      'Canon EOS 90D' : '90D',
      'Canon EOS 300D' : '300D',
      'Canon EOS 350D' : '350D',
      'Canon EOS 400D' : '400D',
      'Canon EOS 450D' : '450D',
      'Canon EOS 500D' : '500D',
      'Canon EOS 550D' : '550D',
      'Canon EOS 600D' : '600D',
      'Canon EOS 650D' : '650D',
      'Canon EOS 700D' : '700D',
      'Canon EOS 750D' : '750D',
      'Canon EOS 800D' : '800D',
      'Canon EOS 850D' : '850D',
      'Canon EOS Kiss Digital X' : 'KissX',
      'EOS Digital Rebel XSi / 450D / Kiss X2' : 'KissX2',
      'EOS Digital Rebel XTi / 400D / Kiss Digital X' : 'KissX',
      'Canon IXY 90F' : '90F',
      'Canon PowerShot A4000 IS' : 'A4000',
      'Canon PowerShot A490' : 'A490',
      'Canon PowerShot G15' : 'G15',
      'Canon PowerShot S110' : 'S110',
      'Canon PowerShot S45' : 'S45',
      'Canon PowerShot S95' : 'S95',
      'Canon PowerShot SX120 IS' : 'SX120',
      'Canon PowerShot SX200 IS' : 'SX200',
      'Canon PowerShot SX240 HS' : 'SX240',
      'iPhone 4S' : 'iPhone4S',
      'iPhone 5' : 'iPhone5',
      'iPhone 5s' : 'iPhone5s',
      'iPhone 6' : 'iPhone6',
      'iPhone 6 Plus' : 'iPhone6p',
      'iPhone 6s' : 'iPhone6s',
      'iPhone 7' : 'iPhone7',
      'NIKON 1 J5' : '1J5',
}

    if model in model_mapping:
        return model_mapping['Model']
