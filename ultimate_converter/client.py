import sys, os, re
from PyQt5 import QtWidgets, QtCore, QtGui

from converter import ultimate_converter, get_obj, check_format, file_pack
 
# for converter
import time, re, os, random, sys, json; 


BASE_DIR =  os.path.dirname(os.path.abspath(__file__))


class Test(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		
		self.setStyleSheet('background:#6f6f7d')
		# main Layout
		self.align_center_layout = QtWidgets.QGridLayout(self)
		self.align_center_layout.setObjectName(u"gridLayout")
		
		
		
		
		# add item
		self.verticalSpacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.align_center_layout.addItem(self.verticalSpacer, 0, 1, 1, 1)
		
		self.horizontalSpacer_4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.align_center_layout.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

		self.horizontalSpacer_3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.align_center_layout.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

		self.verticalSpacer_2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.align_center_layout.addItem(self.verticalSpacer_2, 2, 1, 1, 1)
		

		# ------central widget------

		self.main_widget = QtWidgets.QWidget()
		self.main_widget.setObjectName(u"main_widget")
		self.main_widget.setStyleSheet(u"background:#525261;")
		self.align_center_layout.addWidget(self.main_widget, 1, 1, 1, 1)
		
		


		
		
		
		
		
		
		
		
		
		 
		
		
		
		
		self.main_widget_layout = QtWidgets.QVBoxLayout(self.main_widget)
		self.main_widget_layout.setObjectName(u"verticalLayout_3")
		self.title = QtWidgets.QLabel(self.main_widget)
		self.title.setObjectName(u"title")
		self.title.setStyleSheet(u"color:#fefeff;")
		self.title.setText('Convert')

		self.main_widget_layout.addWidget(self.title, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

		self.widget_from = QtWidgets.QWidget(self.main_widget)
		self.widget_from.setObjectName(u"widget_from")
		self.widget_from.setStyleSheet(u"background:#4b4b5a;")
		self.main_widget_layout.addWidget(self.widget_from)
		
		
		self.from_layout = QtWidgets.QVBoxLayout(self.widget_from)
		self.from_layout.setObjectName(u"verticalLayout")
		
		
		
		self.title_from = QtWidgets.QLabel(self.widget_from)
		self.title_from.setObjectName(u"title_from")
		self.title_from.setStyleSheet(u"color:#dfe1e6;")
		self.title_from.setText('From')
		self.from_layout.addWidget(self.title_from)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		self.widget_file_from = QtWidgets.QWidget(self.widget_from)
		self.widget_file_from.setStyleSheet(u"background:#3f3f4c;")
		self.from_layout.addWidget(self.widget_file_from)
		
		self.widget_file_from_layout = QtWidgets.QVBoxLayout(self.widget_file_from)
		
		self.title_file_from = QtWidgets.QLabel(self.widget_file_from)
		self.title_file_from.setObjectName(u"title_file_from")
		self.title_file_from.setStyleSheet(u"color:#dfe1e6;")
		self.title_file_from.setText('File')
		self.widget_file_from_layout.addWidget(self.title_file_from)
		
		
		
		# QComboBox for type
		self.select_file_from = QtWidgets.QComboBox(self.widget_file_from)
		self.select_file_from.setObjectName(u"select_file_from")
		self.select_file_from.setStyleSheet(u"background:#1d1d2f;color:#ececf1;border:none;padding:3px;")
		self.widget_file_from_layout.addWidget(self.select_file_from)
		
		
		self.select_file_from.addItem("none")
		# get type
		type = check_format()
		for text in type :
			self.select_file_from.addItem(text)
		# run function when changed QComboBox
		self.select_file_from.currentIndexChanged.connect(self.change_format)
		

		
		
		self.but_file_from = QtWidgets.QPushButton(self.widget_file_from)
		self.but_file_from.setText("select file")
		self.but_file_from.setStyleSheet(u"background:#1d1d2f;color:#ececf1;border:none;padding:3px;")
		self.widget_file_from_layout.addWidget(self.but_file_from)
		
		self.but_file_from.clicked.connect(self.get_file)
		
				

		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		self.widget_folder_from = QtWidgets.QWidget(self.widget_from)
		self.widget_folder_from.setStyleSheet(u"background:#3f3f4c;")
		self.from_layout.addWidget(self.widget_folder_from)
		
		self.widget_folder_from_layout = QtWidgets.QVBoxLayout(self.widget_folder_from)
		

		self.title_folder_from = QtWidgets.QLabel(self.widget_folder_from)
		self.title_folder_from.setObjectName(u"title_file_from")
		self.title_folder_from.setStyleSheet(u"color:#dfe1e6;")
		self.title_folder_from.setText('Folder')
		self.widget_folder_from_layout.addWidget(self.title_folder_from)
		
		
		# QComboBox for format
		self.select_folder_from = QtWidgets.QComboBox(self.widget_file_from)
		self.select_folder_from.setObjectName(u"select_folder_from")
		self.select_folder_from.setStyleSheet(u"background:#1d1d2f;color:#ececf1;border:none;padding:3px;")
		self.widget_folder_from_layout.addWidget(self.select_folder_from)
		
		
		self.select_folder_from.addItem("---")

		
		
		self.but_folder_from = QtWidgets.QPushButton(self.widget_file_from)
		self.but_folder_from.setText("select folder")
		self.but_folder_from.setStyleSheet(u"background:#1d1d2f;color:#ececf1;border:none;padding:3px;")
		self.widget_folder_from_layout.addWidget(self.but_folder_from)
		
		self.but_folder_from.clicked.connect(self.get_folder)
		
		
				
		
		
		
		
		
		
		
		self.path_from = QtWidgets.QLineEdit(self.widget_from)
		self.path_from.setObjectName(u"path_from")
		self.path_from.setText(BASE_DIR)
		self.path_from.setStyleSheet(u"background:#12121f;color:#ececf1;border:none;padding:3px;")
		self.from_layout.addWidget(self.path_from)
		
		
		
		
		
		
		
		
 
		
		

		
		
		
		
		
		
		
		


		




 




		
		
		
		
		
		

		self.widget_to = QtWidgets.QWidget(self.main_widget)
		self.widget_to.setObjectName(u"widget_to")
		self.widget_to.setStyleSheet(u"background:#3f3f4c;")
		self.main_widget_layout.addWidget(self.widget_to)
		
		self.to_layout = QtWidgets.QVBoxLayout(self.widget_to)
		self.to_layout.setObjectName(u"verticalLayout_2")
		
		
		
		
		self.title_to = QtWidgets.QLabel(self.widget_to)
		self.title_to.setObjectName(u"title_to")
		self.title_to.setStyleSheet(u"color:#dfe1e6;")
		self.title_to.setText('To')

		self.to_layout.addWidget(self.title_to)

		
		
		
		self.select_to = QtWidgets.QComboBox(self.widget_to)
		self.select_to.setObjectName(u"select_to")
		self.select_to.setStyleSheet(u"background:#1d1d2f;color:#ececf1;border:none;padding:3px;")
		self.to_layout.addWidget(self.select_to)
		
		self.select_to.addItem("---")
		
		
		
		
		self.but_to = QtWidgets.QPushButton(self.widget_to)
		self.but_to.setText("select folder")
		self.but_to.clicked.connect(self.select_folder)
		self.but_to.setStyleSheet(u"background:#1d1d2f;color:#ececf1;border:none;padding:3px;")
		self.to_layout.addWidget(self.but_to)
		
		
		self.path_to = QtWidgets.QLineEdit(self.widget_to)
		self.path_to.setObjectName(u"path_to")
		self.path_to.setStyleSheet(u"background:#12121f;color:#ececf1;border:none;padding:3px;")
		self.path_to.setText(BASE_DIR+r"\return")

		self.to_layout.addWidget(self.path_to)
		
		
		

		
		



		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		

		self.config = QtWidgets.QLineEdit(self.main_widget)
		self.config.setObjectName(u"config")
		self.config.setStyleSheet(u"background:#12121f;color:#ececf1;border:none;padding:3px;")

		self.main_widget_layout.addWidget(self.config)

		
		
		self.run_button = QtWidgets.QPushButton(self.main_widget)
		self.run_button.setObjectName(u"run_button")
		self.run_button.setStyleSheet(u"background:#12121f;color:#ececf1;border:none;padding:3px;")
		self.run_button.setText('Run')
		self.run_button.clicked.connect(self.convert_file)
		self.main_widget_layout.addWidget(self.run_button)
		
		 
		
		
		
		
		
		
		
		
		

		
		
		
		
		
		# select file
		
		self.obj = get_obj()
		self.format = '(*)'
		
		
		
		
	def get_file(self):
		if os.path.exists(self.path_from.text()) :
			path = self.path_from.text()
		else:
			path = 'C:\\'
		
		
		# select file
		file = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', 
		 path, self.format)
		# patch to file
		give_path = file[0]
		
		
		
		

		
		
		

		# patch to file
		
		print(give_path)
		if give_path:
			self.path_from.setText(give_path)
			
			
			# give format
			pattern = re.compile(r'\w+')
			give_format = pattern.findall(give_path)[-1].lower()
			print(give_format)
			
			

			
			
			change_type = check_format(give_format)
			print(change_type)
			if change_type :
				self.select_file_from.clear()
				self.select_file_from.addItem('none')
				for text in change_type:
					self.select_file_from.addItem(text)
			
			
			
			
	def get_folder(self):
		if os.path.exists(self.path_from.text()) :
			path = self.path_from.text()
		else:
			path = 'C:\\'
		folder = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select a directory', path)
		print(folder)
		if folder :
			self.path_from.setText(folder)
		 
			
	def change_format(self):
		# Change available formats
		text = self.select_file_from.currentText()
		if text == 'none':
			 self.format = "(*)"
		elif text:
			string = "("
			print(text)
			self.select_folder_from.clear()
			for format in self.obj[text]['give']:
				self.select_folder_from.addItem(format)
				string = string +' *.'+format
			string = string +  ")"
			print(string)
			self.format = string
			
			self.select_to.clear()
			for format in self.obj[text]['get']:
				self.select_to.addItem(format)
		print('changed')
		
		
		
		
		
	def select_folder(self):
		if os.path.exists(self.path_to.text()) :
			path = self.path_to.text()
		else:
			path = 'C:\\'
		
		folder = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select a directory', path)
		print(folder)
		if folder :
			self.path_to.setText(folder)
		
		
		
		
		
	def convert_file(self):
		print(self.select_file_from.currentText())
		print(self.select_file_from.currentIndex())
		
		print(self.select_folder_from.currentText())
		print(self.select_folder_from.currentIndex())
		
		print(self.path_from.text())
		
		
		print(self.select_to.currentText())
		print(self.select_to.currentIndex())
		
		print(self.path_to.text())

		'''
		image
		1
		png
		0
		D:/Temp/Images/few.PNG
		jpeg
		2
		D:\Work\Project\git\git_work\ine_client\convert\return
		'''
		
		
		
		
		
		
		type = self.select_file_from.currentText()
		
		give_format_folder = self.select_folder_from.currentText()
		
		
		give_path = self.path_from.text()
		
		
		get_format = self.select_to.currentText()
		get_path = self.path_to.text() + '/'
		
		
		
		
		
		if os.path.exists(give_path) and os.path.exists(get_path):
			print(give_path)
			v = give_path.split('/')
			print(v[-1])
			d = v[-1].split('.')
			print(d)
			try: 
				format = d[1]
			except IndexError:
				format = False
				
			if format :
				print('search file')
				
				ultimate_converter(give_path,get_path,get_format,type)
				
				
				
				
				
			else:
				print('search folder')
				if give_format_folder == '---':
					format = False
				else:
					format = give_format_folder
					
				pack = file_pack(give_path,format)
				print(pack)
				for list in pack:
					print(list['path'])
					if len(list['tags']) == 0:
						tag_list = False
					else:
						tag_list = list['tags']
					
					
					ultimate_converter(list['path'],get_path,get_format,type,tags=list['tags'])
				
				
				
				
				
				

				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
		else:
			print('not correct patch')
		
		
		
		

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	w = Test()
	w.resize(640, 570)  # Size window
	w.show()
	sys.exit(app.exec_())
