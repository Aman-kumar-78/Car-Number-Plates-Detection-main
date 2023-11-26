# Car Number Plates Detection
```This Python script captures live video from a camera, detects license plates in the frames, and performs Optical Character Recognition (OCR) on the detected license plates. The extracted license plate numbers are then saved in a MySQL database.```


# Prerequisites
```
Python
OpenCV
PyTesseract
MySQL Connector
```

# Usage
# Ensure that all the required libraries are installed by running:
```
pip install opencv-python pytesseract mysql-connector-python 
Import the necessary modules and set up the cascade classifier and camera.

Initialize the MySQL database connection using the Mysqls class.

Continuously capture frames from the camera, detect license plates, and display the results in real-time.

Press 's' to save the detected license plate. Saved plates are stored in the "plates" folder.

Press 'q' to quit the application.

After the application is closed, it performs OCR on the saved license plate images using Tesseract.

OCR results are inserted into the MySQL database.

Retrieve and print the car numbers stored in the database.
```

# Note
```The script uses the Haar Cascade classifier for license plate detection.
Detected license plates are saved in the "plates" folder with a unique filename.
OCR is performed using Tesseract, and the results are stored in a MySQL database.
Feel free to modify the script according to your needs.```

