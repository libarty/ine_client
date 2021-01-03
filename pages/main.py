import sys, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path += [BASE_DIR+r'\pieces']
sys.path += [BASE_DIR+r'\custom_settings']

from PyQt5 import QtWidgets, QtCore, QtGui

from lang import get_lang
from style import get_style
from ip_server import list_ip
import requests, json




class Main(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.resize(500, 500)