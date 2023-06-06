import sys
import PyQt5.QtWidgets as qw
from aa2 import Ui_MainWindow

class TestWindow(qw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, evn):
        print('鼠标拖入窗口')
        # self.QLabl.setText('文件路径：\n' + evn.mimeData().text())
        # 鼠标放开函数事件
        evn.accept()

    def dropEvent(self, evn):
        print(f'鼠标放开 {evn.posF()}')
        path = evn.mimeData().text()
        self.ui.lineEdit_1.setText(path)
        print('文件路径：\n' + path)

    def dragMoveEvent(self, evn):
        pass
        # print('鼠标移动')

if __name__ == '__main__':
    app = qw.QApplication(sys.argv)
    w = TestWindow()
    w.show()
    sys.exit(app.exec_())
