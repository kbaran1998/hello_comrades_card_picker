import csv
import json

final_set = []

with open('CARDS.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        card_dict = dict()
        card_dict['description'] = row[0]
        card_dict['options'] = []
        for i in range(1, 5):
            if not row[i]:
                break
            consequences_dict = {
                'reputation': row[2+3*i],
                'money': row[2+3*i+1],
                'health': row[2+3*i+2]
            }
            option_dict = {'name': row[i], 'consequences': consequences_dict}
            card_dict['options'].append(option_dict)
        final_set.append(card_dict)

json_object = json.dumps(final_set, indent=4)
print(json_object)

with open("red_cards.json", "w") as outfile:
    outfile.write(json_object)
