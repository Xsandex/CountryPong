from pygame import *


window = display.set_mode((500,500))

background = transform.scale(image.load('sad.jpg'),(500,500))


events = event.get()
events[0].type
clock = time.Clock()
#germany = transform.scale(image.load('Gremany.png'),(10,200))
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



            

class player_1(GameSprite):
    
    def control(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys_pressed[K_s] and self.rect.y < 415:
            self.rect.y += self.speed
class player_2(GameSprite):
    
    def control(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys_pressed[K_DOWN] and self.rect.y < 415:
            self.rect.y += self.speed
    
class Ball(GameSprite):
    def __init__(self,ball_image,player_x, player_y, size_x, size_y,speed_x):
        super().__init__(ball_image,player_x, player_y, size_x, size_y,speed_x)
        self.speed_x = speed_x
        self.speed_y = speed_x
    def update(self):
        global Germany
        global USSR
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if sprite.collide_rect(Germany,self) or sprite.collide_rect(USSR,self):
            self.speed_x *= -1
        if self.rect.y >= 490:
            self.speed_y *= -1
        if self.rect.y <= 0:
            self.speed_y *= -1
        if self.rect.x <= 0:
            self.speed_x *= -1
        if self.rect.x >= 490:
            self.speed_x *= -1
        
Germany = player_1('Gremany.png',25,250,10,100,5)
USSR = player_2('USSR.png',470,250,10,100,5)
Poland = Ball('POLAND.png',10,10,10,10,4)

group = sprite.Group()
group.add(Poland)

while game:
    window.blit(background,(0,0))

    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_a:
                poland = Ball('POLAND.png',Poland.rect.x,Poland.rect.y,10,10,4)
                group.add(poland)

    group.update()
                
    # Poland.move(Germany,USSR)
    group.draw(window)

    Germany.control()
    Germany.reset()

    USSR.control()
    USSR.reset()

    display.update()
    clock.tick(60)
