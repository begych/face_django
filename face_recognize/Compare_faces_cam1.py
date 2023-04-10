
import cv2
import face_recognition
import pickle5 as pickle
import os
import shutil

with open("Data/database.pickle", "rb") as f:
    database = pickle.load(f)

t = 0

while True:
    try:
        if len(os.listdir("Faces_in")) != 0:
            lenlist = len(os.listdir("Faces_in"))
            print('#' * 20)

            for index in range(len(os.listdir("Faces_in"))):
                shutil.move("Faces_in/"+str(os.listdir('Faces_in')[0]),"FacesDir_in/"+str(os.listdir('Faces_in')[0]))

            print("Faces_in to FacesDir_in")


            # for unknown_face_index in range(len(os.listdir("FacesDir_in"))):
            while len(os.listdir("FacesDir_in")) != 0 :

                print(os.listdir("FacesDir_in")[0])

                unknown_face = cv2.imread("FacesDir_in/"+str(os.listdir("FacesDir_in")[0]))
                unknown_face_locations = face_recognition.face_locations(unknown_face)
                unknown_face_encodings = face_recognition.face_encodings(unknown_face, unknown_face_locations)[0]

                t = 0

                for index in range(len(database)):
                    data = database[index]
                    known_face_encodings = data['encodings']

                    compare_matches = face_recognition.compare_faces(known_face_encodings, unknown_face_encodings)

                    print(compare_matches)

                    k = 0
                    for match in compare_matches:
                        if match == True  :
                            k += 1


                    if k >= 10 :
                        print("Face_Detected")
                        print(data['name'])
                        t += 1
                        shutil.move("FacesDir_in/" + str(os.listdir('FacesDir_in')[0]),
                                    "DetectedFaces/" + str(os.listdir('FacesDir_in')[0]))


                if t == 0 :
                    shutil.move("FacesDir_in/" + str(os.listdir('FacesDir_in')[0]),
                                "UnknownFaces/" + str(os.listdir('FacesDir_in')[0]))



            print("+++" * 20)
    except:
        continue