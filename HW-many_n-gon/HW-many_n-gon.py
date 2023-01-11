# -*- coding: utf-8 -*- 

import pygame
import numpy as np 

def nRegularGon(ngon):
    gons5 = []
    radius = 100
    for i in range(ngon):
        deg = i * 360. / ngon
        radian = deg * np.pi / 180
        c = np.cos(radian)
        s = np.sin(radian)
        x = radius * c 
        y = radius * s
        gons5.append([x,y])
    gons5 = np.array(gons5)
    return gons5 
def draw2(g5, color=(180, 180, 0)):
    n = g5.shape[0]
    for i in range(n):
        # for k in range(i+2, ?):
        pygame.draw.line(screen, color, g5[i%n], g5[(i+2)%n], 5)
    return 
def draw6(g6, color=(180, 180, 0)):
    n = g6.shape[0]
    for i in range(n):
        # for k in range(i+2, ?):
        pygame.draw.line(screen, color, g5[i%n], g5[(i+2)%n], 5)
    return 
# let's move the star to (700, 500)
def rotate(poly1, degree):
    radian = np.deg2rad(degree)
    c = np.cos(radian)
    s = np.sin(radian)
    Rr = np.array( [[ c, -s], [s, c] ] )
    #R, R.shape
    ppT1 = Rr @ poly1.T 
    pp1 = ppT1.T
    return pp1 
#
def tranlate(g, tvec):
    tvec = np.array(tvec)
    for i in range(g.shape[0]): # translation by transl vector
        g[i] = g[i] + tvec
    return g 
#

# 게임 윈도우 크기
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800

# 색 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 200, 180)
ORANGE = (255,94,0)
PURPLE = (217, 65, 197)
INDIGO = (5,0,153)
YELLOW = (255,228,0)



# Pygame 초기화
pygame.init()
info = pygame.display.Info()
SIZE = WIDTH, HEIGHT = info.current_w, info.current_h
print(WIDTH, HEIGHT)

# 윈도우 제목
pygame.display.set_caption("Drawing")

# 윈도우 생성
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 게임 화면 업데이트 속도
clock = pygame.time.Clock()

# 게임 종료 전까지 반복
done = False
# 폰트 선택(폰트, 크기, 두껍게, 이탤릭)


poly = np.array( [[350, 200], [250, 350], [450, 350]])
degree = 30
degree4 = 40
degree5 = 50
degree6 = 60
degree7 = 70
degree8 = 80
degree9 = 90


gons5 = nRegularGon(5)
gons6 = nRegularGon(6)
gons7 = nRegularGon(7)
gons8 = nRegularGon(8)
gons9 = nRegularGon(9)
gons10 = nRegularGon(10)
gons12 = nRegularGon(12)
# 게임 반복 구간
while not done:
    # 이벤트 반복 구간
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # 게임 로직 구간

    # 화면 삭제 구간

    # 윈도우 화면 채우기
    screen.fill(WHITE)      
    degree +=5
    degree4 += 7
    degree5 += 2
    degree6 += 1
    degree7 +=3
    degree8 +=4

    gons5r = rotate(gons5.copy(), degree)
    gons5t = tranlate(gons5r, [100, 100])
    pygame.draw.polygon(screen, RED, gons5t)

    gons6r = rotate(gons6.copy(), degree4)
    gons6t = tranlate(gons6r, [300, 100])
    pygame.draw.polygon(screen, ORANGE, gons6t)

    gons7r = rotate(gons7.copy(), degree5)
    gons7t = tranlate(gons7r, [500, 100])
    pygame.draw.polygon(screen, YELLOW, gons7t)

    gons8r = rotate(gons8.copy(), degree6)
    gons8t = tranlate(gons8r, [700, 100])
    pygame.draw.polygon(screen, GREEN, gons8t)

    gons9r = rotate(gons9.copy(), degree7)
    gons9t = tranlate(gons9r, [900, 100])
    pygame.draw.polygon(screen, BLUE, gons9t)

    gons10r = rotate(gons10.copy(), degree8)
    gons10t = tranlate(gons10r, [1100, 100])
    pygame.draw.polygon(screen, PURPLE, gons10t)

    
    gons5r = rotate(gons5.copy(), degree)
    gons5t = tranlate(gons5r, [500, 300])
    # pygame.draw.polygon(screen, BLACK, gons5t)
    draw2(gons5t, YELLOW)

    gons6r = rotate(gons6.copy(), degree)
    gons6t = tranlate(gons6r, [800, 300])
    # pygame.draw.polygon(screen, BLACK, gons5t)
    draw2(gons6t, YELLOW)

    gons8r = rotate(gons8.copy(), degree)
    gons8t = tranlate(gons8r, [1100, 300])
    # pygame.draw.polygon(screen, BLACK, gons5t)
    draw2(gons8t, YELLOW)

    radian = np.deg2rad(degree6)
    c = np.cos(radian)
    s = np.sin(radian)
    R = np.array( [[ c, -s], [s, c] ] )


    cor = np.array( [ 600, 800] )
    pcopy = gons5t.copy()
    for i in range(pcopy.shape[0]): # 1. translation to the origin
        pcopy[i] = pcopy[i] - cor 
    protated = (R @ pcopy.T).T      # 2. rotation 
    # 3. translation back 
    for i in range(protated.shape[0]): # 3. translation, back to origignal location
        protated[i] = protated[i] + cor 


    draw2(protated,YELLOW)
    radian = np.deg2rad(degree5)
    c = np.cos(radian)
    s = np.sin(radian)
    R = np.array( [[ c, -s], [s, c] ] )
    cor = np.array( [ 600, 1000] )
    pcopy = gons5t.copy()
    for i in range(pcopy.shape[0]): # 1. translation to the origin
        pcopy[i] = pcopy[i] - cor 
    protated = (R @ pcopy.T).T      # 2. rotation 
    # 3. translation back 
    for i in range(protated.shape[0]): # 3. translation, back to origignal location
        protated[i] = protated[i] + cor 
    draw2(protated,YELLOW)
    
   

    # 화면 업데이트
    pygame.display.flip()
    clock.tick(60)

# 게임 종료
pygame.quit()