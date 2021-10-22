from quaranscan import QuaRanScanner


app = QuaRanScanner()

if __name__ == '__main__':
    app.SetCameraResolution(1280, 720)
    app.EnablePromptInFeed((25, 700))
    app.DisplayFeed(True)