import sys, os
from PyQt5 import QtWidgets

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path += [BASE_DIR+r'\pieces']

from collapsing_block import CollapsingBlock

class Test(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.resize(1000, 1000)

		lay = QtWidgets.QGridLayout(self)
		lay.setSpacing(0)
		lay.setContentsMargins(0, 0, 0, 0)

		wid1 = QtWidgets.QWidget(self)
		wid1.setStyleSheet('background:black')
		lay.addWidget(wid1,0,0,1,1)

		wid2 = QtWidgets.QWidget(self)
		wid2.setStyleSheet('background:black')
		lay.addWidget(wid2,1,0,1,1)

		wid3 = QtWidgets.QWidget(self)
		wid3.setStyleSheet('background:black')
		lay.addWidget(wid3,0,1,1,1)

		self.wid4 = QtWidgets.QWidget(self)
		self.wid4.setStyleSheet('background:white')
		lay.addWidget(self.wid4,1,1,1,1)

		lay_wid4 = QtWidgets.QVBoxLayout(self)
		lay_wid4.setSpacing(0)
		lay_wid4.setContentsMargins(0, 0, 0, 0)

		print(self.wid4.geometry())
		print(self.wid4.sizeHint().width())
		print(self.wid4.sizeHint().height())
		print(self.wid4.size())

		wid = CollapsingBlock(
			parent=self.wid4,
			text=False,
			max_random=5,
			border=0,
			speed=100,
			stop=20,
			max_pos=20,
			color_block='black',
			height=500,
			width=500,
		)

		lay_wid4.addWidget(wid)


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	w = Test()
	w.show()
	sys.exit(app.exec_())