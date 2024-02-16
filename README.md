<h1>Fire Detection using YOLOv8</h1>
    <p>
        This Python project utilizes the YOLOv8 object detection model to detect fires in real-time using either a
        webcam or a video file as input. When a fire is detected, an alarm sound is triggered to alert the user. The
        alarm has a cooldown period, during which it will not be triggered again if additional fires are detected.
        This project assumes that you have already trained the YOLOv8 model with around 50 images, each repeated 1500
        times, specifically for fire detection. 
    </p> 
<h2>Dependencies</h2>  
    <p>    
        Before running the project, make sure you have the following dependencies installed: 
    </p> 
    <ul> 
        <li>
            <a href="https://pypi.org/project/opencv-python/">OpenCV</a>: Used for image processing and video capture.
        </li>
        <li>
            <a href="https://pypi.org/project/pygame/">Pygame</a>: Used to play the alarm sound.
        </li>
        <li>
            <a href="https://pypi.org/project/cvzone/">cvzone</a>: Used for drawing text and rectangles on the image.
        </li>
        <li>
            <a href="https://pypi.org/project/ultralytics/">Ultralytics</a>: Used to load the YOLOv8 model and perform
            real-time object detection.
        </li> 
    </ul>
    <p>
        Install the dependencies using the following command:
    </p>
    <pre><code>pip install -r requirements.txt</code></pre>
    <pre><code>pip install opencv-python pygame cvzone ultralytics</code></pre>
    

 <h2>Getting Started</h2>
    <ol>
        <li>
            Clone or download the YOLOv8 model repository and place the trained <code>fire.pt</code> file inside the
            project directory.
        </li>
        <li>
            Replace <code>'alarm_sound.wav'</code> with the path to your desired alarm sound file. Make sure the file is
            in WAV format.
        </li>
        <li>
            If you want to run the project using a webcam, set <code>cap = cv2.VideoCapture(0)</code>. For a video file,
            set <code>cap = cv2.VideoCapture('fire4.mp4')</code>.
        </li>
    </ol>

   <h2>Usage</h2>
    <ol>
        <li>
            Run the Python script containing the provided code to start the fire detection system.
        </li>
        <li>
            The program will use the selected video source (webcam or video file) to capture frames.
        </li>
        <li>
            When a fire is detected with a confidence level greater than 50%, a rectangle will be drawn around the
            detected fire, and the label along with the confidence percentage will be displayed on the screen.
        </li>
        <li>
            The alarm sound will be played when a fire is detected, provided the alarm is not already triggered.
        </li>
        <li>
            The alarm will be in a cooldown state for a defined duration (default: 10 seconds) after being triggered
            once. During this time, the alarm will not be triggered even if more fires are detected.
        </li>
        <li>
            After the cooldown duration has passed, the alarm will be ready to trigger again if another fire is
            detected.
        </li>
    </ol>

 <h2>Note</h2>
    <ul>
        <li>
            The provided code assumes that you have trained the YOLOv8 model with a dataset consisting of approximately
            50 fire images, each repeated 1500 times. Make sure the model is well-trained for accurate fire detection.
        </li>
        <li>
            The confidence threshold for fire detection is set to 50%. You can adjust this value based on your
            requirements in the code: <code>if confidence &gt; 50</code>.
        </li>
        <li>
            The cooldown duration is set to 10 seconds by default. You can modify this value by changing the
            <code>cooldown_duration</code> variable in the code.
        </li>
        <li>
            The program will continue to run until you manually stop it. Press 'Ctrl + C' in the terminal or close the
            image window to terminate the execution.
        </li>
    </ul>

 <h2>Credits</h2>
    <ul>
        <li>
            The YOLOv8 model implementation is based on the Ultralytics library (
            <a href="https://github.com/ultralytics/yolov5">https://github.com/ultralytics/yolov5</a>).
        </li>
        <li>
            The cvzone library (<a href="https://github.com/cvzone/cvzone">https://github.com/cvzone/cvzone</a>) is used
            for drawing text and rectangles on the image.
        </li>
    </ul>

 <h2>Disclaimer</h2>
    <p>
        This fire detection system is intended for educational and experimental purposes only. It may not be suitable
        for critical or high-stakes applications. Always use professional and reliable fire detection systems for
        real-world scenarios to ensure the safety of life and property. The author is not responsible for any misuse or
        consequences of using this project.
    </p>
