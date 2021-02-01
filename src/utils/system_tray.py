from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QAction
from PyQt5.QtCore import pyqtSlot

class SystemTray(QSystemTrayIcon):
    def __init__(self, app, model, main_ctrl, main_view, parent=None):
        super(SystemTray, self).__init__(parent)

        self._model = model
        self._app = app
        self._main_ctrl = main_ctrl
        self._main_view = main_view
        
        self.setVisible(True)
        
        # setup menu
        menu = QMenu(parent)
        self.start_stop_action = menu.addAction("Start")
        self.start_stop_action.triggered.connect(lambda: self._main_ctrl.start_stop())
        exit_action = menu.addAction("Exit")
        exit_action.triggered.connect(self._app.quit)
        self.setContextMenu(menu)

        # open main view on click
        self.activated.connect(lambda: self._main_view.show())

        # listen for model event signals
        self._model.dont_sleep_started_changed.connect(self.on_dont_sleep_started_changed)


    @pyqtSlot(bool)
    def on_dont_sleep_started_changed(self, value):
        if value:
            self.start_stop_action.setText("Stop")
            self._app.main_view.show()

        else: 
            self.start_stop_action.setText("Start")
            self._app.main_view.show()