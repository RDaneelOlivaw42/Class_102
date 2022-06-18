import cv2

def take_snapshot():
    #intializing cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while(result):
        #read the frames while the camera is on
        ret, frame = videoCaptureObject.read()

        #cv2.imwrite() - this method is used to store an image to any storage device
        cv2.imwrite("new_picture.jpg", frame)

        result = False
    
    #close the camera
    videoCaptureObject.release()

    #close all other windows using camera
    cv2.destroyAllWindows()

take_snapshot()