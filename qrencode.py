#!/usr/bin/python3

import sys
# Importing library
import qrcode
 
# Data to be encoded
if len(sys.argv) == 3:
        data = sys.argv[1]
        qrfilename = sys.argv[2]
if len(sys.argv) == 4 and sys.argv[1] == "-f":
        textfilename = sys.argv[2]
        qrfilename = sys.argv[3]
        f=open(textfilename)
        data=f.read()
        f.close()

if len(sys.argv) >=3: 
# Encoding data using make() function
	img = qrcode.make(data)
	img.save(qrfilename)
