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

class Exiv2Reader(object):

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

if __name__ == '__main__':
    pass
