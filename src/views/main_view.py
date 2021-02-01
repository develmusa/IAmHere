from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from views.main_view_ui import Ui_MainWindow


class MainView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        # connection ui-widget to controller
        self._ui.spinBox.valueChanged.connect(self._main_controller.change_amount)

        # listen for model event signals
        self._model.amount_changed.connect(self.on_amount_changed)

        # set a default value
        self._main_controller.change_amount(5)

        # Lambda to execute function with value
        self._ui.pushButton.clicked.connect(lambda: self._main_controller.start_stop())

        # listen for model event signals
        self._model.dont_sleep_started_changed.connect(self.on_dont_sleep_started_changed)

    @pyqtSlot(int)
    def on_amount_changed(self, value):
        self._ui.spinBox.setValue(value)

    @pyqtSlot(bool)
    def on_dont_sleep_started_changed(self, value):
        if value:
            self._ui.pushButton.setText("Stop")
        else: 
            self._ui.pushButton.setText("Start")