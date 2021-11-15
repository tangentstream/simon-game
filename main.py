import pygame
import random
import time


class Button:
    def __init__(self, label, color, x, y, width, height):
        self.label = label
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x < self.x + self.width:
            if pos[1] > self.y < self.y + self.height:
                return True
        return False


class Game:

    def __init__(self):
        self.ordem = []; self.sortear()
        self.buttons = [
            Button('azul',    (0, 0, 255),    50, 50, 200, 200),
            Button('amarela', (255, 255, 0), 250, 50, 200, 200),
            Button('verde',   (0, 255, 0),    50, 250, 200, 200),
            Button('ciano',   (0, 255, 255), 250, 250, 200, 200)]

    def sortear(self):
        """generate the sequence"""
        # time.sleep(1)
        self.ordem = []
        self.ordem.append(random.randint(0, 3))
        print(self.ordem)

    def redraw(self, win):
        win.fill((255, 255, 255))
        for b in self.buttons:
            b.draw(win)


def main():

    pygame.init()
    win = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Genius')

    game = Game()

    running = True

    while running:
        pygame.display.update()
        game.redraw(win)

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:

                next_step = game.ordem[0]
                btn = game.buttons[next_step]
                if btn.isOver(pos):
                    print(btn.label)
                    game.sortear()
                else:
                    print('Errado')
                    # ordem.clear()

    pygame.quit()


if __name__ == "__main__":
    main()
