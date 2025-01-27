OpenCV and FaceMeshDetector

The game uses FaceMeshDetector from the cvzone library, which is built on top of OpenCV. This tool detects key facial landmarks such as the eyes, nose, and mouth.
FaceMesh is a deep learning model that detects and tracks the shape of the face. It gives us important data like the positions of the eyes, which are essential for detecting blinks.

Blink Detection

Blink detection is achieved by comparing the distance between specific points on the face, such as the left eye's top and bottom eyelids.
The average ratio between the vertical and horizontal distances of the eye is calculated. If this ratio falls below a certain threshold (indicating that the eyes are closed), it is counted as a blink.

Tracking and Action

The game tracks the interval between blinks by measuring the time difference between consecutive blinks.
This interval is displayed with high precision, in seconds and nanoseconds.

UI Functionality

The game features a ball that moves along a star-shaped path on the screen.
The player must track the ball with their eyes. As the player blinks, the game counts the blinks and calculates the interval between each blink.
The blink count and the time intervals between blinks are displayed as labels on the screen for real-time feedback.

How the Game Plays

The player sees a star-shaped path with 5 points on the screen.
A red ball moves along the path.
The player must track the ball with their eyes while blinking.
Each time the player blinks, the game detects the blink and calculates the time interval between consecutive blinks.
The game ends after 10 seconds, and during this time, the player can monitor the blink count and the interval between each blink.

Main Features

Blink Counter: Tracks the number of blinks during the game session.
Blink Interval Display: Displays the time interval between consecutive blinks with nanosecond precision.
Star Path Animation: A red ball moves along a star-shaped path on the screen, which the player must follow with their eyes.
Real-Time Feedback: The user receives feedback on their blink count and intervals as the game progresses.
