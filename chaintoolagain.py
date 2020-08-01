import maya.OpenMayaUI as omui
import maya.cmds as cmds
from PySide2 import QtWidgets, QtCore
from shiboken2 import wrapInstance

def maya_main_window():
    """return maya main window widget"""
    main_window = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window), QtWidgets.QWidget)


class ChainToolAgain(QtWidgets.QDialog):

    def __init__(self):
        self.selected = cmds.ls(selection=True)
        super(ChainToolAgain, self).__init__(parent=maya_main_window())
        self.qtSignal = QtCore.Signal()

    def create(self):
        self.setWindowTitle('Chain Tool')
        self.setWindowFlags(QtCore.Qt.Tool)
        self.resize(750, 400)
        self.mainLayout = QtWidgets.QVBoxLayout(self)

        self.title_lbl = QtWidgets.QLabel("Create Chain Tool")
        self.title_lbl.setStyleSheet("font: bold 45px")
        self.cop_lbl = QtWidgets.QLabel("Number of Copies")
        self.cop_le = QtWidgets.QLineEdit()
        self.go_btn = QtWidgets.QPushButton("Go")
        self.cancel_btn = QtWidgets.QPushButton("Cancel")

        self.mainLayout.addWidget(self.title_lbl)
        self.mainLayout.addWidget(self.cop_lbl)
        self.mainLayout.addWidget(self.cop_le)
        self.mainLayout.addWidget(self.go_btn)
        self.mainLayout.addWidget(self.cancel_btn)

        #self.cop_le.textChanged.connect(self.updateCopies(self, 2))
        self.go_btn.clicked.connect(lambda: ChainToolAgain.createChain(self, 3, 2, 'x'))

        self.show()

    def updateCopies(self, val):
        _numCopies = val
        int(val)
        ChainToolAgain.createChain(self, val, 2, 'x')



    def createChain(self, copies, distance, axis):
        for x in range(0, copies):
            cmds.duplicate(cmds.ls(selection=True))
            if axis == 'x':
                cmds.move(distance, 0, 0, cmds.ls(selection=True), relative=True)
            if axis == 'y':
                cmds.move(0, distance, 0, cmds.ls(selection=True), relative=True)
            if axis == 'z':
                cmds.move(0, 0, distance, cmds.ls(selection=True), relative=True)