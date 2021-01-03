import os, sys
from PyQt5 import QtWidgets

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path += [BASE_DIR+r'\pieces']

from back_animation import BackGeometryAnimation


class Test(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.resize(1600, 800)
		self.setStyleSheet('background:#494853;')
		wid_2 = BackGeometryAnimation(
			num_x=10,
			num_y=10,
			color='rgba(110, 113, 135, 100)',
			min_size=20,
			max_size=60,
			min_rotate=0,
			max_rotate=90,
			duration=8000,
			parent=self
		)


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	w = Test()
	w.show()
	sys.exit(app.exec_())




























