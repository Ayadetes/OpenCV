import cv2
import matplotlib.pyplot as plt

# Step 1: Load the Image
# User-provided image path
Image = cv2.cvtColor(cv2.imread("example.jpg"), cv2.COLOR_BGR2RGB)


# Convert BGR to RGB for correct color display with matplotlib

# Get image dimensions

height, width, _ = Image.shape

# Step 2: Draw Two Rectangles Around Interesting Regions
# Rectangle 1: Top-left corner
rect_size = (150, 150)  # Width and height of the rectangle
toppadding1 = (20,20)
toppadding2 = (toppadding1[0] + rect_size[0], toppadding1[1] + rect_size[1]) 
 # Calculate bottom-right corner
cv2.rectangle(Image, toppadding1, toppadding2, (0, 255, 255), 2)
# Fixed 20 pixels padding 
#from top-left
# Yellow rectangle


# Rectangle 2: Bottom-right corner
  # 20 pixels padding
  # Magenta rectangle
btmpadding1 = (width - rect_size[0] - 20, height - rect_size[1] - 20)
btmpadding2 = (btmpadding1[0] + rect_size[0], btmpadding1[1] + rect_size[1]) 
cv2.rectangle(Image, btmpadding1, btmpadding2, (255, 0, 255), 2)

# Step 3: Draw Circles at the Centers of Both Rectangles
   # Filled green circle
    # Filled red circle

center1 = (toppadding1[0] + rect_size[0] // 2, toppadding1[1] + rect_size[1] // 2)
center2 = (btmpadding1[0] + rect_size[0] // 2, btmpadding1[1] + rect_size[1] // 2)

# Step 4: Draw Connecting Lines Between Centers of Rectangles
cv2.circle(Image, center1, 10, (0, 255, 0), -1)  # Green circle at center of rectangle 1
cv2.circle(Image, center2, 10, (0, 0, 255), -1)  # Red circle at center of rectangle 2

cv2.line(Image, center1, center2, (0, 255, 0), 2)  # Green line connecting centers
# Step 5: Add Text Labels for Regions and Centers
cv2.putText(Image, "Region 1", (toppadding1[0], toppadding1[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 1, cv2.LINE_AA)
cv2.putText(Image, "Region 2", (btmpadding1[0], btmpadding1[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 1, cv2.LINE_AA)
cv2.putText(Image, "Center1", (center1[0]-40, center1[1] + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 1, cv2.LINE_AA)
cv2.putText(Image, "Center2", (center2[0]-40, center2[1] + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 1, cv2.LINE_AA)
# Step 6: Add Bi-Directional Arrow Representing Height
  # Start near the top-right
arrow_start = (width - 50, 20)  # Starting point of the arrow
arrow_end = (width - 50, height - 20)  # Ending point 
  # End near the bottom-right
cv2.arrowedLine(Image, arrow_start, arrow_end, (0, 0, 0), 2)
cv2.arrowedLine(Image, arrow_end, arrow_start, (0, 0, 0), 2)


# Draw arrows in both directions
  # Downward arrow
 # Upward arrow

# Annotate the height value


# Step 7: Display the Annotated Image
plt.imshow(Image)
plt.axis('off')
plt.show()

