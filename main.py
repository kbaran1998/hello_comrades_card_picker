import json
import random


def read_cards():
    with open('cards.json') as json_file:
        red_cards = json.load(json_file)
    random.shuffle(red_cards)
    return red_cards


input_str = 's'
while input_str != 'q':
    if len(cards) == 0:
        cards = read_cards()
    try:
        input_str = input("card-picker> ")
    except Exception:
        print("Your instruction is incorrect!")
