from constants import *


class Textbox:
    def __init__(self,loc, text):
        textbox_png = pygame.image.load('visuals/Sprites/textbox.png')
        textbox_png = pygame.transform.scale(textbox_png,
                                             (len(text)*8.3+10, screen_dimensions[1] * .08))
        self.img = textbox_png
        self.x_loc = loc[0]
        self.y_loc = loc[1]
        self.rect = self.img.get_rect(midleft=(self.x_loc-10, self.y_loc))
        self.txtSurface = font.render(text, True, black)
        self.txtRect = self.txtSurface.get_rect(midleft=(self.x_loc, self.y_loc))

        screen.blit(self.img, self.rect)
        screen.blit(self.txtSurface, self.txtRect)
        pygame.display.flip()

    def update(self, screen):
        screen.blit(self.img, self.rect)
        screen.blit(self.txtSurface, self.txtRect)

    def check_input(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False