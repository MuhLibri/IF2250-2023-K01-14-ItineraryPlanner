# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RiwayatInterface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from UbahItineraryDialogue import Ui_UbahWindow
from TambahCatatanDialogue import Ui_CatatanWindow
from RiwayatController import *
from ui_Edititinerary import Ui_Edit


class Ui_Riwayat(object):
    riwayatCount = 0
    listRiwayat = RiwayatController.getListRiwayat()
    def openUbah(self):
        self.ubahWindow = QtWidgets.QMainWindow()
        self.ubahUi = Ui_Edit()
        self.ubahUi.setupUi(self.ubahWindow)
        self.ubahWindow.show()

    def openCatatan(self, riwayat):
        self.catatanWindow = QtWidgets.QMainWindow()
        self.catatanUi = Ui_CatatanWindow()
        self.catatanUi.setupUi(self.catatanWindow, riwayat)
        self.catatanWindow.show()

    def setupUi(self, Riwayat):
        Riwayat.setObjectName("Riwayat")
        Riwayat.resize(800, 578)
        self.centralwidget = QtWidgets.QWidget(Riwayat)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, 0, 801, 80))
        self.frame.setStyleSheet("background-color: rgb(42, 174, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 60, 50))
        self.pushButton.setStyleSheet("QPushButton{\n"
"color: white;\n"
"    background-color: rgb(42, 174, 255);\n"
"    border: none;\n"
"font: 16pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(35, 148, 213);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(25, 105, 152);\n"
"}")
        # self.pushButton.setFlat(True)
        # self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(220, 10, 371, 50))
        self.label.setStyleSheet("QLabel{\n"
"background-color: rgb(42, 174, 255);\n"
"font: 16pt;\n"
"color: white;\n"
"}")
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(-1, 76, 801, 501))
        self.scrollArea.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 799, 499))
        self.scrollAreaWidgetContents.setAutoFillBackground(False)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_3.setContentsMargins(0, 3, 0, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        # self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        # self.pushButton_2.setObjectName("pushButton_2")
        # self.verticalLayout_3.addWidget(self.pushButton_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        Riwayat.setCentralWidget(self.centralwidget)

        self.retranslateUi(Riwayat)
        QtCore.QMetaObject.connectSlotsByName(Riwayat)
    
        for elmt in self.listRiwayat:
            self.createNewWidget(elmt)

        # self.pushButton_2.clicked.connect(self.createNewWidget)

    def createNewWidget(self, riwayat):
        newRiwayat = "riwayatFrame" + str(self.riwayatCount)
        newVertical = "verticalName" + str(self.riwayatCount)
        newTitle = "{} Hari di {}".format(RiwayatController.getDuration(riwayat), RiwayatController.getDaerahItinerary(riwayat))
        newDuration = "{} - {}".format(RiwayatController.getStartDate(riwayat), RiwayatController.getEndDate(riwayat))
        newDestination = "{}".format(', '.join([str(elem) for elem in RiwayatController.getListObjekWisata(riwayat)]))
        newUbah = "ubah" + str(self.riwayatCount)
        newCatatan = "catatan" + str(self.riwayatCount)
        self.riwayatCount += 1

        self.riwayatFrame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.riwayatFrame.sizePolicy().hasHeightForWidth())
        self.riwayatFrame.setSizePolicy(sizePolicy)
        self.riwayatFrame.setMinimumSize(QtCore.QSize(800, 150))
        self.riwayatFrame.setMaximumSize(QtCore.QSize(800, 150))
        self.riwayatFrame.setStyleSheet("#" + newRiwayat + "{\n"
"background-color: white;\n"
"border: 1px solid black;\n"
"}")
        self.riwayatFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.riwayatFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.riwayatFrame.setObjectName(newRiwayat)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.riwayatFrame)
        self.verticalLayout_4.setObjectName(newVertical)
        self.TitleLabel = QtWidgets.QLabel(self.riwayatFrame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)

        #Setup title
        self.TitleLabel.setFont(font)
        self.TitleLabel.setObjectName(newTitle)
        self.TitleLabel.setText(newTitle)
        self.verticalLayout_4.addWidget(self.TitleLabel)
        

        #Setup duration
        self.DurationLabel = QtWidgets.QLabel(self.riwayatFrame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.DurationLabel.setFont(font)
        self.DurationLabel.setObjectName(newDuration)
        self.DurationLabel.setText(newDuration)
        self.verticalLayout_4.addWidget(self.DurationLabel)

        #Setup destination
        self.DestinationLabel = QtWidgets.QLabel(self.riwayatFrame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.DestinationLabel.setFont(font)
        self.DestinationLabel.setObjectName(newDestination)
        self.DestinationLabel.setText(newDestination)
        self.verticalLayout_4.addWidget(self.DestinationLabel)

        #Setup ubah
        self.ubahButton = QtWidgets.QPushButton(self.riwayatFrame, clicked = lambda: self.openUbah())
        self.ubahButton.setObjectName(newUbah)
        self.ubahButton.setGeometry(QtCore.QRect(280, 130, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setUnderline(True)
        self.ubahButton.setFont(font)
        self.ubahButton.setText("Ubah")
        self.ubahButton.setStyleSheet("border: none; color:rgb(12, 190, 255);")
        self.verticalLayout_4.addWidget(self.ubahButton, 0, QtCore.Qt.AlignLeft)

        #Setup catatan
        # self.CatatanLabel = QtWidgets.QLabel(self.riwayatFrame)
        # font = QtGui.QFont()
        # font.setPointSize(9)
        # font.setUnderline(True)
        # self.CatatanLabel.setFont(font)
        # self.CatatanLabel.setStyleSheet("color:rgb(12, 190, 255)")
        # self.CatatanLabel.setObjectName(newCatatan)
        # self.CatatanLabel.setText("Catatan")
        # self.verticalLayout_4.addWidget(self.CatatanLabel)

        self.catatanButton = QtWidgets.QPushButton(self.riwayatFrame, clicked = lambda: self.openCatatan(riwayat))
        self.catatanButton.setObjectName(newCatatan)
        self.catatanButton.setGeometry(QtCore.QRect(280, 130, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setUnderline(True)
        self.catatanButton.setFont(font)
        self.catatanButton.setText("Catatan")
        self.catatanButton.setStyleSheet("border: none; color:rgb(12, 190, 255);")
        self.verticalLayout_4.addWidget(self.catatanButton, 0, QtCore.Qt.AlignLeft)

        self.verticalLayout_3.addWidget(self.riwayatFrame, QtCore.Qt.AlignTop)
        self.riwayatFrame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.riwayatFrame.setMinimumSize(QtCore.QSize(745, 0))
        self.riwayatFrame.setMaximumSize(QtCore.QSize(745, 50))
        self.riwayatFrame.setStyleSheet("background-color: white;")
        self.riwayatFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.riwayatFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.riwayatFrame.setObjectName(newRiwayat)
        self.verticalLayout_3.addWidget(self.riwayatFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.addStretch()

        setattr(self, newRiwayat, self.riwayatFrame)

    def retranslateUi(self, Riwayat):
        _translate = QtCore.QCoreApplication.translate
        Riwayat.setWindowTitle(_translate("Riwayat", "MainWindow"))
        # self.pushButton.setText(_translate("Riwayat", "X"))
        self.label.setText(_translate("Riwayat", "Riwayat Itinerary Planner"))
        # self.pushButton_2.setText(_translate("Riwayat", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Riwayat = QtWidgets.QMainWindow()
    ui = Ui_Riwayat()
    ui.setupUi(Riwayat)
    Riwayat.show()
    sys.exit(app.exec_())
