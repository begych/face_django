import cv2
import face_recognition
import pickle5 as pickle
import os
import shutil

from face.models import Get_In, Get_Out

with open("Data/database.pickle", "rb") as f:
    database = pickle.load(f)

t = 0

# gun=str(date)
# name=str(person_id.name)
# slug=gun+ '-' +name
#try
# get_in_create=Get_In.objects.create(get_in=date, slug=slug, count=1,person_id_id=name_id)
# get_in_create.save()
# except
#if Get_in_person_id.date -.get out bary?
#      count+=1
#      slug+=str(count)
#      get_in_create=Get_In.objects.create(get_in=date, slug=slug, count=1,person_id_id=name_id)
#      get_in_create.save()
#else?
#    pass


while True:
    try:
        if len(os.listdir("Faces_out")) != 0:
            lenlist = len(os.listdir("Faces_out"))
            print('#' * 20)

            for index in range(len(os.listdir("Faces_out"))):
                shutil.move("Faces_out/"+str(os.listdir('Faces_out')[0]),"FacesDir_out/"+str(os.listdir('Faces_out')[0]))

            print("Faces_out to FacesDir_out")


            # for unknown_face_index in range(len(os.listdir("FacesDir_in"))):
            while len(os.listdir("FacesDir_out")) != 0 :

                print(os.listdir("FacesDir_out")[0])

                unknown_face = cv2.imread("FacesDir_out/"+str(os.listdir("FacesDir_out")[0]))
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
                        shutil.move("FacesDir_out/" + str(os.listdir('FacesDir_out')[0]),
                                    "DetectedFaces/" + str(os.listdir('FacesDir_out')[0]))


                if t == 0 :
                    shutil.move("FacesDir_out/" + str(os.listdir('FacesDir_out')[0]),
                                "UnknownFaces/" + str(os.listdir('FacesDir_out')[0]))



            print("+++" * 20)
    except:
        continue