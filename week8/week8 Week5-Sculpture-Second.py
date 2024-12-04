#


import cv2
from cv2 import ellipse
from dorothy import Dorothy
import numpy as np

dot = Dorothy(width=900, height=900)

class MySketch:

    thumbnail_size1 = (25, 25) 
    dataset1 = dot.get_images("E:\\vscode\\STEM-4-Creatives-24-25\\week8\\picture02", thumbnail_size1)

    thumbnail_size2 = (50, 50)  
    dataset2 = dot.get_images("E:\\vscode\\STEM-4-Creatives-24-25\\week8\\picture03", thumbnail_size2)

    thumbnail_size3 = (70, 70)  
    dataset3 = dot.get_images("E:\\vscode\\STEM-4-Creatives-24-25\\week8\\picture04", thumbnail_size3)

    thumbnail_size4 = (60, 60) 
    dataset4 = dot.get_images("E:\\vscode\\STEM-4-Creatives-24-25\\week8\\picture05", thumbnail_size4)

    def __init__(self):
        
        dot.start_loop(self.setup, self.draw)  

    def setup(self):
        print("setup")

    def draw(self):
        
        self.draw_first_set()
        self.draw_second_set()
        self.draw_third_set()
        self.draw_fourth_set()
        self.draw_eyes()

    def draw_first_set(self):
        num_faces1 = 20
        for i in range(num_faces1):
            new_canvas = dot.get_layer()
            index = np.random.randint(len(self.dataset1))
            to_paste = self.dataset1[index]
            coords = (300, 300)
            dot.paste(new_canvas, to_paste, coords)
            
            period = 50
            factor = (dot.frame % period) / period
            theta = factor * 2 * np.pi
            rotate = np.array([[np.cos(theta), -np.sin(theta)],
                               [np.sin(theta), np.cos(theta)]])
            
            origin = (dot.width // 2, dot.height // 2)
            new_canvas = dot.transform(new_canvas, rotate, origin)
            dot.draw_layer(new_canvas)

    def draw_second_set(self):
        num_faces2 = 20
        for i in range(num_faces2):
            new_canvas = dot.get_layer()
            index = np.random.randint(len(self.dataset2))
            to_paste = self.dataset2[index]
            coords = (325, 325)  
            dot.paste(new_canvas, to_paste, coords)
            
            period = 50
            factor = (dot.frame % period) / period
            theta = factor * 2 * np.pi
            rotate = np.array([[np.cos(theta), -np.sin(theta)],
                               [np.sin(theta), np.cos(theta)]])
            
            origin = (dot.width // 2, dot.height // 2)
            new_canvas = dot.transform(new_canvas, rotate, origin)
            dot.draw_layer(new_canvas)

    def draw_third_set(self):
        num_faces3 = 20
        for i in range(num_faces3):
            new_canvas = dot.get_layer()
            index = np.random.randint(len(self.dataset3))
            to_paste = self.dataset3[index]
            coords = (200, 200)  
            dot.paste(new_canvas, to_paste, coords)
            
            period = 50
            factor = (dot.frame % period) / period
            theta = factor * 2 * np.pi
            rotate = np.array([[np.cos(theta), -np.sin(theta)],
                               [np.sin(theta), np.cos(theta)]])
            
            origin = (dot.width // 2, dot.height // 2)
            new_canvas = dot.transform(new_canvas, rotate, origin)
            dot.draw_layer(new_canvas)
    
    def draw_fourth_set(self):
        num_faces4 = 20
        for i in range(num_faces4):
            new_canvas = dot.get_layer()
            index = np.random.randint(len(self.dataset4))
            to_paste = self.dataset4[index]
            coords = (250, 250)
            dot.paste(new_canvas, to_paste, coords)
            
            period = 50
            factor = (dot.frame % period) / period
            theta = factor * 2 * np.pi
            rotate = np.array([[np.cos(theta), -np.sin(theta)],
                               [np.sin(theta), np.cos(theta)]])
            
            origin = (dot.width // 2, dot.height // 2)
            new_canvas = dot.transform(new_canvas, rotate, origin)
            dot.draw_layer(new_canvas)



    def draw_eyes(self):
        eye_count = 12  
        eye_size = 40  
        eye_distance = 100 
        new_canvas = dot.get_layer()

        for i in range(eye_count):
            angle = np.random.uniform(0, 2 * np.pi)
            x = int(dot.width // 2 + eye_distance * np.cos(angle))
            y = int(dot.height // 2 + eye_distance * np.sin(angle))

            ellipse(new_canvas, (x, y), (eye_size // 2, eye_size // 4), 0, 0, 360, (255, 255, 255), -1)  
            ellipse(new_canvas, (x, y), (eye_size // 8, eye_size // 8), 0, 0, 360, (0, 0, 0), -1)  

        period = 100
        factor = (dot.frame % period) / period
        theta = factor * 2 * np.pi
        rotate = np.array([[np.cos(theta), -np.sin(theta)],
                           [np.sin(theta), np.cos(theta)]])
        
        origin = (dot.width // 2, dot.height // 2)
        new_canvas = dot.transform(new_canvas, rotate, origin)
        dot.draw_layer(new_canvas)

MySketch()