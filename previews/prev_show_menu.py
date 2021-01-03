import sys, os, re
from PyQt5 import QtWidgets, QtCore

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path += [BASE_DIR + r'\pieces']

from general_functions import BlurEffect
from show_menu import ShowBlurWidget


class Test(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()

		mainLayout = QtWidgets.QVBoxLayout(self)
		mainLayout.setContentsMargins(0, 0, 0, 0)

		# ------central widget------

		background_widget = QtWidgets.QWidget()
		background_widget.setObjectName(u"background_widget")
		mainLayout.addWidget(background_widget)

		# ------center_lay------

		center_lay = QtWidgets.QGridLayout(background_widget)
		center_lay.setObjectName(u"center_lay")

		# ------Spacer for center------

		vs_up = QtWidgets.QSpacerItem(17, 105, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		center_lay.addItem(vs_up, 0, 1, 1, 1)
		hs_left = QtWidgets.QSpacerItem(327, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		center_lay.addItem(hs_left, 1, 0, 1, 1)
		hs_right = QtWidgets.QSpacerItem(326, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		center_lay.addItem(hs_right, 1, 2, 1, 1)
		vs_down = QtWidgets.QSpacerItem(20, 105, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		center_lay.addItem(vs_down, 2, 1, 1, 1)

		# ------block------

		block = QtWidgets.QWidget(background_widget)
		block.setObjectName(u"block")
		block.setStyleSheet('   background: white')
		center_lay.addWidget(block, 1, 1, 1, 1)

		sub_block = QtWidgets.QWidget(block)
		sub_block.setStyleSheet('background-image: url("%s");  ' % (re.sub(r'\\', '/', BASE_DIR + r'\media\img.png')))

		# ------layout for block------

		lay_sub_block = QtWidgets.QVBoxLayout(sub_block)
		lay_sub_block.setObjectName(u"lay_sub_block")
		lay_sub_block.setSpacing(0)
		lay_sub_block.setContentsMargins(0, 0, 0, 0)

		label = QtWidgets.QLabel(sub_block)
		label.setText('@')
		label.setStyleSheet('   background:rgba(27, 28, 35, 100); margin:200')
		lay_sub_block.addWidget(label)

		block.setMinimumSize(QtCore.QSize(sub_block.sizeHint().width(), sub_block.sizeHint().height()))

		# ------CONTENT------

		# Connect blur effect
		self.effect = BlurEffect()
		sub_block.setGraphicsEffect(self.effect)

		show_menu1 = ShowBlurWidget(
			name='showWid',
			effect=self.effect,
			power_blur=5,

			header_pos="LEFT",
			lay_type=False,
			cldNum=2,
			parent_width=53,

			cldHeaderColor=['rgba(0, 255, 0, 130)'],
			cldAreaColor=['rgba(0, 0, 255, 50)'],
			parent_color='rgba(255, 255, 255, 40)',

			butIcon=[['<div>&#xe900;</div>', '<div>&#xe901;</div>']],
			butMargin=[5],
			butPadding=[5],
			butSize=[25],
			butBack=['red'],
			butBackHover=['blue'],
			butColor=['yellow'],
			butColorHover=['black'],
			butBorder=['green'],
			butBorderHover=['brown'],
			parent_x=100,
			parent_y=90,

			parent=block
		)

		wid_child_0 = getattr(show_menu1, '{}_WidgetConnect-{}'.format('showWid', 0))

		# Content for Test, delete later
		lay_content_0 = QtWidgets.QVBoxLayout(wid_child_0.content)
		lay_content_0.setContentsMargins(0, 0, 0, 0)
		label_0 = QtWidgets.QLabel(wid_child_0.content)
		label_0.setText('test')
		label_0.setStyleSheet('padding:15')
		lay_content_0.addWidget(label_0)

		show_menu1.update_anim(
			wid=wid_child_0,
			pos1=wid_child_0.cldActivate.sizeHint().height(),
			pos2=0,
			geometry=show_menu1.mainWidget.geometry(),
			name=show_menu1.mainWidget.objectName()
		)

		wid_child_1 = getattr(show_menu1, '{}_WidgetConnect-{}'.format('showWid', 1))

		# Content for Test, delete later
		lay_content_1 = QtWidgets.QVBoxLayout(wid_child_1.content)
		lay_content_1.setContentsMargins(0, 0, 0, 0)
		label_1 = QtWidgets.QLabel(wid_child_1.content)
		label_1.setText('test')
		label_1.setStyleSheet('padding:15')
		lay_content_1.addWidget(label_1)

		show_menu1.update_anim(
			wid=wid_child_1,
			pos1=wid_child_1.cldActivate.sizeHint().height(),
			pos2=0,
			geometry=show_menu1.mainWidget.geometry(),
			name=show_menu1.mainWidget.objectName()
		)

		show_menu2 = ShowBlurWidget(
			name='showWid2',

			header_pos="LEFT",
			lay_type=False,
			cldNum=2,
			parent_width=153,

			cldHeaderColor=['rgba(0, 255, 0, 130)'],
			cldHeaderMargin=[[13, 1, 4]],  # [1=Left, 2=Top, 3=Right, 4=Down]

			cldAreaColor=['rgba(0, 0, 255, 50)'],
			parent_color='rgba(255, 255, 255, 40)',

			butIcon=[['<div>&#xe900;</div>', '<div>&#xe901;</div>']],
			butMargin=[5],
			butPadding=[5],
			butSize=[25],
			butBack=['red'],
			butBackHover=['blue'],
			butColor=['yellow'],
			butColorHover=['black'],
			butBorder=['green'],
			butBorderHover=['brown'],

			parent=block
		)

		# Scroll content
		tes_wid = QtWidgets.QScrollArea(block)
		# tes_wid.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		tes_wid.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

		tes_wid.setStyleSheet('background:{};border:none;'.format('red'))
		tes_wid.setWidgetResizable(True)

		# Content
		tes_cont = QtWidgets.QWidget()
		tes_wid.setWidget(tes_cont)

		tes_wid.move(200,250)
		test_lay = QtWidgets.QVBoxLayout(tes_cont)

		test_lay.addWidget(show_menu2.mainWidget)

		wid_child_2 = getattr(show_menu2, '{}_WidgetConnect-{}'.format('showWid2', 0))

		# Content for Test, delete later
		lay_content_2 = QtWidgets.QVBoxLayout(wid_child_2.content)
		lay_content_2.setContentsMargins(0, 0, 0, 0)
		label_2 = QtWidgets.QLabel(wid_child_2.content)
		label_2.setText('test')
		label_2.setStyleSheet('padding:15')
		lay_content_2.addWidget(label_2)

		show_menu2.update_anim(
			wid=wid_child_2,
			pos1=wid_child_2.cldActivate.sizeHint().height(),
			pos2=0,
			geometry=show_menu2.mainWidget.geometry(),
			name=show_menu2.mainWidget.objectName()
		)

		wid_child_3 = getattr(show_menu2, '{}_WidgetConnect-{}'.format('showWid2', 1))

		# Content for Test, delete later
		lay_content_3 = QtWidgets.QVBoxLayout(wid_child_3.content)
		lay_content_3.setContentsMargins(0, 0, 0, 0)
		label_3 = QtWidgets.QLabel(wid_child_3.content)
		label_3.setText('test')
		label_3.setStyleSheet('padding:15')
		lay_content_3.addWidget(label_3)

		show_menu2.update_anim(
			wid=wid_child_3,
			pos1=wid_child_3.cldActivate.sizeHint().height(),
			pos2=0,
			geometry=show_menu2.mainWidget.geometry(),
			name=show_menu2.mainWidget.objectName()
		)


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	w = Test()
	w.resize(640, 570)  # Size window
	w.show()
	sys.exit(app.exec_())
