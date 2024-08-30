import os
import time
import uuid
import cv2

DATA_PATH = 'collecting_data'

if not os.path.exists(DATA_PATH):
    os.mkdir(DATA_PATH)
    print('Created:', DATA_PATH)

labels = ['hello', 'thanks', 'yes', 'no', 'iloveyou']
number_of_images = 15

cap = cv2.VideoCapture(0)

for label in labels:
    label_dir = os.path.join(DATA_PATH, label)
    if not os.path.exists(label_dir):
        os.mkdir(label_dir)
        print('Directory created:', label_dir)

    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Press Q for data collecting {}'.format(label),
                    (100, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    1.3, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('Frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break

    for i in range(number_of_images):
        ret, frame = cap.read()
        # Generate a unique filename using uuid and save it in the correct directory
        image_name = os.path.join(label_dir, '{}_{}.jpg'.format(label, str(uuid.uuid1())))
        cv2.imshow('Frame', frame)
        cv2.imwrite(image_name, frame)
        time.sleep(0.3)
        cv2.waitKey(100)

cap.release()
cv2.destroyAllWindows()
