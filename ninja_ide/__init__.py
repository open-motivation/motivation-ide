# -*- coding: utf-8 -*-
#
# This file is part of NINJA-IDE (http://ninja-ide.org).
#
# NINJA-IDE is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# any later version.
#
# NINJA-IDE is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NINJA-IDE; If not, see <http://www.gnu.org/licenses/>.

from __future__ import absolute_import

###############################################################################
# METADATA
###############################################################################

__prj__ = "MOTIVATION-IDE"
__original_author__ = "The NINJA-IDE Team"
__author__ = "Motivation Software"
__mail__ = "info (at) motivation (dot) ga"
__url__ = "http://www.motivation.ga"
__source__ = "http://motivation.ga/ide/source"
__version__ = "2.3"
__license__ = "GPL3"

###############################################################################
# DOC
###############################################################################

"""MOTIVATION-IDE is a Linux/X11 integrated development environment (IDE).
Allows developers to create applications for several purposes using all the
tools and utilities of MOTIVATION-IDE, making the task of writing software easier
and more enjoyable.
"""


###############################################################################
# SET PYQT API 2
###############################################################################

import sip
API_NAMES = ["QDate", "QDateTime", "QString", "QTime", "QUrl", "QTextStream",
             "QVariant"]
API_VERSION = 2
for name in API_NAMES:
    sip.setapi(name, API_VERSION)


###############################################################################
# START
###############################################################################


def setup_and_run():
    # import only on run
    # Dont import always this, setup.py will fail
    from ninja_ide import core
    from multiprocessing import freeze_support

    # Used to support multiprocessing on windows packages
    freeze_support()

    # Run NINJA-IDE
    core.run_ninja()
