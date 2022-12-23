import cv2
import face_recognition
from imutils.video import FPS




def faceRecognition(known_face_encodings, known_face_names):
    
    webcam_video_stream = cv2.VideoCapture(0)
    
    fps = FPS().start()

    face_locations = []
    face_encodings = []

    #loop through every frame in the video
    while True:

        ret,current_frame = webcam_video_stream.read()
        #resize the current frame to 1/4 size r
        current_frame_small = cv2.resize(current_frame,(0,0),fx=0.25,fy=0.25)
        #detect all faces in the image
        face_locations = face_recognition.face_locations(current_frame_small,number_of_times_to_upsample=1,model='hog')
        
        #detect face encodings for all the faces detected
        face_encodings = face_recognition.face_encodings(current_frame_small,face_locations)


        #looping through the face locations and the face embeddings
        for current_face_location,current_face_encoding in zip(face_locations,face_encodings):
            top_pos,right_pos,bottom_pos,left_pos = current_face_location
            
            top_pos = top_pos*4
            right_pos = right_pos*4
            bottom_pos = bottom_pos*4
            left_pos = left_pos*4
            
            #find all the matches 
            all_matches = face_recognition.compare_faces(known_face_encodings, current_face_encoding)
        
            name_of_person = 'Unknown face'
            
            #check if the all_matches have at least one item
            if True in all_matches:
                first_match_index = all_matches.index(True)          #get the index number of face that is located in the first index of all_matches
                name_of_person = known_face_names[first_match_index] #get the name corresponding to the index number and save it in name_of_person
            
            #draw boxes   
            cv2.rectangle(current_frame,(left_pos,top_pos),(right_pos,bottom_pos),(255,0,0),2)
            
            #display the name as text 
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(current_frame, name_of_person, (left_pos,bottom_pos), font, 0.5, (255,255,255),1)
            
            if name_of_person == "Unknown face":
                print("Alert Unknown Person Detected!!!")
        
        #display the video
        cv2.imshow("Webcam Video",current_frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        fps.update()
    
    fps.stop()
    print("Elasped time: {:.2f}".format(fps.elapsed()))
    print("[Approx. FPS: {:.2f}".format(fps.fps()))

    webcam_video_stream.release()
    cv2.destroyAllWindows() 