class Button:
    def __init__(self, image, loc):
        self.img = image
        self.x_loc = loc[0]
        self.y_loc = loc[1]
        self.rect = self.img.get_rect(center=(self.x_loc, self.y_loc))

    def update(self, screen):
        screen.blit(self.img, self.rect)

    def check_input(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
