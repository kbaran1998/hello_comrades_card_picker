import json
import random


def read_cards():
    with open('cards.json') as json_file:
        red_cards = json.load(json_file)
    random.shuffle(red_cards)
    return red_cards


def card_menu(card):
    print()
    input_int = ''
    while input_int != 'q':
        print(card['description'])
        for i in range(len(card['options'])):
            print("         ", i+1, "-", card['options'][i]['name'])
        try:
            input_int = int(input('Make your choice: '))
            if 1 <= input_int <= len(card['options']):
                print(card['options'][i]['consequences'])
                input_int = 'q'
            else:
                print(f"Pick number beteween 1 - {len(card['options'])} !!!")
        except Exception:
            print("Your instruction is incorrect!")
        print()


cards = read_cards()
input_str = 's'
while input_str != 'q':
    if len(cards) == 0:
        cards = read_cards()
    try:
        input_str = input("card-picker> ")
        if input_str == 'pick':
            card_menu(cards.pop())
    except Exception:
        print("Your instruction is incorrect!")
