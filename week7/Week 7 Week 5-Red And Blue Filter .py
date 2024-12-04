import cv2
from dorothy import Dorothy
import numpy as np

dot = Dorothy()

class MySketch:

    def __init__(self):
        dot.start_loop(self.setup, self.draw)  

    def setup(self):
        print("setup")
        self.camera = cv2.VideoCapture(0)
        self.threshold = 50
        self.window_size = 50
        self.buffer = np.zeros((self.window_size, dot.height, dot.width, 3)).astype(dtype=np.uint8)  # Modified to 3 channels
        self.model = self.buffer[0]
        self.write_ptr = 0
    
    def draw(self):
        success, camera_feed = self.camera.read()
        if success:
            camera_feed = cv2.resize(camera_feed, (dot.width, dot.height))
            hsv_image = cv2.cvtColor(camera_feed, cv2.COLOR_BGR2HSV)
            
            # Converting model images to HSV colour space
            model_hsv = cv2.cvtColor(self.model, cv2.COLOR_BGR2HSV)
            
            diff = cv2.absdiff(hsv_image, model_hsv)
            diff_gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)  
            
            thresholded = cv2.threshold(diff_gray, self.threshold, 255, cv2.THRESH_BINARY)[1]
            
            # Creating red and blue light effects
            red_blue_effect = np.zeros_like(camera_feed)
            red_blue_effect[:, :, 0] = thresholded  
            red_blue_effect[:, :, 2] = thresholded  
            
            # Change the black part to red
            red_blue_effect[np.where((red_blue_effect == [0, 0, 0]).all(axis=2))] = [0, 0, 255]
            
            self.model = np.mean(self.buffer, axis=0).astype(dtype=np.uint8)
            self.write_ptr = (self.write_ptr + 1) % self.window_size
            self.buffer[self.write_ptr] = camera_feed

            dot.canvas = red_blue_effect
        
MySketch()