import cv2
import numpy as np
import random
from cv2 import circle
from dorothy import Dorothy

dot = Dorothy()

class MySketch:
    
    def __init__(self):
        dot.start_loop(self.setup, self.draw)

    def setup(self):
        print("setup")
        self.camera = cv2.VideoCapture(0)
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
        self.nose_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_mcs_nose.xml")
        self.mouth_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_mcs_mouth.xml")

        self.width = 640
        self.height = 480

        self.threshold = 50
        self.window_size = 50
        self.buffer = np.zeros((self.window_size, dot.height, dot.width, 3)).astype(dtype=np.uint8)  # Modified to 3 channels
        self.model = self.buffer[0]
        self.write_ptr = 0

    def draw(self):
        success, camera_feed = self.camera.read()
        if success:
            camera_feed = cv2.resize(camera_feed, (self.width, self.height))
            camera_feed = cv2.cvtColor(camera_feed, cv2.COLOR_BGR2RGB)
            camera_feed_grayscale = cv2.cvtColor(camera_feed, cv2.COLOR_RGB2GRAY)
            faces = self.face_cascade.detectMultiScale(camera_feed_grayscale, 1.1, 4)

            for face_x, face_y, face_w, face_h in faces:
                cv2.ellipse(camera_feed,
                            (face_x + face_w // 2, face_y + face_h // 2),
                            (face_w // 4, face_h // 4),
                            0, 0, 360,
                            (0, 255, 0), 2)
            
                

            # Create a white background image
            background_height = self.height + 200  
            background_width = self.width + 200  
            white_background = np.full((background_height, background_width, 3), 255, dtype=np.uint8)

            # Cut the camera feed into six sections
            Tonytype_parts = []  # 定义为列表
            Tonytype_height = self.height // 3
            Tonytype_width = self.width // 2

            positions = [
                (0, 0),  # 左上
                (2 * Tonytype_height, 0),  # 左下
                (Tonytype_height, Tonytype_width),  # 中间上
                (2 * Tonytype_height, Tonytype_width),  # 中间下
                (0, 2 * Tonytype_width),  # 右上
                (Tonytype_height, 2 * Tonytype_width)  # 右下
            ]

            for i in range(3):
                for j in range(2):
                    part = camera_feed[i * Tonytype_height:(i + 1) * Tonytype_height,
                                       j * Tonytype_width:(j + 1) * Tonytype_width]
                    Tonytype_parts.append(part)  # 将切割的部分添加到列表中

            # 随机重叠并放置在白色背景上
            for part, (y_offset, x_offset) in zip(Tonytype_parts, positions):
                y_offset += random.randint(-50, 50)
                x_offset += random.randint(-50, 50)

                # 确保偏移量在合理范围内
                y_offset = max(0, min(y_offset, background_height - Tonytype_height))
                x_offset = max(0, min(x_offset, background_width - Tonytype_width))

                white_background[y_offset:y_offset + part.shape[0],
                                 x_offset:x_offset + part.shape[1]] = part

            dot.canvas = white_background

MySketch()