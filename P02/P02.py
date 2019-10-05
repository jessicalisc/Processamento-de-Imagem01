import cv2
import numpy as np

img = cv2.imread('filhote.jpg')

height, width = img.shape[:2]
res = cv2.resize(img, (width, height//4), interpolation=cv2.INTER_CUBIC)

cv2.imwrite('filhote_1.jpg', res)
cv2.imshow('imagem', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
