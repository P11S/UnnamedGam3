import pygame
import visuals

backing = visuals.Backdrop()
sprites = visuals.Clickable()
code_nums = 10
JUST_LAUNCHED = True


# SCREEN SIZES

screen_dimensions = (1000, 600)
screen_width = screen_dimensions[0]
screen_height = screen_dimensions[1]
ratio = screen_dimensions[0] / screen_dimensions[1]
screen = pygame.display.set_mode(screen_dimensions)

# COLORS
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
grey = pygame.Color(150, 150, 150)

# CARD STUFF
SUITS = ['C', 'S', 'H', 'D']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


font = pygame.font.SysFont("optima", 16)
textfont = pygame.font.SysFont('optimaS',30)
game_end = pygame.font.SysFont('optima', 30)
blackjack = pygame.font.SysFont('optima', 30)

# Dialogue Bits
intro_dialogue = [("...", 2),
                  ("Trying to escape through the back?", 2.5), ("How much did you lose out there?", 2.5),
                ("No matter... It must have been a lot.", 2), ("Well you clearly need some practice.", 2),
                ("Would you join me in a game of Blackjack?", 2.5), ("You'll stay locked in here otherwise.", 3),
                ("Win the key from me and get back out there.", 3), ("Surely you can't keep losing...", 2.5)]

# ("Oh but you're the best Gambler in your GA group?", 3),
#                 ("That's... nice", 1.5
