How It Works:
OpenCV and FaceMeshDetector:

The game uses FaceMeshDetector through OpenCV to detect the face and key facial landmarks (like eyes, nose) to track eye movement.
FaceMesh is a method used to detect and track the shape of the face, providing important data such as the distance between eyes, which is used to detect blinks.

Blink Detection:

When the eyes close (a blink), it is detected by comparing the distance between specific points on the face.
The average ratio between vertical and horizontal distances across the eye is used to determine if the user has blinked.
If the average ratio falls below a threshold (indicating that the eyes are closed), the blink is counted.

Tracking and Action:

The game calculates the interval between blinks by comparing the time between consecutive blinks. This is done by measuring the difference between the current blink's time and the previous blink's time.
Interval: This is the time between two blinks. It's measured with high precision and displayed in the UI in seconds with nanosecond precision.

UI Functionality:

The game displays a ball that moves along a star-shaped path on the screen. The ball moves around the path, and the user must track it with their eyes.
The blink count and blink intervals are shown on the screen as labels, so users can monitor their progress.

How the Game Plays:
The player is shown a star path consisting of 5 points, and a red ball moves along these points.
As the user blinks, the game tracks the blink count and calculates the interval (time difference between blinks).
The ball moves along the star path, and the game ends after 10 seconds. During this time, the player can see how many blinks they've made and the time intervals between each blink.

Main Features:

Blink Counter: Counts the number of blinks during the game session.
Blink Interval Display: Displays the time interval between consecutive blinks with nanosecond precision.
Star Path Animation: The ball moves along a star-shaped path that the user needs to follow with their eyes.
Real-Time Feedback: Users get real-time feedback on their blink count and intervals.#   E y e - B l i n k - C o u n t  
 