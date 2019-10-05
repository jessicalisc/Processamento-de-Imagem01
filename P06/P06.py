import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('filhote.jpg')
rows,cols,ch = img.shape

pts1 = np.float32([[556,265],[568,252],[528,487],[589,890]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(300,300))

cv2.imwrite('filhote_aumento.jpg', dst)
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
