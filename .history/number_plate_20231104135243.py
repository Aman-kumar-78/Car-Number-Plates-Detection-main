

import cv2
import os
import easyocr

# Load the cascade classifier for license plates
harcascade = "model/haarcascade_russian_plate_number.xml"
plate_cascade = cv2.CascadeClassifier(harcascade)

# Initialize the camera
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # width
cap.set(4, 480)  # height

min_area = 500
count = 0

while True:
    success, img = cap.read()

    if not success:
        print("Error accessing the camera.")
        break

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

    for (x, y, w, h) in plates:
        area = w * h
        if area > min_area:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)
            img_roi = img[y: y + h, x: x + w]
            cv2.imshow("ROI", img_roi)

    cv2.imshow("Result", img)

    key = cv2.waitKey(1)  # Capture the key press result once

    if key & 0xFF == ord('s'):
        if 'img_roi' in locals():
            cv2.imwrite("plates/scaned_img_" + str(count) + ".jpg", img_roi)
            cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
            cv2.imshow("Results", img)
            cv2.waitKey(500)
            count += 1
    if key & 0xFF == ord('q'):
        break
        

# Release the camera and close OpenCV windows
cap.release()
cv2.destroyAllWindows()

# Now, perform OCR on the saved images
reader = easyocr.Reader(['en'])
folder_path = "plates"
folder_contents = os.listdir(folder_path)
for i in folder_contents:
    output = reader.readtext(os.path.join(folder_path, i))
    cord = output[0][-2]
    print(cord)
