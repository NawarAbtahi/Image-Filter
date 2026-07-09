import numpy as np
from PIL import Image
from numpy._core import uint8
from blur import blur
from sharp import sharp
from edge_detection import edge_detect

path_input = input("Enter img path: ")
img = Image.open(path_input)
img_mode = img.mode
last_dot = path_input.rfind('.')
file_name = path_input[0 : last_dot]
file_extension = path_input[last_dot:]

img_arr = np.array(img) #grayscale for 2d array

h = 0;
w = 0;
c = 0;

if(img_mode == "RGB" or img_mode == "RGBA"):
    h, w, c = img_arr.shape
else:
    h, w= img_arr.shape

padded_image = np.zeros

if(img_mode == "RGB" or img_mode == "RGBA"):
    zero_quant = [0] * img_arr.shape[2]
    padded_image = np.append(img_arr, np.array([[zero_quant] * w]), axis= 0)
    padded_image = np.append(np.array([[zero_quant] * w]), padded_image, axis=0)
    padded_image = np.append(padded_image, np.array([[zero_quant]] * (h+2)), axis = 1)
    padded_image = np.append(np.array([[zero_quant]] * (h+2)), padded_image, axis= 1)
else:
    padded_image = np.append(img_arr, np.array([[0] * w]), axis=0)
    padded_image = np.append(np.array([[0] * w]), padded_image, axis=0)
    padded_image = np.append(padded_image, np.array([[0]] * (h+2) ), axis=1)
    padded_image = np.append(np.array([[0]] * (h+2)), padded_image, axis=1)

img_filter_options = int(input("1. Blur\n2. Sharp\n3. Edge Detection:\nInput: "))

match img_filter_options:
    case 1:
        blur_img = Image.fromarray(blur(img_mode, img_arr, padded_image).astype(np.uint8))
        blur_img.save(f"{file_name}-blur{file_extension}")
        print("Image has been Blurred!")
    case 2:
        sharp_img = Image.fromarray(sharp(img_mode, img_arr, padded_image).astype(np.uint8))
        sharp_img.save(f"{file_name}-sharp{file_extension}")
        print("Image has been Sharped!")
    case 3:
        edge_detect_img = Image.fromarray(edge_detect(img_mode, img_arr, padded_image).astype(np.uint8))
        edge_detect_img.save(f"{file_name}-edge-detect{file_extension}")
        print("Image's edges has been detected!")

