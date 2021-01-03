import sys, os, re
from PyQt5 import QtWidgets, QtCore

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path += [BASE_DIR + r'\pieces']

from general_functions import BlurEffect
from blur_menu import MoveBlurWidget


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
		
		blur_menu1 = MoveBlurWidget(
			name='blurWid',
			effect=self.effect,
			power_blur=5,
			parent_height=sub_block.sizeHint().height(),
			parent_pos="UP",
			cldNum=2,

			cldColor=['rgba(27, 28, 35, 30)'],
			cldWidth=[90],
			cldHeight=[sub_block.sizeHint().height()],

			but1Icon=['<div>&#xe900;</div>', '<div>&#xe901;</div>'],
			butMargin=[5],
			butPadding=[5],
			butSize=[25],
			butBack=['red'],
			butBackHover=['blue'],
			butColor=['yellow'],
			butColorHover=['black'],
			butBorder=['green'],
			butBorderHover=['brown'],
			parent_y=0,
			type_move=['L', 'Y_S', 'R', 'Y_S'],
			parent=block
		)

		wid_child_0 = getattr(blur_menu1, '{}_WidgetConnect-{}'.format('blurWid', 0))
		wid_child_1 = getattr(blur_menu1, '{}_WidgetConnect-{}'.format('blurWid', 1))

		lay_child_1 = QtWidgets.QVBoxLayout(wid_child_0.cldActivate)
		lay_child_2 = QtWidgets.QVBoxLayout(wid_child_1.cldActivate)

		Label_1 = QtWidgets.QLabel(wid_child_0.cldActivate)
		Label_1.setText('Text - 1')

		Label_2 = QtWidgets.QLabel(wid_child_1.cldActivate)
		Label_2.setText('Text - 2')

		lay_child_1.addWidget(Label_1)
		lay_child_2.addWidget(Label_2)

		vs_1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		vs_2 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		lay_child_1.addItem(vs_1)
		lay_child_2.addItem(vs_2)

		blur_menu2 = MoveBlurWidget(
			name='BlurWid2',
			effect=self.effect,
			power_blur=5,
			parent_x=200,
			parent_y=200,
			parent_pos="UP",
			cldColor=['rgba(27, 28, 35, 30)'],
			cldNum=2,
			but1Icon=['<div>&#xe900;</div>', '<div>&#xe901;</div>'],
			butMargin=[5],
			butPadding=[5],
			butSize=[20],
			butBack=['red'],
			butBackHover=['blue'],
			butColor=['yellow'],
			butColorHover=['black'],
			butBorder=['green'],
			butBorderHover=['brown'],
			duration=[500],
			type_move=['R', 'Y_C', 'ALT_L', 'Y_C'],

			parent=block
		)

		wid_child_3 = getattr(
			blur_menu2,
			'{}_WidgetConnect-{}'.format(
				'BlurWid2',
				0
			)
		)

		wid_child_4 = getattr(
			blur_menu2,
			'{}_WidgetConnect-{}'.format(
				'BlurWid2',
				1
			)
		)

		lay_child_3 = QtWidgets.QVBoxLayout(wid_child_3.cldActivate)
		lay_child_4 = QtWidgets.QVBoxLayout(wid_child_4.cldActivate)

		Label_3 = QtWidgets.QLabel(wid_child_3.cldActivate)
		Label_3.setText('Text -3')

		Label_4 = QtWidgets.QLabel(wid_child_4.cldActivate)
		Label_4.setText('Text -44444444')

		lay_child_3.addWidget(Label_3)
		lay_child_4.addWidget(Label_4)

		wid_child_3.cldActivate.resize(
			wid_child_3.cldActivate.sizeHint().width(),
			wid_child_3.cldActivate.sizeHint().height()

		)
		wid_child_4.cldActivate.resize(
			wid_child_4.cldActivate.sizeHint().width(),
			wid_child_4.cldActivate.sizeHint().height()
		)

		blur_menu2.save_geometry(wid_child_3.cldActivate, res=True)
		blur_menu2.save_geometry(wid_child_4.cldActivate, res=True)
		blur_menu2.update_anim(wid_child_3)
		blur_menu2.update_anim(wid_child_4)

	# type_move=['R', 'Y_C', 'ALT_L', 'Y_C'],
	# type_move=['X_C', 'U', 'X_C', 'ALT_D'],


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	w = Test()
	w.resize(640, 570)  # Size window
	w.show()
	sys.exit(app.exec_())
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
