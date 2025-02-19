import random
from src.handDetection import detect_hand_signal

def play_second_innings(batting_team, target):
    print(f"\n{batting_team} is batting second. Target: {target + 1}")

    score = 0
    while score <= target:
        user_runs = detect_hand_signal() if batting_team == "User" else random.randint(1, 6)
        ai_runs = random.randint(1, 6) if batting_team == "User" else detect_hand_signal()

        if batting_team == "User":
            print(f"{batting_team} played: {user_runs}, AI bowled: {ai_runs}") 
        else:
            print(f"{batting_team} played: {ai_runs}, User bowled: {user_runs}") 

        if user_runs == ai_runs:
            print(f"{batting_team} is out! Final score: {score}")
            break

        score += user_runs if batting_team == "User" else ai_runs
        print(f"Total runs: {score}")
        print(f"Target: {target+1}")

    if score > target:
        print(f"{batting_team} wins!")
    else:
        print("Opponent wins!")
