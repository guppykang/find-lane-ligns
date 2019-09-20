import cv2
import matplotlib.pyplot as plt
import numpy as np

def canny(image): 
    gray_lane_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur_lane_image = cv2.GaussianBlur(gray_lane_image, (5,5), 0)
    canny_lane_image = cv2.Canny(blur_lane_image, 50, 150)
    return canny_lane_image

def region_of_interest(image): 
    height  = image.shape[0]
    polygons = np.array([
        [(200, height), (1100, height), (550, height)]
    ])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 225)
    return mask

image = cv2.imread('test_image.jpg')
lane_image = np.copy(image)
canny_image = canny(lane_image)

cv2.imshow('yoyo', region_of_interest(canny_image));
cv2.waitKey(0)
#plt.imshow(canny_image)
#plt.show(0)

