import cv2
import numpy as np


img = cv2.imread('cover.jpg')
center_x = int(img.shape[1]/2)
center_y = int(img.shape[0]/2)
print(center_x, center_y)
img [center_y-100:center_y+100, center_x-100:center_x+100, 0:3] = [0, 255, 255]
cv2.imshow('cover', img)
cv2.waitKey(0)

# print(img.shape)


# data[1:3, 1:5] *= 2
# print(data)


# print(np.sum(data, axis=0))

# print(type(data))
# print(len(data))
# print(data.shape)




img = cv2.imread('cover.jpg')
print(type(img))
# img = cv2.resize(img, (0, 0), fx=1.5, fy=1.5)
# cv2.imshow('cover', img)
# cv2.waitKey(0)
