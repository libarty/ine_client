import random, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from PyQt5 import QtWidgets, QtCore, QtGui

from general_functions import DegToDis


class ShapeAnimation(QtWidgets.QWidget):
	def __init__(
			self,
			move_x,
			move_y,

			min_size=20,
			max_size=None,
			color='black',
			min_rotate=0,
			max_rotate=None,
			duration=1000,
			if_rotate=True,

			parent=None):
		super(ShapeAnimation, self).__init__(parent)
		if max_size is None:
			max_size = min_size
		if max_rotate is None:
			max_rotate = min_rotate
		self.if_rotate = if_rotate
		# set random value
		rotate = random.randint(min_rotate, max_rotate)
		size = random.randint(min_size, max_size)
		# set type shape 1= square 2 = circle 3 =triangle
		type_ = random.randint(1, 3)
		# set style for shape
		if type_ == 1:
			style = 'background:{};'.format(color)
		elif type_ == 2:
			style = 'background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.999499 {}, stop:1 rgba(255, 255, 255, 0));'.format(
				color
			)
		elif type_ == 3:
			style = 'background:qconicalgradient(cx:0.5 , cy:0, angle:244, stop:0.145 {}, stop:0.1451 rgba(50, 52, 58, 0));'.format(
				color
			)

		# set scene for shape
		# it is need for rotate shape
		val = size / 100
		# hide visibility
		self.setStyleSheet('background:rgba(27, 28, 35, 0); border:none')

		self.resize(145 * val / 1.0000005536974035, 145 * val / 1.0000005536974035)

		self.scene = QtWidgets.QGraphicsScene()
		self.scene.setSceneRect(0, 0, 115 * val / 1.1949939621227593, 115 * val / 1.1949939621227593)

		self.view = QtWidgets.QGraphicsView()
		self.view.setRenderHint(QtGui.QPainter.HighQualityAntialiasing)
		self.view.setScene(self.scene)
		self.view.setSceneRect(0, 0, 00, 0)
		# self.view.setAlignment(Qt.AlignTop | Qt.AlignLeft)
		scene_layout = QtWidgets.QGraphicsLinearLayout(QtCore.Qt.Horizontal)

		form = QtWidgets.QGraphicsWidget()
		form.setLayout(scene_layout)

		self.scene.addItem(form)

		self.main_layout = QtWidgets.QHBoxLayout()
		self.main_layout.addWidget(self.view)

		self.main_layout.setSpacing(0)
		self.main_layout.setContentsMargins(0, 0, 0, 0)
		self.setLayout(self.main_layout)
		# set shape
		self.shape = QtWidgets.QLabel()
		self.shape.resize(size, size)
		self.shape.setStyleSheet(style)
		# set cursor
		pixmap = QtGui.QPixmap(BASE_DIR+r'\media\cur\1.png').scaled(20, 20) 
		cursor = QtGui.QCursor(pixmap)
		self.shape.setCursor(cursor)
		# set rotate shape
		self.shape.setMinimumSize(QtCore.QSize(self.shape.width(), self.shape.height()))

		scene_layout.setContentsMargins(0, 0, 0, 0)

		self.proxy_rb1 = self.scene.addWidget(self.shape)
		self.proxy_rb1.setRotation(rotate)
		self.proxy_rb1.setTransformOriginPoint(self.shape.width() / 2, self.shape.height() / 2)

		scene_layout.addItem(self.proxy_rb1)

		# animation

		self.menuAnimation = QtCore.QVariantAnimation()
		self.menuAnimation.setDuration(duration)

		self.menuAnimation.valueChanged.connect(self.value_change)
		self.menuAnimation.finished.connect(self.again)
		# set standard value for animation
		self.poi_x = move_x
		self.poi_y = move_y
		self.deg = random.randint(0, 360)
		self.mor_les = 1
		#
		self.start_fun()

	def start_fun(self):
		# set last point
		self.menuAnimation.setStartValue(QtCore.QPoint(self.poi_x, self.poi_y))
		change_deg = random.randint(0, 80)
		if not random.randint(30, 100) >= 50:
			self.mor_les = -self.mor_les
		if self.mor_les == -1:
			change_deg = -change_deg
		self.deg = self.deg + change_deg
		now_dis = random.randint(1, 80)

		arr_long = DegToDis(self.deg, now_dis)

		self.poi_x = self.poi_x + arr_long[0]
		self.poi_y = self.poi_y + arr_long[1]

		# set new point
		self.menuAnimation.setEndValue(QtCore.QPoint(self.poi_x, self.poi_y))
		self.menuAnimation.start()

	def value_change(self, value):
		self.move(value.x(), value.y())
		if self.if_rotate:
			self.proxy_rb1.setRotation(value.x())


	def again(self):
		self.start_fun()


class BackGeometryAnimation(QtWidgets.QWidget):
	def __init__(
			self,
			num_x=10,
			num_y=10,
			size=False,
			parent=None,
			*args,
			**kwargs

	):
		super(BackGeometryAnimation, self).__init__(parent)
		if size:
			self.setFixedWidth(size.width())
			self.setFixedHeight(size.height())

		elif parent:
			self.setFixedWidth(parent.width())
			self.setFixedHeight(parent.height())
		# set spacing between widgets
		step_x = self.width() / num_x
		step_y = self.height() / num_y
		self.setStyleSheet('background:black;')
		# set start val for X
		start_val_x = 0
		for x in range(num_x):
			# save old value
			prev_val_x = start_val_x
			# update value
			start_val_x += step_x
			# set start val for Y
			start_val_y = 0
			for y in range(num_y):
				# save old value
				prev_val_y = start_val_y
				# update value
				start_val_y += step_y
				# set random value between old and new
				x_val = random.randint(int(prev_val_x), int(start_val_x))
				y_val = random.randint(int(prev_val_y), int(start_val_y))

				shape = ShapeAnimation(
					move_x=x_val,
					move_y=y_val,

					parent=self,
					*args,
					**kwargs
					)