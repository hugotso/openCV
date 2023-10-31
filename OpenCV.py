import cv2
import numpy as np


data = np.array([[1, 2, 3, 4, 5, 6, 7],
                [1, 2, 3, 4, 5, 6, 7],
                [1, 2, 3, 4, 5, 6, 7]])


data[1:3, 1:5] *= 2
print(data)


# print(np.sum(data, axis=0))

# print(type(data))
# print(len(data))
# print(data.shape)




img = cv2.imread('cover.jpg')
print(type(img))
# img = cv2.resize(img, (0, 0), fx=1.5, fy=1.5)
# cv2.imshow('cover', img)
# cv2.waitKey(0)
