import cv2

im = cv2.imread('filhote.jpg')
img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
cv2.imwrite('filhote_cinza.jpg', img)
print('..|imagem salva com sucesso')
