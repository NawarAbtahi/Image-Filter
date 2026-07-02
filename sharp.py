import numpy as np

kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

def sharp(img_arr, padded_img):
    sharped_arr = np.array(np.zeros(img_arr.shape))
    for row in range(img_arr.shape[0]):
        for column in range(img_arr.shape[1]):
            pixel_matrix = padded_img[row: row+3, column: column+3]
            convolve_img = np.sum(pixel_matrix * kernel)
            if convolve_img >= 255:
                convolve_img = 255
            elif convolve_img <= 0:
                convolve_img = 0
            sharped_arr[row, column] = convolve_img
    return sharped_arr
