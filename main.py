from src.oddEven import odd_even_toss
from src.batOrBowl import decide_bat_or_bowl
from src.firstInnings import play_first_innings
from src.secondInnings import play_second_innings
import os
import logging
import sys
import absl.logging


def main():
    # Suppress TensorFlow & MediaPipe logs
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppress TensorFlow logs
    logging.getLogger("tensorflow").setLevel(logging.ERROR)  # Suppress TensorFlow logs
    logging.getLogger('mediapipe').setLevel(logging.ERROR)
    absl.logging.set_verbosity(absl.logging.ERROR)

    # Redirect stderr to suppress C++ warnings
    sys.stderr = open(os.devnull, 'w')
    print("\n🏏 Welcome to Hand Cricket! 🏏")
    
    toss_winner = odd_even_toss()
    batting_first=""
    if toss_winner=="User":
        batting_first = "User" if toss_winner=="Batting" else "AI"
    else:
        batting_first = "AI" if toss_winner=="Batting" else "User"
    bowling_first = "User" if batting_first == "AI" else "AI"

    target = play_first_innings(batting_first, bowling_first)
    play_second_innings(bowling_first, target, batting_first)

if __name__ == "__main__":
    main()
