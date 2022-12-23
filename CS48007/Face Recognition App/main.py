import os
from faceRecognition import *
from newPerson import *
from train_model import *



def main():

    value = ''
    encodingsPickle = "encodings.pickle"
 
    while value != 'q':

        value = input('Please enter: \n 1 to Add a New Person \n 2 to Start Remote Monitoring.\n 3 to Delete a Person \n q to Quit \n')

        if value == 'q':
            break
        
        elif value == '1':
            print("Add a New Person")
            name = input('Name: ')
                
            if os.path.isdir("dataset/" + name):
                mod = input('Person Already Exists. \nDo you want to modifty the data? \nY/N?\n')
                if mod == 'Y' or mod == 'y':
                    modifyExistingPerson(name)
                else:
                    continue
            else:
                addPerson(name)
            train_face_model()
            
        elif value == '2':
            print("Remote Monitoring")
            data = pickle.loads(open(encodingsPickle, "rb").read())
            faceRecognition(data["encodings"], data["names"])
            
        elif value == '3':
            print("Delete a Person")
            name = input('Please enter the name of the person you want to delete: ')
            deletePerson(name)
            train_face_model()
            
        else:
            print("Print enter a valid input!")

    



if __name__ == "__main__":

    main()