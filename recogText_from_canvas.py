import base64
import pytesseract
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


encode_str = "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"
decoded_string = base64.b64decode(encode_str, validate=True)

str_np = np.frombuffer(decoded_string, dtype=np.uint8)


image = cv2.imdecode(str_np, flags=1)
image = cv2.resize(image, (300, 300))
image = cv2.dilate(image, None, iterations=1)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, img = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
ret1, img2 = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
kernel = np.ones((8, 8), np.uint8)
kernel2 = np.ones((3, 3), np.uint8)
img2 = cv2.morphologyEx(img2, cv2.MORPH_OPEN, kernel)
img2 = cv2.bitwise_not(img2)
for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        if img[x, y] == img2[x, y]:
            img[x, y] = 255
        else:
            img[x, y] = 0
img = cv2.morphologyEx(img, cv2.MORPH_CROSS, kernel2)
img_up = img[0:150, 150:300]
img_up = cv2.resize(img_up, (300, 120))
contours, hierachy = cv2.findContours(img_up, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
image_copy = img_up.copy()

# text = ""
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    rect = cv2.rectangle(image_copy, (x, y), (x + w, y + h), (0, 255, 0), 1)
    cropped = image_copy[y : y + h, x : x + w]
    cv2.imshow("d", cropped)
    text = pytesseract.image_to_string(cropped)
    print(text)
cv2.waitKey(0)
cv2.destroyAllWindows()
