#########################################################
## File Name: hangman.py                               ##
## Description: Starter for Hangman project - ICS3U    ##
#########################################################
import pygame
import random
import os

pygame.init()
winHeight = 480
winWidth = 700
screen=pygame.display.set_mode((winWidth,winHeight))
#---------------------------------------#
# initialize global variables/constants #
#---------------------------------------#
BLACK = (0,0, 0)
WHITE = (255,255,255)
RED = (255,0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)


current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets1') #specify path to image file


btn_font = pygame.font.SysFont("arial", 20)
guess_font = pygame.font.SysFont("arial", 24)
lost_font = pygame.font.SysFont('arial', 45)
word = ''
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

guess = []

Hang_pic = [pygame.image.load(os.path.join(assets_path, 'hangman0.png')), pygame.image.load(os.path.join(assets_path, 'hangman1.png')), pygame.image.load(os.path.join(assets_path, 'hangman2.png')), 
pygame.image.load(os.path.join(assets_path, 'hangman3.png')), pygame.image.load(os.path.join(assets_path, 'hangman4.png')), pygame.image.load(os.path.join(assets_path, 'hangman5.png')), 
pygame.image.load(os.path.join(assets_path, 'hangman6.png'))]

ind = 0


def hangmangame():
    global guess
    global Hang_pic
    global ind
    screen.fill(BLUE)
    # Buttons
    

    spaced = spacedOut(word, guess)
    label1 = guess_font.render(spaced, 1, BLACK)
    rect = label1.get_rect()
    length = rect[2]
    
    screen.blit(label1,(winWidth/2 - length/2, 400))

    pic = Hang_pic[ind]
    screen.blit(pic, (winWidth/2 - pic.get_width()/2 + 20, 150))
    pygame.display.update()


def randomWord():
    #file = open('words.txt')
    
    #f = file.readlines()
    words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
    i = random.randrange(0, len(words) - 1)

    return words[i][:-1]


def hang(guess):
    global word
    if guess.lower() not in word.lower():
        return True
    else:
        return False


def spacedOut(word, guess=[]):
    spacedWord = ''
    guessedLetters = guess
    for x in range(len(word)):
        if word[x] != ' ':
            spacedWord += '_ '
            for i in range(len(guessedLetters)):
                if word[x].upper() == guessedLetters[i]:
                    spacedWord = spacedWord[:-2]
                    spacedWord += word[x].upper() + ' '
        elif word[x] == ' ':
            spacedWord += ' '
    return spacedWord
            



def end(winner=False):
    global ind
    lostTxt = 'You Lose'
    winTxt = 'You win'
    hangmangame()
    pygame.time.delay(1000)
    screen.fill(GREEN)

    if winner == True:
        label = lost_font.render(winTxt, 1, BLACK)
    else:
        label = lost_font.render(lostTxt, 1, BLACK)

    wordTxt = lost_font.render(word.upper(), 1, BLACK)
    wordWas = lost_font.render('The answer was: ', 1, BLACK)

    screen.blit(wordTxt, (winWidth/2 - wordTxt.get_width()/2, 295))
    screen.blit(wordWas, (winWidth/2 - wordWas.get_width()/2, 245))
    screen.blit(label, (winWidth / 2 - label.get_width() / 2, 140))
    pygame.display.update()
    again = True
    while again:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                again = False
    reset()


def reset():
    global ind
    global guess   
    global word

    ind = 0
    guess = []
    word = randomWord()

#MAINLINE

word = randomWord()
done = False

while not done:
    hangmangame()
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            letter = pygame.key.name(event.key)
            if letter != None:
                guess.append(letter)
                
                if hang(letter):
                    if ind != 5:
                        ind += 1
                    else:
                        end()
                else:
                    print(spacedOut(word, guess))
                    if spacedOut(word, guess).count('_') == 0:
                        end(True)
        

pygame.quit()

# always quit pygame when done!
