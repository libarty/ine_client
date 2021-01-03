import os, re
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from PyQt5 import QtWidgets, QtCore, QtGui

from general_functions import NeonEffect, per_to_num, num_to_per, replace_style


# Widget for glowing icon
class StepSwitch(QtWidgets.QWidget):
	def __init__(
			self,

			icon_back=None,  # array of icon for choose setting filter type back
			icon_neon=None,  # array of icon for choose setting filter type neon

			icon_block_color='#FFF',
			icon_back_color='#FFF',
			icon_neon_color='#FFF',
			icon_hover_color='#FFF',
			icon_size=1,

			icon_block_margin=[5],  # margin between each square
			icon_block_width=None,
			icon_block_height=1,

			id_block=0,  # set id for each widgets
			type_block=0,  # defines what it will be radio or checkbox
			neon_effect=False,

			font_weight_neon=0,
			font_weight_qss=488,


			parent=None
	):
		super(StepSwitch, self).__init__(parent)
		# set start value

		# set effect for neon
		self.save_effect = {}
		# set margin
		check = len(icon_block_margin)
		if check < 2:
			icon_block_margin.append(icon_block_margin[0])
		if check < 3:
			icon_block_margin.append(icon_block_margin[0])
		if check < 4:
			icon_block_margin.append(icon_block_margin[1])

		# set size
		if icon_block_width:
			icon_block_width = icon_block_width - icon_block_margin[0] - icon_block_margin[2]
			icon_block_height = icon_block_width * icon_block_height
			icon_size = round(icon_block_width * icon_size)
		else:
			icon_block_height = None
			if not icon_size:
				icon_size = None

		# set color
		self.icon_back_color = icon_back_color
		self.icon_hover_color = icon_hover_color


		# set type for function mousePressEvent
		self.type_block = type_block
		# main Layout
		self.lay = QtWidgets.QHBoxLayout(self)
		self.lay.setSpacing(0)
		# set margin
		self.lay.setContentsMargins(
			icon_block_margin[0],
			icon_block_margin[1],
			icon_block_margin[2],
			icon_block_margin[3]
		)

		# main widget
		self.main_widget = QtWidgets.QWidget(self)
		self.main_widget.setStyleSheet('background:{};'.format(icon_block_color))

		# set size
		if icon_block_width:
			self.main_widget.setFixedWidth(icon_block_width)
		if icon_block_height:
			self.main_widget.setFixedHeight(icon_block_height)
		# add in lay
		self.lay.addWidget(self.main_widget)
		# set layout for centering the content
		lay_icon = QtWidgets.QGridLayout(self.main_widget)
		lay_icon.setSpacing(0)
		lay_icon.setContentsMargins(0, 0, 0, 0)
		# set icon if exists

		if icon_back:
			# set icon
			self.icon_back = QtWidgets.QLabel(self)
			# set font for back neon
			font_id_1 = QtGui.QFontDatabase.addApplicationFont(re.sub(r'\\', '/', BASE_DIR + r'\media\back.ttf'))

			if font_id_1 == -1:
				print('not font back')
			font_back = QtGui.QFont("back", icon_size)
			self.icon_back.setFont(font_back)
			# set effect
			if neon_effect:
				self.effect_back = NeonEffect(color=QtGui.QColor(icon_back_color))
				self.effect_back.setStrength(1)
				# connect label
				self.icon_back.setGraphicsEffect(self.effect_back)

			# set qss
			self.icon_back.setStyleSheet('background:{};color:{};font-size:{}px;'.format(
				'#00000000',
				icon_back_color,
				icon_size))
			# set center text
			self.icon_back.setPalette(QtWidgets.QApplication.palette())
			self.icon_back.setContentsMargins(20, 20, 20, 20)
			self.icon_back.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
			self.icon_back.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

			icon_hover_duration = 100

			# set Cursor
			self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
			# set hover animation for background
			self.ani = QtCore.QVariantAnimation(
				duration=icon_hover_duration,
				startValue=QtGui.QColor(self.icon_back_color),
				endValue=QtGui.QColor(self.icon_hover_color)
			)
			self.ani.valueChanged.connect(self.change_color)

			# set text
			self.icon_back.setText(icon_back)
			# add lay
			lay_icon.addWidget(self.icon_back, 0, 0, 1, 1)
		# set icon if exists
		if icon_neon:
			# set icon
			self.icon_neon = QtWidgets.QLabel(self)
			# set font for line neon
			font_id_2 = QtGui.QFontDatabase.addApplicationFont(
				re.sub(r'\\', '/', BASE_DIR + r'\media\neon_' + str(font_weight_neon) + '.ttf')
			)

			if font_id_2 == -1:
				print('not font line')
			font_line = QtGui.QFont("neon_" + str(font_weight_neon), icon_size)
			self.icon_neon.setFont(font_line)
			if neon_effect:
				# set effect
				self.effect_neon = NeonEffect(color=QtGui.QColor(icon_neon_color))
				self.effect_neon.setStrength(1)
				# connect label
				self.icon_neon.setGraphicsEffect(self.effect_neon)
			# set qss
			self.icon_neon.setStyleSheet('background:{};color:{};font-size:{}px;font-weight:{};'.format(
				'#00000000',
				icon_neon_color,
				icon_size,
				font_weight_qss
			))
			# set center text
			self.icon_neon.setPalette(QtWidgets.QApplication.palette())
			self.icon_neon.setContentsMargins(20, 20, 20, 20)
			self.icon_neon.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
			self.icon_neon.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
			self.icon_neon.hide()

			# set text
			self.icon_neon.setText(icon_neon)
			# add lay
			lay_icon.addWidget(self.icon_neon, 0, 0, 1, 1)
		# set radio or checkbox if exists icon
		if icon_back:
			if self.type_block == 1:
				self.button = QtWidgets.QRadioButton(self)
				self.button.setStyleSheet('background:#00000000;')
				self.button.setObjectName("radio-{}".format(id_block))
				self.button.hide()
			elif self.type_block == 2:
				self.button = QtWidgets.QCheckBox(self)
				self.button.setStyleSheet('background:#00000000;')
				self.button.setObjectName("check_box-{}".format(id_block))
				self.button.hide()

	# change color for back
	def change_color(self, color):
		replaces = replace_style(
			self.icon_back.styleSheet(),
			'color:',
			color.name()
		)
		self.icon_back.setStyleSheet(replaces)
		try:
			self.effect_back.setColor(QtGui.QColor(color.name()))
		except AttributeError:
			pass

	# when mouse in label
	def enterEvent(self, event):
		try:
			self.ani.setStartValue(QtGui.QColor(self.icon_back_color))
			self.ani.setEndValue(QtGui.QColor(self.icon_hover_color))
			self.ani.start()
			super().enterEvent(event)
		except AttributeError:
			pass

	# when mouse out label
	def leaveEvent(self, event):
		try:
			try:
				self.ani.setEndValue(QtGui.QColor(self.save_effect['effect_neon_color_hov']))
			except KeyError:
				self.ani.setEndValue(QtGui.QColor(self.icon_back_color))
			self.ani.setStartValue(QtGui.QColor(self.icon_hover_color))
			self.ani.start()
			super().leaveEvent(event)
		except AttributeError:
			pass

	# function of activation radio or check_box
	def mousePressEvent(self, event):
		if self.type_block == 1 or self.type_block == 2:
			self.button.click()



# set slider for choose settings
class SliderBar(QtWidgets.QWidget):
	def __init__(
			self,
			# from another widgets
			max_slider=0,

			icon_block_margin=[10],  # margin between each square
			h_margin=[10],  # margin between horizontal set block

			icon_block_width=0,

			# own size
			height_slider=10,
			margin_slider=2,
			border_slider=1,

			# color
			slider_back_color=None,
			slider_square_back_color=None,
			slider_square_border_color=None,

			parent=None

	):
		super(SliderBar, self).__init__(parent)

		# set start value
		width_qss = icon_block_width/4 - (margin_slider+border_slider)*2

		# main widget
		lay = QtWidgets.QHBoxLayout(self)
		# copy margin
		lay.setSpacing(h_margin[0])
		lay.setContentsMargins(h_margin[1], h_margin[2], h_margin[3], h_margin[4])
		# set left widget
		self.main_widget = QtWidgets.QWidget(self)
		self.main_widget.setStyleSheet('background:{};'.format(slider_back_color))

		self.main_widget.setFixedHeight(height_slider)
		self.main_widget.setFixedWidth(icon_block_width*max_slider)

		lay.addWidget(self.main_widget)

		# set Layout for content
		main_widget_lay = QtWidgets.QGridLayout(self.main_widget)
		main_widget_lay.setSpacing(0)
		main_widget_lay.setContentsMargins(0, 0, 0, 0)

		# set size
		if icon_block_width:
			icon_block_width = (icon_block_width - icon_block_margin[0] - icon_block_margin[2]) / 2

		# set slider for choose settings
		self.slider = QtWidgets.QSlider(self)
		# set Horizontal slider
		self.slider.setOrientation(QtCore.Qt.Horizontal)
		# set start settings
		self.slider.setMaximum(max_slider)
		self.slider.setMinimum(1)
		self.slider.setValue(1)
		self.slider.setFixedHeight(height_slider)
		# set style
		self.slider.setStyleSheet(
			'''
			QSlider
			{
			background:#00000000;
			margin:0px  %spx 0px  %spx;
			}''' % (
				icon_block_width + icon_block_margin[2],
				icon_block_width + icon_block_margin[0]
			) + '''
			QSlider::groove:horizontal
			{
			height:100%;
			background:rgba(0,0,0,10);
			}
			QSlider::handle:horizontal
			{
			background: rgba(0,0,0,30);
			width: 30px;
			}
			'''
		)

		# Beautiful progress bar
		self.progress_bar_center = QtWidgets.QProgressBar(self)

		# set start settings for center
		self.progress_bar_center.setMaximum(self.slider.maximum())
		self.progress_bar_center.setMinimum(self.slider.minimum())
		self.progress_bar_center.setValue(self.progress_bar_center.minimum())
		self.progress_bar_center.setFixedHeight(height_slider)
		# set style
		self.progress_bar_center.setStyleSheet(
			'''
			QProgressBar {
				border: none;
				text-align: center;
				color: rgba(255, 255, 255, 0);
				margin:0px  %spx 0px %spx;
				background:%s;
			}
			QProgressBar::chunk {
				background-color:%s;
				border: %spx solid %s;
				margin: 0px %spx ;
				width: %spx;
			}''' % (
				icon_block_width + icon_block_margin[2],
				icon_block_width + icon_block_margin[0],
				slider_back_color,
				slider_square_back_color,
				border_slider,
				slider_square_border_color,
				margin_slider,
				width_qss
			)
		)

		# Beautiful progress bar for background
		self.progress_bar_back = QtWidgets.QProgressBar(self)

		# set start settings for background
		self.progress_bar_back.setMaximum(self.slider.maximum()*2+2)
		self.progress_bar_back.setMinimum(self.slider.minimum()-1)
		self.progress_bar_back.setValue(self.slider.minimum())
		self.progress_bar_back.setFixedHeight(height_slider)
		# set style
		self.progress_bar_back.setStyleSheet(
			'''
			QProgressBar {
				border: none;
				background-color: rgba(255, 255, 255, 255);
				text-align: center;
				color: rgba(255, 255, 255, 0);
				background:#00000000;
			}
			QProgressBar::chunk {
				background-color:%s;
				border: %spx solid %s;
				margin: 0px %spx ;
				width: %spx;

			}''' % (
				slider_square_back_color,
				border_slider,
				slider_square_border_color,
				margin_slider,
				width_qss
			)
		)

		# add content in layout
		main_widget_lay.addWidget(self.progress_bar_back, 1, 0, 1, 1)
		main_widget_lay.addWidget(self.progress_bar_center, 1, 0, 1, 1)
		main_widget_lay.addWidget(self.slider, 1, 0, 1, 1)

		# left align
		vs = QtWidgets.QSpacerItem(
					0, 0,
					QtWidgets.QSizePolicy.Expanding,
					QtWidgets.QSizePolicy.Minimum
				)
		lay.addItem(vs)

		# set  connect between slider and progress bar
		self.slider.valueChanged[int].connect(self.connect_slider_bar)

	def connect_slider_bar(self):
		self.progress_bar_center.setValue(self.slider.value())

		if self.slider.value() == self.slider.minimum():
			self.progress_bar_back.setValue(1)
		elif self.slider.value() == self.slider.maximum():
			self.progress_bar_back.setValue(self.progress_bar_back.maximum())
		else:
			self.progress_bar_back.setValue(round(self.progress_bar_back.maximum()/2))


# set filter block for content
class FilterBlock(QtWidgets.QWidget):
	def __init__(
			self,

			title="TITLE",
			title_size=10,
			title_padding=[0],

			# Array

			step_back_arr=[],  # array of icon for choose setting filter type back
			step_neon_arr=[],  # array of icon for choose setting filter type neon
			excep_back_arr=[],  # array of icon for add the slider for choose the degree of exception type back
			excep_neon_arr=[],  # array of icon for add the slider for choose the degree of exception type neon

			# Size
			v_margin=[10],  # margin between vertical set block
			h_margin=[10],  # margin between horizontal set block

			height_slider=50,  # slider height
			margin_slider=2,
			border_slider=1,

			# for back label
			effect_back_radius_max=100,  # setBlurRadius
			effect_back_radius_min=30,

			effect_back_glow_max=2,  # setGlow
			effect_back_glow_min=1,
			# for neon label
			effect_neon_radius_max=40,  # setBlurRadius
			effect_neon_radius_min=0,

			effect_neon_glow_max=4,  # setGlow
			effect_neon_glow_min=0,

			effect_neon_show=46,  # when to show widget from 0 to 100

			# color
			main_color='#FFF',

			title_back_color=None,
			title_text_color='#000',
			left_block_color=None,
			right_block_color=None,

			step_block_color=None,
			step_back_color=None,
			step_max_color=None,
			step_min_color=None,
			step_neon_color=None,
			step_hover_color=None,

			exce_block_color=None,
			exce_back_color=None,
			exce_max_color=None,
			exce_min_color=None,
			exce_neon_color=None,
			exce_hover_color=None,

			slider_back_color=None,
			slider_square_back_color=None,
			slider_square_border_color=None,

			parent=None,

			*args,
			**kwargs

	):
		super(FilterBlock, self).__init__(parent)

		# set standard value

		# color
		title_back_color = title_back_color or main_color
		left_block_color = left_block_color or main_color
		right_block_color = right_block_color or main_color
		step_block_color = step_block_color or main_color
		exce_block_color = exce_block_color or step_block_color or main_color
		self.slider_back_color = slider_back_color or main_color

		# for icon step
		self.step_back_color = step_back_color or title_text_color
		self.step_min_color = step_min_color or step_back_color
		self.step_max_color = step_max_color or step_min_color
		self.step_neon_color = step_neon_color or step_max_color
		self.step_hover_color = step_hover_color or step_neon_color

		# for icon exce
		self.exce_back_color = exce_back_color or step_back_color or title_text_color
		self.exce_min_color = exce_min_color or step_min_color or exce_back_color
		self.exce_max_color = exce_max_color or step_max_color or exce_min_color
		self.exce_neon_color = exce_neon_color or step_neon_color or exce_back_color
		self.exce_hover_color = exce_hover_color or step_hover_color or exce_neon_color

		self.slider_square_back_color = slider_square_back_color or self.step_neon_color
		self.slider_square_border_color = slider_square_border_color or self.slider_square_back_color

		# neon effect
		# for back label
		# setBlurRadius
		self.effect_back_radius_max = effect_back_radius_max
		self.effect_back_radius_min = effect_back_radius_min
		# setGlow
		self.effect_back_glow_max = effect_back_glow_max
		self.effect_back_glow_min = effect_back_glow_min
		# for neon label
		# setBlurRadius
		self.effect_neon_radius_max = effect_neon_radius_max
		self.effect_neon_radius_min = effect_neon_radius_min
		# setGlow
		self.effect_neon_glow_max = effect_neon_glow_max
		self.effect_neon_glow_min = effect_neon_glow_min
		# when to show widget from 0 to 100
		self.effect_neon_show = effect_neon_show

		# set value for slider
		self.margin_slider = margin_slider
		self.height_slider = height_slider
		self.border_slider = border_slider

		self.v_margin = v_margin
		self.h_margin = h_margin
		self.icon_block_margin = kwargs.get('icon_block_margin')
		self.icon_block_width = kwargs.get('icon_block_width')

		# margin
		check = len(v_margin)
		if check < 2:
			self.v_margin.append(self.v_margin[0])
		if check < 3:
			self.v_margin.append(self.v_margin[1])
		if check < 4:
			self.v_margin.append(self.v_margin[1])
		if check < 5:
			self.v_margin.append(self.v_margin[2])

		check = len(h_margin)
		if check < 2:
			self.h_margin.append(self.h_margin[0])
		if check < 3:
			self.h_margin.append(self.h_margin[1])
		if check < 4:
			self.h_margin.append(self.h_margin[1])
		if check < 5:
			self.h_margin.append(self.h_margin[2])

		check = len(title_padding)
		if check < 2:
			title_padding.append(title_padding[0])
		if check < 3:
			title_padding.append(title_padding[0])
		if check < 4:
			title_padding.append(title_padding[1])

		# set list for settings neon effect
		self.save_effect_arr = []
		self.neon_effect = kwargs.get('neon_effect')

		# set start value
		self.max_exce = len(excep_back_arr)

		# Group for radio
		self.sGroup = QtWidgets.QButtonGroup(self, exclusive=True)

		# set maximum number of icons
		self.max_icon = 0

		# main widget
		lay = QtWidgets.QHBoxLayout(self)
		lay.setSpacing(0)
		lay.setContentsMargins(0, 0, 0, 0)
		self.main_widget = QtWidgets.QWidget(self)
		self.main_widget.setStyleSheet('background:{};'.format(main_color))
		lay.addWidget(self.main_widget)

		# main layout for the content
		self.main_lay = QtWidgets.QVBoxLayout(self.main_widget)
		self.main_lay .setSpacing(self.v_margin[0])
		self.main_lay .setContentsMargins(
			self.v_margin[1],
			self.v_margin[2],
			self.v_margin[3],
			self.v_margin[4]
		)

		# Set name of title setting
		label_title = QtWidgets.QLabel(self.main_widget)
		label_title.setText(title)

		# set style
		label_title.setStyleSheet(
			'background:{};color:{};font-size:{}px;padding:{}px {}px {}px {}px;'.format(
				title_back_color,
				title_text_color,
				title_size,
				title_padding[0],
				title_padding[1],
				title_padding[2],
				title_padding[3]
			)
		)
		label_title.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
		self.main_lay.addWidget(label_title)

		# Set widget for choose step or exception
		settings_filter = QtWidgets.QWidget(self.main_widget)
		self.main_lay.addWidget(settings_filter)
		settings_filter_lay = QtWidgets.QHBoxLayout(settings_filter)

		# distance between step_filter and exception
		settings_filter_lay.setSpacing(self.h_margin[0])
		settings_filter_lay.setContentsMargins(
			self.h_margin[1],
			self.h_margin[2],
			self.h_margin[3],
			self.h_margin[4]
		)

		# Set widget for choose step
		self.step_filter = QtWidgets.QWidget(settings_filter)
		self.step_filter.setStyleSheet('background:{}'.format(left_block_color))
		settings_filter_lay.addWidget(self.step_filter)

		# Settings

		# distance between step_wid_block
		step_filter_lay = QtWidgets.QHBoxLayout(self.step_filter)
		step_filter_lay.setSpacing(0)
		step_filter_lay.setContentsMargins(0, 0, 0, 0)

		# add blocks with radio and neon effect
		for x in range(12):
			# set icon
			try:
				icon_back = step_back_arr[x]
				self.max_icon += 1  # for registration each icon and work like id for block
				type_set = 1  # add the radio
			except IndexError:
				icon_back = None
				type_set = 0  # don't add the radio
			try:
				icon_neon = step_neon_arr[x]
			except IndexError:
				icon_neon = None
			# create block with label-icon
			self.step_wid_block = StepSwitch(
				icon_back=icon_back,
				icon_neon=icon_neon,

				icon_block_color=step_block_color,
				icon_back_color=self.step_back_color,
				icon_neon_color=self.step_neon_color,
				icon_hover_color=step_hover_color,

				type_block=type_set,
				id_block=self.max_icon,
				parent=self.step_filter,
				*args,
				**kwargs
			)
			# set id
			setattr(self, 'step_wid_block_{}'.format(x+1), self.step_wid_block)
			# add in layout
			step_filter_lay.addWidget(self.step_wid_block)

			try:
				self.sGroup.addButton(self.step_wid_block.button, x + 1)
			except AttributeError:
				pass

		# save size block slider for found half block
		self.part_size = self.step_wid_block.sizeHint().width()

		# set widget for choose exception
		exception = QtWidgets.QWidget(settings_filter)
		exception.setStyleSheet('background:{}'.format(right_block_color))
		settings_filter_lay.addWidget(exception)

		# distance between exception_wid_block
		exception_lay = QtWidgets.QHBoxLayout(exception)
		exception_lay.setSpacing(0)
		exception_lay.setContentsMargins(0, 0, 0, 0)

		# Settings block
		for x in range(3):
			# set icon
			try:
				icon_back = excep_back_arr[x]
				type_set = 2  # add the radio
			except IndexError:
				icon_back = None
				type_set = 0  # don't add the radio
			try:
				icon_neon = excep_neon_arr[x]
			except IndexError:
				icon_neon = None

			# create block with label-icon
			self.exception_wid_block = StepSwitch(
				icon_back=icon_back,
				icon_neon=icon_neon,

				icon_block_color=exce_block_color,
				icon_back_color=self.exce_back_color,
				icon_neon_color=self.exce_neon_color,
				icon_hover_color=self.exce_hover_color,

				type_block=type_set,
				id_block=x+1,
				parent=self.step_filter,
				*args,
				**kwargs
			)
			# set id
			setattr(self, 'exception_wid_block_{}'.format(x + 1), self.exception_wid_block)
			# connect function add slider for show or hide slider

			try:
				self.exception_wid_block.button.clicked.connect(self.add_slider)
				# set start value for neon
				self.exception_wid_block.effect_neon.setBlurRadius(self.effect_neon_radius_max)
				self.exception_wid_block.effect_neon.setGlow(self.effect_neon_glow_max)
			except AttributeError:
				pass
			try:
				self.exception_wid_block.button.clicked.connect(self.neon_exce)
				self.exception_wid_block.save_effect['effect_back_color_val'] = self.exce_max_color

			except AttributeError:
				pass
			# add
			exception_lay.addWidget(self.exception_wid_block)

		# set Slider for choose setting
		self.slider_widgets = SliderBar(
			parent=self.main_widget,

			# from another widgets
			max_slider=self.max_icon,

			icon_block_margin=self.icon_block_margin,  # margin between each square
			icon_block_width=self.icon_block_width,

			h_margin=self.h_margin,  # margin between horizontal set block

			height_slider=self.height_slider,
			margin_slider=self.margin_slider,
			border_slider=self.border_slider,

			slider_back_color=self.slider_back_color,
			slider_square_back_color=self.slider_square_back_color,
			slider_square_border_color=self.slider_square_border_color,
		)

		self.main_lay.addWidget(self.slider_widgets)

		# connect to functions
		self.slider_widgets.slider.valueChanged[int].connect(self.connect_radio)
		self.slider_widgets.slider.valueChanged[int].connect(self.setpos_1)
		self.sGroup.buttonClicked[int].connect(self.connect_slider)

		# start function for change neon effect
		self.save_effect()

	# connect from radio to slider
	def connect_slider(self, id):
		self.slider_widgets.slider.setValue(id)

	# connect from slider to radio
	def connect_radio(self):
		# search radio
		wid = getattr(self, 'step_wid_block_{}'.format(self.sender().value()))
		wid.button.setChecked(True)
		# start function for change neon effect
		self.show_neon()

	# set function add_slider for settings exception
	def add_slider(self):
		slider = int(self.sender().objectName().split('-')[1])

		if self.sender().isChecked():
			# check if slider exist
			try:
				self.except_slider = getattr(self, 'except_slider_{}'.format(slider))
				# show slider
				self.except_slider.show()
			except AttributeError:
				# add new slider
				self.except_slider = SliderBar(
					parent=self.main_widget,

					# from another widgets
					max_slider=self.max_icon,

					icon_block_margin=self.icon_block_margin,  # margin between each square
					icon_block_width=self.icon_block_width,

					h_margin=self.h_margin,  # margin between horizontal set block

					height_slider=self.height_slider,

					margin_slider=self.margin_slider,
					border_slider=self.border_slider,

					slider_back_color=self.slider_back_color,
					slider_square_back_color=self.slider_square_back_color,
					slider_square_border_color=self.slider_square_border_color,
				)

				# save id slider
				setattr(self, 'except_slider_{}'.format(slider), self.except_slider)
				# add slider
				self.main_lay.addWidget(self.except_slider)
				# connect function for consolidate position
				self.except_slider.slider.valueChanged[int].connect(self.setpos_2)
		else:
			# get slider
			self.except_slider = getattr(self, 'except_slider_{}'.format(slider))
			# hide slider
			self.except_slider.hide()

	# consolidate position

	def setpos_1(self):
		for x in range(self.max_exce):
			try:
				except_slider = getattr(self, 'except_slider_{}'.format(x+1))
				if self.sender().value() > except_slider.slider.value():
					except_slider.slider.setValue(self.slider_widgets.slider.value())
			except AttributeError:
				pass

	def setpos_2(self):
		if self.sender().value() < self.slider_widgets.slider.value():
			self.sender().setValue(self.slider_widgets.slider.value())

	# save settings for optimization
	def save_effect(self):
		# set start value
		# value slider
		slider_max = self.slider_widgets.slider.maximum()
		# color back
		effect_color_back_min = QtGui.QColor(self.step_min_color)
		effect_color_back_max = QtGui.QColor(self.step_max_color)
		# color neon
		effect_color_neon_max = QtGui.QColor(self.step_neon_color)

		# recount values
		for x in range(slider_max):
			# get widgets
			wid = getattr(self, 'step_wid_block_{}'.format(x + 1))
			# set dict for settings neon effect
			self.save_effect_arr.append({})

			# get percent
			percent = num_to_per(
				x+1,
				slider_max,
			)

			# between color
			c1b = bytes.fromhex(effect_color_back_max.name()[1:])
			c2b = bytes.fromhex(effect_color_back_min.name()[1:])
			color_text = bytes(
				map(
					lambda chan: int(chan[0] * (percent / 100) + chan[1] * (1 - percent / 100)), zip(
						c1b,
						c2b
					)
				)
			)

			# save new val
			wid.save_effect['effect_back_color_val'] = "#" + color_text.hex()
			if self.neon_effect :
				wid.save_effect['effect_back_radius_val'] = per_to_num(
					percent,
					self.effect_back_radius_max,
					self.effect_back_radius_min
				)
				wid.save_effect['effect_back_glow_val'] = round(
					per_to_num(
						percent,
						self.effect_back_glow_max,
						self.effect_back_glow_min)
				)

				# set settings for  icon_neon

				if percent > self.effect_neon_show:
					# set transparent color
					percent_val = percent-self.effect_neon_show
					percent_max = 100 - self.effect_neon_show

					alpha_color = per_to_num(
						num_to_per(
							percent_val,
							percent_max
						),
						255,
						1
					)
					effect_color_neon_max.setAlpha(alpha_color)

					# save new val
					wid.save_effect['effect_neon_color_val'] = effect_color_neon_max.name()
					wid.save_effect['effect_neon_radius_val'] = per_to_num(
						percent,
						self.effect_neon_radius_max,
						self.effect_neon_radius_min
					)
					wid.save_effect['effect_neon_glow_val'] = round(
						per_to_num(
							percent,
							self.effect_neon_glow_max,
							self.effect_neon_glow_min
						)
					)

	# start neon for checkbox
	def neon_exce(self):
		# set start value
		style_back = self.sender().parent().icon_back.styleSheet()
		name_style = 'color:'
		effect_color_back_off = QtGui.QColor(self.exce_back_color)
		effect_color_back_on = QtGui.QColor(self.exce_max_color)
		# check checkbox on or off




		if self.sender().isChecked():
			# update hover
			self.sender().parent().save_effect[
				'effect_neon_color_hov'
			] = self.sender().parent().save_effect[
				'effect_back_color_val']

			# show icon neon
			self.sender().parent().icon_neon.show()
			# set style for back label
			self.sender().parent().icon_back.setStyleSheet(
				replace_style(
					style_back,
					name_style,
					effect_color_back_on.name()
				)
			)

			# save new val
			try:
				self.sender().parent().effect_back.setColor(QtGui.QColor(effect_color_back_on))
				self.sender().parent().effect_back.setBlurRadius(self.effect_back_radius_max)
				self.sender().parent().effect_back.setGlow(self.effect_back_glow_max)
			except AttributeError:
				pass
		else:
			self.sender().parent().icon_neon.hide()
			# set style for back label
			self.sender().parent().icon_back.setStyleSheet(
				replace_style(
					style_back,
					name_style,
					effect_color_back_off.name()
				)
			)
			# save new val
			try:
				self.sender().parent().effect_back.setColor(QtGui.QColor(effect_color_back_off))
				self.sender().parent().effect_back.setBlurRadius(0)
				self.sender().parent().effect_back.setGlow(0)
			except AttributeError:
				pass
			# update hove
			self.sender().parent().save_effect['effect_neon_color_hov'] = self.exce_back_color

	# change neon effect

	# for radio
	def show_neon(self):
		# set start value
		# value slider
		slider_val = self.slider_widgets.slider.value()
		slider_max = self.slider_widgets.slider.maximum()
		# color back
		effect_color_back_off = QtGui.QColor(self.step_back_color)

		# recount values
		for x in range(slider_max):
			# get each widget
			wid = getattr(self, 'step_wid_block_{}'.format(x + 1))
			# get settings for widget


			# get style for change if neon effect off
			style_back = wid.icon_back.styleSheet()
			# what parameter are we need for replace color
			name_style = 'color:'


			if slider_val > x:
				# update hove
				wid.save_effect['effect_neon_color_hov'] = wid.save_effect['effect_back_color_val']
				# get percent
				percent = num_to_per(
					x+1,
					slider_max,
				)
				# save new val
				try:
					wid.effect_back.setColor(QtGui.QColor(wid.save_effect['effect_back_color_val']))
					wid.effect_back.setBlurRadius(wid.save_effect['effect_back_radius_val'])
					wid.effect_back.setGlow(wid.save_effect['effect_back_glow_val'])
				except AttributeError:
					pass

				# update stylesheet
				wid.icon_back.setStyleSheet(replace_style(
					style_back,
					name_style,
					wid.save_effect['effect_back_color_val']
				))

				# set settings for  icon_neon

				if percent > self.effect_neon_show:
					wid.icon_neon.show()
					# save new val
					try:
						wid.effect_neon.setColor(QtGui.QColor(wid.save_effect['effect_neon_color_val']))
						wid.effect_neon.setBlurRadius(wid.save_effect['effect_neon_radius_val'])
						wid.effect_neon.setGlow(wid.save_effect['effect_neon_glow_val'])
					except AttributeError:
						pass

					# get style for change if neon effect off
					style_neon = wid.icon_neon.styleSheet()
					# update stylesheet
					wid.icon_neon.setStyleSheet(replace_style(
						style_neon,
						name_style,
						wid.save_effect['effect_neon_color_val']
					))

			else:
				wid.icon_back.setStyleSheet(
					replace_style(
						style_back,
						name_style,
						effect_color_back_off.name()
					)
				)
				wid.icon_neon.hide()
				# save new val
				try:
					wid.effect_back.setColor(QtGui.QColor(effect_color_back_off))
					wid.effect_back.setBlurRadius(0)
					wid.effect_back.setGlow(0)
				except AttributeError:
					pass
				# update hove
				wid.save_effect['effect_neon_color_hov'] = self.step_back_color

























































'''	# for radio
	def show_neon(self):
		# set start value
		# value slider
		slider_val = self.slider_widgets.slider.value()
		slider_max = self.slider_widgets.slider.maximum()
		# color back
		effect_color_back_min = QtGui.QColor(self.step_min_color)
		effect_color_back_max = QtGui.QColor(self.step_max_color)
		effect_color_back_off = QtGui.QColor(self.step_back_color)
		# color neon
		effect_color_neon_max = QtGui.QColor(self.step_neon_color)

		# recount values
		for x in range(slider_max):
			# get each widget
			wid = getattr(self, 'step_wid_block_{}'.format(x + 1))

			# get style for change if neon effect off
			style_back = wid.icon_back.styleSheet()
			# what parameter are we need for replace color
			name_style = 'color:'

			if slider_val > x:
				# get percent
				percent = (x+1) / slider_max * 100
				# between color

				color_percent = percent/10
				c1b = bytes.fromhex(effect_color_back_max.name()[1:])
				c2b = bytes.fromhex(effect_color_back_min.name()[1:])
				color_text = bytes(
					map(
						lambda chan: int(chan[0] * (color_percent / 10) + chan[1] * (1 - color_percent / 10)), zip(
							c1b,
							c2b
						)
					)
				)

				color_val_1 = "#" + color_text.hex()

				# save new val
				try:
					wid.effect_back.setColor(QtGui.QColor(color_val_1))
					wid.effect_back.setBlurRadius(
						per_to_num(percent, self.effect_back_radius_max, self.effect_back_radius_min)
					)
					wid.effect_back.setGlow(
						round(per_to_num(percent, self.effect_back_glow_max, self.effect_back_glow_min))
					)
				except AttributeError:
					pass

				replace_style(style_back, name_style, color_val_1)

				# update stylesheet

				wid.icon_back.setStyleSheet(replace_style(style_back, name_style, color_val_1))

				# set settings for  icon_neon

				if percent > self.effect_neon_show:
					wid.icon_neon.show()
					# set transparent color

					percent_val = percent-self.effect_neon_show
					percent_max = 100 - self.effect_neon_show

					alpha_color = per_to_num(
						num_to_per(
							percent_val,
							percent_max
						),
						255,
						1
					)

					effect_color_neon_max.setAlpha(alpha_color)

					# save new val
					try:
						wid.effect_neon.setColor(effect_color_neon_max)
						wid.effect_neon.setBlurRadius(
							per_to_num(percent, self.effect_neon_radius_max, self.effect_neon_radius_min)
						)
						wid.effect_neon.setGlow(
							round(per_to_num(percent, self.effect_neon_glow_max, self.effect_neon_glow_min))
						)
					except AttributeError:
						pass

					# get style for change if neon effect off
					style_neon = wid.icon_neon.styleSheet()
					# update stylesheet
					wid.icon_neon.setStyleSheet(replace_style(style_neon, name_style, effect_color_neon_max.name()))

			else:
				wid.icon_back.setStyleSheet(
					replace_style(
						style_back,
						name_style,
						effect_color_back_off.name()
					)
				)
				wid.icon_neon.hide()
				# save new val
				try:
					wid.effect_back.setColor(QtGui.QColor(effect_color_back_off))
					wid.effect_back.setBlurRadius(0)
					wid.effect_back.setGlow(0)
				except AttributeError:
					pass'''

