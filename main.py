import pygame
import random
import time
pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Genius')


class button():
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

blue_button = button((0, 0, 255), 50, 50, 200, 200)
outro_botao = button((255, 255, 0), 250, 50, 200, 200)
botao_verde = button((0, 255, 0), 50, 250, 200, 200)
botao_ciano = button((0, 255, 255), 250, 250, 200, 200)

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

while run == True:
    pygame.display.update()
    redrawWindow()

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if ordem.__getitem__(-1) == 1:
                if blue_button.isOver(pos):
                    print('Boa')
                    sortear()
                else:
                    print('Errado')
                    ordem.clear()

            if ordem.__getitem__(-1) == 2:
                if outro_botao.isOver(pos):
                    print('outro')
                    sortear()
                else:
                    print('Errado')
                    ordem.clear()

            if ordem.__getitem__(-1) == 3:
                if botao_verde.isOver(pos):
                    print('verde')
                    sortear()
                else:
                    print('Errado')
                    ordem.clear()

            if ordem.__getitem__(-1) == 4:
                if botao_ciano.isOver(pos):
                    print('ciano')
                    sortear()
                else:
                    print('Errado')
                    ordem.clear()
            run = True

pygame.quit()
