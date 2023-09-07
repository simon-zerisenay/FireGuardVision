from ultralytics import YOLO
import cvzone
import cv2
import math  
import pygame  
import time
     
# Initialize pygame for playing sound
pygame.init()

# Load the sound file (replace 'alarm_sound.wav' with the path to your sound file) 
alarm_sound = pygame.mixer.Sound('alarm_sound.wav') 
 
# Running real-time from webcam
cap = cv2.VideoCapture('fire2.mp4')
model = YOLO('fire.pt') 

# Reading the classes
classnames = ['fire']

# Flag to track if the alarm is already triggered
alarm_triggered = False

# Time duration (in seconds) for the alarm cooldown period
cooldown_duration = 10  # Change this to set the cooldown duration

# Initialize the timestamp for cooldown tracking
cooldown_start_time = 0

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (1440, 680))
    result = model(frame, stream=True)

    # Getting bbox, confidence, and class names information to work with
    for info in result:
        boxes = info.boxes
        for box in boxes:
            confidence = box.conf[0]
            confidence = math.ceil(confidence * 100)
            Class = int(box.cls[0])
            if confidence > 50:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 5)
                cvzone.putTextRect(frame, f'{classnames[Class]} {confidence}%', [x1 + 8, y1 + 100],
                                   scale=1.5, thickness=2)

                # Play the alarm sound when fire is detected and the alarm is not already triggered
                if not alarm_triggered:
                    alarm_sound.play()

                    # Set the flag to True to indicate the alarm is triggered
                    alarm_triggered = True

                    # Start the cooldown timer
                    cooldown_start_time = time.time()

    # Check if the cooldown period has passed
    if alarm_triggered and time.time() - cooldown_start_time > cooldown_duration:
        alarm_triggered = False  # Reset the alarm flag

    cv2.imshow('frame', frame)
    cv2.waitKey(1)
