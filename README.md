尝试写一个自己的PDF解密和转换成WORD文档的小工具，仅考虑了对PDF的支持。
GUI界面选用PyQt5库
PDF本来想选用PyMuPDF库，WORD想选用python-docx库，结果发现了一个pdf2docx库好像就是用前面两个库实现的，尝试了一下发现效果不错（直接就解密并去水印了），就直接拿来用了。

关于拖入文件：
只需要重写MainDialog的方法即可
        def dragEnterEvent(self, evn):
            evn.accept()
        def dropEvent(self, evn):
            path = evn.mimeData().text()
        def dragMoveEvent(self, evn):
            pass

