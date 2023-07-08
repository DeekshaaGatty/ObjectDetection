# ObjectDetection
Python project that utilises OpenCV to detect objects in real time on a video feed, displays the findings in a GUI, and outputs the labels of the objects it detects audibly.

Explanation of the working of the project:

1. The script uses the webcam as the video source and captures frames using `cv2.VideoCapture`.

2. The frames are resized to the desired input dimensions (`INPUT_WIDTH` and `INPUT_HEIGHT`).

3. The pre-trained model for object detection is loaded using `cv2.dnn_DetectionModel`.

4. The model is configured with input settings such as size, scale, mean, and swapRB.

5. The script initializes the text-to-speech engine using `pyttsx3.init()`.

6. A GUI window is created using Tkinter, with labels, buttons, and a canvas for displaying the video.

7. Inside a while loop, frames are continuously read from the video capture.

8. Object detection is performed on each frame using the loaded model and the `net.detect` method. Class IDs, confidences, and bounding boxes are obtained.

9. The detected objects are iterated over, and bounding boxes and labels are drawn on the frame using OpenCV.

10. The script uses the text-to-speech engine to say the label of each detected object.

11. The frame is updated in the GUI canvas using the `app.update_frame` method.

12. The GUI window is updated using `root.update()` to show the updated frame and respond to user interactions.

13. The while loop continues until the "ESC" key is pressed or the GUI window is closed.

14. Once the loop is exited, the video capture is released using `cap.release()` and any remaining OpenCV windows are closed using `cv2.destroyAllWindows()`.

Overall, the script continuously captures frames, performs object detection, updates the GUI with bounding boxes and labels, and provides audio output of the detected objects in real-time.

Note: In __main.py__ replace the file __logo.png__ with the file name that contains the logo you designed for your object detection application.
