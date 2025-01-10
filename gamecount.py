import cv2
import tkinter as tk
import math
import time
from cvzone.FaceMeshModule import FaceMeshDetector

class EyeTrainingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Eye Tracking Star Game")
        self.root.geometry("800x600")
        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()

        # Initialize variables
        self.ball = None
        self.mode = "star"  # Fixed mode
        self.ball_size = 30
        self.speed = 0.01  # Reduced speed for slower movement
        self.t = 0
        self.direction = 1  # 1 for forward, -1 for reverse

        # Timer and Blink Counter
        self.start_time = time.time()
        self.blink_counter = 0
        self.counter = 0
        self.ratio_list = []
        self.blink_intervals = []  # List to store intervals between blinks
        self.last_blink_time = time.time()  # Last blink timestamp

        # Initialize OpenCV and face detector
        self.cap = cv2.VideoCapture(0)
        self.detector = FaceMeshDetector(maxFaces=1)

        # Draw the path and ball
        self.draw_path()
        self.ball = self.canvas.create_oval(0, 0, self.ball_size, self.ball_size, fill="red")

        # Add blink counter display
        self.blink_label = tk.Label(root, text="Blink Count: 0", font=("Arial", 14))
        self.blink_label.pack()

        # Add blink interval display
        self.interval_label = tk.Label(root, text="Blink Interval: 0", font=("Arial", 14))
        self.interval_label.pack()

        # Start animation and blink counter
        self.animate()
        self.update_blink_counter()

    def draw_path(self):
        self.canvas.delete("path")
        if self.mode == "star":
            # Define the points of the star
            radius = 200
            center_x, center_y = 400, 300
            points = []

            for i in range(5):
                angle = math.radians(i * 144)
                x = center_x + radius * math.cos(angle)
                y = center_y + radius * math.sin(angle)
                points.append((x, y))

            # Draw the star shape
            for i in range(len(points)):
                self.canvas.create_line(
                    points[i][0], points[i][1], 
                    points[(i + 1) % len(points)][0], points[(i + 1) % len(points)][1],
                    fill="black", width=5, tags="path"
                )

    def animate(self):
        # Exit game after 10 seconds
        elapsed_time = time.time() - self.start_time
        if elapsed_time > 10:
            print(f"Game Over! Total Blink Count: {self.blink_counter}")
            self.cap.release()
            self.root.destroy()
            return

        if self.mode == "star":
            num_points = 5
            radius = 200
            center_x, center_y = 400, 300
            points = []

            # Calculate the star points
            for i in range(num_points):
                angle = math.radians(i * 144)
                x = center_x + radius * math.cos(angle)
                y = center_y + radius * math.sin(angle)
                points.append((x, y))

            # Update progress
            self.t += self.direction * self.speed
            progress = self.t

            # Reverse direction if end of path is reached
            if progress >= num_points or progress < 0:
                self.direction *= -1
                progress = max(0, min(progress, num_points - 1))

            # Determine current segment and interpolate position
            segment = int(progress) % num_points
            segment_progress = progress - segment

            # Get the two points for the current segment
            x1, y1 = points[segment]
            x2, y2 = points[(segment + 1) % num_points]

            # Interpolate position
            x = x1 + (x2 - x1) * segment_progress
            y = y1 + (y2 - y1) * segment_progress

            self.canvas.coords(
                self.ball,
                x - self.ball_size / 2,
                y - self.ball_size / 2,
                x + self.ball_size / 2,
                y + self.ball_size / 2,
            )

        self.root.after(16, self.animate)

    def update_blink_counter(self):
        success, img = self.cap.read()
        if not success:
            print("Error: Failed to grab frame.")
            return

        img, faces = self.detector.findFaceMesh(img, draw=False)

        if faces:
            face = faces[0]
            left_up = face[159]
            left_down = face[23]
            left_left = face[130]
            left_right = face[243]
            length_ver, _ = self.detector.findDistance(left_up, left_down)
            length_hor, _ = self.detector.findDistance(left_left, left_right)

            ratio = int((length_ver / length_hor) * 100)
            self.ratio_list.append(ratio)
            if len(self.ratio_list) > 3:
                self.ratio_list.pop(0)
            ratio_avg = sum(self.ratio_list) / len(self.ratio_list)

            if ratio_avg < 35 and self.counter == 0:
                self.blink_counter += 1
                self.blink_label.config(text=f"Blink Count: {self.blink_counter}")

                # Calculate the interval between blinks
                current_blink_time = time.time()
                if self.last_blink_time:
                    interval = current_blink_time - self.last_blink_time
                    self.blink_intervals.append(interval)

                    # Display blink interval with nanosecond precision
                    self.interval_label.config(text=f"Blink Interval: {interval:.9f} seconds")

                    print(f"Blink {self.blink_counter}: Interval: {interval:.9f} seconds")

                self.last_blink_time = current_blink_time
                self.counter = 1

            if self.counter != 0:
                self.counter += 1
                if self.counter > 10:
                    self.counter = 0

        self.root.after(25, self.update_blink_counter)

if __name__ == "__main__":
    root = tk.Tk()
    game = EyeTrainingGame(root)
    root.mainloop()
