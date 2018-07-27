# Golden Logo plugin for Krita
from krita import *

class GoldenExtension(Extension):
    def __init__(self, parent):
        super().__init__(parent)
    def setup(self):
        pass
    def createActions(self, window):
        action=window.createAction("golo++","Enlarge","tools/scripts")
        action.triggered.connect(self.enlarge)

    # Actions library
    def enlarge(self):

Krita.instance().addExtension(GoldenExtension(Krita.instance())
