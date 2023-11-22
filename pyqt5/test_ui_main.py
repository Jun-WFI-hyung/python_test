import sys
from typing import Tuple

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QLineEdit
from PyQt5.QtCore import QTimer, Qt, pyqtSignal

from test_ui import Ui_MainWindow

class emulWindow(QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.main_ui: Ui_MainWindow = Ui_MainWindow()
        self.main_ui.setupUi(self)
        # UI update setting
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.UI_update)
        self.timer.start(100) # 0.1sec
        
    def UI_update(self):
        # check connect state
        self.main_ui.retranslateUi(self)
        self.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = emulWindow()
    window.show()
    sys.exit(app.exec_())
    