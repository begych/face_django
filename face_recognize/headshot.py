import cv2
import face_recognition
import os
import pickle5 as pickle


def FaceAdd(username, id):

    with open("face_recognize/Data/database.pickle", "rb") as f:
        database = pickle.load(f)

    # database = {}

    name = username
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

    cap.release()
    cv2.destroyAllWindows()

# FaceAdd("Azamat-Yagmurow-1")