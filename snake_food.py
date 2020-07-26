import sys,random,time,pygame,PyInstaller
from pygame.locals import *


playsurface=pygame.display.set_mode((1280,720))
red=pygame.Color(255,0,0)
black=pygame.Color(0,0,0)
white=pygame.Color(255,255,255)

#此处为bgm设置，如果需要则将file的文件改为你所要用的音乐即可
# file ='bgm.mp3'
# pygame.mixer.init()
# track = pygame.mixer.music.load(file)
# pygame.mixer.music.play(-1)

def GameOver():


    playsurface.fill(black)

    pygame.draw.rect(playsurface,white,Rect(200,200,10,100))
    pygame.draw.rect(playsurface,white,Rect(200,200,100,10))
    pygame.draw.rect(playsurface, white, Rect(300, 200, 10, 100))
    pygame.draw.rect(playsurface, white, Rect(200, 300, 110, 10))

    pygame.draw.rect(playsurface, white, Rect(400, 200, 10, 90))
    pygame.draw.rect(playsurface, white, Rect(490, 200, 10, 90))
    pygame.draw.rect(playsurface, white, Rect(410, 290, 35, 10))
    pygame.draw.rect(playsurface, white, Rect(445, 300, 10, 10))
    pygame.draw.rect(playsurface, white, Rect(455, 290, 35, 10))

    pygame.draw.rect(playsurface, white, Rect(600, 200, 100, 10))
    pygame.draw.rect(playsurface, white, Rect(600, 200, 10, 110))
    pygame.draw.rect(playsurface, white, Rect(600, 300, 100, 10))
    pygame.draw.rect(playsurface, white, Rect(600, 245, 75, 15))

    pygame.draw.rect(playsurface, white, Rect(800, 200, 100, 10))
    pygame.draw.rect(playsurface, white, Rect(800, 200, 10, 110))
    pygame.draw.rect(playsurface, white, Rect(890, 200, 10, 50))
    pygame.draw.rect(playsurface, white, Rect(800, 240, 100, 10))
    pygame.draw.rect(playsurface, white, Rect(804, 250, 16, 10))
    pygame.draw.rect(playsurface, white, Rect(820, 260, 16, 10))
    pygame.draw.rect(playsurface, white, Rect(836, 270, 16, 10))
    pygame.draw.rect(playsurface, white, Rect(852, 280, 16, 10))
    pygame.draw.rect(playsurface, white, Rect(868, 290, 16, 10))
    pygame.draw.rect(playsurface, white, Rect(884, 300, 16, 10))

    pygame.display.flip()
    while True:

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_F5:
                    while True:
                        main()







def main():
    pygame.init()
    fpsClock=pygame.time.Clock()

    pygame.display.set_caption('寒假自学游戏贪吃蛇')
    #初始化蛇头起始位置
    snakePosition=[100,100]
    #初始化蛇的长度
    snakeBody=[[100,100],[80,100],[60,100]]
    foodPosition=[300,300]

    targetflag=1
    direction='right'

    changeDirection=direction
    gamespeed = 10
    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    changeDirection = 'right'
                if event.key == K_LEFT:
                    changeDirection = 'left'
                if event.key == K_UP:
                    changeDirection = 'up'
                if event.key == K_DOWN:
                    changeDirection = 'down'
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
                if event.key == K_8:
                    gamespeed += 1
                    fpsClock = pygame.time.Clock()
                    fpsClock.tick(gamespeed)
                if event.key == K_2 and gamespeed > 1:
                    gamespeed -= 1
                    fpsClock = pygame.time.Clock()
                    fpsClock.tick(gamespeed)
        #控制方向
        if changeDirection == 'left' and not changeDirection == 'right':
            direction = changeDirection
        if changeDirection == 'up' and not changeDirection == 'down':
            direction = changeDirection
        if changeDirection == 'right' and not changeDirection == 'left':
            direction = changeDirection
        if changeDirection == 'down' and not changeDirection == 'up':
            direction = changeDirection

        if direction == 'right':
            snakePosition[0] += 20
        if direction == 'left':
            snakePosition[0] -= 20
        if direction == 'up':
            snakePosition[1] -= 20
        if direction == 'down':
            snakePosition[1] += 20

        snakeBody.insert(0,list(snakePosition))
        #吃到食物
        if snakePosition[0] == foodPosition[0] and snakePosition[1] == foodPosition[1]:
            targetflag = 0
        else:
            snakeBody.pop()
        if targetflag == 0:
            bodylen=len(snakeBody)
            bodylenx = []
            listx = [n for n in range(0,64)]
            for b in range(bodylen):
                n=(snakeBody[b][0])/20
                bodylenx.insert(0,n)
            foodx = sorted(list(set(listx).difference(set(bodylenx))))
            x = random.sample(foodx,1)
            x = x[0]
            #生成食物
            bodyleny = []
            listy = [n for n in range(0, 36)]
            for b in range(bodylen):
                n = (snakeBody[b][1]) / 20
                bodylenx.insert(0, n)
            foody = sorted(list(set(listy).difference(set(bodyleny))))
            y = random.sample(foody, 1)
            y = y[0]


            foodPosition = [int(x*20),int(y*20)]
            targetflag = 1
        playsurface.fill(black)
        #画出蛇
        for positiion in snakeBody:
            pygame.draw.rect(playsurface,white,Rect(positiion[0],positiion[1],20,20))
            pygame.draw.rect(playsurface,red,Rect(foodPosition[0],foodPosition[1],20,20))
        pygame.display.update()
        #如果碰到边界，游戏结束
        if snakePosition[0]>1260 or snakePosition[0]<0:
            GameOver()
        elif snakePosition[1]>700 or snakePosition[1]<0:
            GameOver()


        #如果碰到自己，游戏结束
        bodylenth1=len(snakeBody)
        seatnumber=1
        for i in range(bodylenth1-1):
            if snakePosition == snakeBody[seatnumber]:
                GameOver()
            else:
                seatnumber +=1

        #游戏速度
        fpsClock.tick(gamespeed)


if __name__ == '__main__':

    main()







