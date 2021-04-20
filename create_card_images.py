import os
import json
import shutil
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def text_wrap(text, font, max_width):
    lines = []

    # If the text width is smaller than the image width, then no need to split
    # just add it to the line list and return
    if font.getsize(text)[0] <= max_width:
        lines.append(text)
    else:
        # split the line by spaces to get words
        words = text.split(' ')
        i = 0
        # append every word to a line while its width is shorter than the image width
        while i < len(words):
            line = ''
            while i < len(words) and font.getsize(line + words[i])[0] <= max_width:
                line = line + words[i] + " "
                i += 1
            if not line:
                line = words[i]
                i += 1
            lines.append(line)
    return lines


def center_text_horizontally(image, font, text, height, draw):
    text_width = draw.textsize(text, font)[0]
    position = ((image.size[0]-text_width)/2, height)
    return position


def save_red_card(index, scored, red_cards):
    title_card = red_cards[index]['description']
    FONT = ImageFont.truetype("C:\Windows\Fonts\\ariblk.ttf", 34)

    img = Image.open('red-card-remplate.png')
    txt = title_card
    image_left_border = img.size[0] - 100
    draw = ImageDraw.Draw(img)

    FONT_TITLE = ImageFont.truetype("C:\Windows\Fonts\\ariblk.ttf", 20)

    text_lines = text_wrap(txt, FONT_TITLE, image_left_border)

    RED_COLOUR = (202, 32, 25)
    GRAY_COLOUR = (72, 72, 75)

    iter_height = 50
    for line in text_lines:
        centered_text_coords = center_text_horizontally(
            img, FONT_TITLE, line, iter_height, draw)
        draw.text(centered_text_coords, line, RED_COLOUR, font=FONT_TITLE)
        iter_height += 30

    options = red_cards[index]['options']

    FONT_2 = ImageFont.truetype("C:\Windows\Fonts\\ariblk.ttf", 30)
    FONT_DESC_TEXT = ImageFont.truetype("arial.ttf", 25)

    for option in options:
        centered_text_coords = center_text_horizontally(
            img, FONT_2, option['name'], iter_height, draw)
        draw.text(centered_text_coords,
                  option['name'], GRAY_COLOUR, font=FONT_2)
        if scored:
            iter_height += 30
            result_description = "Reputation       Money       Health"
            centered_text_coords = center_text_horizontally(
                img, FONT_DESC_TEXT, result_description, iter_height, draw)
            draw.text(centered_text_coords, result_description,
                      GRAY_COLOUR, font=FONT_DESC_TEXT)
            iter_height += 30
            result_number = f"     {option['consequences']['reputation']}         {option['consequences']['money']}         {option['consequences']['health']}     "
            centered_text_coords = center_text_horizontally(
                img, FONT_DESC_TEXT, result_description, iter_height, draw)
            draw.text(centered_text_coords, result_number,
                      RED_COLOUR, font=FONT)
        iter_height += 50

    CURRENT_PATH = os.path.abspath(os.getcwd())
    file_name = f"red-card-{index}-scored.png" if scored else f"red-card-{index}-unscored.png"
    SCORED_PATH = os.path.join(CURRENT_PATH, 'red_card_images\\scored')
    UNSCORED_PATH = os.path.join(CURRENT_PATH, 'red_card_images\\unscored')

    img.save(file_name)
    if scored:
        shutil.move(os.path.join(CURRENT_PATH, file_name),
                    os.path.join(SCORED_PATH, file_name))
    else:
        shutil.move(os.path.join(CURRENT_PATH, file_name),
                    os.path.join(UNSCORED_PATH, file_name))


def save_gold_card(index, gold_cards):
    title_card = gold_cards[index]['description']
    img = Image.open('gold-card-remplate.png')
    txt = title_card
    image_left_border = img.size[0] - 100
    draw = ImageDraw.Draw(img)

    FONT_TITLE = ImageFont.truetype("C:\Windows\Fonts\\ariblk.ttf", 40)
    text_lines = text_wrap(txt, FONT_TITLE, image_left_border)

    GOLD_COLOUR = (186, 150, 25)
    GRAY_COLOUR = (72, 72, 75)

    iter_height = 50
    for line in text_lines:
        centered_text_coords = center_text_horizontally(
            img, FONT_TITLE, line, iter_height, draw)
        draw.text(centered_text_coords, line, GOLD_COLOUR, font=FONT_TITLE)
        iter_height += 40

    reward = gold_cards[index]['reward']
    FONT_2 = ImageFont.truetype("C:\Windows\Fonts\\ariblk.ttf", 30)
    iter_height += 50
    centered_text_coords = center_text_horizontally(
        img, FONT_2, reward['type'], iter_height, draw)
    draw.text(centered_text_coords,
              reward['type'], GRAY_COLOUR, font=FONT_2)
    iter_height += 50
    centered_text_coords = center_text_horizontally(
        img, FONT_2, reward['amount'], iter_height, draw)
    draw.text(centered_text_coords,
              reward['amount'], GOLD_COLOUR, font=FONT_2)

    CURRENT_PATH = os.path.abspath(os.getcwd())
    file_name = f"gold-card-{index}.png"
    GOLD_PATH = os.path.join(CURRENT_PATH, 'gold_card_images')

    img.save(file_name)
    shutil.move(os.path.join(CURRENT_PATH, file_name),
                os.path.join(GOLD_PATH, file_name))


"""with open("red_cards.json") as json_file:
    red_cards_json = json.load(json_file)

card_index = 0
for card in red_cards_json:
    save_red_card(card_index, True, red_cards_json)
    save_red_card(card_index, False, red_cards_json)
    print(f"File: red-card-{card_index}", "was SAVED!")
    card_index += 1
"""

with open("gold_cards.json") as json_file:
    gold_cards_json = json.load(json_file)

card_index = 0
for card in gold_cards_json:
    save_gold_card(card_index, gold_cards_json)
    print(f"File: gold-card-{card_index}", "was SAVED!")
    card_index += 1
