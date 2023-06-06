# main.py
# 注入口文件不再注释，仅提供读者测试使用

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QCoreApplication
import os
from aa import *


class Main:

    def __init__(self, ui, root):
        QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
        self.__app = QApplication(sys.argv)
        self.__ui = ui()
        self.__root = root()

    def __close(self):
        os._exit(520)

    def __main(self):
        self.__app.setQuitOnLastWindowClosed(False)
        self.__app.lastWindowClosed.connect(self.__close)  # 设置关闭程序
        self.__ui.setupUi(self.__root)

        self.__root.show()
        sys.exit(self.__app.exec_())

    def run(self):
        self.__main()


if __name__ == '__main__':
    app = Main(Ui_Form, QWidget)
    app.run()
