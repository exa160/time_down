import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFontDatabase, QFont
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout


def get_font(font_path):
    font_data = QFontDatabase.addApplicationFont(font_path)
    font_name = QFontDatabase.applicationFontFamilies(font_data)
    return QFont(font_name)


class CountDown(QWidget):
    def __init__(self):
        super(CountDown, self).__init__()

        self.init_ui()

        text_font = get_font('./font/no59.ttf')
        num_font = get_font('./font/1451.otf')
        text_font.setLetterSpacing(QFont.SpacingType.PercentageSpacing, 88)  # 字间距
        # num_font.setLetterSpacing(QFont.SpacingType.PercentageSpacing, 1)  # 字间距

        grid = QGridLayout()
        self.setLayout(grid)
        # grid.setHorizontalSpacing(1)  # Grid布局行间距
        grid.setVerticalSpacing(0)  # Grid布局行间距
        # grid.setContentsMargins(0, 0, 0, 0)     # Grid布局行间距

        self.space_label = QLabel()
        self.space_label.resize(50, 50)
        self.space_label.setProperty('space_label', '0')

        self.first_line_label = QLabel()
        # self.first_line_label.resize(10, 30)
        self.first_line_label.setProperty('first_line', '1')
        self.first_line_label.setText('距摸鱼结束')
        self.first_line_label.setFont(text_font)

        self.second_line_label = QLabel()
        # self.second_line_label.resize(10, 30)
        self.second_line_label.setProperty('second_line', '2')
        self.second_line_label.setText('还剩')
        self.second_line_label.setFont(text_font)

        self.second_line_label_2 = QLabel()
        # self.second_line_label_2.resize(10, 30)
        self.second_line_label_2.setProperty('third_line', '4')
        self.second_line_label_2.setText('分')
        self.second_line_label_2.setFont(text_font)

        self.number_label = QLabel()
        self.number_label.resize(1, 1)
        self.number_label.setProperty('number_line', '3')
        self.number_label.setText(' 27 ')
        self.number_label.setFont(num_font)
        self.number_label.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.number_label.setMargin(-16)  # 内边距
        self.number_label.setStyleSheet(f'QLabel{{color:red;'
                                        f'font-size:76px ;}}')

        self.l_label = QLabel()
        self.l_label.resize(50, 50)
        self.l_label.setProperty('l_line', '5')
        self.l_label.setText('|')
        self.l_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.l_label.setFont(num_font)
        self.l_label.setMargin(-5)  # 内边距
        self.l_label.setContentsMargins(0, 0, 0, 1000)
        self.l_label.setStyleSheet(f'QLabel{{color:red;font-size:65px ;}}')

        self.e_label = QLabel()
        self.e_label.resize(50, 50)
        self.e_label.setProperty('e_line', '6')
        self.e_label.setText('THE CATCH FISH FINISH\n'
                             'IN 27 MINUTES')
        self.e_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.e_label.setFont(text_font)
        self.e_label.setStyleSheet(f'QLabel{{font-size:20px ;}}')

        # self.e_label.setMargin(-5)  # 内边距
        # self.e_label.setContentsMargins(0, 0, 0, 1000)

        grid.addWidget(self.first_line_label, 1, 0, 1, 3)   # 第一行，占3格
        grid.addWidget(self.second_line_label, 2, 2)        # 第二行，占1格
        grid.addWidget(self.space_label, 2, 4, 2, 5)
        grid.addWidget(self.second_line_label_2, 2, 6)
        grid.addWidget(self.l_label, 2, 0, 3, 2)            # 第二行，占4格
        grid.addWidget(self.number_label, 1, 3, 2, 3)
        grid.addWidget(self.e_label, 3, 2, 3, 5)

        self.setStyleSheet(f'QLabel{{color:white;font-size:30px ;}}')

    def init_ui(self):
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint |  # 窗口无边框
                            Qt.WindowType.WindowStaysOnTopHint|
                            Qt.WindowType.SplashScreen)  # 窗口置顶
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)  # 窗口透明


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = CountDown()
    mainWindow.show()
    sys.exit(app.exec())
