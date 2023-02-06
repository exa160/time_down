import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFontDatabase, QFont
from PyQt6.QtWidgets import QApplication, QLabel


class Demo(QLabel):
    def __init__(self):
        super(Demo, self).__init__()
        font_data = QFontDatabase.addApplicationFont('./font/no59.ttf')
        font_name = QFontDatabase.applicationFontFamilies(font_data)
        font = QFont(font_name)
        # font.setLetterSpacing(QFont.SpacingType.PercentageSpacing, 85)
        self.resize(180, 50)
        self.setProperty('id', '1')
        self.setText('距摸鱼结束')
        self.setFont(font)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint |   # 窗口无边框
                            Qt.WindowType.WindowStaysOnTopHint)   # 窗口置顶
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)  # 窗口透明
        self.setStyleSheet(f'QLabel{{color:white;font-size:30px ;}}')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Demo()
    mainWindow.show()
    sys.exit(app.exec())
