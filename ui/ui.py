from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1053, 794)
        self._centralwidget = QtWidgets.QWidget(MainWindow)
        self._centralwidget.setObjectName("_centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self._centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self._horizontalLayout = QtWidgets.QHBoxLayout()
        self._horizontalLayout.setObjectName("_horizontalLayout")
        self._groupBox2 = QtWidgets.QGroupBox(self._centralwidget)
        self._groupBox2.setObjectName("_groupBox2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self._groupBox2)
        self.verticalLayout.setObjectName("verticalLayout")
        self._label1 = QtWidgets.QLabel(self._groupBox2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._label1.sizePolicy().hasHeightForWidth())
        self._label1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self._label1.setFont(font)
        self._label1.setObjectName("_label1")
        self.verticalLayout.addWidget(self._label1)
        self._nodes_list = QtWidgets.QListWidget(self._groupBox2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._nodes_list.sizePolicy().hasHeightForWidth())
        self._nodes_list.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self._nodes_list.setFont(font)
        self._nodes_list.setObjectName("_nodes_list")
        self.verticalLayout.addWidget(self._nodes_list)
        self._save_log_file = QtWidgets.QPushButton(self._groupBox2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._save_log_file.sizePolicy().hasHeightForWidth())
        self._save_log_file.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self._save_log_file.setFont(font)
        self._save_log_file.setObjectName("_save_log_file")
        self.verticalLayout.addWidget(self._save_log_file)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 10)
        self.verticalLayout.setStretch(2, 1)
        self._horizontalLayout.addWidget(self._groupBox2)
        self._groupBox = QtWidgets.QGroupBox(self._centralwidget)
        self._groupBox.setEnabled(True)
        self._groupBox.setObjectName("_groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self._groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self._horizontalLayout2 = QtWidgets.QHBoxLayout()
        self._horizontalLayout2.setObjectName("_horizontalLayout2")
        self._label2 = QtWidgets.QLabel(self._groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._label2.sizePolicy().hasHeightForWidth())
        self._label2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self._label2.setFont(font)
        self._label2.setObjectName("_label2")
        self._horizontalLayout2.addWidget(self._label2)
        self._node_status = QtWidgets.QTextBrowser(self._groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._node_status.sizePolicy().hasHeightForWidth())
        self._node_status.setSizePolicy(sizePolicy)
        self._node_status.setObjectName("_node_status")
        self._horizontalLayout2.addWidget(self._node_status)
        self._horizontalLayout2.setStretch(0, 2)
        self._horizontalLayout2.setStretch(1, 8)
        self.verticalLayout_4.addLayout(self._horizontalLayout2)
        self._sensor_data_dict = QtWidgets.QTableWidget(self._groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._sensor_data_dict.sizePolicy().hasHeightForWidth())
        self._sensor_data_dict.setSizePolicy(sizePolicy)
        self._sensor_data_dict.setObjectName("_sensor_data_dict")
        self._sensor_data_dict.setColumnCount(2)
        self._sensor_data_dict.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        item.setFont(font)
        self._sensor_data_dict.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        item.setFont(font)
        self._sensor_data_dict.setHorizontalHeaderItem(1, item)
        self.verticalLayout_4.addWidget(self._sensor_data_dict)
        self._label3 = QtWidgets.QLabel(self._groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._label3.sizePolicy().hasHeightForWidth())
        self._label3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self._label3.setFont(font)
        self._label3.setObjectName("_label3")
        self.verticalLayout_4.addWidget(self._label3)
        self._window_logs = QtWidgets.QTextBrowser(self._groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._window_logs.sizePolicy().hasHeightForWidth())
        self._window_logs.setSizePolicy(sizePolicy)
        self._window_logs.setObjectName("_window_logs")
        self.verticalLayout_4.addWidget(self._window_logs)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 5)
        self.verticalLayout_4.setStretch(2, 1)
        self.verticalLayout_4.setStretch(3, 5)
        self._horizontalLayout.addWidget(self._groupBox)
        self._horizontalLayout.setStretch(0, 3)
        self._horizontalLayout.setStretch(1, 9)
        self.horizontalLayout_3.addLayout(self._horizontalLayout)
        MainWindow.setCentralWidget(self._centralwidget)
        self._menubar = QtWidgets.QMenuBar(MainWindow)
        self._menubar.setGeometry(QtCore.QRect(0, 0, 1053, 22))
        self._menubar.setObjectName("_menubar")
        MainWindow.setMenuBar(self._menubar)
        self._statusbar = QtWidgets.QStatusBar(MainWindow)
        self._statusbar.setObjectName("_statusbar")
        MainWindow.setStatusBar(self._statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self._label1.setText(_translate("MainWindow", "节点选择"))
        self._save_log_file.setText(_translate("MainWindow", "保存文本日志"))
        self._label2.setText(_translate("MainWindow", "在线状态"))
        item = self._sensor_data_dict.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "参数名"))
        item = self._sensor_data_dict.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "参数值"))
        self._label3.setText(_translate("MainWindow", "日志信息"))