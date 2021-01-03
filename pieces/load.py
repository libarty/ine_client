from PyQt5 import QtWidgets, QtCore, QtGui
from general_functions import replace_style


# slider
class LoadBar(QtWidgets.QWidget):
	def __init__(
			self,
			parent=None,
			color_back='blue',
			color_load='green',
			width=None,
			height=100,
			duration=1000,
			min_val=2,
			*args,
			**kwargs
	):
		super(LoadBar, self).__init__(parent)
		self.width = width
		self.height = height
		self.min = min_val
		self.setStyleSheet('background:{};'.format('black'))
		# set main widget
		lay = QtWidgets.QHBoxLayout(self)
		lay.setSpacing(0)
		lay.setContentsMargins(0, 0, 0, 0)
		# set main widget
		self.main = QtWidgets.QWidget(self)
		self.main.setStyleSheet('background:{};'.format(color_back))
		if width:
			self.main.setFixedWidth(self.width)

		self.main.setFixedHeight(self.height)
		lay.addWidget(self.main)
		main_lay = QtWidgets.QHBoxLayout(self.main)
		main_lay.setSpacing(0)
		main_lay.setContentsMargins(0, 0, 0, 0)

		# set bar for loader
		self.wid_load = QtWidgets.QWidget(self)
		self.wid_load.setStyleSheet('background:{};'.format(color_load))
		self.wid_load.setFixedHeight(self.height)
		main_lay.addWidget(self.wid_load)

		# animation

		self.group = QtCore.QSequentialAnimationGroup(self)

		self.ani1 = QtCore.QVariantAnimation()
		self.ani2 = QtCore.QVariantAnimation()

		self.ani1.valueChanged.connect(self.value_change)
		self.ani1.setEasingCurve(QtCore.QEasingCurve.OutSine)

		self.ani1.setDuration(duration)

		self.ani2.valueChanged.connect(self.value_change)
		self.ani2.setEasingCurve(QtCore.QEasingCurve.OutSine)

		self.ani2.setDuration(duration)

		self.group.addAnimation(self.ani1)
		self.group.addAnimation(self.ani2)

		self.group.finished.connect(self.again)

		self.start_fun()

	def start_fun(self):
		self.group.start()

	def value_change(self, value):
		self.wid_load.setFixedWidth(value)

	def again(self):
		self.group.start()

	def resizeEvent(self, event):
		super().resizeEvent(event)
		width = self.main.width()

		self.ani2.setEndValue(width)
		self.ani1.setStartValue(width)

		self.ani2.setStartValue(round(width / self.min))
		self.ani1.setEndValue(round(width/self.min))


# block for shape animation of load
class LoadBlock(QtWidgets.QWidget):
	def __init__(
			self,
			parent=None,
			*args,
			**kwargs
	):
		super(LoadBlock, self).__init__(parent)
		# set main widget
		lay = QtWidgets.QHBoxLayout(self)
		lay.setSpacing(0)
		lay.setContentsMargins(0, 0, 0, 0)
		wid = LoadFigure(parent=self, *args, **kwargs)
		lay.addWidget(wid)


# shape animation
class LoadFigure(QtWidgets.QWidget):
	def __init__(
			self,

			color='black',
			duration=1000,

			size=50,
			rotate=0,
			pause=0,
			distance=1,
			size_back=1.2,
			triangle=True,
			circle=True,
			parent=None


	):
		super(LoadFigure, self).__init__(parent)
		# set start value
		self.size = size
		self.color = color
		self.duration = duration
		self.pause = pause
		self.triangle = triangle
		self.circle = circle
		self.distance = distance
		val = size / 100

		# hide visibility
		self.setStyleSheet('background:rgba(27, 28, 35, 0); border:none')
		self.setFixedWidth(round(size*size_back))
		#self.setFixedHeight(50)
		# set scene for shape

		self.resize(145 * val / 1.0000005536974035, 145 * val / 1.0000005536974035)

		self.scene = QtWidgets.QGraphicsScene()
		self.scene.setSceneRect(0, 0, 115 * val / 1.1949939621227593, 115 * val / 1.1949939621227593)

		self.view = QtWidgets.QGraphicsView()
		self.view.setRenderHint(QtGui.QPainter.HighQualityAntialiasing)
		self.view.setScene(self.scene)
		self.view.setSceneRect(0, 0, 0, 0)
		# self.view.setAlignment(Qt.AlignTop | Qt.AlignLeft)
		scene_layout = QtWidgets.QGraphicsLinearLayout(QtCore.Qt.Horizontal)

		form = QtWidgets.QGraphicsWidget()
		form.setLayout(scene_layout)

		self.scene.addItem(form)

		self.main_layout = QtWidgets.QGridLayout()
		self.main_layout.addWidget(self.view)

		self.main_layout.setSpacing(0)
		self.main_layout.setContentsMargins(0, 0, 0, 0)
		self.setLayout(self.main_layout)
		# set shape
		self.shape = QtWidgets.QLabel()
		self.shape.resize(size, size)
		self.shape.setStyleSheet('background:{};'.format(self.color))
		# set rotate shape
		self.shape.setMinimumSize(QtCore.QSize(self.shape.width(), self.shape.height()))

		scene_layout.setContentsMargins(0, 0, 0, 0)

		self.proxy_rb1 = self.scene.addWidget(self.shape)
		self.proxy_rb1.setRotation(rotate)
		self.proxy_rb1.setTransformOriginPoint(self.shape.width() / 2, self.shape.height() / 2)

		scene_layout.addItem(self.proxy_rb1)

		# animation
		self.frame = 0
		self.start_fun()

	def start_fun(self):
		self.frame += 1
		# set animation group
		frame_1 = QtCore.QParallelAnimationGroup(self)
		frame_2 = QtCore.QSequentialAnimationGroup(self)
		frame_3 = QtCore.QSequentialAnimationGroup(self)
		# set pause value
		if self.frame == 1:
			pause_ani = QtCore.QPauseAnimation()
			pause_ani.setDuration(self.pause)
			frame_3.addAnimation(pause_ani)

			if not self.triangle and self.circle:
				self.frame = 4
			else:
				self.frame = 2

		if not self.triangle and not self.circle:
			rotate_start = 0
			rotate_end = 90

			translate_start = 70
			translate_end = 70

			style = True

			self.frame = 9
	
		# set start value

		if self.frame == 2:

			rotate_start = 0
			rotate_end = 90+26

			translate_start = 70
			translate_end = 0

			style = False

		elif self.frame == 3:

			rotate_start = 90+29
			rotate_end = 180

			translate_start = 0
			translate_end = 70

			style = False

			if self.triangle and not self.circle:
				self.frame = 1

		elif self.frame == 4:
			rotate_start = 0
			rotate_end = 90

			translate_start = 70
			translate_end = 50

			style = True

		elif self.frame == 5:
			rotate_start = 0
			rotate_end = 90

			translate_start = 50
			translate_end = 70

			style = True

			if not self.triangle and self.circle:
				self.frame = 3
			else:
				self.frame = 1

		# set animations

		# set rotation
		ani_rotate = QtCore.QVariantAnimation()
		ani_rotate.setDuration(self.duration*2)
		ani_rotate.valueChanged.connect(self.value_change_r)
		ani_rotate.setEasingCurve(QtCore.QEasingCurve.OutSine)
		ani_rotate.setStartValue(rotate_start)
		ani_rotate.setEndValue(rotate_end)

		# set change shape of figure
		translate = QtCore.QVariantAnimation()
		translate.setDuration(self.duration*2)
		translate.valueChanged.connect(
			lambda value, qss=style: self.value_change_t(value, qss)
		)
		translate.setEasingCurve(QtCore.QEasingCurve.OutSine)
		translate.setStartValue(translate_start)
		translate.setEndValue(translate_end)

		# set change position
		move_front = QtCore.QVariantAnimation()
		move_front.setDuration(self.duration)
		move_front.valueChanged.connect(self.value_change_p)
		move_front.setEasingCurve(QtCore.QEasingCurve.OutSine)
		move_front.setStartValue(0)
		move_front.setEndValue(round(self.size * self.distance))

		# set change position inside out
		move_back = QtCore.QVariantAnimation()
		move_back.setDuration(self.duration)
		move_back.valueChanged.connect(self.value_change_p)
		move_back.setEasingCurve(QtCore.QEasingCurve.OutSine)
		move_back.setStartValue(round(self.size * self.distance))  # self.size
		move_back.setEndValue(0)

		# save animations
		frame_2.addAnimation(move_front)
		frame_2.addAnimation(move_back)

		frame_1.addAnimation(frame_2)
		frame_1.addAnimation(ani_rotate)
		frame_1.addAnimation(translate)

		frame_3.addAnimation(frame_1)

		frame_3.finished.connect(self.again)
		frame_3.start()

	# function again animation
	def again(self):
		self.start_fun()

	# function change position of the shape
	def value_change_p(self, value):
		self.move(0, -value)

	# function change rotation of the shape
	def value_change_r(self, value):
		self.proxy_rb1.setRotation(value)

	# set change shape of figure
	def value_change_t(self, value, style):
		if style:
			new_style = 'qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.{}, fx:0.5,fy:0.5, stop:0.999499 {}, stop:1 rgba(255, 0, 0, 0))'.format(
				value,
				self.color
			)
		else:
			val1 = 244 - value
			val2 = 1450 + value * 55
			val3 = val2 + 1
			new_style = 'qconicalgradient(cx:0.5 , cy:0, angle:{}, stop:0.{} {}, stop:0.{} rgba(50, 52, 58, 0))'.format(
				val1,
				val2,
				self.color,
				val3
			)

		style_get = self.shape.styleSheet()
		name = 'background:'

		restyle = replace_style(style_get, name, new_style)
		self.shape.setStyleSheet(restyle)




