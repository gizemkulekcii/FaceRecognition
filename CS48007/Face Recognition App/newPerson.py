import shutil
import cv2
import os


def deletePerson(name):
    
    parent_dir = "dataset/"
    name = name 
    directory = os.path.join(parent_dir, name)
    
    try:
        for file in os.listdir(directory):
            os.remove(os.path.join(directory, file))
        os.rmdir(directory)
        print("Directory '% s' has been removed successfully" % name)
    except :
        print("Directory '% s' can not be removed" % name)
 


def modifyExistingPerson(name):

    parent_dir = "dataset/"
    
    folder_path = os.path.join(parent_dir, name)
     
    for file_object in os.listdir(folder_path):
        file_object_path = os.path.join(folder_path, file_object)
        if os.path.isfile(file_object_path) or os.path.islink(file_object_path):
            os.unlink(file_object_path)
        else:
            shutil.rmtree(file_object_path)


    cam = cv2.VideoCapture(0)

    cv2.namedWindow("Press space to take a photo", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Press space to take a photo", 500, 300)

    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("press space to take a photo", frame)

        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:
            # SPACE pressed
            img_name = "/image_{}.jpg".format(img_counter)
            img_path = folder_path + img_name
            cv2.imwrite(img_path, frame)
            print("{} written!".format(img_path))
            img_counter += 1

    cam.release()

    cv2.destroyAllWindows()


def addPerson(name):
    parent_dir = "dataset/"
    
    path = os.path.join(parent_dir, name)
    
    os.mkdir(path)
    print("Directory '% s' created" % name)


    cam = cv2.VideoCapture(0)

    cv2.namedWindow("press space to take a photo", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("press space to take a photo", 500, 300)

    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("press space to take a photo", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            
            # SPACE pressed
            img_name = "/image_{}.jpg".format(img_counter)
            img_path = path + img_name
            cv2.imwrite(img_path, frame)
            print("{} written!".format(img_path))
            img_counter += 1

    cam.release()

    cv2.destroyAllWindows()
    
'''
import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray


def addPersonPi(name):


    cam = PiCamera()
    cam.resolution = (512, 304)
    cam.framerate = 10
    rawCapture = PiRGBArray(cam, size=(512, 304))
        
    img_counter = 0

    while True:
        for frame in cam.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            image = frame.array
            cv2.imshow("Press Space to take a photo", image)
            rawCapture.truncate(0)
        
            k = cv2.waitKey(1)
            rawCapture.truncate(0)
            if k % 256 == 27: # ESC pressed
                break
            elif k%256 == 32:
                # SPACE pressed
                img_name = "dataset/"+ name +"/image_{}.jpg".format(img_counter)
                cv2.imwrite(img_name, image)
                print("{} written!".format(img_name))
                img_counter += 1
                
        if k % 256 == 27:
            print("Escape hit, closing...")
            break

    cv2.destroyAllWindows()
'''
