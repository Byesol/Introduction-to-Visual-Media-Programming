# -*- coding: utf-8 -*- 
import pygame
import numpy as np 
import os

# 게임 윈도우 크기
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# 색 정의
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Pygame 초기화
pygame.init()

# 윈도우 제목
pygame.display.set_caption("Ball")

# 윈도우 생성
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')

# 게임 화면 업데이트 속도
clock = pygame.time.Clock()

# 공 초기 위치, 크기, 속도
ball_x = int(WINDOW_WIDTH / 2)
ball_y = int(WINDOW_HEIGHT / 2)
ball_dx = 4 # velocity x
ball_dy = 4 # velocity y 
ball_size = 40 # radius

mushroom_image_1 = pygame.image.load(os.path.join(assets_path, 'mushroom1.png'))
mushroom_image_2 = pygame.image.load(os.path.join(assets_path, 'mushroom2.png'))
mushroom_image_3 = pygame.image.load(os.path.join(assets_path, 'mushroom3.png'))
germ_1 = pygame.image.load(os.path.join(assets_path, 'germ1.png'))
germ_2 = pygame.image.load(os.path.join(assets_path, 'germ2.png'))
germ_3 = pygame.image.load(os.path.join(assets_path, 'germ3.png'))
germ_4 = pygame.image.load(os.path.join(assets_path, 'germ4.png'))
germ_5 = pygame.image.load(os.path.join(assets_path, 'germ5.png'))
germ_6 = pygame.image.load(os.path.join(assets_path, 'germ6.png'))
germ_7 = pygame.image.load(os.path.join(assets_path, 'germ7.png'))

# 키보드 이미지 초기 설정
keyboard_image = pygame.image.load(os.path.join(assets_path, 'keyboard.png'))
keyboard_x = int(WINDOW_WIDTH / 2)
keyboard_y = int(WINDOW_HEIGHT / 2)
keyboard_dx = 0
keyboard_dy = 0

sound = pygame.mixer.Sound(os.path.join(assets_path, 'bounce.wav'))

class Ball:
    def __init__(self,):
        self.x = np.random.randint(low=100, high=200)
        self.y = np.random.randint(low=100, high=200)
        self.radius = np.random.randint(low=1, high=30)
        self.dx = np.random.randint(-9, 10)
        self.dy = np.random.randint(-10, 11)
        self.color = (np.random.randint(low=0, high=256), 
                        np.random.randint(low=0, high=256),
                        np.random.randint(low=0, high=256))

        self.time = pygame.time.get_ticks()
        self.period = np.random.uniform(1000, 6000)
    
    def img_insert(self, image):
        self.width = image.get_width()
        self.height = image.get_height()
        self.img = image

    def update(self,):
        if 0:
            current_time = pygame.time.get_ticks()
            if current_time - self.time > self.period: # milisecond
                self.dx = np.random.randint(-19, 20)
                self.dy = np.random.randint(-20, 21)
                self.time = current_time
                pass

        self.x += self.dx 
        self.y += self.dy 

        if self.x + self.width > WINDOW_WIDTH:  # right side bounce
            self.dx *= -1
            sound.play()
        

        if self.x  < 0: # left side bounce
            self.dx *= -1
            sound.play()

        if self.y + self.height > WINDOW_HEIGHT: # bootom side bounce
            self.dy *= -1
            sound.play()

        if self.y  < 0: # top side bounce
            self.dy *= -1
            sound.play()


    def draw(self, screen):
        
        screen.blit(self.img, [self.x, self.y])
    
        
    

# 게임 종료 전까지 반복
done = False

ball = Ball()


#print(ball)
listOfBalls = []
for i in range(101):
    ball = Ball()
    listOfBalls.append(ball)

# 게임 반복 구간
while not done:
    # 이벤트 반복 구간
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keyboard_dx = -3
            elif event.key == pygame.K_RIGHT:
                keyboard_dx = 3
            elif event.key == pygame.K_UP:
                keyboard_dy = -3
            elif event.key == pygame.K_DOWN:
                keyboard_dy = 3
        # 키가 놓일 경우
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                keyboard_dx = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                keyboard_dy = 0


    
    keyboard_x += keyboard_dx
    keyboard_y += keyboard_dy
    

    # 게임 로직 구간
    # 속도에 따라 원형 위치 변경: state update / logic update / parameter update
    # ------------------------

    # -----------------------------------
    # update ball 2
    # your update code here

        
    # -----------------------------------
    # 윈도우 화면 채우기
    screen.fill(WHITE)
    screen.blit(keyboard_image, [keyboard_x, keyboard_y])

    # 화면 그리기 구간
    # 공 그리기
   

    for i in range(10):
        ball = listOfBalls[i]
        ball.img_insert(mushroom_image_1)     
        ball.update()   
        ball.draw(screen)
    for i in range(10,20):
        ball = listOfBalls[i]
        ball.img_insert(mushroom_image_2)     
        ball.update()   
        ball.draw(screen)
    for i in range(20,30):
        ball = listOfBalls[i]
        ball.img_insert(mushroom_image_3)     
        ball.update()   
        ball.draw(screen)
    for i in range(30,40):
        ball = listOfBalls[i]
        ball.img_insert(germ_1)     
        ball.update()   
        ball.draw(screen)
    for i in range(40,50):
        ball = listOfBalls[i]
        ball.img_insert(germ_2)     
        ball.update()   
        ball.draw(screen)
    for i in range(50,60):
        ball = listOfBalls[i]
        ball.img_insert(germ_3)     
        ball.update()   
        ball.draw(screen) 
    for i in range(60,70):
        ball = listOfBalls[i]
        ball.img_insert(germ_4)     
        ball.update()   
        ball.draw(screen) 
    for i in range(70,80):
        ball = listOfBalls[i]
        ball.img_insert(germ_5)     
        ball.update()   
        ball.draw(screen) 
    for i in range(80,90):
        ball = listOfBalls[i]
        ball.img_insert(germ_6)     
        ball.update()   
        ball.draw(screen)
    for i in range(90,101):
        ball = listOfBalls[i]
        ball.img_insert(germ_7)     
        ball.update()   
        ball.draw(screen)

      
    
   
    


    # 화면 업데이트
    pygame.display.flip()
    # 초당 60 프레임으로 업데이트
    clock.tick(60) # 60 frames per second
                   # ball_dx = 4
                   # ball_velocity_x = 4 pixels / 1 frame * 60 (frames / second)
                    #                = 240 pixels / second
# 게임 종료
pygame.quit()