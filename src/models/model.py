from PyQt5.QtCore import QObject, pyqtSignal

from domain.dont_sleep import DontSleep


class Model(QObject):
    amount_changed = pyqtSignal(int)
    dont_sleep_started_changed = pyqtSignal(bool)

    def __init__(self):
        super().__init__()

        self._idle_time = 0
        self._dont_sleep_started = False
        self._dont_sleep = DontSleep()

    @property
    def idle_time(self):
        return self._idle_time

    @idle_time.setter
    def amount(self, value):
        self._idle_time = value
        self._dont_sleep.idle_time = value
        self.amount_changed.emit(value)

    def start_stop(self):
        self._dont_sleep_started = not self._dont_sleep_started
        self.dont_sleep_started_changed.emit(self._dont_sleep_started)
        if self._dont_sleep_started:
            self._dont_sleep.start()
        else:
            self._dont_sleep.stop()


    @property
    def dont_sleep_started(self):
        return self._dont_sleep_started

    @dont_sleep_started.setter
    def dont_sleep_started(self, value):
        self._dont_sleep_started = value
        self.dont_sleep_started_changed.emit(value)


