# Finger Counter
The Finger counter program that uses OpenCV Hand Landmark is an application that utilizes hand recognition and landmark technology (key points on the hand) using OpenCV to count the number of open fingers. The application then sends the detected finger count information to a dot matrix display device via serial communication using ESP32.

The process begins with capturing an image of the hand through a camera and applying landmark detection using OpenCV to identify the location of the fingertip. From these locations, the program counts the number of open fingers by identifying the landmark configuration corresponding to the number of open fingers. The counting result is then sent via serial communication to the dot matrix display device, which is used to display a number representing the count of open fingers.

This program combines various technologies, such as image processing (OpenCV), landmark recognition, serial communication, and the use of ESP32, to create an application that can count the number of open fingers and display the result on a dot matrix display device.

# Video User's Guide
![image](https://github.com/abdullahnajib-web/Finger-Counter/blob/main/documents/manual.mp4)
