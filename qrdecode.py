#!/Users/yetkin/miniconda3/bin/python3

import glob
import cv2
import pandas as pd
import pathlib
import sys

#kaynak: https://practicaldatascience.co.uk/data-science/how-to-read-qr-codes-in-python-using-opencv


def read_qr_code(filename):
    """Read an image and read the QR code.
    
    Args:
        filename (string): Path to file
    
    Returns:
        qr (string): Value from QR code
    """
    
    try:
        img = cv2.imread(filename)
        detect = cv2.QRCodeDetector()
        value, points, straight_qrcode = detect.detectAndDecode(img)
        return value
    except:
        return


if len(sys.argv) >= 2:
    filename=sys.argv[1]
    #print(filename)
    message = read_qr_code(filename)
    print(message)
