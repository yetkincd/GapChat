./capture_photo2.py
./otp_crypto.py -d $(./qrdecode.py qr.jpg) >otp_output.txt
./messagebox1.py "$(cat otp_output.txt)"
