import os.path
import sys
import time

from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import QApplication, QMenu

from timer import start_time, get_hours, diff_time_cal
from units.constant import config
from widget.gui_label import LabelGui


class CountDown(LabelGui):
    def __init__(self):
        super(CountDown, self).__init__()

        self.diff_pos = None    # 点击组件时相对组件左上角位置

        self.init_ui()
        self.timer_thread = MyThread()
        self.timer_thread.signal.connect(self.set_text_num)
        self.timer_thread.start()

    def init_ui(self):
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint |    # 窗口无边框
                            Qt.WindowType.WindowStaysOnTopHint |   # 窗口置顶
                            Qt.WindowType.SplashScreen)            # 隐藏任务栏图标
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)  # 窗口透明
        self.setGeometry(config.qt_pos_x, config.qt_pos_y, 180, 80)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        # print(event.scenePosition(), event.globalPosition(), event.pos(), self.pos())
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.diff_pos = event.scenePosition()
            event.accept()

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.move((event.globalPosition() - self.diff_pos).toPoint())
            event.accept()

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        pos = self.frameGeometry().topLeft()
        config.qt_pos_x, config.qt_pos_y = pos.x(), pos.y()
        config.save()
        event.accept()

    def contextMenuEvent(self, event):
        context_menu = QMenu(self)
        menu_setting = context_menu.addAction("设置")
        menu_quit = context_menu.addAction("退出")
        action = context_menu.exec(self.mapToGlobal(event.pos()))
        if action == menu_setting:
            pass
        elif action == menu_quit:
            QApplication.instance().quit()


class MyThread(QThread):
    signal = pyqtSignal(str, str, str)

    def __init__(self):
        super(MyThread, self).__init__()

    def send_signal(self, hour, minute, second):
        if hour > 0:
            text, unit_c, unit_e = f'{hour}', '小时', 'HOURS'
        elif minute > 0:
            text, unit_c, unit_e = f'{minute}', '分', 'MINUTES'
        elif second >= 0:
            text, unit_c, unit_e = f'{second}', '秒', 'SECONDS'
        else:
            return
        self.signal.emit(text, unit_c, unit_e)

    def run(self):
        last_start_datetime = start_time()
        next_start_datetime = last_start_datetime
        temp_hour, temp_minute, temp_second = 0, 0, 0

        while True:
            if next_start_datetime != last_start_datetime:
                last_start_datetime = next_start_datetime
            now, hour, minute, second = diff_time_cal(next_start_datetime)
            if now.hour <= get_hours(now.weekday()):
                if second != temp_second:
                    self.send_signal(hour, minute, second)
                    temp_second = second
            else:
                if next_start_datetime == last_start_datetime:
                    next_start_datetime = start_time()
                    now, hour, minute, second = diff_time_cal(next_start_datetime)
                if second != temp_second:
                    self.send_signal(hour, minute, second)
                    temp_second = second

            time.sleep(0.05)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = CountDown()
    mainWindow.show()
    sys.exit(app.exec())
