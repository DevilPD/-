import pygame
import random
from pygame.constants import APPACTIVE

from pygame.draw import rect
from pygame.mixer import stop
from pygame.time import Clock

SIZE = 10

class Color:
    def __init__(self):
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.LIME_GREEN = (74, 155, 16)
        self.RED = (255,0,0)
        self.BLUE = (0,51,204)

    def random(self):
        r = 0
        r = random.randrange(1,4)
        if r == 1:
            return self.WHITE
        elif r == 2:
            return self.LIME_GREEN
        elif r == 3:
            return self.BLUE

class Timer:
    def __init__(self):
        self.time = 0

    def run(self):
        self.time += 0.01

class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.color = ()
        self.vx = 0
        self.vy = 0

        self.start_x = 0
        self.start_y = 0

    def gravity(self, time):
        self.vy = self.start_y + (98 * (time ** 2))/2 

    def update(self):
        self.x += self.vx
        self.y = self.vy

    def draw(self, screen, x, y):
        color = Color()
        pygame.draw.circle(screen, self.color, \
            [x, y], SIZE)  

class Mark:
    def __init__(self):
        color = Color()
        self.x = 0
        self.y = 0
        self.color = color.WHITE

    def marking(self, screen, x, y):
        pygame.draw.circle(screen, self.color, \
            [x, y], SIZE)  

class HashableRect(pygame.Rect):
    def __hash__(self):
        return hash(tuple(self))

def make_ball(x,y):
    ball = Ball()
    color = Color()

    ball.x = x
    ball.y = y
    ball.vx = 0 / 10 # 초속 0m로 가로방향 등속운동
    ball.vy = 98
    ball.color = color.RED

    ball.start_x = x
    ball.start_y = y

    return ball

def mark_ball(x,y):
    mark = Mark()

    mark.x = x
    mark.y = y

    return mark

def main():

    color = Color()
    pygame.init()

    screen = pygame.display.set_mode([1000, 1000])

    font = pygame.font.SysFont('새굴림',30)

    pygame.display.set_caption('Hello World!')

    clock = pygame.time.Clock()

    ball_list = []
    stop_ball_list = []

    done = False 

    timer_active = False
    stop = True
    time = 0.00

    while not done:
        if stop == False:
            timer_active = True

        t = round(time, 2)
        word = str(t) + '초'

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                ball = make_ball(event.pos[0], event.pos[1])
                timer_active = False
                stop = False
                ball_list = []
                stop_ball_list = []
                time = 0.00
                ball_list.append(ball)
        
        key_event = pygame.key.get_pressed()

        if key_event[pygame.K_ESCAPE]:
            ball_list = []
            stop_ball_list = []
            timer_active = False
            stop = True
            time = 0.00

        if timer_active == True:
            time += 0.01

        for ball in ball_list:
            ball.gravity(time)
            ball.update()

        text = font.render(word,True,color.WHITE)

        screen.fill(color.BLACK)
        screen.blit(text,(900,30))

        for ball in ball_list:
            color = Color()
            ball.draw(screen, ball.x, ball.y)

            if t.is_integer() == True :
                mark = mark_ball(ball.x, ball.y)
                stop_ball_list.append(mark)

            try:
                for sb in stop_ball_list:
                    sb.marking(screen, sb.x, sb.y)
            except:
                pass

                

        dt = clock.tick_busy_loop(100)
        pygame.display.update()
        

    pygame.quit()

if __name__ == '__main__':
    main()

# https://m.blog.naver.com/kkang2yah/222035127326