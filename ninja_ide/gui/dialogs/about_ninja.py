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

import webbrowser

from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QVBoxLayout
from PyQt4.QtGui import QHBoxLayout
from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QPixmap
from PyQt4.QtCore import Qt
from PyQt4.QtCore import QSize
from PyQt4.QtCore import SIGNAL

import ninja_ide
from ninja_ide import resources


class AboutNinja(QDialog):

    def __init__(self, parent=None):
        QDialog.__init__(self, parent, Qt.Dialog)
        self.setWindowTitle(self.tr("About MOTIVATION-IDE"))
        self.setMaximumSize(QSize(0, 0))

        vbox = QVBoxLayout(self)

        #Create an icon for the Dialog
        pixmap = QPixmap(resources.IMAGES['icon'])
        self.lblIcon = QLabel()
        self.lblIcon.setPixmap(pixmap)

        hbox = QHBoxLayout()
        hbox.addWidget(self.lblIcon)

        lblTitle = QLabel(
                '<h1>MOTIVATION-IDE</h1>\n<i>by Motivation Software - Based on NINJA-IDE<i>')
        lblTitle.setTextFormat(Qt.RichText)
        lblTitle.setAlignment(Qt.AlignLeft)
        hbox.addWidget(lblTitle)
        vbox.addLayout(hbox)
        #Add description
        vbox.addWidget(QLabel(
self.tr("""MOTIVATION-IDE, is a
Linux integrated development environment specially designed
to build Python Applications.
MOTIVATION-IDE provides tools to simplify the Python-software development
and handles all kinds of situations thanks to its rich extensibility.""")))
        vbox.addWidget(QLabel(self.tr("Version: %s") % ninja_ide.__version__))
        link_ninja = QLabel(
            self.tr('Website: <a href="%s"><span style=" '
                'text-decoration: underline; color:#ff9e21;">'
                '%s</span></a>') %
                (ninja_ide.__url__, ninja_ide.__url__))
        vbox.addWidget(link_ninja)
        link_source = QLabel(
            self.tr('Source Code: <a href="%s"><span style=" '
            'text-decoration: underline; color:#ff9e21;">%s</span></a>') %
                (ninja_ide.__source__, ninja_ide.__source__))
        vbox.addWidget(link_source)

        self.connect(link_ninja, SIGNAL("linkActivated(QString)"),
            self.link_activated)
        self.connect(link_source, SIGNAL("linkActivated(QString)"),
            self.link_activated)

    def link_activated(self, link):
        webbrowser.open(str(link))
