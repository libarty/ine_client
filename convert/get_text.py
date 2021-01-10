import os, cv2, pytesseract
from PIL import Image


'''
img - patch to image file 
size - increase size for better clarity
chan - change sensitivity (contrast)
save - save black and white image for tests
'''

def get_text_image(img, size, chan, lang='eng', save=False):
	# patch to tesseract.exe
	
	patch = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
	if not os.path.exists(patch) :
		patch = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
	pytesseract.pytesseract.tesseract_cmd = patch
	scale_percent = int(size)
	image = cv2.imread(img)
	width = int(image.shape[1] * scale_percent / 100)
	height = int(image.shape[0] * scale_percent / 100)
	dim = (width, height)
	resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
	gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)        #
	ret, threshold_image = cv2.threshold(gray, chan, 150, 1, cv2.THRESH_BINARY)
	if save :
		os.mkdir(base_dir+"\gray")
		filename_dir = base_dir +"\gray\{}.png".format(os.getpid())
		cv2.imwrite(filename_dir, threshold_image)
	text = pytesseract.image_to_string(threshold_image, config='--psm 11',lang=lang)
	return text