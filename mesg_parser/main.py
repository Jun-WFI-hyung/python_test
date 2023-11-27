import sys
from typing import Tuple

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QLineEdit, QCheckBox, QTableWidgetItem, QHBoxLayout, QWidget, QHeaderView, QComboBox, QVBoxLayout
from PyQt5.QtCore import QTimer, Qt, pyqtSignal, QSize, QEvent

from main_ui import Ui_MainWindow

class TypeComboBox(QWidget):
    def __init__(self):
        super().__init__()

        # 콤보박스 초기화
        self.comboBox = QComboBox(self)
        self.comboBox.addItems(["Option 1", "Option 2", "Option 3"])

        # 이벤트 필터 설정
        self.comboBox.installEventFilter(self)

        # 레이아웃 설정
        # layout = QVBoxLayout()
        # layout.addWidget(self.comboBox)
        # self.setLayout(layout)
        self.setFixedSize(QSize(111,30))

    def eventFilter(self, obj, event):
        if obj == self.comboBox and event.type() == QEvent.Wheel:
            # 콤보박스에서 마우스 휠 이벤트를 무시
            return True
        return super().eventFilter(obj, event)

class ParserMainWindow(QMainWindow):
    relay_on_signal = pyqtSignal()
    relay_off_signal = pyqtSignal()
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.main_ui: Ui_MainWindow = Ui_MainWindow()
        self.main_ui.setupUi(self)
        self.main_ui.tableWidget.setColumnWidth(1, 111)
        self.main_ui.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)
        self.main_ui.add_button.clicked.connect(self.add_column)

    def UI_update(self):
        self.main_ui.retranslateUi(self)
        
    def add_column(self) -> None:
        row = self.main_ui.tableWidget.rowCount()
        self.main_ui.tableWidget.insertRow(row)
        combobox = self.get_combobox(row)
        # combobox.setObjectName(f'cb_{row}')
        # combobox.setFixedSize(QSize(111,30))
        # layout = QHBoxLayout()
        # layout.addWidget(combobox, stretch=0, alignment=Qt.AlignCenter)
        # container = QWidget()
        # container.setLayout(layout)
        self.main_ui.tableWidget.setCellWidget(row, 1, combobox)
        
        # text = "ddddd"
        # item = QTableWidgetItem(text)
        # item.setTextAlignment(Qt.AlignCenter)
        # self.main_ui.tableWidget.setItem(row, 1, item)
        self.UI_update()
        
    def get_combobox(self, row: int) -> TypeComboBox:
        combobox = TypeComboBox()
        combobox.setObjectName(f'cb_{row}')
        combobox.setFixedSize(QSize(111,30))
        # combobox.addItem("Char")
        # combobox.addItem("U_Char")
        # combobox.addItem("Short")
        # combobox.addItem("U_Short")
        # combobox.addItem("Int")
        # combobox.addItem("U_Int")
        # combobox.addItem("Long")
        # combobox.addItem("U_Long")
        # combobox.addItem("LongLong")
        # combobox.addItem("U_LongLong")
        # combobox.addItem("Float")
        # combobox.addItem("Double")
        # combobox.addItem("Char[]")
        return combobox
    




if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication(sys.argv)
    window = ParserMainWindow()
    window.show()
    sys.exit(app.exec_())
    