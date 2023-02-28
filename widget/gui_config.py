from random import randint

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout

from units import config


class ConfigWindow(QWidget):
    """

    """
    def __init__(self):
        super().__init__()

        # self.setFixedSize(100, 300)
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel("Another Window % d" % randint(0, 100))
        layout.addWidget(self.label)
        save_button = QPushButton('保存')
        cancel_button = QPushButton('取消')

        save_button.clicked.connect(config.save)
        cancel_button.clicked.connect(self.hide)

        button_layout = QHBoxLayout()
        button_layout.addWidget(save_button)
        button_layout.addWidget(cancel_button)
        layout.addLayout(button_layout)

    def closeEvent(self, event):
        event.ignore()
        self.hide()
        # return super(ConfigWindow, self).close()

