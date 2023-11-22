rm qrout.png
python3 get_input.py > otp_input.txt

ENCODED_INPUT=$(python3 otp_crypto2.py otp_input.txt)

#echo xxx > otp_input.txt
#rm otp_input.txt

python3 qrencode.py $ENCODED_INPUT qrout.png
#./qrencode.py \"$(./otp_crypto2.py $(./get_input.py))\" qrout.png
open qrout.png
