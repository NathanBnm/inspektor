#!/usr/bin/env python3
'''
   Copyright 2020 Adi Hezral <hezral@gmail.com>

   This file is part of Inspektor.

    Inspektor is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Inspektor is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Inspektor.  If not, see <http://www.gnu.org/licenses/>.
'''
import os
import sys

# Get launch script dir
launch_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

# # Update sys.path to include modules
# if launch_dir == "/usr/bin":
#     modules_path = "/usr/share/com.github.hezral.inspektor/"
# else:
#     modules_path = launch_dir + "/inspektor"

modules_path = "/usr/share/com.github.hezral.inspektor/"

sys.path.insert(0, modules_path)

print(sys.path)

try:
    import application
except ImportError:
    print("Failed to import module main.py!")
    print("Installation was assumed to be at:", modules_path)
    sys.exit(1)

app = application.InspektorApp()
app.run(sys.argv)

