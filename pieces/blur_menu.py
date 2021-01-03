from collections import defaultdict
from PyQt5 import QtWidgets, QtCore

from icon_button import SetIcon
from general_functions import GeneralFunctions, set_pos, type_fun


# Object for some widgets
class MB_Content(QtWidgets.QWidget):
	def __init__(
			self,
			layCon=None,
			parentCon=None,
			type_move=None,
			effect=False,
			cldColor='white',
			cldWidth=False,
			cldHeight=False,
			duration=1000,
			save=None,
			*args,
			**kwargs
	):
		# set parent
		super(MB_Content, self).__init__(parentCon)
		# set type_move and effect for functions change_position
		self.type_move = type_move
		self.effect = effect
		self.save = save
		# delete main object
		self.resize(0, 0)
		# create icon
		self.icon_wid = SetIcon(*args, **kwargs)
		# create child widget
		self.cldActivate = QtWidgets.QWidget(parentCon)
		# set size
		if cldWidth:
			self.cldActivate.setFixedWidth(cldWidth)
		if cldHeight:
			self.cldActivate.setFixedHeight(cldHeight)
		# set color
		self.cldActivate.setStyleSheet('background:{}'.format(cldColor))
		# add icon in lay
		layCon.addWidget(self.icon_wid)
		# create animation
		self.animation = QtCore.QVariantAnimation()
		self.animation.setDuration(duration)
		self.animation.valueChanged.connect(self.change_position)

	# change position child widget
	@QtCore.pyqtSlot("QVariant")
	def change_position(self, val):
		parent = self.save[self.icon_wid.parent().objectName()]

		self.cldActivate.move(val.x(), val.y())
	# move for parent widget where is buttons
		if self.type_move[2] == 'ALT_R':
			self.icon_wid.parent().move(val.x() + self.cldActivate.width(), parent.y())
		elif self.type_move[2] == 'ALT_L':
			self.icon_wid.parent().move(val.x() - parent.width() , parent.y())
		elif self.type_move[3] == 'ALT_U':
			self.icon_wid.parent().move(parent.x(),   val.y() - parent.height())
		elif self.type_move[3] == 'ALT_D':
			self.icon_wid.parent().move(parent.x(),   val.y() + self.cldActivate.height())

		if self.effect:
			self.effect.addEffectRect(self.cldActivate.objectName(), self.cldActivate.geometry())

	# Invert Animation
	def swap_values(self):
		self.animation.blockSignals(True)
		start_value = self.animation.startValue()
		end_value = self.animation.endValue()
		self.animation.setStartValue(end_value)
		self.animation.setEndValue(start_value)
		self.animation.blockSignals(False)


# Set blur widget
class MoveBlurWidget(GeneralFunctions,QtWidgets.QWidget):
	save = {}

	def __init__(
			self,
			name="default",
			effect=False,
			power_blur=1,
			parent_width=False,
			parent_height=False,
			parent_x=0,
			parent_y=0,
			parent_color='white',
			parent_pos="",
			cldNum=1,
			lay_type=True,
			type_move=['L', 'Y_C', 'R', 'Y_C'],
			parent=None,
			kwas_val=[2, 1],
			kwas_type=[1],
			type_anim=True,

			*args,
			**kwargs
	):
		# set parent
		super(MoveBlurWidget, self).__init__(parent)
		# delete main object
		self.resize(0, 0)
		# set standard val
		self.effect = effect
		if self.effect:
			self.effect.setBlurRadius(power_blur)
			self.effect.setEnabled(True)
		self.name = name
		self.type_move = type_move
		# ----Widget for button-----
		self.mainWidget = QtWidgets.QWidget(parent)
		self.mainWidget.setObjectName(u"{}_mainWidget".format(self.name))
		self.mainWidget.setStyleSheet('background:{}'.format(parent_color))
		self.mainWidget.move(parent_x, parent_y)
		# ----lay for button-----
		if lay_type:
			MB_widget_lay = QtWidgets.QVBoxLayout(self.mainWidget)
		else:
			MB_widget_lay = QtWidgets.QHBoxLayout(self.mainWidget)
		# Set object name
		MB_widget_lay.setObjectName(u"{}_MB_widget_lay".format(self.name))
		# ----delete margin-----
		MB_widget_lay.setSpacing(0)
		MB_widget_lay.setContentsMargins(0, 0, 0, 0)
		# ----set QSpacer----
		if parent_pos == "DOWN":
			vs = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
			MB_widget_lay.addItem(vs)

		# create buttonGroup for all radio in other widgets
		self.bGroup = QtWidgets.QButtonGroup(self, exclusive=True)
		# create array id with starting value 0
		id = defaultdict(int)
		# create list for off radio
		self.off_arr = {}

		# array enumeration
		for x in range(cldNum):
			# create new array with other values
			new_arr = {}
			id['kwas_val'] = 0
			id['kwas_type'] = 0
			for key, value in sorted(kwargs.items()):
				# save in the new array
				new_arr[key] = [
					kwargs.get(key)[id[key]],
					kwargs.get(key)[type_fun(id[key], kwargs.get(key), 1, 1)]
				] if key == 'but1Icon' else kwargs.get(key)[id[key]]

				# Update the id according to different logic
				id[key] = type_fun(id[key], value, kwas_type[id['kwas_type']], kwas_val[id['kwas_val']])
				id['kwas_val'] = type_fun(id['kwas_val'], kwas_val)
				id['kwas_type'] = type_fun(id['kwas_type'], kwas_type)
			# rename for butIcon
			new_arr['butIcon'] = new_arr.pop('but1Icon')

			if self.effect:
				new_arr['effect'] = self.effect

			# Create widgets
			child_wid = MB_Content(
				layCon=MB_widget_lay,
				parentCon=parent,
				type_move=self.type_move,
				save=self.save,
				*args,
				**new_arr
			)

			# Set name for objects
			# for general widget
			child_wid.setObjectName('{}_WidgetConnect-{}'.format(self.name, x))
			setattr(self, child_wid.objectName(), child_wid)
			# for label
			child_wid.cldActivate.setObjectName('{}_cldActivate-{}'.format(self.name, x))
			# for radio
			child_wid.icon_wid.radio.setObjectName('{}_radioChild-{}'.format(self.name, x))
			self.off_arr[child_wid.icon_wid.radio.objectName()] = False
			# add radio for switching between buttons
			self.bGroup.addButton(child_wid.icon_wid.radio, x)

		# Face Buttons radio
		self.face_radio = QtWidgets.QRadioButton(self.mainWidget)
		# skip face radio
		self.face_radio.move(-self.face_radio.width(), 0)
		# ---ADD---
		self.face_radio.setObjectName('{}_radioChild-{}'.format(self.name, 999999999))
		self.bGroup.addButton(self.face_radio, 999999999)
		
		# ----set QSpacer----
		if parent_pos == "UP":
			vs = QtWidgets.QSpacerItem(0, 0,  QtWidgets.QSizePolicy.Minimum,  QtWidgets.QSizePolicy.Expanding)
			MB_widget_lay.addItem(vs)

		# Set geometry for parent
		# after declaring geometry of MB_Content
		if parent_width:
			self.mainWidget.setFixedWidth(parent_width)
		else:
			self.mainWidget.setFixedWidth(self.mainWidget.sizeHint().width())
		if parent_height:
			self.mainWidget.setFixedHeight(parent_height)
		else:
			self.mainWidget.setFixedHeight(self.mainWidget.sizeHint().height())

		# Save geometry
		# if need ALT_...
		self.save_geometry(self.mainWidget)
		parent_geometry = self.save[self.mainWidget.objectName()]
		for x in range(cldNum):
			# get every child widget
			chiWid = getattr(self, '{}_WidgetConnect-{}'.format(self.name, x))
			# set position relative to parent
			chiWid.cldActivate.move(
				set_pos(parent_geometry, self.type_move[0], chiWid.cldActivate),
				set_pos(parent_geometry, self.type_move[1], chiWid.cldActivate)
			)
			# save geometry
			self.save_geometry(chiWid.cldActivate)
			# set values start and end
			self.update_anim(chiWid)

		# Connect all button to functions
		self.bGroup.buttonToggled.connect(self.run_animation)
		self.bGroup.buttonClicked.connect(self.offRadioButton)

		# set animation group
		if type_anim:
			self.aGroup = QtCore.QSequentialAnimationGroup(self)
		else:
			self.aGroup = QtCore.QParallelAnimationGroup(self)

		# set face widget for second animation
		self.second_widget = None
		self.remember_name = {}
		self.sum = 1


