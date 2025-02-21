import random
from src.handDetection import detect_hand_signal

def play_second_innings(batting_team, target, bowling_team):
    print(f"\n{batting_team} is batting second. Target: {target + 1}")

    score = 0
    while score <= target:
        runs_scored = detect_hand_signal() if batting_team == "User" else random.randint(1, 6)
        bowled = random.randint(1, 6) if batting_team == "User" else detect_hand_signal()

        print(f"{batting_team} played: {runs_scored}, {bowling_team} bowled: {bowled}")

        if runs_scored == bowled:
            print(f"{batting_team} is out! Final score: {score}")
            break

        score += runs_scored
        print(f"Total runs: {score}")
        print(f"Target: {target+1}")

    if score > target:
        print(f"{batting_team} wins!")
    else:
        print(f"{bowling_team} wins!")
