import csv
import json


def convert_red_cards():
    final_set = []

    with open('RED_CARDS.csv', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            card_dict = dict()
            card_dict['description'] = row[0].replace(";", ",")
            card_dict['options'] = []
            for i in range(1, 4):
                if not row[i]:
                    break
                consequences_dict = {
                    'reputation': row[1+3*i],
                    'money': row[1+3*i+1],
                    'health': row[1+3*i+2]
                }
                option_dict = {'name': row[i],
                               'consequences': consequences_dict}
                card_dict['options'].append(option_dict)
            final_set.append(card_dict)

    json_object = json.dumps(final_set, indent=4)
    print(json_object)
    with open("red_cards.json", "w") as outfile:
        outfile.write(json_object)


def convert_gold_cards():
    final_set = []
    with open('CARDS_GOLD.csv', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            card_dict = dict()
            card_dict['description'] = row[0].replace(";", ",")
            amount_type_arr = row[1].split()
            if amount_type_arr[1] == "Money":
                amount_type_arr[1] = "money"
            elif amount_type_arr[1] == "REP":
                amount_type_arr[1] = "reputation"
            else:
                amount_type_arr[1] = "health"
            card_dict['reward'] = {
                "amount": amount_type_arr[0], "type": amount_type_arr[1]}
            final_set.append(card_dict)

    json_object = json.dumps(final_set, indent=4)
    with open("gold_cards.json", "w") as outfile:
        outfile.write(json_object)


convert_gold_cards()
