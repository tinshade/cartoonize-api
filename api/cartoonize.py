import cv2
import numpy as np
import os
'''
#This program generates a cartoonized image of the given image!
img = cv2.imread("image.jpg")

def color_quantization(img, k):
	data = np.float32(img).reshape((-1, 3))
	criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
	ret, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
	center = np.uint8(center)
	result = center[label.flatten()]
	result = result.reshape(img.shape)
	return result

img_1 = color_quantization(img, 7)
blurred = cv2.medianBlur(img_1, 3)
while True:
	cv2.imshow("blurred", blurred)
	cv2.imwrite("blurred.png",blurred)
	if cv2.waitKey(1) == 0x1b: # ESC
		print('ESC pressed. Exiting ...')
		break
'''

def cartoonize(user_name,name, curr_ext, pref_ext):
	try:
		path = "./media/user_images/uploads/"
		try:
			if curr_ext.lower() not in ["jpg",'jpeg']:
				return "Invalid File Type"
		except:
			return "Invalid File Type"
		
		img = cv2.imread(path+name)
		
		def color_quantization(img, k):
			data = np.float32(img).reshape((-1, 3))
			criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
			ret, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
			center = np.uint8(center)
			result = center[label.flatten()]
			result = result.reshape(img.shape)
			return result

		img_1 = color_quantization(img, 7)
		
		blurred = cv2.medianBlur(img_1, 3)
		cv2.imwrite(f"./media/user_images/served/{user_name}.{pref_ext}",blurred)
		return "Success"
	except:
		return "Not Found"