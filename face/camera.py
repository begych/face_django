import cv2


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
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()


class VideoCamera_2(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(2)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# import cv2
# import face_recognition
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
#         ret, image = self.video.read()
#         if ret:
#             small_image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
#             face_locations0 = face_recognition.face_locations(small_image)
#
#             for index, (x, y, w, h) in enumerate(face_locations0):
#                 x *= 2
#                 y *= 2
#                 w *= 2
#                 h *= 2
#                 faces = image[x:w, h:y]
#                 # pil_img = Image.fromarray(faces)
#                 # pil_img.save(f"Faces_in/{count}_face_img.jpg")
#                 cv2.imwrite('face_recognize/Faces_in/face_in_' + str(index) + '.jpg', faces)
#                 cv2.rectangle(image, (h, x), (y, w), (0, 0, 255), 2)
#             # cv2.imshow('Cam 0', image)
#
#             ret, jpeg = cv2.imencode('.jpg', image)
#         return jpeg.tobytes()
#
#
# class VideoCamera_2(object):
#     def __init__(self):
#         # Using OpenCV to capture from device 0. If you have trouble capturing
#         # from a webcam, comment the line below out and use a video file
#         # instead.
#         self.video = cv2.VideoCapture(2)
#         # If you decide to use video.mp4, you must have this file in the folder
#         # as the main.py.
#         # self.video = cv2.VideoCapture('video.mp4')
#
#     def __del__(self):
#         self.video.release()
#
#     def get_frame(self):
#         ret, image = self.video.read()
#         if ret:
#             small_image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
#             face_locations0 = face_recognition.face_locations(small_image)
#
#             for index, (x, y, w, h) in enumerate(face_locations0):
#                 x *= 2
#                 y *= 2
#                 w *= 2
#                 h *= 2
#                 faces = image[x:w, h:y]
#                 # pil_img = Image.fromarray(faces)
#                 # pil_img.save(f"Faces_in/{count}_face_img.jpg")
#                 cv2.imwrite('face_recognize/Faces_in/face_in_' + str(index) + '.jpg', faces)
#                 cv2.rectangle(image, (h, x), (y, w), (0, 0, 255), 2)
#             # cv2.imshow('Cam 0', image)
#
#             ret, jpeg = cv2.imencode('.jpg', image)
#         return jpeg.tobytes()
#
#
# def gen(camera):
#     while True:
#         frame = camera.get_frame()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
