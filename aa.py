# MyWindow.py

from PyQt5 import QtCore, QtGui, QtWidgets


class NewQLineEdit(QtWidgets.QLineEdit):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAcceptDrops(True)  # 删除没有影响，目前不确定（因为True和False测试结果一样）
        self.setDragEnabled(True)  # 删除没有影响，（因为True和False测试结果一样）

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():  # 当文件拖入此区域时为True
            event.accept()  # 接受拖入文件
        else:
            event.ignore()  # 忽略拖入文件

    def dropEvent(self, event):  # 本方法为父类方法，本方法中的event为鼠标放事件对象
        urls = [u for u in event.mimeData().urls()]  # 范围文件路径的Qt内部类型对象列表，由于支持多个文件同时拖入所以使用列表存放
        for url in urls:
            self.setText(url.path()[1:])  # 将Qt内部类型转换为字符串类型


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1043, 453)
        Form.setAcceptDrops(True)
        self.lineEdit = NewQLineEdit(Form)  # 此处更改
        self.lineEdit.setGeometry(QtCore.QRect(70, 230, 881, 41))
        self.lineEdit.setAcceptDrops(True)
        self.lineEdit.setStyleSheet("font: 12pt \"Arial\";")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(430, 160, 311, 41))
        self.label.setStyleSheet(
            "font: 12pt \"黑体\";\n"
            "font: 14pt \"微软雅黑\";"
        )
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "扫地僧-smile"))
