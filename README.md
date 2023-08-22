# Object Detection 

This is a simple object detection application built using OpenCV and Tkinter, which allows you to perform real-time object detection using a camera feed.

## Features

- Real-time object detection using a pre-trained model.
- Graphical user interface (GUI) using Tkinter.
- Object labels and confidence scores displayed on the GUI.
- Text-to-speech feedback for detected object labels.

## Requirements

- Python 3.x
- OpenCV (`opencv-python`)
- Tkinter (usually included with Python installations)
- Pillow (`Pillow`)
- Pyttsx3 (`pyttsx3`)

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/DeekshaaGatty/ObjectDetection.git
    cd ObjectDetection
    ```

2. Install the required packages

3. Run the application:

    ```bash
    python main.py
    ```

## Usage

- Upon running the application, a GUI window will appear displaying the camera feed.
- Detected objects will be labeled on the video frame along with confidence scores.
- Press the "Stop" button on the GUI to exit the application.

## Configuration

- You can adjust the `THRESHOLD`, `INPUT_WIDTH`, and `INPUT_HEIGHT` constants in `main.py` to customize object detection parameters.
- Make sure to have the correct paths for model configuration (`configPath`), weights (`weightsPath`), and class names (`classFile`) in the script.

## Credits

- The pre-trained model used in this project is based on the COCO dataset.
- Class names used in the project are derived from the COCO dataset classes.

Feel free to modify and extend this project according to your needs. If you have any questions or suggestions, please create an issue in this repository. Happy coding!
