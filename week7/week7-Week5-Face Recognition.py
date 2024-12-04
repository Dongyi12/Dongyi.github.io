import cv2
from cv2 import circle
from dorothy import Dorothy

dot = Dorothy()

class MySketch:
    
    def __init__(self):
        dot.start_loop(self.setup, self.draw)  

    def setup(self):
        print("setup")
        self.camera = cv2.VideoCapture(0)
        self.face_cascade = cv2.CascadeClassifier("week7/data/haarcascade_frontalface_default.xml")
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
        self.nose_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_mcs_nose.xml")
        self.mouth_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_mcs_mouth.xml")

    def draw(self):
        dot.background(dot.black)
        success, camera_feed = self.camera.read()
        if success:
            camera_feed = cv2.resize(camera_feed, (dot.width, dot.height))
            camera_feed = cv2.cvtColor(camera_feed, cv2.COLOR_BGR2RGB)
            camera_feed_grayscale = cv2.cvtColor(camera_feed, cv2.COLOR_RGB2GRAY)
            faces = self.face_cascade.detectMultiScale(camera_feed_grayscale, 1.1, 4)
            
            for face_x, face_y, face_w, face_h in faces:
                face_pixels = camera_feed[face_y:face_y+face_h, face_x:face_x+face_w].copy()
                skip = 12
                downsampled = face_pixels[::skip, ::skip]
                radius = 6
                for i in range(downsampled.shape[0]):
                    for j in range(downsampled.shape[1]):
                        colour = (int(downsampled[j][i][0]), int(downsampled[j][i][1]), int(downsampled[j][i][2]))
                        x = face_x + (i * skip)
                        y = face_y + (j * skip)
                        circle(dot.canvas,
                               center=(x, y), radius=radius,
                               color=colour, thickness=-1)

                # Eyes Recognition
                roi_gray = camera_feed_grayscale[face_y:face_y+face_h, face_x:face_x+face_w]
                roi_color = camera_feed[face_y:face_y+face_h, face_x:face_x+face_w]
                eyes = self.eye_cascade.detectMultiScale(roi_gray)
                for (ex, ey, ew, eh) in eyes:
                    circle(dot.canvas,
                           center=(face_x + ex + ew//2, face_y + ey + eh//2), radius=radius,
                           color=(255, 0, 0), thickness=-1)

                # Nose Recognition
                if not self.nose_cascade.empty():
                    nose = self.nose_cascade.detectMultiScale(roi_gray)
                    for (nx, ny, nw, nh) in nose:
                        circle(dot.canvas,
                               center=(face_x + nx + nw//2, face_y + ny + nh//2), radius=radius,
                               color=(0, 255, 0), thickness=-1)

                # Mouth Recognition
                if not self.mouth_cascade.empty():
                    mouth = self.mouth_cascade.detectMultiScale(roi_gray)
                    for (mx, my, mw, mh) in mouth:
                        circle(dot.canvas,
                               center=(face_x + mx + mw//2, face_y + my + mh//2), radius=radius,
                               color=(0, 0, 255), thickness=-1)

MySketch()