import json
import random
from typing import Dict, List
from card_stack import CardStack
from officer import PoliceOfficer
from player import Player

RED_NODES = set([3, 6, 9, 13, 15, 17, 21, 26, 29,
                 30, 34, 38, 44, 46, 48, 49, 52, 56, 58, 61])
GOLD_NODES = set([22, 31, 42, 53, 54])
blue_nodes = []


def read_map() -> Dict:
    with open("map.json") as json_file:
        map = json.load(json_file)
    print("MAP IMPORTED")
    return map


def read_cards(file_name) -> List:
    with open(file_name) as json_file:
        import_cards = json.load(json_file)
    random.shuffle(import_cards)
    print("IMPORTED ", file_name)
    return import_cards


def read_poi():
    with open("poi.json") as json_file:
        poi = json.load(json_file)
    print("Points of Interest IMPORTED")
    blue_nodes = set([obj['id'] for obj in poi])
    return poi


points_of_interest = read_poi()
gold_cards = CardStack(read_cards("gold_cards.json"))
red_cards = CardStack(read_cards("red_cards.json"))
map = read_map()

picked_players = False
player_number = -1
while not picked_players:
    try:
        player_number = int(input("Pick player number: "))
        if 2 < player_number <= 4:
            picked_players = True
        else:
            print("Player number can be either 3 or 4")
    except Exception:
        print("Player number went wrong")
        picked_players = False

types_players = [PoliceOfficer.AGENT, PoliceOfficer.COMMISONNER,
                 PoliceOfficer.CHIEF, PoliceOfficer.AGENT] if player_number == 4 else [PoliceOfficer.AGENT, PoliceOfficer.COMMISONNER,
                                                                                       PoliceOfficer.CHIEF]

random.shuffle(types_players)

players = []
positions = set()
for i in range(player_number):
    picked_name = False
    while not picked_name:
        try:
            player_name = input("Pick player name: ")
            pos = random.randint(1, 62)
            while pos in positions:
                pos = random.randint(1, 62)
            players.append(Player(player_name, types_players[i], pos))
            picked_name = True
        except Exception:
            print("Player name was chosen wrong!")
            picked_name = False

print('\nPlayers:\n')
for p in players:
    print(p.__str__())

events = []


def round(player):
    if player.getPos() in RED_NODES:
        current_card = red_cards.pick_card()
        player.display_card(current_card, "red")
        picked_option = -1
        while picked_option < 1 or picked_option > len(current_card["options"]):
            try:
                picked_option = int(input("Pick your option: "))
                if picked_option < 1 or picked_option > len(current_card["options"]):
                    print("Your choice was outside of range!")
            except Exception:
                print("Your instruction is incorrect!")
        player.apply_card(current_card["options"][picked_option])
        event = f"\n{player.getName()} got a RED card and got '{current_card["description"]}' for their resources.\nTheir stats are: {player.getStats()}\n"
        events.append(event)
        print(event)
    elif player.getPos() in GOLD_NODES:
        current_card = gold_cards.pick_card()
        player.display_card(current_card, "gold")
        reward = {current_card['reward']['type']: current_card['reward']['amount']}
        player.apply_card(reward)
        event = f"\n{player.getName()} got a GOLD card and got '{current_card["description"]}' for their resources.\nTheir stats are: {player.getStats()}\n"
        events.append(event)
        print(event)
    elif player.getPos() in blue_nodes:


round_number = 1

# while len(points_of_interest) != 0:


"""input_str = 's'
while input_str != 'q':
    if len(cards) == 0:
        cards = read_cards()
    try:
        input_str = input("card-picker> ")
    except Exception:
        print("Your instruction is incorrect!")
"""
