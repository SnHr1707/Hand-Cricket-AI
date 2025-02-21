import random
from src.handDetection import detect_hand_signal

def decide_bat_or_bowl(toss_winner):
    if toss_winner == "User":
        print("Choose Bat or Bowl by showing 1 for Bat, 2 for Bowl:")
        detected_fingers = None  
        
        while detected_fingers is None or detected_fingers == 0:
            detected_fingers = detect_hand_signal()
        
        print(f"You chose to: {'Bat' if detected_fingers == 1 else 'Bowl'}")
        
        return "Batting" if detected_fingers == 1 else "Bowling"
    
    else:
        choice = random.choice(["Batting", "Bowling"])
        print(f"\nAI chose to {choice.lower()} first!")
        return choice
