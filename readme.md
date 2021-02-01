## Usage

1. Install Dependencies: ```pip3 install -r requirements.txt```
2. Start App: ```python3 src/__main__.py```

sudo pacman -S tk
NOTE: You must install tkinter on Linux to use MouseInfo. Run the following: sudo apt-get install python3-tk python3-dev

## Develop

1. Install Dependencies: ```pip3 install -r requirements.txt```
2. Install PyQt: ```pip install pyqt5```

Convert QT-Creatorfile to Pythonfile

```bash
pyuic5 .\src\resources\mainView.ui -o .\src\views\main_view_ui.py
```