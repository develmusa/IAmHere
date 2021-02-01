from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QObject
import os

class IconHelper(QObject):
    def __init__(self, app, tray, model):
        super().__init__()
        self.ICONS_DIR_STR = "ressources"
        self._icon = QtGui.QIcon(self.get_icon_path("icon.png"))
        self._icon_active = QtGui.QIcon(self.get_icon_path("icon_active.png"))

        self._model = model
        self._app = app
        self._tray = tray

        self._app.setWindowIcon(self._icon)
        self._tray.setIcon(self._icon)

        # listen for model event signals
        self._model.dont_sleep_started_changed.connect(self.on_dont_sleep_started_changed)


    @pyqtSlot(bool)
    def on_dont_sleep_started_changed(self, value):
        if value:
            self._app.setWindowIcon(self._icon_active)
            self._tray.setIcon(self._icon_active)

        else: 
            self._app.setWindowIcon(self._icon)
            self._tray.setIcon(self._icon)

    def get_base_dir(self) -> str:
        base_dir_str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print(base_dir_str)
        print(os.path.dirname(os.path.abspath(__file__)))
        # -__file__ is the file that was started, in other words mindfulness-at-the-computer.py
        return base_dir_str

    def get_icon_path(self, i_file_name: str) -> str:
        ret_icon_path_str = os.path.join(self.get_base_dir(), self.ICONS_DIR_STR, i_file_name)
        print(ret_icon_path_str)
        return ret_icon_path_str


    