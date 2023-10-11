import sys
import time
from S_DES import S_DES
from extended_function import extended_function
from bruteforce_cracking import bruteforce_cracking
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # 初始化UI元素
        self.setWindowTitle("窗口开关示例")

        # 连接按钮点击事件到toggle_page方法,用于切换页面
        self.ui.pushButton.clicked.connect(self.toggle_page1)
        self.ui.pushButton_2.clicked.connect(self.toggle_page2)
        self.ui.pushButton_3.clicked.connect(self.toggle_page3)

        # 连接按钮点击事件到encrypt_page1方法，用于在页面1加密
        self.ui.Button_encrypt1.clicked.connect(self.encrypt_page1)
        # 连接按钮点击事件到decrypt_page1方法，用于在页面1解密
        self.ui.Button_decrypt1.clicked.connect(self.decrypt_page1)

        # 连接按钮点击事件到encrypt_page2方法，用于在页面2加密
        self.ui.Button_encrypt2.clicked.connect(self.encrypt_page2)
        # 连接按钮点击事件到decrypt_page2方法，用于在页面2解密
        self.ui.Button_decrypt2.clicked.connect(self.decrypt_page2)

        # 连接按钮点击事件到encrypt_page2方法，用于在页面3破解
        self.ui.Button_change1_3.clicked.connect(self.Brute_orce)

        # 用一个变量来跟踪窗口的状态
        self.is_window_open = True

    def toggle_page1(self):
        self.ui.stackedWidget1.setCurrentIndex(0)

    def encrypt_page1(self):
        # 获取page1中文本
        input_text_page1 = (self.ui.lineEdit_text1.text())
        input_key_page1 = (self.ui.lineEdit_key1.text())
        label_text_page1 = S_DES([int(char) for char in input_text_page1], [int(char) for char in input_key_page1])
        label_text_page1 = [str(num) for num in label_text_page1]
        self.ui.label.setText(''.join(label_text_page1))

    def decrypt_page1(self):
        # 获取page1中文本
        input_text_page1 = self.ui.lineEdit_text1.text()
        input_key_page1 = self.ui.lineEdit_key1.text()
        label_text_page1 = S_DES([int(char) for char in input_text_page1], [int(char) for char in input_key_page1], inv=True)
        label_text_page1 = [str(num) for num in label_text_page1]
        self.ui.label.setText(''.join(label_text_page1))

    def toggle_page2(self):
        self.ui.stackedWidget1.setCurrentIndex(1)

    def encrypt_page2(self):
        # 获取page2中文本
        input_text_page2 = (self.ui.lineEdit_text2.text())
        input_key_page2 = (self.ui.lineEdit_key2.text())
        label_text_page2 = extended_function(input_text_page2, [int(char) for char in input_key_page2])
        self.ui.label2.setText(label_text_page2)

    def decrypt_page2(self):
        # 获取page2中文本
        input_text_page2 = self.ui.lineEdit_text2.text()
        input_key_page2 = self.ui.lineEdit_key2.text()
        label_text_page2 = extended_function(input_text_page2, [int(char) for char in input_key_page2], inv=True)
        self.ui.label2.setText(label_text_page2)

    def toggle_page3(self):
        self.ui.stackedWidget1.setCurrentIndex(2)

    def Brute_orce(self):
        input_ciphertext_page3 = self.ui.lineEdit_ciphertext_3.text()
        input_plaintext_page3 = self.ui.lineEdit_plaintext_3.text()
        start_time = time.perf_counter()
        label_text_page3 = bruteforce_cracking(input_ciphertext_page3, input_plaintext_page3)
        elapsed_time = time.perf_counter() - start_time
        if label_text_page3:
            self.ui.label3.setText(str(label_text_page3) + "   耗时为" + str(elapsed_time))
        else:
            self.ui.label3.setText("无匹配密码")

    def open_close_window(self):
        if self.is_window_open:
            self.hide()  # 关闭窗口
            self.is_window_open = False
        else:
            self.show()  # 打开窗口
            self.is_window_open = True


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(916, 662)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 871, 591))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(30, 90, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 260, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 440, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.stackedWidget1 = QtWidgets.QStackedWidget(self.frame_2)
        self.stackedWidget1.setGeometry(QtCore.QRect(0, 10, 711, 581))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget1.sizePolicy().hasHeightForWidth())
        self.stackedWidget1.setSizePolicy(sizePolicy)
        self.stackedWidget1.setObjectName("stackedWidget1")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_key1 = QtWidgets.QLabel(self.page)
        self.label_key1.setGeometry(QtCore.QRect(120, 290, 41, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_key1.setFont(font)
        self.label_key1.setObjectName("label_key1")
        self.Button_encrypt1 = QtWidgets.QPushButton(self.page)
        self.Button_encrypt1.setGeometry(QtCore.QRect(230, 380, 93, 28))
        self.Button_encrypt1.setObjectName("Button_encrypt1")
        self.lineEdit_key1 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_key1.setGeometry(QtCore.QRect(170, 300, 411, 21))
        self.lineEdit_key1.setObjectName("lineEdit_key1")
        self.lineEdit_text1 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_text1.setGeometry(QtCore.QRect(170, 270, 411, 21))
        self.lineEdit_text1.setObjectName("lineEdit_text1")
        self.label_text1 = QtWidgets.QLabel(self.page)
        self.label_text1.setGeometry(QtCore.QRect(70, 260, 101, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_text1.setFont(font)
        self.label_text1.setObjectName("label_text1")
        self.Button_decrypt1 = QtWidgets.QPushButton(self.page)
        self.Button_decrypt1.setGeometry(QtCore.QRect(390, 380, 93, 28))
        self.Button_decrypt1.setObjectName("Button_decrypt1")
        self.listView_1 = QtWidgets.QListView(self.page)
        self.listView_1.setGeometry(QtCore.QRect(170, 140, 411, 51))
        self.listView_1.setObjectName("listView_1")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(340, 160, 400, 15))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.stackedWidget1.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.lineEdit_text2 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_text2.setGeometry(QtCore.QRect(180, 280, 411, 21))
        self.lineEdit_text2.setObjectName("lineEdit_text2")
        self.Button_decrypt2 = QtWidgets.QPushButton(self.page_2)
        self.Button_decrypt2.setGeometry(QtCore.QRect(400, 390, 93, 28))
        self.Button_decrypt2.setObjectName("Button_decrypt2")
        self.lineEdit_key2 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_key2.setGeometry(QtCore.QRect(180, 310, 411, 21))
        self.lineEdit_key2.setObjectName("lineEdit_key2")
        self.label_text2 = QtWidgets.QLabel(self.page_2)
        self.label_text2.setGeometry(QtCore.QRect(60, 270, 121, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_text2.setFont(font)
        self.label_text2.setObjectName("label_text2")
        self.label_key2 = QtWidgets.QLabel(self.page_2)
        self.label_key2.setGeometry(QtCore.QRect(130, 300, 41, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_key2.setFont(font)
        self.label_key2.setObjectName("label_key2")
        self.listView_3 = QtWidgets.QListView(self.page_2)
        self.listView_3.setGeometry(QtCore.QRect(180, 150, 411, 51))
        self.listView_3.setObjectName("listView_3")
        self.label2 = QtWidgets.QLabel(self.page_2)
        self.label2.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.label2.setGeometry(QtCore.QRect(360, 170, 400, 15))
        self.label2.setText("")
        self.label2.setObjectName("label2")
        self.Button_encrypt2 = QtWidgets.QPushButton(self.page_2)
        self.Button_encrypt2.setGeometry(QtCore.QRect(240, 390, 93, 28))
        self.Button_encrypt2.setObjectName("Button_encrypt2")
        self.stackedWidget1.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_ciphertext3 = QtWidgets.QLabel(self.page_3)
        self.label_ciphertext3.setGeometry(QtCore.QRect(540, 240, 72, 15))
        self.label_ciphertext3.setObjectName("label_ciphertext3")
        self.label_plaintext3 = QtWidgets.QLabel(self.page_3)
        self.label_plaintext3.setGeometry(QtCore.QRect(160, 240, 72, 15))
        self.label_plaintext3.setObjectName("label_plaintext3")
        self.label_key3 = QtWidgets.QLabel(self.page_3)
        self.label_key3.setGeometry(QtCore.QRect(100, 390, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_key3.setFont(font)
        self.label_key3.setObjectName("label_key3")
        self.Button_change1_3 = QtWidgets.QPushButton(self.page_3)
        self.Button_change1_3.setGeometry(QtCore.QRect(310, 310, 93, 28))
        self.Button_change1_3.setObjectName("Button_change1_3")
        self.lineEdit_ciphertext_3 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_ciphertext_3.setGeometry(QtCore.QRect(40, 60, 261, 171))
        self.lineEdit_ciphertext_3.setObjectName("lineEdit_ciphertext_3")
        self.lineEdit_plaintext_3 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_plaintext_3.setGeometry(QtCore.QRect(420, 60, 261, 171))
        self.lineEdit_plaintext_3.setObjectName("lineEdit_plaintext_3")
        self.label3 = QtWidgets.QLabel(self.page_3)
        self.label3.setGeometry(QtCore.QRect(160, 350, 411, 200))
        self.label3.setText("")
        self.label3.setWordWrap(True)
        self.stackedWidget1.addWidget(self.page_3)
        self.horizontalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.stackedWidget1.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Binary"))
        self.pushButton_2.setText(_translate("MainWindow", "String"))
        self.pushButton_3.setText(_translate("MainWindow", "暴力破解"))
        self.label_key1.setText(_translate("MainWindow", "key："))
        self.Button_encrypt1.setText(_translate("MainWindow", "加密"))
        self.label_text1.setText(_translate("MainWindow", "明文/密文："))
        self.Button_decrypt1.setText(_translate("MainWindow", "解密"))
        self.Button_decrypt2.setText(_translate("MainWindow", "解密"))
        self.label_text2.setText(_translate("MainWindow", "ASCII字符串："))
        self.label_key2.setText(_translate("MainWindow", "key："))
        self.Button_encrypt2.setText(_translate("MainWindow", "加密"))
        self.label_ciphertext3.setText(_translate("MainWindow", "密文"))
        self.label_plaintext3.setText(_translate("MainWindow", "明文"))
        self.label_key3.setText(_translate("MainWindow", "keys："))
        self.Button_change1_3.setText(_translate("MainWindow", "暴力破解"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
