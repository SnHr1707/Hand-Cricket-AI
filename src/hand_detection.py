import os
import cv2
import mediapipe as mp
import logging

# Suppress TensorFlow and MediaPipe logs
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppress TensorFlow warnings
logging.getLogger("tensorflow").setLevel(logging.ERROR)  # Suppress TensorFlow logs
logging.getLogger('mediapipe').setLevel(logging.ERROR)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

def detect_hand_signal():
    cap = cv2.VideoCapture(0)
    hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8)

    detected_fingers = None  # Start with no value

    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)  # Flip horizontally for natural interaction
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb_frame)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                fingers_up = [
                    hand_landmarks.landmark[i].y < hand_landmarks.landmark[i-2].y
                    for i in [8, 12, 16, 20]
                ]
                detected_fingers = sum(fingers_up) + 1  # Thumb is always counted
                
                # Draw landmarks on the hand
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                if detected_fingers > 0:  # If a valid hand signal is detected, return it
                    cap.release()
                    cv2.destroyAllWindows()
                    return detected_fingers
        
        # Show the webcam feed
        cv2.imshow("Hand Detection", frame)

        # Press 'q' to manually exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
