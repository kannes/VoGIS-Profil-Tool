# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_vogisprofiltoolplot.ui'
#
# Created: Mon Feb  9 14:29:24 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_VoGISProfilToolPlot(object):
    def setupUi(self, VoGISProfilToolPlot):
        VoGISProfilToolPlot.setObjectName(_fromUtf8("VoGISProfilToolPlot"))
        VoGISProfilToolPlot.resize(836, 472)
        VoGISProfilToolPlot.setModal(True)
        self.gridLayout_2 = QtGui.QGridLayout(VoGISProfilToolPlot)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.IDC_bClose = QtGui.QPushButton(VoGISProfilToolPlot)
        self.IDC_bClose.setObjectName(_fromUtf8("IDC_bClose"))
        self.gridLayout.addWidget(self.IDC_bClose, 3, 8, 1, 1)
        self.IDC_bDxfLine = QtGui.QPushButton(VoGISProfilToolPlot)
        self.IDC_bDxfLine.setObjectName(_fromUtf8("IDC_bDxfLine"))
        self.gridLayout.addWidget(self.IDC_bDxfLine, 3, 6, 1, 1)
        self.IDC_bDxfPnt = QtGui.QPushButton(VoGISProfilToolPlot)
        self.IDC_bDxfPnt.setObjectName(_fromUtf8("IDC_bDxfPnt"))
        self.gridLayout.addWidget(self.IDC_bDxfPnt, 3, 4, 1, 1)
        self.IDC_bShpPnt = QtGui.QPushButton(VoGISProfilToolPlot)
        self.IDC_bShpPnt.setObjectName(_fromUtf8("IDC_bShpPnt"))
        self.gridLayout.addWidget(self.IDC_bShpPnt, 3, 3, 1, 1)
        self.IDC_bShpLine = QtGui.QPushButton(VoGISProfilToolPlot)
        self.IDC_bShpLine.setObjectName(_fromUtf8("IDC_bShpLine"))
        self.gridLayout.addWidget(self.IDC_bShpLine, 3, 5, 1, 1)
        self.IDC_bACadTxt = QtGui.QPushButton(VoGISProfilToolPlot)
        self.IDC_bACadTxt.setObjectName(_fromUtf8("IDC_bACadTxt"))
        self.gridLayout.addWidget(self.IDC_bACadTxt, 3, 2, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(VoGISProfilToolPlot)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.IDC_cbDecimalDelimiter = QtGui.QComboBox(VoGISProfilToolPlot)
        self.IDC_cbDecimalDelimiter.setObjectName(_fromUtf8("IDC_cbDecimalDelimiter"))
        self.IDC_cbDecimalDelimiter.addItem(_fromUtf8(""))
        self.IDC_cbDecimalDelimiter.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.IDC_cbDecimalDelimiter)
        self.label_2 = QtGui.QLabel(VoGISProfilToolPlot)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.IDC_cbDelimiter = QtGui.QComboBox(VoGISProfilToolPlot)
        self.IDC_cbDelimiter.setEditable(False)
        self.IDC_cbDelimiter.setObjectName(_fromUtf8("IDC_cbDelimiter"))
        self.IDC_cbDelimiter.addItem(_fromUtf8(""))
        self.IDC_cbDelimiter.addItem(_fromUtf8(""))
        self.IDC_cbDelimiter.addItem(_fromUtf8(""))
        self.IDC_cbDelimiter.addItem(_fromUtf8(""))
        self.IDC_cbDelimiter.setItemText(3, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.IDC_cbDelimiter)
        self.IDC_chkHekto = QtGui.QCheckBox(VoGISProfilToolPlot)
        self.IDC_chkHekto.setObjectName(_fromUtf8("IDC_chkHekto"))
        self.horizontalLayout.addWidget(self.IDC_chkHekto)
        self.IDC_chkLineAttributes = QtGui.QCheckBox(VoGISProfilToolPlot)
        self.IDC_chkLineAttributes.setChecked(True)
        self.IDC_chkLineAttributes.setObjectName(_fromUtf8("IDC_chkLineAttributes"))
        self.horizontalLayout.addWidget(self.IDC_chkLineAttributes)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 9)
        self.IDC_frPlot = QtGui.QFrame(VoGISProfilToolPlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IDC_frPlot.sizePolicy().hasHeightForWidth())
        self.IDC_frPlot.setSizePolicy(sizePolicy)
        self.IDC_frPlot.setMinimumSize(QtCore.QSize(0, 350))
        self.IDC_frPlot.setFrameShape(QtGui.QFrame.StyledPanel)
        self.IDC_frPlot.setFrameShadow(QtGui.QFrame.Raised)
        self.IDC_frPlot.setObjectName(_fromUtf8("IDC_frPlot"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.IDC_frPlot)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout.addWidget(self.IDC_frPlot, 0, 0, 1, 9)
        self.IDC_frToolbar = QtGui.QFrame(VoGISProfilToolPlot)
        self.IDC_frToolbar.setFrameShape(QtGui.QFrame.StyledPanel)
        self.IDC_frToolbar.setFrameShadow(QtGui.QFrame.Raised)
        self.IDC_frToolbar.setObjectName(_fromUtf8("IDC_frToolbar"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.IDC_frToolbar)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout.addWidget(self.IDC_frToolbar, 1, 0, 1, 9)
        self.IDC_bText = QtGui.QPushButton(VoGISProfilToolPlot)
        self.IDC_bText.setObjectName(_fromUtf8("IDC_bText"))
        self.gridLayout.addWidget(self.IDC_bText, 3, 0, 1, 1)
        self.IDC_bExcel = QtGui.QPushButton(VoGISProfilToolPlot)
        self.IDC_bExcel.setObjectName(_fromUtf8("IDC_bExcel"))
        self.gridLayout.addWidget(self.IDC_bExcel, 3, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 7, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 10, 0, 1, 1)

        self.retranslateUi(VoGISProfilToolPlot)
        QtCore.QObject.connect(self.IDC_bClose, QtCore.SIGNAL(_fromUtf8("clicked()")), VoGISProfilToolPlot.reject)
        QtCore.QObject.connect(self.IDC_bText, QtCore.SIGNAL(_fromUtf8("clicked()")), VoGISProfilToolPlot.exportTxt)
        QtCore.QObject.connect(self.IDC_bShpPnt, QtCore.SIGNAL(_fromUtf8("clicked()")), VoGISProfilToolPlot.exportShpPnt)
        QtCore.QObject.connect(self.IDC_bShpLine, QtCore.SIGNAL(_fromUtf8("clicked()")), VoGISProfilToolPlot.exportShpLine)
        QtCore.QObject.connect(self.IDC_bExcel, QtCore.SIGNAL(_fromUtf8("clicked()")), VoGISProfilToolPlot.exportCsvXls)
        QtCore.QObject.connect(self.IDC_bACadTxt, QtCore.SIGNAL(_fromUtf8("clicked()")), VoGISProfilToolPlot.exportAutoCadTxt)
        QtCore.QObject.connect(self.IDC_bDxfPnt, QtCore.SIGNAL(_fromUtf8("clicked()")), VoGISProfilToolPlot.exportDxfPnt)
        QtCore.QObject.connect(self.IDC_bDxfLine, QtCore.SIGNAL(_fromUtf8("clicked()")), VoGISProfilToolPlot.exportDxfLine)
        QtCore.QMetaObject.connectSlotsByName(VoGISProfilToolPlot)

    def retranslateUi(self, VoGISProfilToolPlot):
        VoGISProfilToolPlot.setWindowTitle(_translate("VoGISProfilToolPlot", "VoGIS Profil Tool", None))
        self.IDC_bClose.setText(_translate("VoGISProfilToolPlot", "Schließen", None))
        self.IDC_bDxfLine.setText(_translate("VoGISProfilToolPlot", "DXF Linie", None))
        self.IDC_bDxfPnt.setText(_translate("VoGISProfilToolPlot", "DXF Punkt", None))
        self.IDC_bShpPnt.setText(_translate("VoGISProfilToolPlot", "Shp Punkt", None))
        self.IDC_bShpLine.setText(_translate("VoGISProfilToolPlot", "Shp Linie", None))
        self.IDC_bACadTxt.setText(_translate("VoGISProfilToolPlot", "Autocad Text", None))
        self.label.setText(_translate("VoGISProfilToolPlot", "Dezimalzeichen (für Text, csv):", None))
        self.IDC_cbDecimalDelimiter.setItemText(0, _translate("VoGISProfilToolPlot", ",", None))
        self.IDC_cbDecimalDelimiter.setItemText(1, _translate("VoGISProfilToolPlot", ".", None))
        self.label_2.setText(_translate("VoGISProfilToolPlot", "Spaltentrennzeichen (Text):", None))
        self.IDC_cbDelimiter.setItemText(0, _translate("VoGISProfilToolPlot", "tab", None))
        self.IDC_cbDelimiter.setItemText(1, _translate("VoGISProfilToolPlot", ";", None))
        self.IDC_cbDelimiter.setItemText(2, _translate("VoGISProfilToolPlot", ",", None))
        self.IDC_chkHekto.setText(_translate("VoGISProfilToolPlot", "Hektometrie Attribute", None))
        self.IDC_chkLineAttributes.setText(_translate("VoGISProfilToolPlot", "Linien Attribute", None))
        self.IDC_bText.setText(_translate("VoGISProfilToolPlot", "Textdatei", None))
        self.IDC_bExcel.setText(_translate("VoGISProfilToolPlot", "Excel / CSV", None))

