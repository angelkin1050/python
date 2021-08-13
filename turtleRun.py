
"""
라이브러리: 도서관,미리 누군가가 어떤 주제에 관해서 함수를 만들어놓은 것
turtle(거북이,거북이 게임에 관련된 함수가 미리 저장되어 있다.)
등작인물: 악당(devil),먹이(feed),주인공 거북이(이름x)
함수
1. 가공에 필요한 데이터를 입력한다
2. 입력받는 데이터를 가공한다.
3. 가공된 데이터를 내보낸다.
def(define : 정의하다)
def 함수이름(입력값) :
가공하는곳
"""
#turtle 라이브러리를 사용하는 방법
import turtle as t
import random
devil = t.Turtle()
devil.shape("turtle")
devil.color("aquamarine")
devil.speed(0)
devil.up()
devil.goto(0,200)

feed = t.Turtle()
feed.shape("circle")
feed.color("Deeppink")
feed.speed(0)
feed.up()
feed.goto(-200,-100)

def turn_right() :
    t.setheading(0)
def turn_left() :
    t.setheading(180)
def turn_up() :
    t.setheading(90)
def turn_down() :
    t.setheading(270)
def play():
    t.forward(10)
    ang = devil.towards(t.pos())
    devil.setheading(ang)
    devil.forward(7)

    if t.distance(feed) < 12 :
        feed_x = random.randint(-230,230)
        feed_y = random.randint(-230,230)
        feed.goto(feed_x,feed_y)
        
    if t.distance(devil) >= 12:
        t.ontimer(play,100)
        
t.setup(500,500)
t.bgcolor("coral")
t.shape("turtle")
t.color("yellow")
t.speed(0)
t.up()

t.onkeypress(turn_right,"Right")
t.onkeypress(turn_left,"Left")
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_down,"Down")
t.listen()
play()




