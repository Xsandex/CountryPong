from pygame import *


window = display.set_mode((500,500))

game = True
pressed_key = pygame.key.get_pressed()

class player_1():
    def __init__(self,player_speed,player_size)
        self.speed = player_speed
        self.size = player_size
    def control():
        if pressed_key


while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False


clock.tick(60)
pygame.display.update()
