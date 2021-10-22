# ******************************************************************************
#   Project: QuaRanScanner, SIP BCNHS 2021
#
#   Desc: <insert short description here>
#   
#   Team Members:
#       1.
#       2.
#       3.
#
#   Adviser: 
#       1. Phillip Raymund De Oca  
#
#   Code Author:
#       1. Mark Angelo Tarvina (mttarvina@gmail.com)    - Consultant
#       2.
#
#   Last Updated: 22.Oct.21 by Mark Tarvina
# ******************************************************************************




from quaranscan import QuaRanScanner


app = QuaRanScanner()

if __name__ == '__main__':
    app.SetCameraResolution(1280, 720)
    app.EnablePromptInFeed((25, 700))
    app.DisplayFeed(True)