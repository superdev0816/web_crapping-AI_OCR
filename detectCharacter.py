import base64
import pytesseract
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def detect_str(encode_str):
    new_str = encode_str.replace("data:image/png;base64,", "")
    decoded_string = base64.b64decode(new_str, validate=True)

    str_np = np.frombuffer(decoded_string, dtype=np.uint8)


    image = cv2.imdecode(str_np, flags=1)


    image = cv2.resize(image, (300, 120))
    image = cv2.dilate(image, None, iterations=1)
    image = cv2.GaussianBlur(image, (1, 9), 2)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresholded = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

    # Invert the image
    inverted = cv2.bitwise_not(thresholded)

    # Find contours in the image
    contours, _ = cv2.findContours(inverted, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create a blank image
    extracted_letter = np.zeros_like(image)

    # Draw contours on the blank image
    for contour in contours:
        cv2.drawContours(extracted_letter, [contour], 0, (255, 255, 255), -1)


    ret, img = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    kernel = np.ones((5, 5), np.uint8)

    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

    result = np.ones_like(img.shape)
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            if img[x][y] != extracted_letter[x][y]:
                img[x][y] = 0
            else:
                img[x][y] = 255
    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    contours, hierachy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    image_copy = img.copy()
    text = ""
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)

        cropped = image_copy[y : y + h, x : x + w]
        text = pytesseract.image_to_string(cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return text


