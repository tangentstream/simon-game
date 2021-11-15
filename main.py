import pygame
import random
import time
pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Genius')


class Button:
    def __init__(self, color, x, y, width, height):
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
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

blue_button = Button((0, 0, 255), 50, 50, 200, 200)
outro_botao = Button((255, 255, 0), 250, 50, 200, 200)
botao_verde = Button((0, 255, 0), 50, 250, 200, 200)
botao_ciano = Button((0, 255, 255), 250, 250, 200, 200)

def redrawWindow():
    win.fill((255,255,255))
    blue_button.draw(win)
    outro_botao.draw(win)
    botao_verde.draw(win)
    botao_ciano.draw(win)

run = True

ordem = []

def sortear():
    time.sleep(1)
    numero = random.randint(1, 4)
    ordem.append(numero)
    print(ordem)




sortear()

while run:
    pygame.display.update()
    redrawWindow()

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            next_step = ordem[-1]
            mapping = {
                1: (blue_button, 'Boa'),
                2: (outro_botao, 'outro'),
                3: (botao_verde, 'verde'),
                4: (botao_ciano, 'ciano')}
            btn, label = mapping[next_step]

            if btn.isOver(pos):
                print(label)
                sortear()
            else:
                print('Errado')
                # ordem.clear()

pygame.quit()
