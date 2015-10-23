#!/usr/bin/env python

#############################################################################
##
## This file is part of Taurus, a Tango User Interface Library
## 
## http://www.tango-controls.org/static/taurus/latest/doc/html/index.html
##
## Copyright 2011 CELLS / ALBA Synchrotron, Bellaterra, Spain
## 
## Taurus is free software: you can redistribute it and/or modify
## it under the terms of the GNU Lesser General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
## 
## Taurus is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU Lesser General Public License for more details.
## 
## You should have received a copy of the GNU Lesser General Public License
## along with Taurus.  If not, see <http://www.gnu.org/licenses/>.
##
#############################################################################

import fandango,vacca,traceback
#from panic.gui import AlarmGUI
from taurus.qt.qtgui.taurusgui.utils import PanelDescription
from panic.gui.gui import AlarmGUI



class VaccaPanic(AlarmGUI):
    """
    It is a class that inherits from AlarmGUI.

    This Panel show the alarms, and allow to interact with them.

    """

    @staticmethod
    def getPanelDescription(name='Panic',model=''):
        """
        :param name: Name for Panel
        :param model: Model for the Panel
        :return: Panel Descritption Object
        """
        return PanelDescription(name,'vacca.vaccaPanic.VaccaPanic',model)

    @staticmethod
    def getDefaultIcon():
        """
        :return: The Default Icon Path.
        """
        path = 'image/icons/panic.gif'
        return path

    @classmethod
    def __test__(klass,arg=None):
        from PyQt4 import Qt
        qapp = Qt.QApplication([])
        i = klass()
        print i
        print klass
        i.show()

        
if __name__ == '__main__':
    import sys
    VaccaPanic.__test__(*sys.argv[1:])
        
