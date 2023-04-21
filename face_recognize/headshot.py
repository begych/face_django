import shutil

import cv2
import face_recognition
import os
import pickle5 as pickle
from .config import host, user, password, db_name
import pymysql

from face.models import Person


def FaceAdd(username, id):

    # with open("face_recognize/Data/database.pickle", "rb") as f:
    #     database = pickle.load(f)

    database = {}

    name = username
    person_id = id
        # input("Name: ")

    os.mkdir(f"face_recognize/Photo's_Data/{name}")


    cap = cv2.VideoCapture(0)

    encodings = []
    count = 0
    frame_id = 0
    while True:
        ret, frame = cap.read()
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        multiplier = fps * 0.5
        # print('[+]', fps)
        if ret:
            frame_id += 1
            print(frame_id)
            if frame_id % multiplier == 0:
                print(count)

                cv2.imwrite(f"face_recognize/Photo's_Data/{name}/{count}.jpg", frame)

                face_locations = face_recognition.face_locations(frame)
                face_encodings = face_recognition.face_encodings(frame, face_locations)[0]

                encodings.append(face_encodings)

                count = count + 1

        cv2.imshow("Video", frame)
        if cv2.waitKey(1) & (count == 10):
            # print(encodings)
            break

    data = {"name": name, "encodings": encodings}
    database[len(database)] = data
    with open(f"face_recognize/Data/database.pickle", "wb") as file:
        file.write(pickle.dumps(database))

    shutil.copy2(f"/home/mtmerkz-10/PycharmProjects/face_django/face_recognize/Photo's_Data/{str(username)}/1.jpg" ,
                 f"/home/mtmerkz-10/PycharmProjects/face_django/face_recognize/KnownFaces/{str(person_id)}.jpg"
                 )

    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("successfully connected....")
        print("#" * 20)

        try:
            with connection.cursor() as cursor:

                update_query = "UPDATE `face_person` SET  " \
                               "image = %s WHERE id = %s;"
                val = (f"{str(person_id)}.jpg", str(person_id))
                cursor.execute(update_query, val)
                connection.commit()

        finally:
            connection.close()

    except Exception as ex :
        print("connection refused....")
        print(ex)
    cap.release()
    cv2.destroyAllWindows()

# FaceAdd("Azamat-Yagmurow-1")