rm qrout.png
./get_input.py > otp_input.txt

ENCODED_INPUT=$(./otp_crypto2.py otp_input.txt)

#echo xxx > otp_input.txt
#rm otp_input.txt

./qrencode.py $ENCODED_INPUT qrout.png
#./qrencode.py \"$(./otp_crypto.py $(./get_input.py))\" qrout.png
open qrout.png
