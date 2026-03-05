import cv2 
image = cv2.imread("ZExampleImage.png")
cv2.namedWindow("Example Window", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Example Window", 500,600)
unref = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_img = cv2.resize(unref, (300,300))


cv2.imshow("Example Window", gray_img)
key = cv2.waitKey(0)
if key == ord('s'):
    cv2.imwrite("Grayified.png", gray_img)
else: 
    print("Image Not Saved")
cv2.destroyAllWindows()

print(f"Image Dimensions: {image.shape}")
