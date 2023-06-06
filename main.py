if __name__ == '__main__':
    # 导入相关库
    import sys
    import os
    import window
    from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog
    from PyQt5.QtCore import Qt
    # 相关类
    class MainDialog(QDialog):
        def __init__(self, parent=None):
            super(QDialog, self).__init__(parent)
            self.ui = window.Ui_Dialog()
            self.ui.setupUi(self)
            # 右上角按钮调整
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint | Qt.WindowMinimizeButtonHint)
            # 绑定按钮函数
            self.ui.toolButtonTarget.clicked.connect(self.clickButtonTarget)
            self.ui.toolButtonExport.clicked.connect(self.clickButtonExport)
            self.ui.pushButtonDecrypt.clicked.connect(self.clickButtonDecrypt)
            self.ui.pushButtonConvert.clicked.connect(self.clickButtonConvert)
            # lineEdit
            self.ui.lineEditTarget.setPlaceholderText('选择或拖入一个PDF文件')
            self.ui.lineEditTarget.setReadOnly(True)
            self.ui.lineEditExport.setPlaceholderText('当前目录')
            self.ui.lineEditExport.setReadOnly(True)

        def clickButtonTarget(self):
            fileName, fileType = QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(), "PDF File(*.pdf)")
            self.ui.lineEditTarget.setText(fileName)
        def clickButtonExport(self):
            directory = QFileDialog.getExistingDirectory(self, "选取导出文件夹", os.getcwd())
            self.ui.lineEditExport.setText(directory)
        def clickButtonDecrypt(self):
            if(self.ui.lineEditTarget.text()!=""):  # 如果有选择PDF文件才需要处理
                if(self.ui.lineEditExport.text()!=""):  # 如果有指定路径就取值
                    myDecrypt(self.ui.lineEditTarget.text(), self.ui.lineEditExport.text())
                else:
                    myDecrypt(self.ui.lineEditTarget.text(), os.getcwd())
        def clickButtonConvert(self):
            if(self.ui.lineEditTarget.text()!=""):  # 如果有选择PDF文件才需要处理
                if(self.ui.lineEditExport.text()!=""):  # 如果有指定路径就取值
                    myConvert(self.ui.lineEditTarget.text(), self.ui.lineEditExport.text())
                else:
                    myConvert(self.ui.lineEditTarget.text(), os.getcwd())

    # 方法：PDF解密
    def myDecrypt(fileName,exportDirectory):
        print(fileName,exportDirectory)

    # 方法：转换WORD
    def myConvert(fileName,exportDirectory):
        print(fileName,exportDirectory)

    # 打开窗口
    myapp = QApplication(sys.argv)
    myDlg = MainDialog()
    myDlg.show()
    sys.exit(myapp.exec_())


# PDF水印？




