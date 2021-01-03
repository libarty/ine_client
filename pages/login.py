import sys, os, requests, json, re ,socket
from PyQt5 import QtWidgets, QtCore, QtGui


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path += [BASE_DIR+r'\pieces']
sys.path += [BASE_DIR+r'\custom_settings']

from back_animation import BackGeometryAnimation
from lang import get_lang
from style import get_style
from ip_server import list_ip
from general_functions import validate_password
from main import *








# login
# url = "http://127.0.0.1:8000/api/extra_user/post/"
#
#
# # for phone
# data2 = {
# 	"user": 19,
# 	'phone': int('900879'),
# }
# headers = {'Authorization': 'Token ' + '4eeef4bfe6707e87eb8fea3e14f00a7bbfa48950'}
# try:
# 	v = requests.post(url, data=data2, headers=headers)
#
# 	s = json.loads(v.content.decode('utf-8'))
# 	print(s)
# except:
# 	print('b')
#
# url4 = "http://127.0.0.1:8000/api/user/"
#
# get_id = requests.get(url4 + '?username=' + 'admin')
# get_id_dict = json.loads(get_id.content.decode('utf-8'))
# print(get_id_dict[0]['id'])




# url = "http://127.0.0.1:8000/api/auth/token/login/"
# data = {
# 	'username':'admin',
# 	'password':'1',
# }
# res = requests.post(url, data=data)
#
# token=json.loads(res.content.decode('utf-8'))
# print(token)
#
#
# from rest_framework import permissions
# permission_classes = [permissions.IsAuthenticated]
# headers
# d = {'Authorization': token}

# import requests, json
# # get
# url = "http://127.0.0.1:8000/api/static/"
# token = '4eeef4bfe6707e87eb8fea3e14f00a7bbfa48950'
# headers = {'Authorization': 'Token '+ token}
#
# res = requests.get(url,headers=headers)
# pars=json.loads(res.content.decode('utf-8'))
# print(pars)




class TextBlock(QtWidgets.QWidget):
	def __init__(
			self,
			parent=None,
			back_color='white',
			title_color="white",
			title_text_color="black",
			title_size=10,
			title_padding=0,
			title_center=True,
			title_text='title',
			edit_color='white',
			edit_text_color='black',
			edit_size=10,
			edit_padding=20,
			edit_text='text',

			type="Text",
	):
		super(TextBlock, self).__init__(parent)
		self.setStyleSheet("background:{};".format('yellow'))
		# set layout
		self.lay = QtWidgets.QVBoxLayout(self)
		self.lay.setSpacing(0)
		self.lay.setContentsMargins(0, 0, 0, 0)
		# main widget
		self.main = QtWidgets.QWidget(self)
		self.main.setStyleSheet("background:{};".format(back_color))

		self.lay.addWidget(self.main)
		self.main_lay = QtWidgets.QVBoxLayout(self.main)
		self.main_lay.setSpacing(0)
		self.main_lay.setContentsMargins(0, 0, 0, 0)

		self.label = QtWidgets.QLabel(self)
		self.label.setStyleSheet("background:{};color:{};font-size:{}px;padding:{}px;".format(
			title_color,
			title_text_color,
			title_size,
			title_padding,
		))
		if title_center:
			self.label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
		self.label.setText(title_text)


		if type == "Text":
			self.edit = QtWidgets.QLineEdit(self)
		elif type == "Password":
			self.edit = QtWidgets.QLineEdit(self)
			self.edit.setEchoMode(QtWidgets.QLineEdit.Password)
		elif type == "Phone":
			self.edit = QtWidgets.QLineEdit(self)
			onlyInt = QtGui.QIntValidator()
			self.edit.setValidator(onlyInt)
		elif type == "Radio":
			self.edit = QtWidgets.QRadioButton(self)
		elif type == "Textarea":
			self.edit = QtWidgets.QTextEdit(self)
		
		pixmap = QtGui.QPixmap(BASE_DIR+r'\media\cur\3.png').scaled(20, 20) 
		cursor = QtGui.QCursor(pixmap)
		self.edit.setCursor(cursor)
		
		self.edit.setStyleSheet('border:none;background:{};color:{};font-size:{}px;padding:{}px;'.format(
			edit_color,
			edit_text_color,
			edit_size,
			edit_padding,
		))
		self.edit.setText(edit_text)


		self.label.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.main.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)




		self.main_lay.addWidget(self.label)
		self.main_lay.addWidget(self.edit)







class Test(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.resize(500, 500)
		pixmap = QtGui.QPixmap(BASE_DIR+r'\media\cur\1.png').scaled(20, 20) 
		cursor = QtGui.QCursor(pixmap)
		self.setCursor(cursor)
		# set cursor
		pixmap = QtGui.QPixmap(BASE_DIR+r'\media\cur\2.png').scaled(20, 20) 
		cursor2 = QtGui.QCursor(pixmap)


		# check connect to server
		v = False
		x = 0
		while v == False:
			try:
				test = requests.get(list_ip[x], timeout=5)
				self.url = list_ip[x]
				v = True
			except:
				if list_ip[x] == list_ip[-1]:
					self.url = False
					v = True
			x += 1










		# set array of widget names
		self.arr_id = {
			'log_sign_in': ['log_nickname', 'log_password'],  # exit, Registration, entry
			'log_registration': ['log_nickname', 'log_password', 'log_password_c', 'log_email', 'log_phone'],  # back->Sign_in, next->Check_code
			'log_check_code': ['log_code-1', 'log_code-2'],  # back->Registration, entry
		}

		# set main layout
		lay = QtWidgets.QVBoxLayout(self)
		lay.setSpacing(0)
		lay.setContentsMargins(0, 0, 0, 0)
		# set main widget
		main = QtWidgets.QWidget(self)
		main.setStyleSheet("background:{};".format(get_style('log_main_color')))
		lay.addWidget(main)
		# set layout for center other widgets
		main_lay = QtWidgets.QGridLayout(main)
		main_lay.setSpacing(0)
		main_lay.setContentsMargins(0, 0, 0, 0)

		# set animation background
		back = BackGeometryAnimation(
			num_x=10,
			num_y=10,
			color=get_style('log_back_color'),
			min_size=20,
			max_size=60,
			min_rotate=0,
			max_rotate=90,
			duration=8000,
			parent=self
		)
		main_lay.addWidget(back, 0, 0, 1, 1, alignment=QtCore.Qt.AlignCenter)
		# set text widget
		for x in self.arr_id:
			center = QtWidgets.QWidget(self)
			# set id
			setattr(self, 'center_{}'.format(x), center)
			center.setStyleSheet("background:{};".format(get_style('log_center_color')))
			center.setFixedWidth(get_style('log_center_width'))
			# set layout for content
			center.center_lay = QtWidgets.QVBoxLayout(center)
			center.title = QtWidgets.QLabel(center)

			# set style for title
			center.title.setStyleSheet("background:{};padding:{}px;color:{};font-size:{}px;".format(
				get_style('log_title_color'),
				get_style('log_title_padding'),

				get_style('log_title_text_color'),
				get_style('log_title_size')
			))
			if get_style('log_title_center'):
				center.title.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

			# set text
			center.title.setText(get_lang(x))
			center.center_lay.addWidget(center.title)

			# set triangle style
			# for left
			style_left = 'background:qconicalgradient(cx:{} , cy:0.5, angle:{}, stop:0.1450 {}, stop:0.1451 {})'.format(
				0,
				334,
				get_style('log_edblock_triangle_color'),
				get_style('log_edblock_triangle_back'),
			)
			# for right
			style_right = 'background:qconicalgradient(cx:{} , cy:0.5, angle:{}, stop:0.1450 {}, stop:0.1451 {})'.format(
				1,
				153,
				get_style('log_edblock_triangle_color'),
				get_style('log_edblock_triangle_back'),
			)



			for y in range(len(self.arr_id[x])):
				center.text_block = TextBlock(
					parent=center,
					back_color=get_style('log_edblock_back_color'),
					title_color=get_style('log_edblock_title_color'),
					title_text_color=get_style('log_edblock_title_text_color'),
					title_size=get_style('log_edblock_title_size'),
					title_padding=get_style('log_edblock_title_padding'),
					title_center=get_style('log_edblock_title_center'),
					title_text=get_lang(self.arr_id[x][y]),

					edit_color=get_style('log_edblock_edit_color'),
					edit_text_color=get_style('log_edblock_edit_text_color'),
					edit_size=get_style('log_edblock_edit_size'),
					edit_padding=get_style('log_edblock_edit_padding'),
					edit_text='',

					type='Password' if 'password' in  self.arr_id[x][y]  else 'Phone' if 'phone' in  self.arr_id[x][y] else 'Text'
				)
				

				# set id
				setattr(self, 'text_block_{}_{}'.format(x, self.arr_id[x][y]), center.text_block)
				center.center_lay.addWidget(center.text_block)
			# block for error
			center.error_block = QtWidgets.QLabel(center)
			center.error_block.setStyleSheet('background:{};color:{};font-size:{};padding:{}px'.format(
				get_style('log_error_back_color'),
				get_style('log_error_text_color'),
				get_style('log_error_size'),
				get_style('log_error_padding'),
			))
			center.error_block.hide()
			center.center_lay.addWidget(center.error_block)
			# block for buttons
			center.widget_button = QtWidgets.QWidget(center)
			center.widget_button_lay = QtWidgets.QHBoxLayout(center.widget_button)
			center.center_lay.addWidget(center.widget_button)
			# add center widget
			main_lay.addWidget(center, 0, 0, 1, 1, alignment=QtCore.Qt.AlignCenter)
			# set right button
			center.right_button = QtWidgets.QPushButton(center)
			center.right_button.setStyleSheet('border:none;{}'.format(style_right))
			center.right_button.setFixedHeight(get_style('log_button_size'))
			center.right_button.setFixedWidth(get_style('log_button_size'))
			# set left button
			center.left_button = QtWidgets.QPushButton(center)
			center.left_button.setStyleSheet('border:none;{}'.format(style_left))
			center.left_button.setFixedHeight(get_style('log_button_size'))
			center.left_button.setFixedWidth(get_style('log_button_size'))
			
			# set cursor
			center.right_button.setCursor(cursor2)
			center.left_button.setCursor(cursor2)

			# set buttons on the sides
			center.vs = QtWidgets.QSpacerItem(
				0, 0,
				QtWidgets.QSizePolicy.Expanding,
				QtWidgets.QSizePolicy.Minimum
			)

			# set layout
			center.widget_button_lay.addWidget(center.left_button)
			center.widget_button_lay.addItem(center.vs)
			center.widget_button_lay.addWidget(center.right_button)

			# hide each block
			center.hide()

		# get each block individually

		# get login block
		self.login = getattr(self, 'center_{}'.format(list(self.arr_id)[0]))


		try:
			way = open(BASE_DIR + r'\cookies\token.json', 'r')
			save_log = json.load(way)

			log = getattr(self, 'text_block_{}_{}'.format(
				list(self.arr_id)[0],
				self.arr_id[list(self.arr_id)[0]][0]
			))
			pas = getattr(self, 'text_block_{}_{}'.format(
				list(self.arr_id)[0],
				self.arr_id[list(self.arr_id)[0]][1]
			))

			log.edit.setText(save_log['username'])
			pas.edit.setText(save_log['password'])

		except FileNotFoundError:
			pass


		if not self.url:
			self.login.error_block.show()
			self.login.error_block.setText(get_lang('ServerError000'))



		self.login.show()

		# set buttons for login block
		self.login.button_registr = QtWidgets.QPushButton(self.login)
		self.login.button_registr.setStyleSheet('border:none;background:{};color:{};padding:{}px;font-size:{}px;'.format(
			get_style('log_edblock_registr_color'),
			get_style('log_edblock_registr_text_color'),
			get_style('log_edblock_registr_padding'),
			get_style('log_edblock_registr_size'),
		))
		self.login.button_registr.setText(get_lang('log_registration'))
		# set layout
		self.login.center_lay.addWidget(self.login.button_registr)
		# set cursor
		self.login.button_registr.setCursor(cursor2)


		# get Registration block
		self.regist = getattr(self, 'center_{}'.format(list(self.arr_id)[1]))

		# get user verification block
		self.check_code = getattr(self, 'center_{}'.format(list(self.arr_id)[2]))

		if self.url :
			# exit the program
			self.login.left_button.clicked.connect(self.close_program)
			# enter the program
			self.login.right_button.clicked.connect(self.user_enter)
			# go to registration panel
			self.login.button_registr.clicked.connect(self.show_center_regist)
			# back to login block
			self.regist.left_button.clicked.connect(self.show_center_login)
			# go to the user verification block
			self.regist.right_button.clicked.connect(self.show_center_code)
			# back to registration panel
			self.check_code.left_button.clicked.connect(self.show_center_regist)
			# add user
			self.check_code.right_button.clicked.connect(self.add_user)


			self.get_ip = socket.gethostbyname(socket.gethostname())

	# function for user enter
	def user_enter(self):
		# get field username and password
		username = getattr(self, 'text_block_{}_{}'.format(
			list(self.arr_id)[0],
			self.arr_id[list(self.arr_id)[0]][0]
		)).edit.text()
		password = getattr(self, 'text_block_{}_{}'.format(
			list(self.arr_id)[0],
			self.arr_id[list(self.arr_id)[0]][1]
		)).edit.text()

		# get url for enter
		url = "api/auth/token/login/"
		url2 = "api/user/"
		# check fields
		if '@' in username:
			user = requests.get(self.url + url2 + '?email=' + username)
			user_dict = json.loads(user.content.decode('utf-8'))
			if not user_dict:
				self.login.error_block.show()
				self.login.error_block.setText(get_lang('login_error001'))
		else:
			user = requests.get(self.url + url2 + '?username=' + username)
			user_dict = json.loads(user.content.decode('utf-8'))
			if not user_dict:
				self.login.error_block.show()
				self.login.error_block.setText(get_lang('login_error001'))
		# login user
		if user_dict:
			data = {
				'username': user_dict[0]['username'],
				'password': password,
			}
			res = requests.post(self.url + url, data=data)
			# get token
			token = json.loads(res.content.decode('utf-8'))
			# check token
			try:
				token['non_field_errors']
				self.login.error_block.show()
				self.login.error_block.setText(get_lang('login_error002'))
			except KeyError:
				# save cookie
				copy = open(BASE_DIR + r'\cookies\token.json', 'w')
				token['username'] = username
				token['password'] = password
				copy.write(json.dumps(token))
				copy.close()

	def show_center_regist(self):
		self.login.hide()
		self.check_code.hide()
		self.regist.show()
		# delete check code

	def show_center_login(self):
		self.regist.hide()
		self.login.show()











	def show_center_code(self):
		#print(list(self.arr_id)[1])

		'/api/already_ip/get/?ip_name=127.0.0.1:80001'

		url = "api/already_ip/get/?ip_name="
		url2 = "api/user/"
		url3 = 'api/extra_user/get/?phone='
		url4 = 'api/auth/users/'

		check_ip = requests.get(self.url + url + self.get_ip)
		check_ip_dict = json.loads(check_ip.content.decode('utf-8'))
		if check_ip_dict:
			self.regist.error_block.show()
			self.regist.error_block.setText(get_lang('login_error003'))
		else:
			# get text
			password_text = getattr(self, 'text_block_{}_{}'.format(
				list(self.arr_id)[1],
				self.arr_id[list(self.arr_id)[1]][1]
			)).edit.text()
			c_password_text = getattr(self, 'text_block_{}_{}'.format(
				list(self.arr_id)[1],
				self.arr_id[list(self.arr_id)[1]][2]
			)).edit.text()
			phone_text = getattr(self, 'text_block_{}_{}'.format(
				list(self.arr_id)[1],
				self.arr_id[list(self.arr_id)[1]][4]
			)).edit.text()
			email_text = getattr(self, 'text_block_{}_{}'.format(
				list(self.arr_id)[1],
				self.arr_id[list(self.arr_id)[1]][3]
			)).edit.text()
			username_text = getattr(self, 'text_block_{}_{}'.format(
				list(self.arr_id)[1],
				self.arr_id[list(self.arr_id)[1]][0]
			)).edit.text()

			# check validate fields
			if re.search(r'[^a-z0-9_]', username_text):
				self.regist.error_block.show()
				self.regist.error_block.setText(get_lang('login_error004.1'))
			elif len(username_text) > 20 or len(username_text) < 3:
				self.regist.error_block.show()
				self.regist.error_block.setText(get_lang('login_error004.2'))
			else:
				user = requests.get(self.url + url2 + '?username=' + username_text)
				user_dict = json.loads(user.content.decode('utf-8'))
				if user_dict:
					self.regist.error_block.show()
					self.regist.error_block.setText(get_lang('login_error004.3'))
				else:

					if '@' in email_text and '.' in email_text:
						user = requests.get(self.url + url2 + '?email=' + email_text)
						user_dict = json.loads(user.content.decode('utf-8'))
						if user_dict:
							self.regist.error_block.show()
							self.regist.error_block.setText(get_lang('login_error005.1'))
						else:
							if len(phone_text) >= 9:
								phone_get = requests.get(self.url + url3 + phone_text)
								phone_dict = json.loads(phone_get.content.decode('utf-8'))
								if phone_dict:
									self.regist.error_block.show()
									self.regist.error_block.setText(get_lang('login_error006.2'))
								else:

									err = validate_password(password_text)
									if err['ErrorPassword']:
										self.regist.error_block.show()
										self.regist.error_block.setText(get_lang('login_error007.1'))
									else:
										if not password_text == c_password_text:
											self.regist.error_block.show()
											self.regist.error_block.setText(get_lang('login_error007.2'))
										else:
											try:
												data = {
													'username': username_text,
													'password': password_text,
													'email': email_text,
												}
												res = requests.post(self.url + url4, data=data)
												self.regist.hide()
												self.check_code.show()
											except:
												print("something error")

							else:
								self.regist.error_block.show()
								self.regist.error_block.setText(get_lang('login_error006.1'))
					else:
						self.regist.error_block.show()
						self.regist.error_block.setText(get_lang('login_error005.2'))






























	def add_user(self):


		# get text
		password = getattr(self, 'text_block_{}_{}'.format(
			list(self.arr_id)[1],
			self.arr_id[list(self.arr_id)[1]][1]
		)).edit.text()
		phone = getattr(self, 'text_block_{}_{}'.format(
			list(self.arr_id)[1],
			self.arr_id[list(self.arr_id)[1]][4]
		)).edit.text()
		username = getattr(self, 'text_block_{}_{}'.format(
			list(self.arr_id)[1],
			self.arr_id[list(self.arr_id)[1]][0]
		)).edit.text()

		code_1 = getattr(self, 'text_block_{}_{}'.format(
			list(self.arr_id)[2],
			self.arr_id[list(self.arr_id)[2]][0]
		)).edit.text()
		code_2 = getattr(self, 'text_block_{}_{}'.format(
			list(self.arr_id)[2],
			self.arr_id[list(self.arr_id)[2]][1]
		)).edit.text()

		url = 'api/auth/users/activation/'

		data = {
			'uid': code_1,
			'token': code_2,
		}
		try:
			res = requests.post(self.url + url, data=data)
			res_dict = json.loads(res.content.decode('utf-8'))
			self.check_code.error_block.show()
			self.check_code.error_block.setText(get_lang('login_error008'))
			print(res_dict)
		except:
			# login
			url = "api/auth/token/login/"
			url2 = "api/extra_user/post/"
			url3 = "api/already_ip/post/"
			url4 = "api/user/"
			data = {
				'username': username,
				'password': password,
			}
			res = requests.post(self.url + url, data=data)
			# get token
			token = json.loads(res.content.decode('utf-8'))
			# check token
			try:
				token['non_field_errors']
				self.login.error_block.show()
				self.login.error_block.setText(get_lang('login_error002'))
			except KeyError:
				# get id for extra user fields
				get_id = requests.get(self.url + url4 + '?username=' + username)
				get_id_dict = json.loads(get_id.content.decode('utf-8'))
				
				# for phone
				data2 = {
					'user': int(get_id_dict[0]['id']),
					'phone': int(phone),
				}
				# for ip
				data3 = {
					'ip_name': self.get_ip,
				}
				headers = {'Authorization': 'Token '+ token["auth_token"]}

				requests.post(self.url + url2, data=data2, headers=headers)
				requests.post(self.url + url3, data=data3, headers=headers)
				# save cookie
				copy = open(BASE_DIR + r'\cookies\token.json', 'w')
				token['username'] = username
				token['password'] = password
				copy.write(json.dumps(token))
				copy.close()










	def close_program(self):
		print('close')
		self.close()




if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	w = Test()
	w.show()
	app.exit(app.exec())

