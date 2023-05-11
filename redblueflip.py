#!/usr/bin/env python3
import cv2
from PIL import Image
import sys
def main():
    if len(sys.argv) != 2:
        sys.exit("use: redblueflip.py image.jpg")
    image = sys.argv[1]
    image = cv2.imread(image) # open image
    image = image[:, :, ::-1] # flip red and blue chans
    saveas = 'flipped_%s' %(sys.argv[1])
    print(saveas)
    cv2.imwrite(saveas, image) # save image.

if __name__ == "__main__":
    main()
