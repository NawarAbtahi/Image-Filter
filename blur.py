import numpy as np

kernel = (1/9) * np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
])

def blur(img_mode, img_arr, padded_img):
    blurred_arr = []

    def color_blur():
        nonlocal blurred_arr
        zero_count = [0] * img_arr.shape[2]
        blurred_arr = np.array([[zero_count for _ in range(img_arr.shape[1])] for _ in range(img_arr.shape[0])])   

        for row in range(img_arr.shape[0]):
            for column in range(img_arr.shape[1]):
                for channel in range(img_arr.shape[2]):
                    pixel_matrix = padded_img[row:row+3, column:column+3, channel]
                    convolve_img = np.sum(pixel_matrix * kernel)
                    blurred_arr[row, column, channel] = convolve_img
        return blurred_arr


    def grayscale_blur():        
        nonlocal blurred_arr
        blurred_arr = np.array(np.zeros(img_arr.shape))

        for row in range(img_arr.shape[0]):
            for column in range(img_arr.shape[1]):
                pixel_matrix = padded_img[row: row+3, column: column+3]
                convolve_img = np.sum(pixel_matrix * kernel)
                if(convolve_img >= 255):
                    convolve_img = 255
                elif(convolve_img <= 0):
                    convolve_img = 0
                blurred_arr[row, column] = convolve_img
        return blurred_arr

    
    if(img_mode == "RGB" or img_mode == "RGBA"):
        return color_blur()
        
    else:
        return grayscale_blur()
