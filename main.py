import cv2
import tkinter as tk
from PIL import Image, ImageTk
import pyttsx3

THRESHOLD = 0.55
INPUT_WIDTH = 940
INPUT_HEIGHT = 580
OUTPUT_WIDTH = 940
OUTPUT_HEIGHT = 580

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, INPUT_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, INPUT_HEIGHT)

classNames= []
classFile = 'coco.names'
with open(classFile,'rt') as f:
    classNames=[line.rstrip() for line in f]

configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

engine = pyttsx3.init()

class VideoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title(".")
        self.root.configure(bg="cyan")
        self.create_widgets()

    def create_widgets(self):
        self.img = ImageTk.PhotoImage(Image.open("logo.png"))
        self.lbl_image = tk.Label(self.root, image=self.img,bg="cyan")
        self.lbl_image.pack()

        # Add a label indicating that object detection is being performed
        self.lbl_heading = tk.Label(self.root, text="Object Detection Mini Project", font=("TimesNewRoman", 34),foreground="indigo",bg="cyan")
        self.lbl_heading.pack()

        self.canvas = tk.Canvas(self.root, width=OUTPUT_WIDTH, height=OUTPUT_HEIGHT)
        self.canvas.pack()

        self.btn_stop = tk.Button(self.root, text="Stop", command=self.stop_video,width=10,font=("TimesNewRoman", 24),foreground="blue",bg="powderblue")
        self.btn_stop.pack(pady=10)

    def stop_video(self):
        self.root.destroy()

    def update_frame(self, frame):
        self.frame = cv2.resize(frame, (OUTPUT_WIDTH, OUTPUT_HEIGHT))
        self.photo = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.photo = ImageTk.PhotoImage(image=Image.fromarray(self.photo))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

root = tk.Tk()
app = VideoGUI(root)

while True:
    success, img = cap.read()
    img = cv2.resize(img, (INPUT_WIDTH, INPUT_HEIGHT))
    classIds, confs, bbox = net.detect(img, confThreshold=THRESHOLD)

    if len(classIds) != 0:
        for classId, confidence, box in zip(classIds.flatten(),confs.flatten(),bbox):
            label = classNames[classId-1].upper()
            cv2.rectangle(img, box, color=(0,255,0), thickness=2)
            cv2.putText(img, label, (box[0]+10, box[1]+30), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            cv2.putText(img, str(round(confidence*100,2)), (box[0]+200, box[1]+30), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)

            engine.say(label)
            engine.runAndWait()

    app.update_frame(img)
    root.update()

    if cv2.waitKey(1) == 27 or not tk._default_root:  # Check if "ESC" key has been pressed or GUI window is closed
        break

cap.release()
cv2.destroyAllWindows()
