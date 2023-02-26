import pygame # 1. pygame 선언
import random 
 
pygame.init() # 2. pygame 초기화
 
# 3. pygame에 사용되는 전역변수 선언
WHITE = (255,255,255) # 게임판 색깔
size = [800,800] # 게임 실행시 크기
screen = pygame.display.set_mode(size)
 
done= False # 게임종료 확인
clock= pygame.time.Clock() # FPS설정
 
# pygame에 사용하도록 비행기 이미지를 호출
airplane = pygame.image.load('images/plane.png') # 비행기 사진 업로
airplane = pygame.transform.scale(airplane, (60, 45)) # 비행기 사진 크기 정의
 
# 4. pygame 무한루프
def runGame():
    global done, airplane
    bomb_image = pygame.image.load('images/bomb.png')
    bomb_image = pygame.transform.scale(bomb_image, (50, 50))
    bombs = []
    x = 20 
    y = 24
    
    for i in range(5):
        rect = pygame.Rect(bomb_image.get_rect())
        rect.left = random.randint(0, size[0])
        rect.top = -100
        dy = random.randint(3, 9)
        bombs.append({'rect': rect, 'dy': dy})
 
    while not done: 
        clock.tick(60) #FPS 60으로 설정
        screen.fill(WHITE) 
 
        for event in pygame.event.get(): # [X] 키 누르면 게임 종료
            if event.type == pygame.QUIT:
                done=True
 
            # 방향키 입력에 대한 이벤트 처리
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_UP:
                    y -= 50
                elif event.key == pygame.K_DOWN:
                    y += 50
                elif event.key == pygame.K_RIGHT:
                    x += 50
                elif event.key == pygame.K_LEFT:
                    x -= 50
                    
        for bomb in bombs:
            bomb['rect'].top += bomb['dy']
            if bomb['rect'].top > size[1]:
                bombs.remove(bomb)
                rect = pygame.Rect(bomb_image.get_rect())
                rect.left = random.randint(0, size[0])
                rect.top = -100
                dy = random.randint(3, 9)
                bombs.append({'rect': rect, 'dy': dy})                    
    
        screen.blit(airplane, (x, y)) # 비행기가 움직이는 좌표
        
        screen.blit(bomb_image, bomb['rect'])
        pygame.display.update() # 게임 스크린 업데이트
 
runGame()
pygame.quit()