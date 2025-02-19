import random
from src.hand_detection import detect_hand_signal

def odd_even_toss():
    print("Choose Odd or Even by showing 1 for Odd, 2 for Even:")
    detected_fingers = None  # Ensure it waits for a valid input

    while detected_fingers is None or detected_fingers == 0:
        detected_fingers = detect_hand_signal()  

    print(f"You chose: {'Odd' if detected_fingers == 1 else 'Even'}")
    
    user_runs = detect_hand_signal()
    ai_runs = random.randint(1, 6)

    print(f"\nYou showed {user_runs}, AI chose {ai_runs}")

    toss_sum = user_runs + ai_runs
    toss_winner = "User" if (toss_sum % 2 == 0 and detected_fingers == 2) or (toss_sum % 2 != 0 and detected_fingers == 1) else "AI"

    print(f"Toss Result: {'Even' if toss_sum % 2 == 0 else 'Odd'}. {toss_winner} won the toss!")
    
    return toss_winner
