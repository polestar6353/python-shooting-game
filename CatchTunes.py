import pygame
import time
import random

#오브젝트를 넣기 위한 클래스
class obj:       #오브젝트를 제작하기 위한 클래스이다.
    def __init__(self):  #기본적으로 선언되면, 객체의 x좌표와 y좌표, 그리고 스피드가 0으로 초기화되어 주어진다.
        self.x = 0
        self.y = 0
        self.speed = 0
    def put_img(self,address): #이미지를 작성하기 위한 함수. 만일 확장자가 png면 convert_alpha를, 그렇지 않으면 그냥 이미지를 부여하고, 해당 이미지의 크기의 가로와 세로를 sx, sy로 갖는다.
        if address[-3:] =="png":
            self.img = pygame.image.load(address).convert_alpha()
        else :
            self.img = pygame.image.load(address)
        self.sx, self.sy = self.img.get_size()
    def change_size(self, sx, sy): #이미지의 크기를 변경하기 위한 함수. 원하는 sx, sy값을 입력하면 해당 크기로 가로 세로가 리사이징 된 이미지를 갖게 된다.
        self.img = pygame.transform.scale(self.img, (sx, sy))
        self.sx, self.sy = self.img.get_size()
    def show(self): #이미지를 화면에 표시한다.
        screen.blit(self.img, (self.x, self.y))


def init_game(): # 게임 시작시 한번만 호출하면 된다.
    global screen, clock, font, enermy, enermy_img, enermy_sound, enermy_rand_respawn, music_good, volum_val, background_normal,\
        music_bad, music_stage, music_quize, best_catch, tutorial_save_speed, run, maingame, background_hard, background, size, player, background_normal_start,\
        hardmodemessege,enermy_sound_piano, hardmodemessage, supportmodemessage, background_result, background_volum, background_tutorial, background_hard_start
    pygame.init()  # 게임을 초기화시킨다

    size = [700, 800]  # 게임의 사이즈. 몇정도가 적당?
    screen = pygame.display.set_mode(size)

    title = "catch tunes"
    pygame.display.set_caption(title)  # 제목을 적고 붙인다.

    clock = pygame.time.Clock()  # fps설정하기 위해 Clock을 설정한다.
    font = pygame.font.Font(r"resource\font\NanumGothic.ttf", 20)  # 게임용 폰트. 나눔고딕을 20포인트로 사용할 예정.

    # 이하의 while문 밖의 값들은, 게임중에 단 한번만 불러오면 되기 때문에 따로 함수로 만들지 않음.
    # 캐릭터 설정
    player = obj()
    player.put_img(r"resource\image\캐릭터.jpg")
    player.change_size(40, 40)
    player.x = round(size[0] / 2 - player.sx / 2)
    player.y = size[1] - player.sy - 5
    player.speed = 15


    # 모드 설정 관련

    hardmodemessage=obj()
    hardmodemessage.put_img(r"resource\image\하드모드ONOFF.jpg")
    hardmodemessage.change_size(230,40)
    hardmodemessage.x=460
    hardmodemessage.y=600

    supportmodemessage=obj()
    supportmodemessage.put_img(r"resource\image\서포트모드ONOFF.jpg")
    supportmodemessage.change_size(230,40)
    supportmodemessage.x=460
    supportmodemessage.y=550

    # 배경 설정



    background = obj()
    background.put_img(r"resource\image\메인화면.jpg")

    background_normal = obj()
    background_normal.put_img(r"resource\image\노멀모드입장.jpg")

    background_hard = obj()
    background_hard.put_img(r"resource\image\하드모드입장.jpg")

    background_normal_start = obj()
    background_normal_start.put_img(r"resource\image\노멀모드진행.jpg")

    background_hard_start = obj()
    background_hard_start.put_img(r"resource\image\하드모드진행.jpg")

    background_tutorial = obj()
    background_tutorial.put_img(r"resource\image\튜토리얼모드입장.jpg")

    background_volum = obj()
    background_volum.put_img(r"resource\image\볼륨창.jpg")

    background_result = obj()
    background_result.put_img(r"resource\image\결과화면.jpg")
    # 적 설정
    enermy = []
    enermy_img = [r"resource\image\도.jpg", r"resource\image\레.jpg", r"resource\image\미.jpg", r"resource\image\파.jpg",\
                  r"resource\image\솔.jpg", r"resource\image\라.jpg", r"resource\image\시.jpg", r"resource\image\높은도.jpg"]
    enermy_sound = [r"resource\sound\낮은도.wav", r"resource\sound\레.wav", r"resource\sound\미.wav", r"resource\sound\파.wav",\
                    r"resource\sound\솔.wav", r"resource\sound\라.wav", r"resource\sound\시.wav", r"resource\sound\높은도.wav"]
    enermy_sound_piano = [r"resource\sound\피아노도.wav",r"resource\sound\피아노레.wav",r"resource\sound\피아노미.wav",\
                          r"resource\sound\피아노파.wav",r"resource\sound\피아노솔.wav",r"resource\sound\피아노라.wav",\
                          r"resource\sound\피아노시.wav",r"resource\sound\피아노높은도.wav"]
    enermy_rand_respawn = [0, 1, 2, 3, 4, 5, 6, 7]  # 적이 나타나는 위치를 랜덤하게 바꿔주기 위해 사용할 리스트.

    # 음악 설정
    music_good = pygame.mixer.Sound(r"resource\sound\정답.wav")  # 정답을 맞추면 재생할 음악.
    music_bad = pygame.mixer.Sound(r"resource\sound\부부.wav")  # 틀리면 재생할 음악
    music_stage = pygame.mixer.Sound(r"resource\sound\엔딩화면.wav")  # 엔딩 화면에서 사용할 음악.
    music_quize = ['', '', '', '', '', '', '', '']  # 음악을 사용하기 위해 일곱개의 빈 배열을 먼저 초기화 한다.
    volum_val=1
    # 기타 설정
    best_catch = 0
    tutorial_save_speed = 5

    run = True  # 메인 반복문을 반복하기 시작한다.
    maingame = "메뉴"  # 시작하면 메인화면으로 갈 수 있게 하기 위해.

#게임 초기값들과 관련이 있는 함수
def start_setting():
    global left_go, right_go, up_go, down_go, space_go, respawn, crashble, a_list, speedup, catch_count, hardmode, Starting_hardmod, boom_event, \
        stopTime, boom_count, speed_save, boom_list, m_list, esc_event, supportmode, easymode, pianomode, stage_music

    # 시작 이벤트 기본 설정. 키보드
    left_go = False
    right_go = False
    up_go = False
    down_go = False
    space_go = False
    esc_event = False
    # 시작 이벤트 기본 설정. 적
    respawn = True
    crashble = False
    a_list = []
    speedup = 0
    catch_count = 0

    #각종 모드 및 음악에 대한 설정.
    easymode = False
    hardmode = False
    Starting_hardmod = False
    supportmode = False
    pianomode = False
    stage_music = True

    # 폭탄 관련 이벤트
    boom_event = False
    stopTime = 0
    speed_save = 0
    boom_count = 3
    boom_list = []

    # 미사일 리스트
    m_list = []

#시작화면과 관련된 함수
def main_menu():
    global maingame, Starting_hardmod, hardmode, player, background_normal_start, size, supportmode, pianomode, volum_val, hardmodemessage, supportmodemessage

    clock.tick(60)                      #시작화면도 60프레임.
    for event in pygame.event.get():    #이벤트를 받는다
        if event.type ==pygame.QUIT:     #종료버튼을 누르면 종료.
            maingame = "닫기"
        if event.type == pygame.KEYDOWN: #키보드 이벤트를 받는다.
            if event.key == pygame.K_h: #키보드 윗 키를 눌렀을때,
                if(hardmode==True):      #하드모드였다면
                    hardmode=False       #하드모드를 끈다
                    Starting_hardmod=False #스타팅 하드모드는 속도가 5.0부터 시작하는 기본 하드모드 옵션이다.
                else:                    #하드모드가 아니였다면
                    hardmode=True        #하드모드를 켠다.
                    Starting_hardmod=True
            elif event.key == pygame.K_p: #p가 눌러지면
                if(supportmode==True):    #서포트모드가 True였다면
                    supportmode=False     #끈다
                else:                     #아니라면
                    supportmode=True      #켠다

                    #하드모드가 설정되었습니다 메세지 출력
            elif event.key == pygame.K_s:   #s가 입력되면 게임시작으로
                maingame="게임시작"
            elif event.key == pygame.K_t:    #t가 입력되면 튜토리얼로
                maingame="튜토리얼"
            elif event.key == pygame.K_ESCAPE:  #esc가 입력되면 종료로
                maingame="닫기"
            elif event.key == pygame.K_1:       #1번키가 입력되면 볼륨조절로
                maingame="소리조절"
            elif event.key == pygame.K_g:       #피아노모드를 ON OFF
                if(pianomode==True):
                    pianomode=False
                    testsound_guitar = pygame.mixer.Sound(enermy_sound[0])
                    testsound_guitar.set_volume(volum_val)
                    testsound_guitar.play()
                elif(pianomode==False):
                    pianomode=True
                    testsound_piano = pygame.mixer.Sound(enermy_sound_piano[0])
                    testsound_piano.set_volume(volum_val)
                    testsound_piano.play()
    background.show()                   #시작화면을 그린다.

    if (hardmode == True):
        hardmodemessage.show()
    if (supportmode ==True):
        supportmodemessage.show()


    text11 = font.render('기타 ', True, (255,255,255))
    text12 = font.render('피아노', True,(255,255,255))
    if(pianomode==True):
        screen.blit(text12, (405,400))
    elif(pianomode==False):
        screen.blit(text11, (405,400))

    pygame.display.flip()

    player.x = round(size[0] / 2 - player.sx / 2)  # 플레이어의 위치를 중앙점으로 고정한다.(이걸 쓰는 이유는 위로 부딪혀서 가서 죽었을때 다시할때 위치 바꾸기가...)
    player.y = player.y = size[1] - player.sy - 5  # 플레이어의 위치를 중앙점으로 고정한다.(이걸 쓰는 이유는 위로 부딪혀서 가서 죽었을때 다시할때 위치 바꾸기가...)

def game_start():
    global maingame
    clock.tick(60)
    for event in pygame.event.get():    #이벤트를 받는다
        if event.type ==pygame.QUIT:     #종료버튼을 누르면 종료.
            maingame = "닫기"
        if event.type == pygame.KEYDOWN: #키보드 이벤트를 받는다.
            if event.key == pygame.K_SPACE: #키보드 스페이스바를 눌렀을떄.
                maingame = "게임진짜시작"
            elif event.key == pygame.K_ESCAPE:
                maingame = "메뉴"

    if (hardmode == True):  # 하드모드라면
        background_hard.show()  # 하드모드의 배경을 그린다
    else:
        background_normal.show()  # 아니라면 기본모드의 배경을 그린다

    pygame.display.flip()

#키 이벤트를 받음.
def get_key_Event():
    # 키 이벤트를 받는다.
    global maingame, left_go, right_go, up_go, down_go, space_go, boom_event, esc_event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 게임을 종료하면.
            maingame = "닫기"
        if event.type == pygame.KEYDOWN:  # 키보드를 누를 떄.
            if event.key == pygame.K_LEFT:
                left_go = True
            elif event.key == pygame.K_RIGHT:
                right_go = True
            elif event.key == pygame.K_UP:
                up_go = True
            elif event.key == pygame.K_DOWN:
                down_go = True
            elif event.key == pygame.K_SPACE: #발사키
                space_go = True
            elif event.key == pygame.K_z:   #폭탄키(z)
                boom_event = True
            elif event.key == pygame.K_ESCAPE:
                esc_event =True

        elif event.type == pygame.KEYUP:  # 키보드를 뗄 때.
            if event.key == pygame.K_LEFT:
                left_go = False
            elif event.key == pygame.K_RIGHT:
                right_go = False
            elif event.key == pygame.K_UP:
                up_go = False
            elif event.key == pygame.K_DOWN:
                down_go = False
            elif event.key == pygame.K_SPACE:
                space_go = False

#키 이벤트의 처리. 이동.
def player_move():
    global player
    if left_go == True:             #왼쪽이동
        player.x -= player.speed
        if player.x <=0:            #왼쪽끝범위제한
            player.x = 0
    elif right_go == True:          #오른쪽이동
        player.x += player.speed
        if player.x+player.sx >=size[0]:   #오른쪽끝범위제한
            player.x = size[0] - player.sx
    if up_go ==True:                #위와 묶지 않은것은 대각이동을 포함하기 위해. 위쪽이동.
        player.y -= player.speed
        if player.y<=100:            #위쪽이동제한
            player.y =100
    elif down_go == True:           #아래쪽이동
        player.y += player.speed
        if player.y>size[1]-player.sy-5:    #아래쪽이동제한
            player.y=size[1]-player.sy-5

#무기 발사와 관련된 함수.
def player_shot():
    global space_go
    d_list = []   #미사일을 지우기 위한 리스트.
    if space_go == True:             #스페이스바가 눌러져 있는 상태라면,
        missile1 = obj()             #미사일 객체를 만든다.
        missile1.put_img(r"resource\image\미사일.jpg")
        missile1.change_size(10, 10)
        missile1.x = player.x + round(player.sx / 2) - round(missile1.sx/2)
        missile1.y = player.y - 2
        missile1.speed = 20
        m_list.append(missile1)      #미사일을 m 리스트에 담아서 여러개 존재할 수 있게 한다.
        space_go = False
    for i in range(len(m_list)):     #m리스트에 있는 미사일 하나하나마다.
        m = m_list[i]
        m.y -= m.speed               #미사일은 위로 계속 진행해 나간다.
        if m.y <= -10:               #미사일이 화면 밖으로 나가면. d_list에 담는다.
            d_list.append(i)
    d_list.reverse()                 #인덱스를 뒤집어줘서 한번에 다수를 처리할때의 에러가 나지 않게 함.
    for d in d_list:                 #d리스트에 있는 미사일의 인덱스를 찾아 m리스트에서 삭제.
        del m_list[d]


#폭탄과 관련된 이벤트
#폭탄을 사용시
def boom_start(): #폭탄 이벤트. 정지시킴
    global boom_count,boom_event, enermy, stopTime, speed_save
    if(boom_count>0):                             #붐은 주어진 갯수만큼만 사용할 수 있다.
        boom_count-=1                             #사용하면 갯수가 줄어든다.
        stopTime = time.time()                    #사용즉시 시간을 스톱 타임이라는 변수에 담는다.
        for i in range(len(enermy_img)):          #적 물체들에 대하여
            if(enermy[i].speed!=0):               #붐의 연속 사용을 막기 위해(연속 저장시 속도가 0으로 고정되는 문제가 있었음)
                speed_save=enermy[i].speed        #원래 적 물체의 속도를 speed_save에 저장
            enermy[i].speed=0                     #물체의 현재 속도를 0으로
    boom_event = False
#폭탄이 끝날때
def boom_end(): #폭탄이 끝남. 다시이동시킴
    global boom_event, enermy, stopTime, speed_save
    for i in range(len(enermy_img)):              #모든 적에 대해~
        enermy[i].speed = speed_save              #저장된 속도를 돌려준다.
#폭탄의 시작과 끝을 체크.
def boom_check():
    if boom_event==True:
        boom_start()
    if (time.time() > stopTime + 2 and stopTime != 0): #붐의 효과는 2초.
        boom_end()
#폭탄이 나오는 이벤트
def Drop_boom():
    #폭탄이 나오는 이벤트. 폭탄이 내려온다.
    d_list=[]                 #
    if random.random() > 0.999: #((1-0.999)*60*100%), 즉. 6%확률로 매초 폭탄이 나온다. 확률조정 필요.
        boom_item = obj()      #boom_item을 오브젝트화.
        boom_item.put_img(r"resource\image\폭탄.jpg")
        boom_item.change_size(50, 50)
        boom_item.x=random.randrange(0, size[0] - player.sx-round(player.sx/2)) #붐은 플레이어가 갈 수 있는 랜덤 범위 내에서 떨어진다.
        boom_item.y=10
        boom_item.speed=5
        boom_list.append(boom_item)
    for i in range(len(boom_list)):
        b = boom_list[i]
        b.y += b.speed
        if b.y>=size[1]:       #붐이 화면 밑으로 내려가면
            d_list.append(i)   #d리스트에 붐을 담는다.
    d_list.reverse()           #d리스트의 인덱스를 뒤집고
    for d in d_list:           #d리스트에 있는 붐을 꺼내 지운다.
        del(boom_list[d])

#적이 나오는 이벤트
def Drop_enermy():
            global respawn, target, crashble, speedup, target_number, volum_val
            if hardmode==True:
                random.shuffle(enermy_rand_respawn)       #랜덤하게 나온다!
            else:
                enermy_rand_respawn.sort()
            if respawn == True:
                for i in range(len(enermy_img)):
                    respawn = False           #다내려가면 True한다
                    enermy.append(i)  # 적을 만들어보자
                    enermy[i] = obj()
                    enermy[i].put_img(enermy_img[i])
                    enermy[i].change_size(int(size[0]/len(enermy_img)),200)  # 사실 (size[0]/len(enermy_img),40)
                    enermy[i].x = (size[0]/len(enermy_img))*enermy_rand_respawn[i]  # 사실 (size[0]/len(enermy_img))*i
                    enermy[i].y = -200
                    enermy[i].speed = 5 + speedup

                    if(hardmode==True and Starting_hardmod==False):    #하드모드는 속도 초기화 한번.
                        enermy[i].speed=5
                        speedup=0
                    if(pianomode==True):            #피아노모드가 트루면
                        music_quize[i] = pygame.mixer.Sound(enermy_sound_piano[i]) #피아노소리를담고
                    elif (pianomode==False):        #피아노모드가 펄스면
                        music_quize[i] = pygame.mixer.Sound(enermy_sound[i])    #기타소리를담아라.
                    music_quize[i].set_volume(volum_val)
                    a_list.append(enermy[i])
                target_number=random.randint(0,len(enermy_img)-1)
                target=enermy[target_number]
                music_quize[target_number].play()
                # print(enermy_img[target_number])     #타겟이 무엇인지 프린트해준다
                crashble = True

            d2_list = []
            for i in range(len(a_list)):
                a = a_list[i]
                a.y += a.speed
                if a.y>=size[1]:
                    d2_list.append(i)
                    speedup+=0.03
            d2_list.reverse()               #인덱스를 뒤집어줘서 한번에 다수를 처리할때의 에러가 나지 않게 함.
            for d in d2_list:
                del(a_list[d])
                respawn = True

#충돌과 관련된 이벤트
def crash(a,b):  #충돌 판단
    if (a.x-b.sx+5 <= b.x) and (b.x <= a.x+a.sx-5):
        if (a.y-b.sy < b.y) and (b.y <= a.y+a.sy):
            return True     #a,b객체가 충돌 범위 내에 있으면 True를, 그외의 경우는 False를 리턴한다.
        else : return False
    else :
        return False

#적을 맞췄을 때의 이벤트.
def crash_missile_enermy():
            global maingame, catch_count, crashble

            dm_list = []    #맞춰진 미사일들을 지우기 위한 리스트를 만든다.
            da_list = []    #맞춰진 적들을 지우기 위한 리스트를 만든다.
            for i in range(len(m_list)):    #발사되어있는 미사일들 중
                for j in range(len(a_list)):    #현재 존재하는 적들 중.
                    m = m_list[i]               #미사일 1개의 개체와
                    a = a_list[j]               #적 1개의 개체에 대해
                    if crash(m, a) == True:     #만일 충돌한다면(True)라면,
                        if(a!=target):            #그 적이 타겟 속성이 아니라면,
                            music_bad.play()    #뿌뿌 하는 음악을 재생한다
                            maingame = "결과화면"       #타겟이 아니면 플레이어가 패배하기 때문..
                        else:                   #맞춘 적이 타겟 속성이라면
                            music_good.play()   #정답 음악을 재생한다.
                            catch_count +=1     #정답 카운트를 1 늘린다.
                            for k in range(len(a_list)):    #남아있는 적들을
                                a_list[k].change_size(0,0)  #사이즈를 0x0으로 한다(1픽셀로 만듬. 왜? ->안보이게 하기 위해서.)
                                crashble=False  #1픽셀이라 안보여도 닿으면 죽기 때문에, 죽지 않게 하기 위해 크래시블을 False로 해둔다.(나중에 적과 나의 충돌 부분 참고)
                        dm_list.append(i)       #충돌된 미사일을 dm_list에
                        da_list.append(j)       #충돌된 적을 dm_list에
            dm_list = list(set(dm_list))        #혹시나 충돌 판정이 오래 남아 중복될수 있으므로 set으로 바꾸고 다시 list화시킨다.
            da_list = list(set(da_list))
            dm_list.reverse()                   #지울때 에러를 피하기 위해 인덱스를 뒤집어준다.
            da_list.reverse()
            for dm in dm_list:                  #dm리스트와 da리스트에 있는 개체들을 뽑아 원래 미사일과, 적 리스트에서 지워준다.
                del m_list[dm]
            for da in da_list:
                del a_list[da]

#내가 폭탄과 부딪혔을때의 이벤트.
def crash_player_bomb():
    global boom_count

    d_list = []                         #먹은 폭탄을 게임내에서 지우기 위한 리스트.
    for i in range(len(boom_list)):     #떨어지는 폭탄 리스트들에 대하여
        b = boom_list[i]                #b는 리스트 내의 폭탄이다.
        if crash(b, player) == True:    #폭탄과 플레이어가 충돌한다면
            boom_count += 1             #폭탄 갯수를 1개 늘려라.
            d_list.append(i)            #충돌된 폭탄을 d리스트에 넣어라
    d_list = list(set(d_list))          #d리스트에서 중복을 제거
    d_list.reverse()                    #d리스트의 인덱스를 뒤집는다
    for d in d_list:                    #폭탄리스트에서 먹은 폭탄을 제거.
        del boom_list[d]

#내가 적과 부딪혔을때의 이벤트
def crash_player_enermy():
    global maingame
    if (crashble == True):                    #crashble이 True라면
        for i in range(len(a_list)):          #화면에 있는 모든 적들에 대해
            a = a_list[i]
            if crash(a, player) == True:      #플레이어와 적이 충돌시
                maingame = "결과화면"                 #엔딩화면으로

#게임에서 점수창을 표시하는 이벤트
def print_ingame_score():
    global best_catch, target_number
    if catch_count>=best_catch:   #현재 정답 수가 최고 기록을 넘어가면
        best_catch=catch_count    #최고 기록이 된다.
    text_score = font.render('맞춘 정답 수: %s' % catch_count, True, (255,255,255))    #현재 스코어를 작성.
    screen.blit(text_score, (5,5))                                                 #현재 스코어를 보여줌
    text_best_score = font.render('최고 기록: %s' % best_catch, True, (255,255,255))   #최대 스코어를 작성
    screen.blit(text_best_score, (5,35))                                           #최대 스코어를 보여줌
    text_boomcount = font.render('남은 필살기 수: %s' % boom_count, True, (255, 255, 255)) #폭탄 수를 작성.
    screen.blit(text_boomcount, (size[0]-160, 5))
    if(supportmode==True):
        target_name=enermy_img[target_number][15:-4]
        text_supportmode = font.render(target_name,True, (255, 255, 255))
        screen.blit(text_supportmode, (size[0]-140, size[1]/2))

def master_volum():
    global music_stage,music_bad,music_stage,volum_val

    music_good.set_volume(volum_val)
    music_bad.set_volume(volum_val)
    music_stage.set_volume(volum_val)

def tutorial():
    global maingame
    clock.tick(60)
    for event in pygame.event.get():  # 이벤트를 받는다
        if event.type == pygame.QUIT:  # 종료버튼을 누르면 종료.
            maingame = "닫기"
        if event.type == pygame.KEYDOWN:  # 키보드 이벤트를 받는다.
            if event.key == pygame.K_SPACE:  # 키보드 스페이스바를 눌렀을떄.
                maingame = "튜토리얼시작"
            elif event.key == pygame.K_ESCAPE:
                maingame = "메뉴"

    background_tutorial.show()
    pygame.display.flip()



init_game()
while(run == True):
    music_stage.stop() #만일 게임오버 음악이 나오고 있었으면 끈다.
    start_setting() #초기값들을 다시 세팅해준다.

    #########메인메뉴 부분#############
    while(maingame == "메뉴"):
        main_menu()
    #########메인게임 부분###############
    while(maingame == "게임시작"):
        game_start()


    while(maingame == "게임진짜시작"):
        clock.tick(60) #프레임 수
        master_volum()
        get_key_Event() #키관련 이벤트를 불러옴

        player_move()   #움직임 관련 이벤트를 불러옴

        player_shot()   #미사일 발사 관련 이벤트를 불러옴

        boom_check()  #폭탄 사용관련 이벤트
        Drop_boom() #폭탄이 내려온다

        Drop_enermy() #적이 내려온다
        crash_missile_enermy() #적과 미사일이 충돌했을 시.

        crash_player_bomb()
        crash_player_enermy()

        # 그리기 (레이어는 먼저 그린게 뒤로 간다)
        if(hardmode==True):           #하드모드라면
            background_hard_start.show()    #하드모드의 배경을 그린다
        else:
            background_normal_start.show()         #아니라면 기본모드의 배경을 그린다
        player.show()
        for m in m_list:              #미사일을 그린다
            m.show()
        for b in boom_list:           #폭탄을 그린다
            b.show()
        for a in a_list:              #적을 그린다
            a.show()

        if catch_count>=20:           #20개 이상 정답을 맞추면
            hardmode=True             #하드모드에 진입한다.
                             #폭탄 수를 보여줌
        print_ingame_score()
        pygame.display.flip()   #업데이트

    while(maingame=="결과화면"):  #게임오버된다면,
        clock.tick(60)

        for event in pygame.event.get():
            if event.type ==pygame.QUIT:         #게임을 종료하면.
                maingame = "닫기"                    #종료됨
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  #스페이스바를 누르면
                    maingame = "메뉴"                 #메인화면으로
                if event.key == pygame.K_ESCAPE: #esc를 누르면
                    maingame = "닫기"                 #종료됨

        background_result.show()

        if catch_count>=best_catch:
            best_catch=catch_count

        text5 = font.render('%s' %catch_count, True, (255, 255, 255))
        screen.blit(text5, (398, 301))
        text6 = font.render('%s' %best_catch, True,(255,255,255))
        screen.blit(text6, (495, 397))

        pygame.display.flip()
        if(stage_music==True):
            music_stage.play()
            stage_music=False
    ########튜토리얼부분###########
    while(maingame=="튜토리얼"):
        tutorial()

    while(maingame=="튜토리얼시작"):
        clock.tick(60)
        get_key_Event() #키관련 이벤트를 불러옴
        player_move()   #움직임 관련 이벤트를 불러옴
        player_shot()   #미사일 발사 관련 이벤트를 불러옴
        Drop_enermy()

        if esc_event==True:
            maingame="메뉴"

        for i in range(len(enermy_img)): #모든 적들에 대해
            if boom_event==True:         #z가 눌러지면
                enermy[i].y=30           #y축 위치를 30으로
                enermy[i].speed =0       #못움직이게 속도를 0으로
            speedup = 0.01               #속도 증가는 0.01로.
        d_list=[]
        for i in range(len(m_list)):    #모든 미사일에 대해
            for j in range(len(a_list)):#모든 적들에 대해
                m = m_list[i]           #미사일 m과
                a = a_list[j]           #적 a가
                if crash(m, a) == True: #충돌시
                    d_list.append(i)    #해당 미사일의 정보를 d_리스트에 담음
                    d_list = list(set(d_list))  #d_리스트의 중복을 제거
                    d_list.reverse()            #d_리스트를 일단 뒤집어줌
                    for k in range(len(a_list)): #충돌한 친구가어떤친군지를 찾아서
                        if(a==enermy[k]):
                            music_quize[k].set_volume(volum_val)    #소리를 조정하고
                            music_quize[k].play()  #소리를 재생한다.
        for d in d_list:  # d리스트와 있는 개체들을 뽑아 미사일을 지워준다.
            del m_list[d]

        if(hardmode==False):
            background_normal_start.show()   #배경을 그린다
        elif(hardmode==True):
            background_hard_start.show()

        player.show()       #캐릭터를 그린다
        for m in m_list:    #미사일을 그린다
            m.show()
        for a in a_list:    #적들을 그린다
            a.show()

        pygame.display.flip()

    while(maingame=="소리조절"):
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 게임을 종료하면.
                maingame = "닫기"  # 종료됨
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  #왼쪽키를누르면
                    if(volum_val>=0.2):         #소리가 0.1보다 클때
                        volum_val -= 0.1        #소리가 감소
                        master_volum()          #볼륨 함수를 호출
                        music_good.play()       #확인용 재생
                if event.key == pygame.K_RIGHT: #오른쪽 키를 누르면
                    if (volum_val <= 0.9):      #소리가 0.9보다 작을때
                        volum_val += 0.1        #소리가 증가
                        master_volum()          #볼륨 함수를 호출
                        music_good.play()       #확인용 재생
                if event.key == pygame.K_ESCAPE:#esc가 눌러지면
                    maingame="메뉴"                  #메인메뉴로
        print_volum_val=str(volum_val)[0:3]
        background_volum.show()  #배경을그린다
        text_volum2 = font.render(print_volum_val, True, (255, 255, 255))
        screen.blit(text_volum2, (180, 552))
        pygame.display.flip()
    while(maingame=="닫기"):  #maingame이 닫기가 되면
        run = False       #더이상 메인 반복문을 반복하지 않는다.(즉 이제 처리되고 종료된다)
        pygame.quit()     #게임을 종료한다
        break             #혹시모르니 반복문을 탈출한다.
