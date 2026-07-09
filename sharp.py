import numpy as np

kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

def sharp(img_mode,img_arr, padded_img):
    sharped_arr = []

    def color_sharp():
        nonlocal sharped_arr
        zero_count = [0] * img_arr.shape[2]
        sharped_arr = np.array([[zero_count for _ in range(img_arr.shape[1])] for _ in range(img_arr.shape[0])])   

        for row in range(img_arr.shape[0]):
            for column in range(img_arr.shape[1]):
                for channel in range(img_arr.shape[2]):
                    pixel_matrix = padded_img[row:row+3, column:column+3, channel]
                    convolve_img = np.sum(pixel_matrix * kernel)
                    if convolve_img >= 255:
                        convolve_img = 255
                    elif convolve_img <= 0:
                        convolve_img = 0
                    sharped_arr[row, column, channel] = convolve_img
        return sharped_arr
    

    def grayscale_sharp():
        nonlocal sharped_arr
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

    if(img_mode == "RGB" or img_mode == "RGBA"):
        return color_sharp()
    else:
        return grayscale_sharp()
