from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QEventLoop, QTimer

app = QApplication([])

loop = QEventLoop()

# QTimer을 사용하여 몇 초 후에 이벤트 루프를 종료하는 예제
timer = QTimer()
timer.timeout.connect(loop.quit)
timer.start(5000)  # 5초 후에 timeout 시그널이 발생하도록 설정

# 이벤트 루프 시작
loop.exec_()

print("Event loop has exited.")

# Queue를 이용한 종료시그널 방법도 있긴 함.