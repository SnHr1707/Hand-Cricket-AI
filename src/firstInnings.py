import random
from src.handDetection import detect_hand_signal

def play_first_innings(batting_team, bowling_team):
    print(f"\n{batting_team} is batting first!")

    score = 0
    while True:
        runs_scored = detect_hand_signal() if batting_team == "User" else random.randint(1, 6)
        bowler = random.randint(1, 6) if batting_team == "User" else detect_hand_signal()
        print(f"{batting_team} played: {runs_scored}, {bowling_team} bowled: {bowler}") 

        if runs_scored == bowler:
            print(f"{batting_team} is out! Final score: {score}")
            return score

        score += runs_scored
        print(f"Total runs: {score}")
