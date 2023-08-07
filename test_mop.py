import cv2 as cv

image = cv.imread("test.jpg", 0)

from PIL import Image
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

fname='test.jpg'
# blur_radius = 1.0
threshold = 50

img = Image.open(fname).convert('L')
img = 255 - np.asarray(img)
print(img.shape)
# (160, 240)

# smooth the image (to remove small objects)
# imgf = ndimage.gaussian_filter(img, blur_radius)
threshold = 50

# find connected components
labeled, nr_objects = ndimage.label(img > threshold) 
print(type(nr_objects))
# exit(0)
print("Number of objects is {}".format(nr_objects))
# Number of objects is 4 

plt.imsave('out.png', labeled)
plt.imshow(labeled)

plt.show()