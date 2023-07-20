# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eQRpklza7ENF5lPLz7g12_llNtMnphnF
"""

import cv2
import matplotlib.pyplot as plt

"""importing cv2

reading the image
"""

image = cv2.imread('/content/parrot.jpeg')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()

"""converting image into gray scale"""

gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(cv2.cvtColor(gray_img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()

inv_img = 255 - gray_img
plt.imshow(cv2.cvtColor(inv_img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()

blurred = cv2.GaussianBlur(inv_img, (21,21), 0)

"""to make the image blur so that the sketch will be clear"""

inv_blur = 255 - blurred
pencil_sketch = cv2.divide(gray_img, inv_blur, scale=256.0)
plt.imshow(cv2.cvtColor(pencil_sketch, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()

