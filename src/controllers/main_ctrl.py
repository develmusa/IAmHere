from PyQt5.QtCore import QObject, pyqtSlot


class MainController(QObject):
    def __init__(self, model):
        super().__init__()
        self._model = model

    # Takes Signal from UI
    @pyqtSlot(int)
    def change_amount(self, value):
        self._model.amount = value

    @pyqtSlot()
    def start_stop(self):
        self._model.start_stop()