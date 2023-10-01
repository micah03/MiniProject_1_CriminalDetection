# MiniProject_1_CriminalDetection
Mini Project done in Sem-3 Criminal Detection using Face Recognition in Python

This Python program is designed to perform criminal detection in a video clip using face recognition. It takes an image file containing the face of the criminal to be detected and a video clip in which the detection will be performed.

# Instructions
1. Click on "Choose the Image file" to select the image file containing the face of the criminal you want to detect.
2. Click on "Choose the Video file" to select the video clip in which you want to perform the detection.
3. Click "Click to continue" to start the detection process.

# Face Recognition
The program uses the face_recognition library to perform face recognition on the provided image and video frames. It compares the known face (criminal's face from the image) with the faces in each frame of the video to determine if a match is found.

For each frame in the video, the following information is collected:

* Frame number
* Percentage match with the known face
The results are stored in a CSV file named "framedata.csv," which contains the frame number and the percentage match.

# Output Options
After the detection process, you have three options to explore the results:

1. Detect-face: Clicking this option will find the frame with the highest percentage match and display it along with additional information, such as frame timestamp and percentage match.

2. Detect-max-match face: Clicking this option will find the frame with the maximum percentage match and display it with frame timestamp and percentage match.

3. Detect screen time: This option calculates the screen time of the detected face in the video and displays it. Screen time is calculated as the number of frames where the face was detected divided by the frame rate of the video.

# Note
* If the program does not detect any faces in a frame, it will mark it as "Not detected" in the CSV file.
* The program also calculates the screen time of the detected face in the video and displays it when you choose the "Detect screen time" option.
