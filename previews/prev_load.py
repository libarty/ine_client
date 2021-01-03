import sys, os
from PyQt5 import QtWidgets, QtCore

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path += [BASE_DIR + r'\pieces']

from load import LoadFigure, LoadBlock, LoadBar


class Test(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.resize(500, 500)
		self.setStyleSheet("background:#11111b;")

		lay = QtWidgets.QVBoxLayout(self)
		lay.setSpacing(0)
		lay.setContentsMargins(0, 0, 0, 0)

		main = QtWidgets.QWidget(self)
		lay.addWidget(main)

		main_lay = QtWidgets.QHBoxLayout(main)
		main_lay.setSpacing(0)
		main_lay.setContentsMargins(200, 0, 200, 0)

		label = QtWidgets.QLabel(self)
		label.setText('Loading')
		label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignVCenter)
		label.setStyleSheet('background:#11111b;color:#ebebf9;font-size:50px;padding:0px 0px 50px 0px;')

		main_lay.addWidget(label)

		wid1 = LoadBlock(
			distance=3,
			size_back=1.7,
			size=20,
			parent=main,
			pause=2000,
			duration=1250,
			triangle=False,
			circle=True,
			color='#ebebf9'
		)
		main_lay.addWidget(wid1)

		wid2 = LoadBlock(
			distance=3,
			size_back=1.7,
			size=20,
			parent=main,
			pause=1500,
			duration=1250,
			triangle=True,
			circle=False,
			color='#ebebf9'
		)
		main_lay.addWidget(wid2)

		wid3 = LoadBlock(
			distance=3,
			size_back=1.7,
			size=20,
			parent=main,
			pause=1000,
			duration=1250,
			triangle=True,
			circle=True,
			color='#ebebf9'
		)
		main_lay.addWidget(wid3)

		load_bar = LoadBar(
			parent=self,
			color_back='white',
			color_load='black',
		)
		lay.addWidget(load_bar)


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	w = Test()
	w.show()
	sys.exit(app.exec_())