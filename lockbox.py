from constants import *
from button import *
import random


class LockBox:
    def __init__(self, entries):
        self.columns = entries
        self.row1_buttons = []
        self.row1_keys = []
        self.build_row_1()
        self.row2_buttons = []
        self.row2_keys = []
        self.build_row_2()
        self.code_reached = 1

    def build_row_1(self):
        x_ticks = .9 * screen_width / (self.columns - 1)
        entry_x_loc = -x_ticks / 2
        for i in range(2, self.columns+2):
            entry_x_loc += x_ticks
            button = Button(sprites.box_button, (entry_x_loc, .82 * screen_height))
            key = random.randint(0, 1)
            self.row1_buttons.append(button)
            self.row1_keys.append(key)

    def build_row_2(self):
        x_ticks = .9 * screen_width / (self.columns - 1)
        entry_x_loc = -x_ticks / 2
        for i in range(2, self.columns+2):
            entry_x_loc += x_ticks
            button = Button(sprites.box_button, (entry_x_loc, .94 * screen_height))
            key = abs(self.row1_keys[i-2]-1)
            self.row2_buttons.append(button)
            self.row2_keys.append(key)
