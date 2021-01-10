import sys, os, re
from PyQt5 import QtWidgets, QtCore, QtGui


 



BASE_DIR =  os.path.dirname(os.path.abspath(__file__))

 



class Test(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		# main Layout
		self.gridLayout = QtWidgets.QGridLayout(self)
		self.gridLayout.setObjectName(u"gridLayout")
		
		# add item
		self.verticalSpacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)
		
		self.horizontalSpacer_4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

		self.horizontalSpacer_3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

		self.verticalSpacer_2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.gridLayout.addItem(self.verticalSpacer_2, 2, 1, 1, 1)
		

		# ------central widget------

		self.main_widget = QtWidgets.QWidget()
		self.main_widget.setObjectName(u"main_widget")
		self.main_widget.setStyleSheet(u"background:red;")
		self.gridLayout.addWidget(self.main_widget, 1, 1, 1, 1)
		
		


		
		
		
		
		
		
		
		
		
		
		
		
		
		
		self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.main_widget)
		self.verticalLayout_3.setObjectName(u"verticalLayout_3")
		self.title = QtWidgets.QLabel(self.main_widget)
		self.title.setObjectName(u"title")
		self.title.setStyleSheet(u"color:white;")
		self.title.setText('Convert')

		self.verticalLayout_3.addWidget(self.title, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

		self.widget_from = QtWidgets.QWidget(self.main_widget)
		self.widget_from.setObjectName(u"widget_from")
		self.widget_from.setStyleSheet(u"background:blue;")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_from)
		self.verticalLayout.setObjectName(u"verticalLayout")
		self.header_from = QtWidgets.QWidget(self.widget_from)
		self.header_from.setObjectName(u"header_from")
		self.header_from.setStyleSheet(u"background:green;")
		self.horizontalLayout = QtWidgets.QHBoxLayout(self.header_from)
		self.horizontalLayout.setObjectName(u"horizontalLayout")
		self.title_from = QtWidgets.QLabel(self.header_from)
		self.title_from.setObjectName(u"title_from")
		self.title_from.setStyleSheet(u"color:red;")
		self.title_from.setText('From')

		self.horizontalLayout.addWidget(self.title_from)

		self.horizontalSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

		self.horizontalLayout.addItem(self.horizontalSpacer)




		self.verticalLayout.addWidget(self.header_from)


		self.but_from = QtWidgets.QPushButton(self.widget_from)
		self.but_from.setText("select file")
		self.but_from.clicked.connect(self.fromgetfile)
		self.verticalLayout.addWidget(self.but_from)




		self.patch_from = QtWidgets.QLineEdit(self.widget_from)
		self.patch_from.setObjectName(u"patch_from")
		self.patch_from.setText(BASE_DIR)
		
		self.patch_from.setStyleSheet(u"background:white;")

		self.verticalLayout.addWidget(self.patch_from)
		
		
		
		
		
		self.verticalLayout_3.addWidget(self.widget_from)

		self.widget_to = QtWidgets.QWidget(self.main_widget)
		self.widget_to.setObjectName(u"widget_to")
		self.widget_to.setStyleSheet(u"background:blue;")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_to)
		self.verticalLayout_2.setObjectName(u"verticalLayout_2")
		self.header_to = QtWidgets.QWidget(self.widget_to)
		self.header_to.setObjectName(u"header_to")
		self.header_to.setStyleSheet(u"background:green;")
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header_to)
		self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
		self.title_to = QtWidgets.QLabel(self.header_to)
		self.title_to.setObjectName(u"title_to")
		self.title_to.setStyleSheet(u"color:red;")
		self.title_to.setText('To')

		self.horizontalLayout_2.addWidget(self.title_to)

		self.horizontalSpacer_2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

		self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

		self.select_to = QtWidgets.QComboBox(self.header_to)
		self.select_to.addItem("Svg")
		self.select_to.addItem("Ttf")
		self.select_to.addItem("png")
		self.select_to.setObjectName(u"select_to")
		self.select_to.setStyleSheet(u"background:white;")

		self.horizontalLayout_2.addWidget(self.select_to)


		self.verticalLayout_2.addWidget(self.header_to)


		self.but_to = QtWidgets.QPushButton(self.widget_from)
		self.but_to.setText("select file")
		self.but_to.clicked.connect(self.togetfile)
		self.verticalLayout_2.addWidget(self.but_to)




		self.patch_to = QtWidgets.QLineEdit(self.widget_to)
		self.patch_to.setObjectName(u"patch_to")
		self.patch_to.setStyleSheet(u"background:white;")
		self.patch_to.setText(BASE_DIR)

		self.verticalLayout_2.addWidget(self.patch_to)


		self.verticalLayout_3.addWidget(self.widget_to)

		self.config = QtWidgets.QLineEdit(self.main_widget)
		self.config.setObjectName(u"config")
		self.config.setStyleSheet(u"background:white;")

		self.verticalLayout_3.addWidget(self.config)

		
		
		self.run_button = QtWidgets.QPushButton(self.main_widget)
		self.run_button.setObjectName(u"run_button")
		self.run_button.setStyleSheet(u"background:white;")
		self.run_button.setText('Run')
		self.run_button.clicked.connect(self.convert_file)
		self.verticalLayout_3.addWidget(self.run_button)
		
		
	def fromgetfile(self):
		file = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', 
		 'c:\\',"Image files (*.jpg *.gif *.png)")
		print(file[0])
		self.patch_from.setText(file[0])
	def togetfile(self):
		file = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', 
		 'c:\\',"Image files (*.jpg *.gif *.png)")
		print(file[0])
		self.patch_to.setText(file[0])
		
	def convert_file(self):
		print(self.patch_to.text())
		print(self.patch_from.text())
		print(self.select_to.currentText())
		print(self.select_to.currentIndex())
		
		
		
		'''
		#Clear()
		addItems()

		Adds items in a list object

		currentText()

		currentIndex()
		'''

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	w = Test()
	w.resize(640, 570)  # Size window
	w.show()
	sys.exit(app.exec_())
