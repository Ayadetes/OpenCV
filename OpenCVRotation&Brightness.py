import cv2 
import matplotlib.pyplot as plt
import numpy 

image = cv2.cvtColor(cv2.imread("assets/MarioBG.png"), cv2.COLOR_BGR2RGB)
(w,h) = image.shape[:2]
center = (w//2, h//2)
M = cv2.getRotationMatrix2D(center, 45, 1)
rotated = cv2.warpAffine(image, M, (w,h))

plt.imshow(rotated)
plt.title("rotated")
plt.show()

brightness_matrix = numpy.ones(image.shape, dtype="uint8") *  50
brighter = cv2.add(image, brightness_matrix)

plt.imshow(brighter)
plt.title("brightened")
plt.show()