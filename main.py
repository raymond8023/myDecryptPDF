if __name__ == '__main__':
    # 导入相关库
    import sys
    import os
    import window
    from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox
    from PyQt5.QtCore import Qt
    import pdf2docx
    # 相关类
    class MainDialog(QDialog):
        def __init__(self, parent=None):
            super(QDialog, self).__init__(parent)
            self.ui = window.Ui_Dialog()
            self.ui.setupUi(self)
            # 右上角按钮调整
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint | Qt.WindowMinimizeButtonHint)
            # 接受拖入
            self.setAcceptDrops(True)
            # 绑定按钮函数
            self.ui.toolButtonTarget.clicked.connect(self.clickButtonTarget)
            self.ui.toolButtonExport.clicked.connect(self.clickButtonExport)
            self.ui.pushButtonConvert.clicked.connect(self.clickButtonConvert)
            # lineEdit
            self.ui.lineEditTarget.setPlaceholderText('选择或拖入一个PDF文件')
            self.ui.lineEditTarget.setReadOnly(True)
            self.ui.lineEditExport.setPlaceholderText('当前目录')
            self.ui.lineEditExport.setText(os.getcwd()+'\\')
            self.ui.lineEditExport.setReadOnly(True)
            # 调试区

        # 重写拖入相关方法
        def dragEnterEvent(self, evn):
            # print('鼠标拖入窗口')
            # 鼠标放开函数事件
            evn.accept()
        def dropEvent(self, evn):
            # print(f'鼠标放开 {evn.posF()}')
            path = evn.mimeData().text()
            # print('文件路径：\n' + path)
            # print(path[-3:])
            if(path[-3:]=='pdf'):
                self.ui.lineEditTarget.setText(path[8:].replace('/','\\'))
                myConvert(self.ui.lineEditTarget.text(), self.ui.lineEditExport.text())
                QMessageBox.information(self, " ", "转换完成！", QMessageBox.Ok)

        def dragMoveEvent(self, evn):
            pass
            # print('鼠标移动')

        def clickButtonTarget(self):
            fileName, fileType = QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(), "PDF File(*.pdf)")
            self.ui.lineEditTarget.setText(fileName.replace('/','\\'))
        def clickButtonExport(self):
            directory = QFileDialog.getExistingDirectory(self, "选取导出文件夹", os.getcwd())
            self.ui.lineEditExport.setText(directory.replace('/','\\')+'\\')
        def clickButtonConvert(self):
            if(self.ui.lineEditTarget.text()!=""):  # 如果有选择PDF文件才需要处理
                myConvert(self.ui.lineEditTarget.text(), self.ui.lineEditExport.text())
                QMessageBox.information(self, " ", "转换完成！", QMessageBox.Ok)


    # 方法：转换WORD
    def myConvert(fileName,exportDirectory):
        exportFileName=exportDirectory+os.path.splitext(os.path.basename(fileName).split('/')[-1])[0]+'.docx'
        pdf2docx.parse(fileName, exportFileName)
        # print(fileName, exportFileName)

    # 打开窗口
    myapp = QApplication(sys.argv)
    myDlg = MainDialog()
    myDlg.show()
    sys.exit(myapp.exec_())





