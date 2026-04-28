import cv2

def detect_threat(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Simple motion detection (basic prototype)
    blur = cv2.GaussianBlur(gray, (21, 21), 0)

    # Dummy threat detection box (for demo)
    cv2.putText(frame, "Monitoring...", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Example alert simulation
    # Replace this with ML model later
    return frame
