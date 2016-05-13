# -*- coding: utf-8 -*
import random
from wordlist import WORDS

WORD_AMOUNT = 25


count_dict = {
#BLUE
0:8,
#RED
1:8,
#INNOCENT
2:7,
#ASSASIN
3:1,
}

def create_board(first=0):
    words = random.sample(WORDS,WORD_AMOUNT)
    board = {}
    count_dict[first] += 1
    count = 1
    for word in words:
        while 1:
            color = random.randint(0,3)
            if count_dict.get(color):
                board['c'+str(count)] = 'color' + str(color)
                board['v'+str(count)] = word
                count += 1
                count_dict[color] -= 1
                break
    return board

if __name__ == "__main__":
    board = create_board()
    template = open('template.html', 'r')
    html = template.read()
    template.close()
    new_html = html.format(**board)
    template_white = open('template_white.html', 'r')
    html_white = template_white.read()
    template_white.close()
    new_html_white = html_white.format(**board)
    f2 = open('board_color.html', 'w')
    f2.write(new_html)
    f2.close()
    f2 = open('board_white.html', 'w')
    f2.write(new_html_white)
    f2.close()
