import cv2

print(cv2.data.haarcascades)

face_cascade = cv2.CascadeClassifier('haarcascades_frontalface_default.xml')

capture = cv2.VideoCapture()

if not capture.isOpened():
    print("Error, could not open camera")
    exit()
    
while True:
    
    ret, frame = capture.read()
    
    if not ret:
        print("Failed to capture image")
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        face_emo = frame[y:y + h, x:x + w]
            
        results = DeepFace.analyze(face_emo, actions=['emotion'], enforce_detection=False)
            
        dominant_emotion = results[0]['dominant_emotion']
            
        cv2.putText(frame, dominant_emotion, (x, y - 10), 

        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    
    cv2.imshow("cv2 face detection, press q to quit or exit", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
capture.release()
cv2.destroyAllWindows()
