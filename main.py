import cv2

def convert_to_grayscale(image):
    """Converte uma imagem colorida para níveis de cinza.

    Args:
        image: A imagem colorida a ser convertida.

    Returns:
        A imagem em níveis de cinza.
    """

    (height, width, channels) = image.shape
    gray_image = np.zeros((height, width), dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            R, G, B = image[i, j, :]
            gray_level = (R + G + B) / 3
            gray_image[i, j] = gray_level

    return gray_image


image = cv2.imread("image.jpg")
gray_image = convert_to_grayscale(image)

cv2.imshow("Imagem colorida", image)
cv2.imshow("Imagem em níveis de cinza", gray_image)
cv2.waitKey(0)
