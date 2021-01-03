import random
from PyQt5 import QtWidgets, QtCore



class SimpleBlock(QtWidgets.QWidget):
	def __init__(
			self,
			color_block='black',
			border=1,
			width=500,
			height=500,
			pos_x=0,
			pos_y=0,
			show=True,
			id_x=0,
			id_y=0,
			speed=100,
			max_id_x=10,
			max_id_y=10,
			max_pos=100,
			many=2,
			stop=50,
			parent=None
	):
		super(SimpleBlock, self).__init__(parent)
		# set standard value
		self.setGeometry(pos_x, pos_y, width, height)

		# set lay
		lay = QtWidgets.QVBoxLayout(self)
		lay.setSpacing(0)
		lay.setContentsMargins(0, 0, 0, 0)
		# set label with text
		self.main = QtWidgets.QLabel(self)
		self.main.setStyleSheet('background:{};border:{}px solid black'.format(color_block, border))
		lay.addWidget(self.main)
		# set text

		# set for check visible
		self.show = show

		# stop random widget in first line
		random_stop = 1
		if id_x == 0 or id_y == 0:
			random_stop = random.randint(1, 100)

		if random_stop < stop:
			duration = (max_id_x + max_id_y) * speed - (
				random.randint(
					(id_x - 1 + id_y - 1) * speed,
					(id_x + id_y) * speed)
			)
			# set animation
			self.ani = QtCore.QVariantAnimation()
			self.ani.setDuration(duration)

			self.ani.valueChanged.connect(self.value_change)

			max_pos_id = max_pos+(id_x+id_y)

			self.ani.setStartValue(QtCore.QPoint(pos_x, pos_y))
			self.ani.setEndValue(QtCore.QPoint(
				random.randint(pos_x + max_pos_id, pos_x + max_pos_id * many),
				random.randint(pos_y + max_pos_id, pos_y + max_pos_id * many))
			)
			self.ani.setEasingCurve(QtCore.QEasingCurve.InExpo)
			self.start_animation()

	def start_animation(self):
		self.ani.start()

	def value_change(self, value):
		self.move(value.x(), value.y())


class CollapsingBlock(QtWidgets.QWidget):
	def __init__(
			self,
			num_x=20,
			num_y=20,
			border=0,
			width=100,
			height=100,
			min_random=1,
			max_random=5,
			text=True,
			parent=None,
			*args,
			**kwargs
	):
		super(CollapsingBlock, self).__init__(parent)
		self.resize(width, height)

		# check number format
		if width/num_x == round(width / num_x) and height/num_y == round(height / num_y):

			# create grid
			for x in range(num_x):
				for y in range(num_y):
					# simple square  widget
					wid = SimpleBlock(
						border=border,
						width=width/num_x,
						height=height/num_y,
						pos_x=x*width/num_x,
						pos_y=y*height/num_y,
						show=True,
						id_x=x,
						id_y=y,
						max_id_x=num_x,
						max_id_y=num_y,
						parent=self,
						*args,
						**kwargs
					)
					# set id
					setattr(self, 'colla_block_{}_{}'.format(x, y), wid)
					wid.setObjectName('colla_block_{}_{}'.format(x, y))
					if text:
						wid.main.setText('{}_{}'.format(x, y))
			# update block
			for x in range(num_x):
				for y in range(num_y):
					# get widget by id
					s_wid = getattr(self, 'colla_block_{}_{}'.format(x, y))
					# random size
					big = random.randint(min_random, max_random)
					# continue if the start_widgets is visible
					if s_wid.show:
						check = True
						# check the around_widgets is visible
						for x1 in range(big):
							for y1 in range(big):
								try:
									a_wid = getattr(self, 'colla_block_{}_{}'.format(x + x1, y + y1))
									if not a_wid.show:
										check = False
								except AttributeError:
									pass
						# continue if the around_widgets is visible is visible
						if check:
							# find all the widgets around
							for x_1 in range(big):
								for y_1 in range(big):
									# exclude the start_widget
									if not (x_1 == 0 and y_1 == 0):
										try:
											wid_1 = getattr(self, 'colla_block_{}_{}'.format(x + x_1, y + y_1))
											wid_1.main.setStyleSheet(
												'background:{};border:{}px solid black'.format('green', border))
											wid_1.show = False
											wid_1.hide()
										except AttributeError:
											pass
									else:
										# set new size
										s_wid.resize(width / num_x * big, height / num_y * big)
		else:
			print('Sorry but error in num_x/num_y and width/height')
			lay = QtWidgets.QVBoxLayout(self)
			lay.setSpacing(0)
			lay.setContentsMargins(0, 0, 0, 0)
			self.main = QtWidgets.QLabel(self)
			self.main.setStyleSheet('background:{};'.format(kwargs.get('color_block')))
			lay.addWidget(self.main)





