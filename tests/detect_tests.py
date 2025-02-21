import cv2
import mediapipe as mp
import time

# Define Finger Tip Landmarks (Thumb to Pinky)
FINGER_TIPS = [4, 8, 12, 16, 20]

# Timer setup
last_time = time.time()

def count_fingers(hand_landmarks):
    count = 0
    if hand_landmarks:
        landmarks = hand_landmarks.landmark
        # Check each finger
        for tip in FINGER_TIPS[1:]:  # Exclude thumb (special case)
            if landmarks[tip].y < landmarks[tip - 2].y:  # Compare with second knuckle
                count += 1
        
        # Thumb special case (based on x-coordinates)
        if landmarks[FINGER_TIPS[0]].x > landmarks[FINGER_TIPS[0] - 1].x:
            count += 1
    return count

def get_right_hand_finger_count(hands, cap):
    global last_time
    ret, frame = cap.read()
    if not ret:
        return None

    # Convert to RGB for Mediapipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Hand Detection
    hand_results = hands.process(rgb_frame)

    if hand_results.multi_hand_landmarks and hand_results.multi_handedness:
        for hand_landmarks, handedness in zip(hand_results.multi_hand_landmarks, hand_results.multi_handedness):
            label = handedness.classification[0].label  # 'Left' or 'Right'
            if label == 'Left':  # Only process right hand
                finger_count = count_fingers(hand_landmarks)
                
                # Print detected value every 2 seconds
                current_time = time.time()
                if current_time - last_time >= 1:
                    last_time = current_time
                    return finger_count
    return None

def detect_hand_signal():
    
    # Initialize Mediapipe Hands
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils

    # Initialize Webcam
    cap = cv2.VideoCapture(0)

    # Define Hand Detection Model
    hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
    while cap.isOpened():
        finger_count = get_right_hand_finger_count(hands, cap)
        if finger_count is not None:
            print(f"Right hand detected fingers: {finger_count}")
            return finger_count

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    while(True):
        fingers = detect_hand_signal()
        print(fingers)
        if fingers==3:
            break
        