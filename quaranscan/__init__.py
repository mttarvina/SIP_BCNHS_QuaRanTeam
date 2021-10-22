import cv2 as cv


class QuaRanScanner:
    def __init__(self):
        self.cam = cv.VideoCapture(0, cv.CAP_DSHOW)                             # access main camera, use DirectShow as backend
        self.qrDetector = cv.QRCodeDetector()
        self.camResWidth = 0
        self.camResWidth = 0
        self.promptInFeedEn = False


    def SetCameraResolution(self, width, height):
        self.camResWidth = width
        self.camResHeight = height
        self.cam.set(3, width)
        self.cam.set(4, height)


    def EnablePromptInFeed(self, promptLoc):
        self.promptInFeedEn = True
        self.promptInFeedLoc = promptLoc


    def DisplayPromptInFeed(self, prompt, color):
        if self.promptInFeedEn:
            cv.putText(self.img, prompt, self.promptInFeedLoc, cv.FONT_ITALIC, 1, color, 2)


    def DisplayFeed(self, bQRDetect):
        if self.cam.isOpened():
            while True:
                flag, self.img = self.cam.read()                                # capture an image from camera
                
                if bQRDetect:
                    decodedText, qrCorners, flag = self.qrDetector.detectAndDecode(self.img)
                    if decodedText:
                        self.DisplayPromptInFeed(f'QR Code: {decodedText}', (0, 255, 0))
                    else:
                        self.DisplayPromptInFeed('QR Code: ', (0, 0, 255))

                cv.imshow('Video', self.img)                                    # display image in window
                keyInterrupt = cv.waitKey(1) & 0xFF                             # wait for key interrupt
                if keyInterrupt == 27:                                          # escape key
                    break
            self.cam.release()                                                  # might need to remove this later
            cv.destroyAllWindows()                                              # might need to remove this later