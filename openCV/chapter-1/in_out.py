import cv2 as cv


# Iinput
img = cv.imread(filename)
img = cv.imread(filename, cv.IMREAD_GRAYSCALE)

# storing image
cv.imwrite(filename, img)

# getting the pixel intensity of a pixel
_intensity= img[y, x]

    # Changing pixels
        #img[x, y] = 128


# Visualizing images
    #img = cv.imread('image.jpg')
    #cv.namedWindow('image', cv.WINDOW_AUTOSIZE)
    #cv.imshow('image', img)
    #cv.waitKey()

