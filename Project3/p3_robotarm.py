import pygame
import numpy as np

# 게임 윈도우 크기
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800

# 색 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def Rmat(deg):
    radian = np.deg2rad(deg)
    c = np.cos(radian)
    s = np.sin(radian)
    R = np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
    return R


def Tmat(a, b):
    H = np.eye(3)  # identity, 3x3
    H[0, 2] = a
    H[1, 2] = b
    return H


# Pygame 초기화
pygame.init()

# 윈도우 제목
pygame.display.set_caption("Drawing")

# 윈도우 생성
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 게임 화면 업데이트 속도
clock = pygame.time.Clock()

# 게임 종료 전까지 반복
done = False


# 폰트 선택(폰트, 크기, 두껍게, 이탤릭)
font = pygame.font.SysFont('FixedSys', 40, True, False)
degree = 10
degree2 = 20
degree3 = 20
# radian = np.deg2rad(degree)
# c = np.cos(radian)
# s = np.sin(radian)
# R = np.array([[c, -s], [s, c]])
# R, R.shape

poly = np.array([[-50, 0, 1], [50, 0, 1], [50, 20, 1], [-50, 20, 1]])
poly = poly.T  # 3*3 matrix

poly1 = np.array([[550, 800, 1], [450, 800, 1], [450, 650, 1], [550, 650, 1]])
poly1 = poly1.T  # 3*3 matrix

poly2 = np.array([[-30, 30, 1], [30, 30, 1], [30, -120, 1], [-30, -120, 1]])
poly2 = poly2.T  # 3*3 matrix

cor = np.array([100, 100, 1])
cor3 = np.array([0, 0, 1])
cor4 = np.array([0, -60, 1])
cor5 = np.array([30, -60, 1])
cor6 = np.array([-30, -60, 1])
cor7 = np.array([30, -90, 1])
cor8 = np.array([-30, -90, 1])


done = False
begin= True
mode = 0
while not done:
    # 이벤트 반복 구간
    if begin == True:
        screen.fill(WHITE)
        text_start = font.render('Choose mode 1 or 2', True, BLACK)
        text_start1 = font.render('Control mode1 : move automatically', True, BLACK)
        text_start2 = font.render('Control mode 2 : control by keyboard a, b, c', True, BLACK)
        screen.blit(text_start, [400, 300])
        screen.blit(text_start1, [300, 400])
        screen.blit(text_start2, [250, 500])
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:           
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    mode = 1
                    begin = False
                elif event.key == pygame.K_2:
                    mode = 2
                    begin = False
    else:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:           
                done = True

        screen.fill(WHITE)

        if mode == 1:
            degree += 1
            degree2 += 2
            degree3 += 3
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:           
                            done = True
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_a]:
                degree += 3
            if keystate[pygame.K_b]:
               degree2 += 3
            if keystate[pygame.K_c]:
               degree3 += 3              
     



        H = Tmat(0, 0)  
        H1 = Tmat(300, 600) @ Rmat(degree)
        H2 = Tmat(500, 680) @ Rmat(degree)
        H3 = Tmat(500, 680) @ Rmat(degree) @ Tmat(0, -100) @ Rmat(degree2)
        H4 = Tmat(500, 680) @ Rmat(degree) @ Tmat(0, -100) @ Rmat(degree2) @ Tmat(0, -100) @ Rmat(degree3)
        H5 = Tmat(500, 680) @ Rmat(degree) @ Tmat(0, -100) @ Rmat(degree2) @ Tmat(0, -100) @ Rmat(degree3) @Tmat(0,-100)
        pp = H @ poly1

        pp1 = H1 @ poly
        corp1 = H1@cor

        pp2 = H2 @ poly2
        corp2 = H2@cor

        pp3 = H3 @ poly2
        corp3 = H3@cor3

        pp4 = H4 @ poly2
        corp4 = H4@cor3

        corp5 = H5@cor3
        corp6 = H5@cor4
        corp7 = H5@cor5
        corp8 = H5@cor6
        corp9 = H5@cor7
        corp10 = H5@cor8


        q = pp[0:2, :].T  # N*2 matrix
        q1 = pp1[0:2, :].T  # N*2 matrix
        q2 = pp2[0:2, :].T  # N*2 matrix
        q3 = pp3[0:2, :].T  # N*2 matrix
        q4 = pp4[0:2, :].T  # N*2 matrix


        pygame.draw.polygon(screen, RED, q, 4)
        pygame.draw.polygon(screen, RED, q2, 4)
        pygame.draw.polygon(screen, RED, q3, 4)
        pygame.draw.polygon(screen, RED, q4, 4)    


        pygame.draw.circle(screen,(255,128,128),[500,680],3)
        
        pygame.draw.circle(screen,(255,128,128),corp3[:2],3)
        pygame.draw.circle(screen,(255,128,128),corp4[:2],3)
        #pygame.draw.circle(screen,(255,128,128),corp5[:2],3)
        #pygame.draw.circle(screen,(255,128,128),corp6[:2],3)
        pygame.draw.line(screen,RED,corp5[:2],corp6[:2],5)
        pygame.draw.line(screen,RED,corp7[:2],corp8[:2],5)
        pygame.draw.line(screen,RED,corp7[:2],corp9[:2],5)
        pygame.draw.line(screen,RED,corp8[:2],corp10[:2],5)
        
  
    # 화면에 텍스트 표시

    # 화면 업데이트
    pygame.display.flip()

    # 초당 60 프레임으로 업데이트
    clock.tick(60)

# 게임 종료
pygame.quit()
