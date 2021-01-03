from PyQt5 import QtWidgets, QtCore, QtGui, sip
import math, ctypes, sys, re


# Check password for validity
def validate_password(password):
	log = {'ErrorPassword':[],'GoodPassword':[]}
	if re.search(r'[^a-z0-9A-Z\W]', password):
		log['ErrorPassword'].append('001')
	if len(password) < 8:
		log['ErrorPassword'].append('002')
	if not re.search(r"\d", password):
		log['ErrorPassword'].append('003')
	if not re.search(r"[a-zA-Z]", password):
		log['ErrorPassword'].append('004')
	if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
		log['GoodPassword'].append('001')
	if re.search(r"\W", password):
		log['GoodPassword'].append('002')
	return log

# functions for turning numbers into percentages and vice versa
def per_to_num(per, mx, mn=0):
	return (mx - mn) * per / 100 + mn
def num_to_per(per, max):
	return per / max * 100
# function for replace style sheet
def replace_style(style, name_qss, color):
	return style.replace(
		re.search(
			r'(^|[^-])' + name_qss + '(.*?)\;',
			style
		).group(2),
		color
	)

# Set neon effect for widget
if sys.platform == 'win32':
	# the exported function name has illegal characters on Windows, let's use
	# getattr to access it
	_qt_blurImage = getattr(ctypes.CDLL('Qt5Widgets.dll'),
		'?qt_blurImage@@YAXPEAVQPainter@@AEAVQImage@@N_N2H@Z')
else:
	try:
		qtgui = ctypes.CDLL('libQt5Widgets.so')
	except:
		qtgui = ctypes.CDLL('libQt5Widgets.so.5')
	_qt_blurImage = qtgui._Z12qt_blurImageP8QPainterR6QImagedbbi


class NeonEffect(QtWidgets.QGraphicsColorizeEffect):
	_blurRadius = 5.
	_glow = 2

	def glow(self):
		return self._glow

	@QtCore.pyqtSlot(int)
	def setGlow(self, glow):
		if glow == self._glow:
			return
		self._glow = max(1, min(glow, 10))
		self.update()

	def blurRadius(self):
		return self._blurRadius

	@QtCore.pyqtSlot(int)
	@QtCore.pyqtSlot(float)
	def setBlurRadius(self, radius):
		if radius == self._blurRadius:
			return
		self._blurRadius = max(1., float(radius))
		self.update()

	def applyBlurEffect(self, blurImage, radius, quality, alphaOnly, transposed=0, qp=None):
		blurImage = ctypes.c_void_p(sip.unwrapinstance(blurImage))
		radius = ctypes.c_double(radius)
		quality = ctypes.c_bool(quality)
		alphaOnly = ctypes.c_bool(alphaOnly)
		transposed = ctypes.c_int(transposed)
		if qp:
			qp = ctypes.c_void_p(sip.unwrapinstance(qp))
		_qt_blurImage(qp, blurImage, radius, quality, alphaOnly, transposed)

	def draw(self, qp):
		pm, offset = self.sourcePixmap(QtCore.Qt.LogicalCoordinates, self.PadToEffectiveBoundingRect)
		if pm.isNull():
			return

		# use a double sized image to increase the blur factor
		scaledSize = QtCore.QSize(pm.width() * 2, pm.height() * 2)
		blurImage = QtGui.QImage(scaledSize, QtGui.QImage.Format_ARGB32_Premultiplied)
		blurImage.fill(0)
		blurPainter = QtGui.QPainter(blurImage)
		blurPainter.drawPixmap(0, 0, pm.scaled(scaledSize,
			QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
		blurPainter.end()

		# apply the blurred effect on the image
		self.applyBlurEffect(blurImage, 1 * self._blurRadius, True, False)

		# start the painter that will use the previous image as alpha
		tmpPainter = QtGui.QPainter(blurImage)
		# using SourceIn composition mode we use the existing alpha values
		# to paint over
		tmpPainter.setCompositionMode(tmpPainter.CompositionMode_SourceIn)
		color = QtGui.QColor(self.color())
		color.setAlpha(color.alpha() * self.strength())
		# fill using the color
		tmpPainter.fillRect(pm.rect(), color)
		tmpPainter.end()

		# repeat the effect which will make it more "glowing"
		for g in range(self._glow):
			qp.drawImage(0, 0, blurImage.scaled(pm.size(),
				QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))

		super().draw(qp)







# Set blur effect for widget
class BlurEffect(QtWidgets.QGraphicsBlurEffect):
	obj = {}

	def addEffectRect(self, name, val):
		self.obj[name] = val
		self.update()

	def delEffectRect(self, name):
		del self.obj[name]

	def draw(self, qp):
		if self.obj is None:
			super().draw(qp)
			print('bao')
		else:
			qp.save()
			qp.setClipRect(qp.viewport())
			super().draw(qp)
			fullRegion = QtGui.QRegion(qp.viewport())
			for key in self.obj:
				val = self.obj[key]
				fullRegion -= QtGui.QRegion(val)

			qp.setClipRegion(fullRegion)
			self.drawSource(qp)
			qp.restore()

# Set position from another widget
def set_pos(
		parent,
		pos,
		child='',
		tp=True,
		tc=True
):
	v = ''
	if tp:
		parent_height = parent.height()
		parent_width = parent.width()
	else:
		parent_height = parent.sizeHint().height()
		parent_width = parent.sizeHint().width()
	if tc:
		child_height = child.height()
		child_width = child.width()
	else:
		child_height = child.sizeHint().height()
		child_width = child.sizeHint().width()
	if pos == 'U':
		v = parent.y() - child_height
	elif pos == 'D':
		v = parent.y() + parent_height
	elif pos == 'L':
		v = parent.x() - child_width
	elif pos == 'R':
		v = parent.x() + parent_width
	elif pos == 'Y_S':
		v = parent.y()
	elif pos == 'X_S':
		v = parent.x()
	elif pos == 'Y_E':
		v = parent.y() + parent_height - child_height
	elif pos == 'X_E':
		v = parent.x() + parent_width - child_width
	elif pos == 'Y_C':
		v = parent.y() + (parent_height / 2) - (child_height / 2)
	elif pos == 'X_C':
		v = parent.x() + (parent_width / 2) - (child_width / 2)
	elif pos == 'ALT_R':
		v = child.x() + child_width
	elif pos == 'ALT_D':
		v = child.y() + child_height
	elif pos == 'ALT_L':
		v = child.x() - child_width
	elif pos == 'ALT_U':
		v = child.y() - child_height

	return v


# function for array recalculation
def type_fun(
		id,
		child=None,
		type=3,
		number=1
):
	end = 0 if type == 1 else len(child) - 1 if type == 2 else id
	return id + number if id + number <= len(child) - 1 else end


class RunAnimation(object):
	@QtCore.pyqtSlot(QtWidgets.QAbstractButton, bool)
	def run_animation(self, but, state):
		# Run only one time
		if state:
			# Set parent in front of all
			self.mainWidget.raise_()

			# get id from name radio for MB_Content
			id = int(but.objectName().split('-')[1])
			# Check if radio is face_radio
			# get first widget
			if not id == 999999999:
				wid = getattr(self, '{}_WidgetConnect-{}'.format(self.name, id))
				self.remember_name[wid.objectName()] = 0
			else:
				wid = self.second_widget
			# Check if object is new or old
			if len(self.remember_name) > self.sum:
				self.sum = len(self.remember_name)
			elif self.aGroup.animationCount() > 0:
				wid.swap_values()
			# Delete last animation
			# should be between wid.swap_values() and self.second_widget.swap_values()
			if self.aGroup.animationCount() > 0:
				self.aGroup.takeAnimation(0)
			# Add second widget
			if self.second_widget is not None:
				# Invert
				self.second_widget.swap_values()
				self.aGroup.addAnimation(self.second_widget.animation)
			# Check if radio is face_radio
			# save second_widget
			if not id == 999999999:
				self.second_widget = wid
			else:
				wid.swap_values()
				self.second_widget = None
			# Add first animation
			self.aGroup.addAnimation(wid.animation)
			# Start animation
			self.aGroup.start()


class OffRadioButton(object):
	# off for Radio
	def offRadioButton(self, but):
		if self.off_arr[but.objectName()]:
			self.off_arr[but.objectName()] = False
			self.off_arr[self.face_radio.objectName()] = True
			self.face_radio.setChecked(True)
		else:
			for b in self.off_arr:
				self.off_arr[b] = False
			self.off_arr[but.objectName()] = True


class SaveGeometry(object):
	# function for save or update geometry of widgets
	def save_geometry(
			self,
			wid,
			name=False,
			res=False):
		if name:
			id = name
		else:
			id = wid.objectName()
		try:
			self.save[id]
		except KeyError:
			self.save[id] = wid.geometry()
		if res:
			self.save[id] = wid.geometry()


class UpdateAnimation(object):
	# function for update start values if geometry has been changed
	def update_anim(
			self,
			wid,
			pos1=False,
			pos2=False,
			geometry=False,
			name=False,
	):
		try:
			parent = self.save[self.mainWidget.objectName()]
			child = self.save[wid.cldActivate.objectName()]
		except AttributeError:
			print('UpdateAnimation: not Attribute')
		except KeyError:
			print('UpdateAnimation: not Key')

		if pos1 is False:
			pos1 = QtCore.QPoint(
				set_pos(parent, self.type_move[2], child),
				set_pos(parent, self.type_move[3], child)
			)
		if pos2 is False:
			pos2 = QtCore.QPoint(
				set_pos(parent, self.type_move[0], child),
				set_pos(parent, self.type_move[1], child)
			)
		wid.animation.setStartValue(pos2)
		wid.animation.setEndValue(pos1)
		# set geometry for blur effect
		if self.effect and geometry:
			self.effect.addEffectRect(
				wid.cldActivate.objectName() if name is False else name,
				geometry
			)
		elif self.effect and not geometry:
			self.effect.addEffectRect(
				wid.cldActivate.objectName(),
				QtCore.QRect(
					pos2.x(),
					pos2.y(),
					child.width(),
					child.height()
				)
			)


class GeneralFunctions(
	RunAnimation,
	OffRadioButton,
	SaveGeometry,
	UpdateAnimation
):
	pass





# turn degrees into distance
def DegToDis(degrees, distance):
	radians = degrees * math.pi / 180;
	cos = math.cos(radians);
	sin = math.sin(radians);
	x1 = distance * cos;
	y1 = distance * sin;
	arr = [round(x1, 15), round(y1, 15)]  # round is short val
	return arr