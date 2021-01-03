import os, re
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from PyQt5 import QtWidgets, QtGui, QtCore
from general_functions import replace_style


# get new format color for QColor
def get_color(text):
	arr = re.findall(r'\w+', text)
	if arr[0] == "rgba" or arr[0] == "rgb":
		h = 0
		while h < 3:
			h += 1
			arr[h] = int(arr[h])
		try:
			last_val = int(arr[4])
		except IndexError:
			last_val = 255
		print(last_val)
		color = QtGui.QColor(arr[1], arr[2], arr[3], last_val).name(
			QtGui.QColor(arr[1], arr[2], arr[3], last_val).NameFormat(1))
	else:
		color = QtGui.QColor(text).name(QtGui.QColor(text).NameFormat(1))
	return color


# Create Text-icon in label
class LabelIcon(QtWidgets.QLabel):
	def __init__(self, rad, parent=None):
		super(LabelIcon, self).__init__(parent)
		# connect to radio
		self.rad = rad
		# set Cursor
		self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

	# change color
	def change_color(self, color='', connect=True, type=True):
		if type:
			name_qss = 'background:'
		else:
			name_qss = 'color:'
		if connect:
			obj = self
		else:
			obj = self.rad
		# set style
		obj.setStyleSheet(
			replace_style(
				obj.styleSheet(),
				name_qss,
				color.name(color.NameFormat(1))
			)
		)
		
	# when mouse in label
	def enterEvent(self, event):
		self.aGroup.setDirection(QtCore.QAbstractAnimation.Forward)
		self.aGroup.start()
		super().enterEvent(event)

	# when mouse out label
	def leaveEvent(self, event):
		self.aGroup.setDirection(QtCore.QAbstractAnimation.Backward)
		self.aGroup.start()
		super().leaveEvent(event)

	# connect to radio
	def mousePressEvent(self, event):
		self.rad.click()


# Set Icon but
class SetIcon(QtWidgets.QWidget):
	def __init__(
			self,
			butSize=20,
			butMargin=1,
			butPadding=0,
			butBack="white",
			butBackHover=None,
			butColor="black",
			butColorHover=None,
			butBorder=None,
			butBorderHover=None,
			butDuration=1000,
			butIcon=["<", ">"],
			parent=None
	):
		super(SetIcon, self).__init__(parent)
		# set standart val and change format color
		butBack = get_color(butBack)
		butBackHover = get_color(butBackHover or butBack)
		butColor = get_color(butColor)
		butColorHover = get_color(butColorHover or butColor)
		butBorder = get_color(butBorder or butColor)
		butBorderHover = get_color(butBorderHover or butBorder)
		# set icon
		self.icon = butIcon
		# set lay
		lay = QtWidgets.QGridLayout(self)
		lay.setSpacing(0)
		lay.setContentsMargins(0, 0, 0, 0)
		# Create Radio
		self.radio = QtWidgets.QRadioButton(self)
		self.radio.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
		# ADD
		lay.addWidget(self.radio, 0, 0, 1, 1)
		# set style for radio
		self.radio.setStyleSheet(
			'QRadioButton{background: %s;}QRadioButton::indicator {background-color:rgba(255, 255, 255, 0);}' %
			(butBorder)
		)
		# Create Icon
		self.label = LabelIcon(self.radio, self)
		# set font for label
		fontId = QtGui.QFontDatabase.addApplicationFont(re.sub(r'\\', '/', BASE_DIR + r'\media\settings_post.ttf'))

		if fontId == -1:
			print('not font')
			self.icon = ["<", ">"]
		font = QtGui.QFont("settings_post", butSize)
		self.label.setFont(font)
		# set text for label
		self.label.setText(self.icon[0])
		# set position center for label
		self.label.setAlignment(QtCore.Qt.AlignCenter)
		self.label.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		# ADD
		lay.addWidget(self.label, 0, 0, 1, 1)
		# set style for label
		self.label.setStyleSheet(
			'background: %s;color: %s;margin:%s;padding:%s;' %
			(butBack, butColor, butMargin, butPadding)
		)
		# set animation
		self.label.aGroup = QtCore.QParallelAnimationGroup(self)
		arry = [
			[butBack, butBackHover, True, True],
			[butColor, butColorHover, True, False],
			[butBorder, butBorderHover, False, True]
		]
		an = []
		for id, val in enumerate(arry):
			ani = QtCore.QVariantAnimation(
				duration=butDuration,
				startValue=QtGui.QColor(val[0]),
				endValue=QtGui.QColor(val[1])
			)
			an.append(ani)
			an[id].valueChanged.connect(
				lambda color, connect=val[2], type=val[3]: self.label.change_color(color, connect, type)
			)
			self.label.aGroup.addAnimation(an[id])
		# watch when radio on or off
		self.radio.toggled.connect(self.change_text)

	# change icon when user click to label
	def change_text(self):
		if self.radio.isChecked():
			try: 
				self.label.setText(self.icon[1])
			except IndexError:
				print('no icon')
				self.label.setText(self.icon[0])
		else:
			self.label.setText(self.icon[0])