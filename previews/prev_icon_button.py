import sys, os
from PyQt5 import QtWidgets

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path += [BASE_DIR+r'\pieces']

from icon_button import SetIcon


class Test(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		
		lay = QtWidgets.QVBoxLayout(self)
		
		icon_wid_1 = SetIcon()
		
		lay.addWidget(icon_wid_1)

		icon_wid_2 = SetIcon(
			butMargin=5,
			butPadding=5,
			butBack='red',
			butBackHover='blue',
			butColor='yellow',
			butColorHover='black',
			butBorder='green',
			butBorderHover='brown',
			butIcon=['<div>&#xe900;</div>', '<div>&#xe901;</div>']
		)
		
		lay.addWidget(icon_wid_2)

		icon_wid_3 = SetIcon(
			butSize=25,
			butMargin=5,
			butPadding=5,
			butBack='red',
			butBackHover='blue',
			butColor='yellow',
			butColorHover='black',
			butBorder='green',
			butBorderHover='brown',
			butIcon=['<div>&#xe900;</div>', '<div>&#xe901;</div>']
		)
		
		lay.addWidget(icon_wid_3)

		buttonGroup = QtWidgets.QButtonGroup(self, exclusive=True)
		buttonGroup.buttonClicked[int].connect(self.onButtonClicked)
		buttonGroup.addButton(icon_wid_1.radio, 1)
		buttonGroup.addButton(icon_wid_2.radio, 2)
		buttonGroup.addButton(icon_wid_3.radio, 3)

	def onButtonClicked(self, id):
		print(id)


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	w = Test()
	w.show()
	sys.exit(app.exec_())




