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
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False


class Game:

    def __init__(self):
        self.sequence = []
        self.next_step = 0
        self.level = 3
        self.buttons = [
            Button('azul',    (0, 0, 255),    50, 50, 200, 200),
            Button('amarela', (255, 255, 0), 250, 50, 200, 200),
            Button('verde',   (0, 255, 0),    50, 250, 200, 200),
            Button('ciano',   (0, 255, 255), 250, 250, 200, 200)]

    def new_sequence(self):
        """generate a sequence of n steps."""
        self.sequence = [random.randint(0, 3) for _ in range(self.level)]
        self.next_step = 0
        self.play_demo()
        return self.sequence

    def play_demo(self):
        print(self.sequence)

    def redraw(self, win):
        win.fill((255, 255, 255))
        for b in self.buttons:
            b.draw(win)

    def press_button(self, i):
        expect = self.sequence[self.next_step]
        print(f"pressed button {i}:", self.buttons[i].label)
        print(f"expecting button {expect} at step {self.next_step}")
        if i == expect:
            self.next_step += 1
            print("correto")
            if self.next_step == len(self.sequence):
                print("Você ganhou!")
                self.level += 1
                self.new_sequence()
        else:
            print("Errado!")
            self.play_demo()
            self.next_step = 0


def main():

    pygame.init()
    win = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Genius')

    game = Game()
    game.new_sequence()

    running = True

    while running:
        pygame.display.update()
        game.redraw(win)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, b in enumerate(game.buttons):
                    if b.isOver(pygame.mouse.get_pos()):
                        game.press_button(i)

    pygame.quit()


if __name__ == "__main__":
    main()
