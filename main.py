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
    batting_first = toss_winner if decide_bat_or_bowl(toss_winner) == "User" else "AI"
    bowling_first = "User" if batting_first == "AI" else "AI"

    target = play_first_innings(batting_first)
    play_second_innings(bowling_first, target)

if __name__ == "__main__":
    main()
