# ******************************************************************************
# THIS CONTAINS ALL DEBUG CODES THAT NEED TO BE TESTED
# ******************************************************************************




# ******************************************************************************
# Basic code to livestream from webcam

# import cv2

# cam = cv2.VideoCapture(0)                                                       # access main camera
# fps = cam.get(cv2.CAP_PROP_FPS)                                                 # get native camera fps value
# print(f'FPS = {fps}')

# while True:
#     flag, img = cam.read()                                                      # capture an image from camera
#     cv2.imshow('Video', img)                                                    # display image in window

#     keyInterrupt = cv2.waitKey(1) & 0xFF                                        # wait for key interrupt
#     if keyInterrupt == 27:                                                      # escape key
#         break

# cam.release()
# cv2.destroyAllWindows()




# ******************************************************************************
# QR code detector
import cv2

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)                                        # access main camera, use DirectShow as backend
fps = cam.get(cv2.CAP_PROP_FPS)                                                 # get native camera fps value
print(f'FPS = {fps}')

cam.set(3, 1280) # set frame width
cam.set(4, 720) # set frame height

qrDetector = cv2.QRCodeDetector()                                               # create an instance of QR code detector

while True:
    flag, img = cam.read()                                                      # capture an image from camera
    decodedText, qrCorners, flag = qrDetector.detectAndDecode(img)
    if decodedText:
        cv2.putText(img, f'QR Detected: {decodedText}', (25, 450), cv2.FONT_ITALIC, 1, (0, 255, 0), 2)
    else:
        cv2.putText(img, f'QR missing', (25, 450), cv2.FONT_ITALIC, 1, (0, 0, 255), 2)

    cv2.imshow('Video', img)                                                    # display image in window
    keyInterrupt = cv2.waitKey(1) & 0xFF                                       # wait for key interrupt
    if keyInterrupt == 27:                                                      # escape key
        break

cam.release()
cv2.destroyAllWindows()


