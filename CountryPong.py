from pygame import *


window = display.set_mode((500,500))

background = transform.scale(image.load(r"C:\Users\STAS\OneDrive\Рабочий стол\CountryPong-main\sad.jpg"),(500,500))


events = event.get()
events[0].type
clock = time.Clock()
germany = transform.scale(image.load(r'C:\Users\STAS\OneDrive\Рабочий стол\CountryPong-main\Gremany.png'),(10,200))
game = True
class GameSprite(sprite.Sprite):
 #конструктор класса
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #вызываем конструктор класса (Sprite):
       sprite.Sprite.__init__(self)


       #каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed


       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 #метод, отрисовывающий героя на окне
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Ball(GameSprite):
    def move():
        if sprite.collide_rect(player_1,Ball):
            self.rect.x -= self.speed
            self.rect.y -= self.speed
        if sprite.collide_rect(player_2,Ball):
            self.rect.x += self.speed
            self.rect.y += self.speed
class player_1(GameSprite):
    
    def control():
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys_pressed[K_s] and self.rect.y < 415:
            self.rect.y += self.speed
class player_2(GameSprite):
    
    def control():
        keys_pressed = key.get_pressed()
        if keys_pressed[KEY_UP] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys_pressed[KEY_DOWN] and self.rect.y < 415:
            self.rect.y += self.speed
    

Germany = player_1(r'C:\Users\STAS\OneDrive\Рабочий стол\CountryPong-main\Gremany.png',25,250,10,100,5)
USSR = player_2(r'C:\Users\STAS\OneDrive\Рабочий стол\CountryPong-main\USSR.png',470,250,10,100,5)
Poland = Ball(r'C:\Users\STAS\OneDrive\Рабочий стол\CountryPong-main\POLAND.png',250,250,10,10,5)

while game:
    window.blit(background,(0,0))

    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(germany,(10,100))
    display.update()
clock.tick(60)
     
