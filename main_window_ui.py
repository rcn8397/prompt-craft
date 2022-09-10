# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/promptcraft.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 750)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(540, 750))
        MainWindow.setMaximumSize(QtCore.QSize(540, 750))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 521, 691))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.clear_btn = QtWidgets.QPushButton(self.tab_3)
        self.clear_btn.setGeometry(QtCore.QRect(360, 240, 80, 25))
        self.clear_btn.setObjectName("clear_btn")
        self.layoutWidget = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget.setGeometry(QtCore.QRect(21, 291, 327, 216))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.modeBox = QtWidgets.QComboBox(self.layoutWidget)
        self.modeBox.setEditable(False)
        self.modeBox.setCurrentText("")
        self.modeBox.setMaxVisibleItems(2)
        self.modeBox.setObjectName("modeBox")
        self.gridLayout_2.addWidget(self.modeBox, 0, 1, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 3, 1, 1)
        self.precisionBox = QtWidgets.QComboBox(self.layoutWidget)
        self.precisionBox.setObjectName("precisionBox")
        self.gridLayout_2.addWidget(self.precisionBox, 0, 4, 1, 2)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 2)
        self.n_samples = QtWidgets.QSpinBox(self.layoutWidget)
        self.n_samples.setProperty("value", 1)
        self.n_samples.setObjectName("n_samples")
        self.gridLayout_2.addWidget(self.n_samples, 1, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 1, 3, 1, 1)
        self.height = QtWidgets.QSpinBox(self.layoutWidget)
        self.height.setMaximum(512)
        self.height.setProperty("value", 512)
        self.height.setObjectName("height")
        self.gridLayout_2.addWidget(self.height, 1, 4, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.n_iter = QtWidgets.QSpinBox(self.layoutWidget)
        self.n_iter.setProperty("value", 1)
        self.n_iter.setObjectName("n_iter")
        self.gridLayout_2.addWidget(self.n_iter, 2, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 2, 3, 1, 1)
        self.width = QtWidgets.QSpinBox(self.layoutWidget)
        self.width.setMaximum(512)
        self.width.setProperty("value", 256)
        self.width.setObjectName("width")
        self.gridLayout_2.addWidget(self.width, 2, 4, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 2)
        self.strength = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.strength.setMaximum(1.0)
        self.strength.setSingleStep(0.01)
        self.strength.setProperty("value", 0.8)
        self.strength.setObjectName("strength")
        self.gridLayout_2.addWidget(self.strength, 3, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 2)
        self.ddim_eta = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.ddim_eta.setObjectName("ddim_eta")
        self.gridLayout_2.addWidget(self.ddim_eta, 4, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 4, 3, 1, 1)
        self.ddim_step = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.ddim_step.setObjectName("ddim_step")
        self.gridLayout_2.addWidget(self.ddim_step, 4, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 5, 0, 1, 1)
        self.plms = QtWidgets.QCheckBox(self.layoutWidget)
        self.plms.setObjectName("plms")
        self.gridLayout_2.addWidget(self.plms, 6, 0, 1, 2)
        self.rand_seed = QtWidgets.QCheckBox(self.layoutWidget)
        self.rand_seed.setEnabled(True)
        self.rand_seed.setObjectName("rand_seed")
        self.gridLayout_2.addWidget(self.rand_seed, 5, 5, 1, 1)
        self.seed = QtWidgets.QSpinBox(self.layoutWidget)
        self.seed.setEnabled(True)
        self.seed.setProperty("value", 3)
        self.seed.setObjectName("seed")
        self.gridLayout_2.addWidget(self.seed, 5, 2, 1, 2)
        self.use_seed = QtWidgets.QCheckBox(self.layoutWidget)
        self.use_seed.setEnabled(True)
        self.use_seed.setObjectName("use_seed")
        self.gridLayout_2.addWidget(self.use_seed, 6, 5, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(21, 12, 52, 17))
        self.label_4.setObjectName("label_4")
        self.prompt = QtWidgets.QPlainTextEdit(self.tab_3)
        self.prompt.setGeometry(QtCore.QRect(21, 43, 421, 192))
        self.prompt.setObjectName("prompt")
        self.run_btn = QtWidgets.QPushButton(self.tab_3)
        self.run_btn.setGeometry(QtCore.QRect(320, 610, 179, 25))
        self.run_btn.setObjectName("run_btn")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 510, 217, 58))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 0, 1, 1)
        self.init_img = QtWidgets.QLineEdit(self.layoutWidget1)
        self.init_img.setEnabled(False)
        self.init_img.setObjectName("init_img")
        self.gridLayout.addWidget(self.init_img, 0, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 1, 0, 1, 1)
        self.outdir = QtWidgets.QLineEdit(self.layoutWidget1)
        self.outdir.setObjectName("outdir")
        self.gridLayout.addWidget(self.outdir, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_14 = QtWidgets.QLabel(self.tab_4)
        self.label_14.setGeometry(QtCore.QRect(40, 20, 67, 17))
        self.label_14.setObjectName("label_14")
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 540, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuabout = QtWidgets.QMenu(self.menubar)
        self.menuabout.setObjectName("menuabout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionRun = QtWidgets.QAction(MainWindow)
        self.actionRun.setObjectName("actionRun")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionRun)
        self.menuFile.addAction(self.actionExit)
        self.menuabout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuabout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.modeBox.setCurrentIndex(-1)
        self.clear_btn.clicked.connect(self.prompt.clear)
        self.run_btn.clicked.connect(MainWindow.run_prompt)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.clear_btn.setText(_translate("MainWindow", "Clear"))
        self.label_7.setText(_translate("MainWindow", "Mode"))
        self.label_9.setText(_translate("MainWindow", "Precision"))
        self.label.setText(_translate("MainWindow", "n_samples"))
        self.label_12.setText(_translate("MainWindow", "Height"))
        self.label_3.setText(_translate("MainWindow", "n_iter"))
        self.label_13.setText(_translate("MainWindow", "Width"))
        self.label_2.setText(_translate("MainWindow", "strength"))
        self.label_6.setText(_translate("MainWindow", "ddim_eta"))
        self.label_8.setText(_translate("MainWindow", "ddim_step"))
        self.label_5.setText(_translate("MainWindow", "Seed"))
        self.plms.setText(_translate("MainWindow", "plms"))
        self.rand_seed.setText(_translate("MainWindow", "rand seed"))
        self.use_seed.setText(_translate("MainWindow", "use seed"))
        self.label_4.setText(_translate("MainWindow", "Prompt"))
        self.prompt.setPlainText(_translate("MainWindow", "Potrait of Batman, intricate, highly detailed, digital painting, art station, smooth, sharp focus, illustration, art by artgerm and greg rutkowski and alphonse much"))
        self.prompt.setPlaceholderText(_translate("MainWindow", "Potrait of Batman, intricate, highly detailed, digital painting, art station, smooth, sharp focus, illustration, art by artgerm and greg rutkowski and alphonse much"))
        self.run_btn.setText(_translate("MainWindow", "Run"))
        self.label_10.setText(_translate("MainWindow", "init-img"))
        self.init_img.setText(_translate("MainWindow", "~/Pictures/test.png"))
        self.label_11.setText(_translate("MainWindow", "outdir"))
        self.outdir.setText(_translate("MainWindow", "outputs"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Stable Diffusion"))
        self.label_14.setText(_translate("MainWindow", "TBD"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "GFPGAN"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuabout.setTitle(_translate("MainWindow", "Help"))
        self.actionRun.setText(_translate("MainWindow", "Run"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setToolTip(_translate("MainWindow", "Exit Prompt Craft"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
