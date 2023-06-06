尝试写一个自己的PDF解密和转换成WORD文档的小工具，仅考虑了对PDF的支持。
GUI界面选用PyQt5库
PDF选用pyMU库
WORD选用docx库

关于拖入文件：
只需要重写MainDialog的方法即可
        def dragEnterEvent(self, evn):
            evn.accept()
        def dropEvent(self, evn):
            path = evn.mimeData().text()
            if(path[-3:]=='pdf'):
                self.ui.lineEditTarget.setText(path)
        def dragMoveEvent(self, evn):
            pass
