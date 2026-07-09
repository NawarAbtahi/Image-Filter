import numpy as np

kernel = np.array([
    [0, -1, 0],
    [-1, 4, -1],
    [0, -1, 0]
])

def edge_detect(img_mode, img_arr, padded_img):
    edge_detected_arr = []

    def color_edge_detection():
        nonlocal edge_detected_arr
        edge_detected_arr = np.zeros(img_arr.shape)
        channels = img_arr.shape[2]
        color_channels = 3 if channels == 4 else channels
        for row in range(img_arr.shape[0]):
            for column in range(img_arr.shape[1]):
                for channel in range(color_channels):
                    pixel_matrix = padded_img[row:row+3, column:column+3, channel]
                    convolve_img = np.sum(pixel_matrix * kernel)
                    if convolve_img >= 255:
                        convolve_img = 255
                    elif convolve_img <= 0:
                        convolve_img = 0
                    edge_detected_arr[row, column, channel] = convolve_img
                if channels == 4:
                    edge_detected_arr[row, column, 3] = img_arr[row, column, 3]
        return edge_detected_arr

    def grayscale_edge_detection():
        nonlocal edge_detected_arr
        edge_detected_arr = np.array(np.zeros(img_arr.shape))

        for row in range(img_arr.shape[0]):
            for column in range(img_arr.shape[1]):
                pixel_matrix = padded_img[row: row+3, column: column+3]
                convolve_img = np.sum(pixel_matrix * kernel)
                if convolve_img >= 255:
                    convolve_img = 255
                elif convolve_img <= 0:
                    convolve_img = 0
                edge_detected_arr[row, column] = convolve_img
        return edge_detected_arr

    
    if(img_mode == "RGB" or img_mode == "RGBA"):
        return color_edge_detection()
    else:
        return grayscale_edge_detection()
