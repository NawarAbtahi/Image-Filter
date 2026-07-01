import numpy as np

kernel = (1/9) * np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
])



def blur(img_arr, padded_img):
    blurred_arr = np.array(np.zeros(img_arr.shape))
    for row in range(img_arr.shape[0]):
        for column in range(img_arr.shape[1]):
            pixel_matrix = padded_img[row: row+3, column: column+3]
            convolve_img = np.sum(pixel_matrix * kernel)
            blurred_arr[row, column] = convolve_img
    return blurred_arr

