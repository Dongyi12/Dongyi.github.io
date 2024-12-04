from dorothy import Dorothy
from cv2 import circle
import random

dot = Dorothy(width=1200, height=800)  # Increase canvas size

class MySketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw)

    def setup(self):
        print("setup")
        self.num_circles = 100  # Initial number of circles
        self.min_radius = 3
        self.max_radius = 10
        self.circles = []

        # Generate initial random circles, ensuring no overlap
        for _ in range(self.num_circles):
            self.add_new_circle()

    def add_new_circle(self):
        while True:
            radius = random.randint(self.min_radius, self.max_radius)
            x = random.randint(radius, dot.width - radius)
            y = random.randint(radius, dot.height - radius)
            color = random.choice([dot.lavender, dot.aqua, dot.fuchsia, dot.blueviolet])
            new_circle = [x, y, radius, color]
            if not self.is_overlapping(new_circle):
                self.circles.append(new_circle)
                break

    def is_overlapping(self, new_circle):
        x_new, y_new, radius_new, _ = new_circle
        for x, y, radius, _ in self.circles:
            distance = ((x - x_new) ** 2 + (y - y_new) ** 2) ** 0.5
            if distance < radius + radius_new:
                return True
        return False

    def draw(self):
        dot.background((255, 0, 100))

        # Generate new circles at intervals
        if dot.frame % 10 == 0:
            self.add_new_circle()

        # Update and draw all circles, making them move smoothly towards the mouse
        for i, circle_data in enumerate(self.circles):
            x, y, radius, color = circle_data
            new_x = x + (dot.mouse_x - x) * 0.1  # Further reduce step size for smoother movement
            new_y = y + (dot.mouse_y - y) * 0.1
            temp_circle = [new_x, new_y, radius, color]

            # Check if the new position overlaps
            if not self.is_overlapping(temp_circle):
                self.circles[i][0] = new_x
                self.circles[i][1] = new_y

            new_x = x + (dot.mouse_x - x) * 0.1  # Further reduce step size for smoother movement
            new_y = y + (dot.mouse_y - y) * 0.1
            circle(dot.canvas, (int(self.circles[i][0]), int(self.circles[i][1])), radius, color, -1)

MySketch()