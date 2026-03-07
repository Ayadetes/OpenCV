import cv2
import matplotlib.pyplot as plt

image = cv2.imread("assets/MarioBG.png")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("RGB")
plt.show()

greyscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(greyscale)
plt.title("Greyscaled")
plt.show()

cropped_img = image[100:300, 200:400]
cropped_rgb = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title("Cropped")
plt.show()