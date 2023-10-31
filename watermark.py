import cv2
import numpy as np
# type np.uint8 np.float16 np.float32

img = cv2.imread('cover.jpg')
img = img.astype(np.float16)
watermark_img = cv2.imread('watermark.jpg')
watermark_pos = [800, 500]
img[watermark_pos[0]:watermark_pos[0]+watermark_img.shape[0], watermark_pos[1]:watermark_pos[1]+watermark_img.shape[1], :] += watermark_img
index = img >= 255
img[index] = 255
print(index.shape)
img = img.astype(np.uint8)
cv2.imshow('cover', img)
cv2.waitKey(0)