#!/Users/yetkin/miniconda3/bin/python

# import the opencv library
import cv2

# define a video capture object
vid = cv2.VideoCapture(0)
frames=120 #frame countdown 
while(True):
	# Capture the video frame
	# by frame
	ret, frame = vid.read()
	if frames > 0:
            cv2.putText(frame, 
                    "QR kodunu gosterin: "+str(frames), 
                    (50, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, 
                    (0, 255, 255), 
                    2, 
                    cv2.LINE_4)
	frames = frames - 1
	# Display the resulting frame
	cv2.imshow('frame', frame)
	if frames < 0:
            cv2.imwrite('qr.jpg',frame)
            break
            
	
	# the 'q' button is set as the
	# quitting button you may use any
	# desired button of your choice
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()

