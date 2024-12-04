from dorothy import Dorothy
from cv2 import rectangle, ellipse, addWeighted
import numpy as np

dot = Dorothy()
class MySketch:
    
    
    def __init__(self):
        dot.start_loop(self.setup, self.draw)

    def setup(self):
        # Loading audio files using absolute paths
        audio_path = "E:\\vscode\\STEM-4-Creatives-24-25\\week2\\audio\\Week 3 Week 5-Vision.mp3"
        dot.music.start_file_stream(audio_path)
       
        
        # Initialising rounded rectangular parameters
        self.num_rects_left_music = 50 
        self.rect_location_left = np.random.randint(0, [dot.width // 3, dot.height], (self.num_rects_left_music, 2))
        self.rect_rate_left = np.random.randint(1, 7, 100) 
        self.rect_measure_left = np.random.randint(6, 30, (self.num_rects_left_music, 2)) 

        self.num_rects_middle = 50  
        self.rect_positions_middle = np.random.randint(dot.width // 3, 2 * dot.width // 3, (self.num_rects_middle, 2))
        self.rect_speeds_middle = np.random.randint(1, 7, self.num_rects_middle) 
        self.rect_sizes_middle = np.random.randint(7, 30, (self.num_rects_middle, 2))  
        self.num_rects_right = 50 
        self.rect_positions_right = np.random.randint(2 * dot.width // 3, dot.width, (self.num_rects_right, 2))
        self.rect_speeds_right = np.random.randint(1, 7, self.num_rects_right) 
        self.rect_sizes_right = np.random.randint(7, 30, (self.num_rects_right, 2))  

    def draw(self):
        #Translucent layer overlay for trailing effect
        cover_left = dot.get_layer()
        rectangle(cover_left, (0, 0), (dot.width // 3, dot.height), dot.white, -1)
        dot.draw_layer(cover_left, 0.2)

        cover_middle = dot.get_layer()
        rectangle(cover_middle, (dot.width // 3, 0), (2 * dot.width // 3, dot.height), dot.white, -1)
        dot.draw_layer(cover_middle, 0.2)

        cover_right = dot.get_layer()
        rectangle(cover_right, (2 * dot.width // 3, 0), (dot.width, dot.height), dot.white, -1)
        dot.draw_layer(cover_right, 0.2)

        # Updating and drawing rounded rectangles
        for i in range(self.num_rects_left_music):
            pos = self.rect_location_left[i]
            speed = self.rect_rate_left[i]
            amplitude = dot.music.amplitude()
            size = (int(self.rect_measure_left[i][0] * (1 + amplitude * 5)),  
                    int(self.rect_measure_left[i][1] * (1 + amplitude * 5))) 

          
            pos[1] = (pos[1] + speed) % dot.height

            # Update the position of the rectangle so that it is away from the mouse
            mouse_pos = np.array([dot.mouse_x, dot.mouse_y])
            direction = pos - mouse_pos
            distance = np.linalg.norm(direction)
            if distance < 100: 
                direction = direction / distance 
                pos += (direction * speed).astype(int) 

            self.draw_rounded_rect_radius(dot.canvas, pos, size, 5, dot.blueviolet, dot.cyan)

        # Updating and drawing rounded rectangles
        for i in range(self.num_rects_middle):
            pos = self.rect_positions_middle[i]
            speed = self.rect_speeds_middle[i]
            amplitude = dot.music.amplitude()
            size = (int(self.rect_sizes_middle[i][0] * (1 + amplitude * 5)),
                    int(self.rect_sizes_middle[i][1] * (1 + amplitude * 5))) 

            pos[1] = (pos[1] + speed) % dot.height

            # Update the position of the rectangle so that it is away from the mouse 
            mouse_pos = np.array([dot.mouse_x, dot.mouse_y])
            direction = pos - mouse_pos
            distance = np.linalg.norm(direction)
            if distance < 100:  
                direction = direction / distance 
                pos += (direction * speed).astype(int) 

            self.draw_rounded_rect_radius(dot.canvas, pos, size, 5, dot.deeppink, dot.cyan)

        for i in range(self.num_rects_right):
            pos = self.rect_positions_right[i]
            speed = self.rect_speeds_right[i]
            amplitude = dot.music.amplitude()
            size = (int(self.rect_sizes_right[i][0] * (1 + amplitude * 5)), 
                    int(self.rect_sizes_right[i][1] * (1 + amplitude * 5)))  

            pos[1] = (pos[1] + speed) % dot.height

            mouse_pos = np.array([dot.mouse_x, dot.mouse_y])
            direction = pos - mouse_pos
            distance = np.linalg.norm(direction)
            if distance < 100: 
                direction = direction / distance  
                pos += (direction * speed).astype(int)

            self.draw_rounded_rect_radius(dot.canvas, pos, size, 5, dot.crimson, dot.plum)

        if dot.frame == 175:
            dot.stop_record()

    def draw_rounded_rect_radius(self, img, center, size, radius, fill_color, border_color):
        x, y = center
        w, h = size
        # Draw the main rectangle with fill color
        rectangle(img, (x - w//2 + radius, y - h//2), (x + w//2 - radius, y + h//2), fill_color, -1)
        rectangle(img, (x - w//2, y - h//2 + radius), (x + w//2, y + h//2 - radius), fill_color, -1)
        ellipse(img, (x - w//2 + radius, y - h//2 + radius), (radius, radius), 180, 0, 90, fill_color, -1)
        ellipse(img, (x + w//2 - radius, y - h//2 + radius), (radius, radius), 270, 0, 90, fill_color, -1)
        ellipse(img, (x - w//2 + radius, y + h//2 - radius), (radius, radius), 90, 0, 90, fill_color, -1)
        ellipse(img, (x + w//2 - radius, y + h//2 - radius), (radius, radius), 0, 0, 90, fill_color, -1)
        
        # Draw the border with reduced opacity to make it lighter
        temp_layer_border = np.zeros_like(img)
        
        rectangle(temp_layer_border, (x - w//2 + radius, y - h//2), (x + w//2 - radius, y + h//2), border_color, 1)
        rectangle(temp_layer_border, (x - w//2, y - h//2 + radius), (x + w//2, y + h//2 - radius), border_color, 1)
        ellipse(temp_layer_border, (x - w//2 + radius, y - h//2 + radius), (radius, radius), 180, 0, 90, border_color, 1)
        ellipse(temp_layer_border, (x + w//2 - radius, y - h//2 + radius), (radius, radius), 270, 0, 90, border_color, 1)
        ellipse(temp_layer_border, (x - w//2 + radius, y + h//2 - radius), (radius, radius), 90, 0, 90, border_color, 1)
        ellipse(temp_layer_border, (x + w//2 - radius, y + h//2 - radius), (radius, radius), 0, 0, 90, border_color, 1)

        addWeighted(img, 1, temp_layer_border, 0.5, 0, img)

        # Draw the inner cyan rectangle with smooth transition
        inner_w = int(w * 0.5)
        inner_h = int(h * 0.5)
        
        temp_layer = np.zeros_like(img)
        
        rectangle(temp_layer, (x - inner_w // 2, y - inner_h // 2), (x + inner_w // 2, y + inner_h // 2), dot.cyan, -1)
        
        addWeighted(img, 1, temp_layer, 0.5, 0, img)
    
MySketch()