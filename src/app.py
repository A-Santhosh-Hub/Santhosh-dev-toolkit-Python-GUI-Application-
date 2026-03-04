"""
TextTools Desktop App
Powered by PyQt5 + QtWebEngine - Works on Python 3.9 to 3.14
No .NET, no pythonnet, no WebView2 required.
"""

import sys
import os
import json

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtCore import QObject, pyqtSlot, QUrl, Qt
from PyQt5.QtGui import QIcon


def resource_path(relative):
    try:
        base = sys._MEIPASS
    except AttributeError:
        base = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(base, relative)


class Bridge(QObject):
    def __init__(self, main_window):
        super().__init__()
        self._win = main_window

    @pyqtSlot(result=str)
    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(
            self._win, "Open File", "",
            "All Supported (*.txt *.md *.json *.js *.css *.html *.htm *.py *.c *.cpp *.java);;"
            "Text Files (*.txt *.md);;"
            "Code Files (*.json *.js *.css *.html *.htm *.py *.c *.cpp *.java);;"
            "All Files (*.*)"
        )
        if not path:
            return json.dumps(None)
        try:
            with open(path, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
            return json.dumps({"name": os.path.basename(path), "content": content})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @pyqtSlot(result=str)
    def open_html_file(self):
        path, _ = QFileDialog.getOpenFileName(
            self._win, "Open HTML File", "",
            "HTML Files (*.html *.htm);;All Files (*.*)"
        )
        if not path:
            return json.dumps(None)
        try:
            with open(path, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
            return json.dumps({"name": os.path.basename(path), "content": content})
        except Exception as e:
            return json.dumps({"error": str(e)})

    @pyqtSlot(str, str, result=str)
    def save_file(self, content, suggested_name):
        path, _ = QFileDialog.getSaveFileName(
            self._win, "Save File", suggested_name, "All Files (*.*)"
        )
        if not path:
            return json.dumps(False)
        try:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            return json.dumps(True)
        except Exception as e:
            return json.dumps({"error": str(e)})

    @pyqtSlot(str, result=str)
    def preview_html(self, html_content):
        preview = PreviewWindow(html_content, self._win)
        preview.show()
        return json.dumps(True)


class PreviewWindow(QMainWindow):
    def __init__(self, html_content, parent=None):
        super().__init__(parent)
        self.setWindowTitle("HTML Preview - TextTools")
        self.resize(1024, 768)
        self.setAttribute(Qt.WA_DeleteOnClose)
        view = QWebEngineView()
        view.setHtml(html_content, QUrl("about:blank"))
        self.setCentralWidget(view)


class AppPage(QWebEnginePage):
    def javaScriptConsoleMessage(self, level, message, line, source):
        pass


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TextTools - Format, Clean & Convert")
        self.setMinimumSize(900, 600)
        self.resize(1280, 820)

        icon_path = resource_path(os.path.join('assets', 'icon.png'))
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

        self.view = QWebEngineView()
        page = AppPage(self.view)
        self.view.setPage(page)

        self.channel = QWebChannel()
        self.bridge = Bridge(self)
        self.channel.registerObject("bridge", self.bridge)
        self.view.page().setWebChannel(self.channel)

        html_path = resource_path(os.path.join('assets', 'index.html'))
        self.view.setUrl(QUrl.fromLocalFile(html_path))
        self.setCentralWidget(self.view)


def main():
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    app.setApplicationName("TextTools")
    app.setOrganizationName("SanStudio")

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
