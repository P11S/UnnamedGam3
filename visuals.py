import pygame
from constants import *

screen_dimensions = (1000, 600)
ratio = screen_dimensions[0] / screen_dimensions[1]


class Backdrop:
    """
    This class will house every 'Background' style image that is used in the game
    """

    def __init__(self):
        # Backdrop for the main menu
        menu_png = pygame.image.load('visuals/Backdrops/EFH_menu.png')
        menu_png = pygame.transform.scale(menu_png, screen_dimensions)
        self.menu = menu_png
        # Backdrop for the main game room
        mainroom_png = pygame.image.load('visuals/Backdrops/EFH_mainroom.png')
        mainroom_png = pygame.transform.scale(mainroom_png, screen_dimensions)
        self.mainroom = mainroom_png
        # Backdrop for the settings screen
        settings_png = pygame.image.load('visuals/Backdrops/EFH_settings.png')
        settings_png = pygame.transform.scale(settings_png, screen_dimensions)
        self.settings = settings_png
        # Backdrop for the achievements screen
        achievements_png = pygame.image.load('visuals/Backdrops/EFH_achievements.png')
        achievements_png = pygame.transform.scale(achievements_png, screen_dimensions)
        self.achievements = achievements_png
        # Backdrop for the stairwell
        stairs_png = pygame.image.load('visuals/Backdrops/EFH_stairs.png')
        stairs_png = pygame.transform.scale(stairs_png, screen_dimensions)
        self.stairs = stairs_png
        # Backdrop for the task rooms
        task1_png = pygame.image.load('visuals/Backdrops/EFH_task1.png')
        task1_png = pygame.transform.scale(task1_png, screen_dimensions)
        self.task1 = task1_png
        # Backdrop for the lockbox menu
        lockbox_png = pygame.image.load('visuals/Backdrops/EFH_lockbox.png')
        lockbox_png = pygame.transform.scale(lockbox_png, screen_dimensions)
        self.lockbox = lockbox_png
        # Backdrop for the escape menu
        # Backdrop for the main menu
        escape_png = pygame.image.load('visuals/Backdrops/escape.png')
        escape_png = pygame.transform.scale(escape_png, screen_dimensions)
        self.escape = escape_png
        # Backdrop for rules
        rules_png = pygame.image.load('visuals/Backdrops/EFH_rules.png')
        rules_png = pygame.transform.scale(rules_png, screen_dimensions)
        self.rules = rules_png


class Clickable:
    """
    This class will house every 'sprite' that one can click throughout the game
    """

    def __init__(self):
        # Sprite for the button with path MENU -> MAIN GAME
        menu_to_mainscreen_png = pygame.image.load('visuals/Sprites/menu_to_main.png')
        menu_to_mainscreen_png = pygame.transform.scale(menu_to_mainscreen_png,
                                                        (screen_dimensions[0]*.16, screen_dimensions[1]*.5))
        self.menu_to_mainscreen = menu_to_mainscreen_png
        # Sprite for button with path ANYWHERE -> MENU
        any_to_menu_png = pygame.image.load('visuals/Sprites/exit_to_home.png')
        any_to_menu_png = pygame.transform.scale(any_to_menu_png,
                                                 (screen_dimensions[0] * .05, screen_dimensions[1] * .05 * ratio))
        self.any_to_menu = any_to_menu_png
        # Sprite for button with path MENU -> SETTINGS
        menu_to_settings_png = pygame.image.load('visuals/Sprites/to_settings.png')
        menu_to_settings_png = pygame.transform.scale(menu_to_settings_png,
                                                      tuple(i * 0.08 for i in screen_dimensions))
        self.menu_to_settings = menu_to_settings_png
        # Sprite for button with path MAINSCREEN -> TASK1
        task1_png = pygame.image.load('visuals/Sprites/task1.png')
        task1_png = pygame.transform.scale(task1_png,
                                           (screen_dimensions[0]*.25, screen_dimensions[1]*.1))
        self.task1 = task1_png
        # Sprite for the button with path MENU -> ACHIEVEMENTS
        menu_to_achievements_png = pygame.image.load('visuals/Sprites/to_achievements.png')
        menu_to_achievements_png = pygame.transform.scale(menu_to_achievements_png,
                                                          tuple(i * 0.15 for i in screen_dimensions))
        self.menu_to_achievements = menu_to_achievements_png
        # Sprite for the button with path TASK -> MAIN GAME
        task_to_main_png = pygame.image.load('visuals/Sprites/task_to_main.png')
        task_to_main_png = pygame.transform.scale(task_to_main_png, (screen_dimensions[0] * .05,
                                                                     screen_dimensions[1] * .05 * ratio))
        self.task_to_main = task_to_main_png
        # Sprite for the button DEAL
        deal_png = pygame.image.load('visuals/Sprites/deal.png')
        deal_png = pygame.transform.scale(deal_png,
                                                          tuple(i * 0.1 for i in screen_dimensions))
        self.deal = deal_png
        # Sprite for the button HIT
        hit_png = pygame.image.load('visuals/Sprites/hit.png')
        hit_png = pygame.transform.scale(hit_png,
                                          tuple(i * 0.1 for i in screen_dimensions))
        self.hit = hit_png
        # Sprite for the button STAND
        stand_png = pygame.image.load('visuals/Sprites/stand.png')
        stand_png = pygame.transform.scale(stand_png,
                                           tuple(i * 0.1 for i in screen_dimensions))
        self.stand = stand_png
        # Sprite for the lock box
        lock_png = pygame.image.load('visuals/Sprites/lock.png')
        lock_png = pygame.transform.scale(lock_png,
                                           (screen_dimensions[0] * .35, screen_dimensions[1] * .35))
        self.lock = lock_png
        # Sprite for the button with path LOCK BOX -> CARD TABLE
        box_to_table_png = pygame.image.load('visuals/Sprites/box_to_table.png')
        box_to_table_png = pygame.transform.scale(box_to_table_png,
                                                  (screen_dimensions[0] * .05, screen_dimensions[1] * .05 * ratio))
        self.box_to_table = box_to_table_png
        # Sprite for the lock box buttons
        box_button_png = pygame.image.load('visuals/Sprites/box_button.png')
        box_button_png = pygame.transform.scale(box_button_png,
                                                  (screen_dimensions[0] * .06, screen_dimensions[1] * .06 * ratio))
        self.box_button = box_button_png
        # Sprite for the lock box buttons
        textbox_png = pygame.image.load('visuals/Sprites/textbox.png')
        textbox_png = pygame.transform.scale(textbox_png,
                                             (screen_dimensions[0] * .4, screen_dimensions[1] * .09))
        self.textbox = textbox_png
        # Sprite for rules
        rules_png = pygame.image.load('visuals/Sprites/main_to_rules.png')
        rules_png = pygame.transform.scale(rules_png,
                                           (screen_dimensions[0] * .065, screen_dimensions[1] * .12))
        self.rules = rules_png
