# import cv2
#
#
# class VideoCamera(object):
#     def __init__(self):
#         # Using OpenCV to capture from device 0. If you have trouble capturing
#         # from a webcam, comment the line below out and use a video file
#         # instead.
#         self.video = cv2.VideoCapture(0)
#         # If you decide to use video.mp4, you must have this file in the folder
#         # as the main.py.
#         # self.video = cv2.VideoCapture('video.mp4')
#
#     def __del__(self):
#         self.video.release()
#
#     def get_frame(self):
#         success, image = self.video.read()
#         # We are using Motion JPEG, but OpenCV defaults to capture raw images,
#         # so we must encode it into JPEG in order to correctly display the
#         # video stream.
#         ret, jpeg = cv2.imencode('.jpg', image)
#         return jpeg.tobytes()
#
#
# def gen(camera):
#     while True:
#         frame = camera.get_frame()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

import cv2
import face_recognition

class VideoCamera(object):

    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')


    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        ret, face_locations = face_recognition.face_locations(image)

        for index, (x, y, w, h) in enumerate(face_locations):
            # x *= 4
            # y *= 4
            # w *= 4
            # h *= 4
            # faces = image[x:w, h:y]
            # pil_img = Image.fromarray(faces)
            # pil_img.save(f"Faces_in/{count}_face_img.jpg")
            # cv2.imwrite('Faces_in/face_in_' + str(index) + '.jpg', faces)
            cv2.rectangle(image, (h, x), (y, w), (0, 0, 255), 2)
        # cv2.imshow('Cam 0', image)

        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
