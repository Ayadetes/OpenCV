import cv2 
image = cv2.imread("ZExampleImage.png")
cv2.namedWindow("Example Window", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Example Window", 500,500)
cv2.imshow("Example Window", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Image Dimensions: {image.shape}")