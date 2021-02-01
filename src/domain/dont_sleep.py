import pyautogui 
import threading

class DontSleep():
    def __init__(self):

        self._is_running = False
        self._idle_time = 5
        self._move_distance = 10
        self._last_position = pyautogui.position()
        self._timer = None

    @property
    def idle_time(self):
        return self._idle_time

    @idle_time.setter
    def idle_time(self, value):
        self._idle_time = value

    def move(self):
        pyautogui.moveRel(0, -self._move_distance)
        pyautogui.moveRel(0, self._move_distance)        

    def stay_awake(self):
        if self._is_running:
            position_now = pyautogui.position()
            if self._last_position == position_now:
                self.move()
            else:
                self._last_position = position_now
            self._timer = threading.Timer(self._idle_time, self.stay_awake)
            self._timer.start()

    def start(self):
        self._is_running = True
        self.stay_awake()

    def stop(self):
        self._is_running = False
        if self._timer:
            self._timer.cancel()
