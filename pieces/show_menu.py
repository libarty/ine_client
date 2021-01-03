from PyQt5 import QtWidgets, QtCore
from icon_button import SetIcon

from collections import defaultdict

from general_functions import GeneralFunctions, set_pos, type_fun

# Object for some widgets
class SB_Content(QtWidgets.QWidget):
	def __init__(
			self,
			parentCon=None,
			effect=False,
			cld_lay_type=True,
			cldWidth=False,
			cldHeight=False,
			cldHeaderColor='black',
			cldHeaderMargin=[0, 0, 0, 0],  # [1=Left, 2=Top, 3=Right, 4=Down]
			cldAreaColor='white',
			duration=1000,
			save=None,
			*args,
			**kwargs
	):
		# set parent
		super(SB_Content, self).__init__(parentCon)
		# set type_move and effect for functions change_position
		self.effect = effect
		self.save = save

		# Scroll content
		self.cldActivate = QtWidgets.QScrollArea()
		self.cldActivate.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		self.cldActivate.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		self.cldActivate.setStyleSheet('background:{};border:none;'.format(cldAreaColor))
		self.cldActivate.setWidgetResizable(True)
		# Content
		self.content = QtWidgets.QWidget()
		self.cldActivate.setWidget(self.content)

		# set geometry
		if cldWidth:
			self.content.setFixedWidth(cldWidth)
		if cldHeight:
			self.content.setFixedHeight(cldHeight)

		# Add buttons
		self.icon_wid = SetIcon(*args, **kwargs)

		# set mini header
		if not cld_lay_type:
			self.min_header_but = QtWidgets.QWidget()
			# set color
			self.min_header_but.setStyleSheet('background:{};'.format(cldHeaderColor))
			# create lay
			self.lay_min_header = QtWidgets.QHBoxLayout(self.min_header_but)
			# set margin
			check = len(cldHeaderMargin)
			if check < 2:
				cldHeaderMargin.append(cldHeaderMargin[0])
			if check < 3:
				cldHeaderMargin.append(cldHeaderMargin[0])
			if check < 4:
				cldHeaderMargin.append(cldHeaderMargin[1])
			self.lay_min_header.setContentsMargins(*cldHeaderMargin)
			self.lay_min_header.setSpacing(0)

		# create animation
		self.animation = QtCore.QVariantAnimation()
		self.animation.setDuration(duration)
		self.animation.valueChanged.connect(self.change_size)

	# change position child widget
	@QtCore.pyqtSlot("QVariant")
	def change_size(self, val):
		par = self.cldActivate.parent()
		parent = self.save[par.objectName()]
		par.setFixedHeight(val+parent.height())
		self.cldActivate.setMaximumHeight(val)
		# update blur effect
		if self.effect:
			self.effect.addEffectRect(
				par.objectName(),
				par.geometry()
			)

	# Invert Animation
	def swap_values(self):
		self.animation.blockSignals(True)
		start_value = self.animation.startValue()
		end_value = self.animation.endValue()
		self.animation.setStartValue(end_value)
		self.animation.setEndValue(start_value)
		self.animation.blockSignals(False)

# Set blur widget
class ShowBlurWidget(GeneralFunctions, QtWidgets.QWidget):
	save = {}
	# set start value
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
			header_pos="",
			cldNum=1,
			lay_type=True,
			parent=None,
			kwas_val=[1],
			kwas_type=[1],
			type_anim=True,
			*args,
			**kwargs
	):
		# set parent
		super(ShowBlurWidget, self).__init__(parent)
		# delete main object
		self.resize(0, 0)
		# set standard val
		self.effect =effect
		if self.effect:
			self.effect.setBlurRadius(power_blur)
			self.effect.setEnabled(True)
		# set name object
		# it is need for blur effect
		self.name = name

		# ----Main widget with content-----
		self.mainWidget = QtWidgets.QWidget(parent)
		self.mainWidget.setObjectName(u"{}_mainWidget".format(self.name))
		self.mainWidget.setStyleSheet('background:{}'.format(parent_color))

		# ----horizontal Lay for mainWidget-----
		mainWidget_lay = QtWidgets.QVBoxLayout(self.mainWidget)
		# delete margin
		mainWidget_lay.setContentsMargins(0, 0, 0, 0)
		mainWidget_lay.setSpacing(0)

		# create header for buttons left right
		if lay_type:
			self.SB_header = QtWidgets.QWidget(self)
			self.SB_header .setStyleSheet('background:{}'.format(kwargs.get('cldHeaderColor')[0]))
			# vertical Lay for buttons
			self.lay_SB_header = QtWidgets.QHBoxLayout(self.SB_header )
			# set margin
			cld_header_margin = kwargs.get('cldHeaderMargin')[0]
			check = len(cld_header_margin)
			if check < 2:
				cld_header_margin.append(cld_header_margin[0])
			if check < 3:
				cld_header_margin.append(cld_header_margin[0])
			if check < 4:
				cld_header_margin.append(cld_header_margin[1])
			self.lay_SB_header.setContentsMargins(*cld_header_margin)
			self.lay_SB_header.setSpacing(0)

			# align the buttons to the right
			if header_pos == "RIGHT":
				vs_2 = QtWidgets.QSpacerItem(
					0, 0,
					QtWidgets.QSizePolicy.Expanding,
					QtWidgets.QSizePolicy.Minimum
				)
				self.lay_SB_header.addItem(vs_2)
			# add header first in mainWidget
			mainWidget_lay.addWidget(self.SB_header)

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
				new_arr[key] = kwargs.get(key)[id[key]]
				# Update the id according to different logic
				id[key] = type_fun(id[key], value, kwas_type[id['kwas_type']], kwas_val[id['kwas_val']])
				id['kwas_val'] = type_fun(id['kwas_val'], kwas_val)
				id['kwas_type'] = type_fun(id['kwas_type'], kwas_type)
			if self.effect:
				new_arr['effect'] = self.effect

			# Create widgets
			child_wid = SB_Content(
				parentCon=parent,
				save=self.save,
				cld_lay_type=lay_type,
				*args,
				**new_arr
			)
			# Set name for objects
			# for general widgets
			child_wid.setObjectName('{}_WidgetConnect-{}'.format(self.name, x))
			setattr(self, child_wid.objectName(), child_wid)
			# for radio
			child_wid.icon_wid.radio.setObjectName('{}_radioChild-{}'.format(self.name, x))
			self.off_arr[child_wid.icon_wid.radio.objectName()] = False
			# for area
			child_wid.cldActivate.setObjectName('{}_cldActivate-{}'.format(self.name, x))
			# add radio for switching between buttons
			self.bGroup.addButton(child_wid.icon_wid.radio, x)

			# add widgets in different lay
			if lay_type:
				# Add in header
				self.lay_SB_header.addWidget(child_wid.icon_wid)
			else:
				# align the buttons to the right
				vs_2 = QtWidgets.QSpacerItem(
					0, 0,
					QtWidgets.QSizePolicy.Expanding,
					QtWidgets.QSizePolicy.Minimum
				)
				if header_pos == "RIGHT":
					child_wid.lay_min_header.addItem(vs_2)
				# Add buttons
				child_wid.lay_min_header.addWidget(child_wid.icon_wid)
				if header_pos == "LEFT":
					child_wid.lay_min_header.addItem(vs_2)
				# Add in main widget
				mainWidget_lay.addWidget(child_wid.min_header_but)

			# Add in main widget
			mainWidget_lay.addWidget(child_wid.cldActivate)

		# Face Buttons radio
		self.face_radio = QtWidgets.QRadioButton(self.mainWidget)
		# skip face radio
		self.face_radio.move(-self.face_radio.width(), 0)
		# ---ADD---
		self.face_radio.setObjectName('{}_radioChild-{}'.format(self.name, 999999999))
		self.bGroup.addButton(self.face_radio, 999999999)

		# ----set QSpacer----
		vs = QtWidgets.QSpacerItem(0, 0,  QtWidgets.QSizePolicy.Minimum,  QtWidgets.QSizePolicy.Expanding)
		mainWidget_lay.addItem(vs)
		if lay_type and header_pos == "LEFT":
			vs_2 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
			self.lay_SB_header.addItem(vs_2)

		# Set main geometry settings
		# set position
		self.mainWidget.move(parent_x, parent_y)

		# Set geometry for parent
		# after declaring geometry of SB_Content
		if parent_width:
			self.mainWidget.setFixedWidth(parent_width)
		else:
			self.mainWidget.setFixedWidth(self.mainWidget.sizeHint().width())
		if parent_height:
			self.mainWidget.setFixedHeight(parent_height)
		else:
			if lay_type:
				self.mainWidget.setFixedHeight(self.SB_header.sizeHint().height())
			else:
				self.mainWidget.setFixedHeight(child_wid.min_header_but.sizeHint().height()*cldNum)

		self.save_geometry(self.mainWidget)
		for x in range(cldNum):
			# get every child widget
			chiWid = getattr(self, '{}_WidgetConnect-{}'.format(self.name, x))
			# save geometry
			self.save_geometry(child_wid.cldActivate)
			# set values start and end
			self.update_anim(
				wid=chiWid,
				pos1=chiWid.cldActivate.sizeHint().height(),
				pos2=0,
				geometry=self.mainWidget.geometry(),
				name=self.mainWidget.objectName()
			)

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