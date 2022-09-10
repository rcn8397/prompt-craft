#!/usr/bin/env python3
import sys
import os

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)

from PyQt5.uic import loadUi
from main_window_ui import Ui_MainWindow

class Window( QMainWindow, Ui_MainWindow ):
    def __init__( self, parent = None ):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.actionExit.triggered.connect(self.close)
        self.actionRun.triggered.connect(self.run_prompt)
        self.actionAbout.triggered.connect(self.about)

    def run_prompt(self):
        print( 'working' )
        prompt = self.prompt.toPlainText()
        print( prompt )
        n_samples = self.n_samples.value()
        n_iter    = self.n_iter.value()
        strength  = self.strength.value()
        cmd = 'python scripts/img2img.py --prompt "{}" --n_iter {} --init-img {} --strength {}'   
        print( cmd.format( prompt, n_samples, n_iter, strength ) )
        os.system( cmd )

    def about(self):
        QMessageBox.about(
            self,
            "About Sample Editor",
            "<p>A sample text editor app built with:</p>"
            "<p>- PyQt</p>"
            "<p>- Qt Designer</p>"
            "<p>- Python</p>",
        )

class FindReplaceDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/find_replace.ui", self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())    
