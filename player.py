from officer import PoliceOfficer


class Player():

    def __init__(self, name, type_player, position):
        self.name = name
        self.type = type_player
        self.position = position
        self.resources = {
            "reputation": 0,
            "money": 0,
            "health": 10
        }

    def display_card(self, card, type_card):
        print(self.name, "landed on the", type, "card")
        print(card["description"])
        if type_card == 'red':
            if PoliceOfficer.AGENT:
                for i in range(len(card["options"])):
                    n = i + 1
                    print(n, ". ", card["options"][i])
            else:
                for i in range(len(card["options"])):
                    n = i + 1
                    print(n, ". ", card["options"][i]['name'])
        else:
            print(card["reward"])

    def __str__(self) -> str:
        return f'(name: {self.name}, type: {self.type}, position: {self.position})'

    def apply_card(self, card_resources):
        for resource in card_resources:
            self.resources[resource] = self.resources[resource] + \
                card_resources[resource]

    def getPos(self):
        return self.position

    def getStats(self):
        return self.resources

    def getName(self):
        return self.name
