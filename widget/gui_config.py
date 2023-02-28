from random import randint

from PyQt6.QtGui import QDoubleValidator
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QLineEdit

from units import config


class ConfigWindow(QWidget):
    """

    """
    def __init__(self):
        super().__init__()

        self.config_dict = {}
        # self.setFixedSize(100, 300)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setWindowTitle('设置')
        alpha_label = QLabel('透明度(0.01-1.00)')
        layout.addWidget(alpha_label)

        alpha_layout = QHBoxLayout()
        self.show_alpha_wd = QLineEdit(f'{config.qt_show_alpha}')
        self.hide_alpha_wd = QLineEdit(f'{config.qt_hide_alpha}')
        double_validator = QDoubleValidator()
        double_validator.setRange(0.01, 1.00, 2)
        self.show_alpha_wd.setValidator(double_validator)
        self.hide_alpha_wd.setValidator(double_validator)
        self.config_dict.update({'qt_show_alpha': self.show_alpha_wd,
                                'qt_hide_alpha': self.hide_alpha_wd, })

        alpha_layout.addWidget(QLabel('聚焦：'))
        alpha_layout.addWidget(self.show_alpha_wd)
        alpha_layout.addWidget(QLabel('失焦：'))
        alpha_layout.addWidget(self.hide_alpha_wd)
        layout.addLayout(alpha_layout)

        save_button = QPushButton('保存')
        cancel_button = QPushButton('取消')

        save_button.clicked.connect(self.save)
        cancel_button.clicked.connect(self.hide)

        button_layout = QHBoxLayout()
        button_layout.addWidget(save_button)
        button_layout.addWidget(cancel_button)
        layout.addLayout(button_layout)

    def save(self):
        for config_name, widget in self.config_dict.items():
            config[config_name] = float(widget.text())
        config.save()
        # self.hide()

    def closeEvent(self, event):
        event.ignore()
        self.hide()
        # return super(ConfigWindow, self).close()

