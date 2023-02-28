import os

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFontDatabase, QFont, QEnterEvent
from PyQt6.QtWidgets import QLabel, QMainWindow, QWidget, QGridLayout

from units import base_path, config


class LabelGui(QMainWindow):
    def __init__(self):
        super(LabelGui, self).__init__()
        self.main_widget = None  # 主框架组件

        self.text_font = None  # 文本字体
        self.num_font = None  # 数字字体

        self.space_label = None  # 空白占位
        self.first_line_label = None  # 第一行文字
        self.second_line_label = None  # 第二行文字-1
        self.second_line_label_2 = None  # 第二行文字-2-单位
        self.number_label = None  # 数字
        self.l_label = None  # 文本-|
        self.e_label = None  # 英文文本
        self.label_init()

    def label_init(self) -> None:
        self.init_font()
        self.init_space_label()
        self.init_first_line_label()
        self.init_second_line_label()
        self.init_second_line_label_2()
        self.init_number_label()
        self.init_l_label()
        self.init_e_label()
        self.init_main_widget()

    def init_main_widget(self) -> None:
        """
        初始化主组件并
        :return: None
        """
        grid = QGridLayout()
        # grid.setHorizontalSpacing(1)  # Grid布局行间距
        grid.setVerticalSpacing(0)
        # grid.setContentsMargins(0, 0, 0, 0)
        grid.addWidget(self.space_label, 0, 0, 6, 8)
        grid.addWidget(self.first_line_label, 1, 0, 1, 3)  # 第一行，占3格
        grid.addWidget(self.second_line_label, 2, 2)  # 第二行，占1格
        grid.addWidget(self.second_line_label_2, 2, 6)
        grid.addWidget(self.l_label, 2, 0, 3, 2)  # 第二行，占4格
        grid.addWidget(self.number_label, 1, 3, 2, 3)
        grid.addWidget(self.e_label, 3, 2, 3, 5)

        self.main_widget = QWidget()
        self.main_widget.setLayout(grid)
        self.setCentralWidget(self.main_widget)
        self.setStyleSheet(f'QLabel{{color:white;font-size:30px ;}}')

    def init_font(self) -> None:
        self.text_font = self.get_font(os.path.join(base_path, 'font', 'no59.ttf'))  # 注意放入字体
        self.num_font = self.get_font(os.path.join(base_path, 'font', '1451.otf'))
        self.text_font.setLetterSpacing(QFont.SpacingType.PercentageSpacing, 88)  # 字间距
        # self.num_font.setLetterSpacing(QFont.SpacingType.PercentageSpacing, 1)  # 字间距

    def init_space_label(self) -> None:
        self.space_label = QLabel()
        self.space_label.resize(50, 50)
        self.space_label.setProperty('space_label', '0')

    def init_first_line_label(self) -> None:
        self.first_line_label = QLabel()
        self.first_line_label.setProperty('first_line', '1')
        self.first_line_label.setText(config.qt_text.get('LABEL_1'))
        self.first_line_label.setFont(self.text_font)

    def init_second_line_label(self) -> None:
        self.second_line_label = QLabel()
        self.second_line_label.setProperty('second_line', '2')
        self.second_line_label.setText(config.qt_text.get('LABEL_2'))
        self.second_line_label.setFont(self.text_font)

    def init_second_line_label_2(self) -> None:
        self.second_line_label_2 = QLabel()
        self.second_line_label_2.setProperty('third_line', '4')
        self.second_line_label_2.setText(config.qt_text.get('LABEL_3'))
        self.second_line_label_2.setFont(self.text_font)

    def init_number_label(self) -> None:
        self.number_label = QLabel()
        self.number_label.resize(1, 1)
        self.number_label.setProperty('number_line', '3')
        self.number_label.setText(config.qt_text.get('LABEL_NUM').format(text=27))
        self.number_label.setFont(self.num_font)
        self.number_label.setAlignment(Qt.AlignmentFlag.AlignBottom |
                                       Qt.AlignmentFlag.AlignRight)
        self.number_label.setMargin(-16)  # 内边距
        self.number_label.setStyleSheet(f'QLabel{{color:red;'
                                        f'font-size:76px ;}}')

    def init_l_label(self) -> None:
        self.l_label = QLabel()
        self.l_label.resize(50, 50)
        self.l_label.setProperty('l_line', '5')
        self.l_label.setText('|')
        self.l_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.l_label.setFont(self.num_font)
        self.l_label.setMargin(-6)  # 内边距
        # self.l_label.setContentsMargins(100, 0, 0, 0)  # 边距
        self.l_label.setStyleSheet(f'QLabel{{color:red;font-size:65px ;}}')

    def init_e_label(self) -> None:
        self.e_label = QLabel()
        self.e_label.resize(150, 80)
        self.e_label.setProperty('e_line', '6')
        self.e_label.setText(config.qt_text.get('LABEL_4').format(text=27, unit='MINUTES'))
        self.e_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.e_label.setFont(self.num_font)
        self.e_label.setContentsMargins(3, 0, 0, 0)  # 边距
        self.e_label.setStyleSheet(f'QLabel{{color:white;font-size:16px ;}}')

        # self.e_label.setMargin(-5)  # 内边距
        # self.e_label.setContentsMargins(0, 0, 0, 1000)

    # def set_grid_pos(self, grid):

    def enterEvent(self, event: QEnterEvent) -> None:
        self.setWindowOpacity(config.qt_show_alpha)
        self.space_label.setStyleSheet('QLabel{border-radius: 7px; background-color:rgba(31, 32, 34, 80%)}')
        event.accept()

    def leaveEvent(self, event: QEnterEvent) -> None:
        self.setWindowOpacity(config.qt_hide_alpha)
        self.space_label.setStyleSheet('QLabel{background-color:None}')
        event.accept()

    def set_text_num(self, text, unit_c, unit_e) -> None:
        """
        设置文本：数字，中文单位及英文单位
        :param text: 数字
        :param unit_c: 中文单位
        :param unit_e: 英文单位
        :return: None
        """
        self.second_line_label_2.setText(unit_c)
        self.number_label.setText(config.qt_text.get('LABEL_NUM').format(text=text))
        self.e_label.setText(config.qt_text.get('LABEL_4').format(text=text, unit=unit_e))

    @staticmethod
    def get_font(font_path) -> QFont:
        """
        根据路径加载字体
        :param font_path: 字体路径
        :return: QFont
        """
        font_data = QFontDatabase.addApplicationFont(font_path)
        font_name = QFontDatabase.applicationFontFamilies(font_data)
        return QFont(font_name)
