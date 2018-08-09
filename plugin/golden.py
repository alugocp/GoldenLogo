# Golden Logo plugin for Krita
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from krita import *

class GoldenExtension(Extension):
    def __init__(self, parent):
        super().__init__(parent)
    def setup(self):
        self.i=0
    def createActions(self, window):
        action=window.createAction("golopp","Enlarge","tools/scripts")
        action.triggered.connect(self.enlarge)
        action=window.createAction("golomm","Reduce","tools/scripts")
        action.triggered.connect(self.reduce)

    # Actions library
    def enlarge(self):
        self.i+=1
        QMessageBox.information(QWidget(),"Test","i is "+str(self.i))
    def reduce(self):
        self.i-=1
        QMessageBox.information(QWidget(),"Test","i is "+str(self.i))

# Add to Krita instance
Krita.instance().addExtension(GoldenExtension(Krita.instance()))
