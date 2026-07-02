from PIL import Image
from blur import blur
from sharp import sharp
import numpy as np

img = Image.open("./images/test-image-2.png")

img_arr = np.array(img.convert('L')) #grayscale for 2d array

h, w = img_arr.shape

padded_image = np.append(img_arr, np.array([[0] * w]), axis=0)
padded_image = np.append(np.array([[0] * w]), padded_image, axis=0)
padded_image = np.append(padded_image, np.array([[0]] * (h+2) ), axis=1)
padded_image = np.append(np.array([[0]] * (h+2)), padded_image, axis=1)

blurred_img = Image.fromarray(blur(img_arr,padded_image).astype(np.uint8))

blurred_img.save("./images/test-image-2-blur.png")
