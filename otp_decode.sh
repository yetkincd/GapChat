python3 capture_photo2.py
python3 otp_crypto2.py -d $(python3 qrdecode.py qr.jpg) >otp_output.txt
python3 messagebox1.py "$(cat otp_output.txt)"
