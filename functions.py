from tkinter import *

def resizeImage(img, newWidth, newHeight):
    oldWidth = img.width()
    oldHeight = img.height()

    # Create a new PhotoImage with the desired dimensions
    newPhotoImage = PhotoImage(width=newWidth, height=newHeight)

    # Scale the image pixel by pixel
    for x in range(newWidth):
        for y in range(newHeight):
            xOld = int(x * oldWidth / newWidth)
            yOld = int(y * oldHeight / newHeight)
            rgb = '#%02x%02x%02x' % img.get(xOld, yOld)
            newPhotoImage.put(rgb, (x, y))

    return newPhotoImage