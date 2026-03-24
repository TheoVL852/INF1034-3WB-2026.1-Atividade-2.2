from turtle import *
from time import sleep

t = Turtle()
t.speed(0)

def bandeira():
    for _ in range(2):
        t.fd(600)
        t.lt(90)
        t.fd(300)
        t.lt(90)

def ret(cor):
    t.color(cor)
    t.begin_fill()
    t.fillcolor(cor)
    for _ in range(2):
        t.fd(200)
        t.lt(90)
        t.fd(300)
        t.lt(90)
    t.end_fill()
    t.color('black')

def ret2(cor):
    t.color(cor)
    t.begin_fill()
    t.fillcolor(cor)
    for _ in range(2):
        t.fd(600)
        t.lt(90)
        t.fd(100)
        t.lt(90)
    t.end_fill()
    t.color('black')

def inicio():
    t.color('black')
    t.pu()
    t.goto(-300,-150)
    t.pd()

# Bandeira da Polonia (25XP)

inicio()

bandeira()

t.color('red')
t.begin_fill()
t.fillcolor('red')
for _ in range(2):
    t.fd(600)
    t.lt(90)
    t.fd(150)
    t.lt(90)
t.end_fill()

sleep(2)
t.clear()

# Bandeira Nigéria (25XP)

inicio()

bandeira()

ret("green")
t.fd(400)
ret("green")

sleep(2)
t.clear()

# Bandeira Italia (25XP)

inicio()

bandeira()

ret('green')
t.fd(400)
ret('red')

sleep(2)
t.clear()

# Bandeira França (25XP)

inicio()

bandeira()

ret('blue')
t.fd(400)
ret('red')

sleep(2)
t.clear()

# Banderia Niger (50XP)

inicio()

bandeira()

ret2('green')
t.pu()
t.lt(90)
t.fd(200)
t.rt(90)
t.pd()
ret2('orange')

t.pu()
t.goto(0,-45)
t.pd()
t.color('orange')
t.begin_fill()
t.fillcolor('orange')
t.circle(45)
t.end_fill()

sleep(2)
t.clear()

# Bandeira emirados arabes (50XP)

inicio()

bandeira()

ret2('black')
t.pu()
t.lt(90)
t.fd(200)
t.rt(90)
t.pd()
ret2('green')

inicio()
t.color('red')
t.begin_fill()
t.fillcolor('red')

for _ in range(2):
    
    t.fd(100)
    t.lt(90)
    t.fd(300)
    t.lt(90)

t.end_fill()

sleep(2)
t.clear()

# Bandeira Chile (50XP)

inicio()
bandeira()

t.color('blue')
t.begin_fill()
t.fillcolor('blue')

for _ in range(2):
    
    t.fd(200)
    t.lt(90)
    t.fd(300)
    t.lt(90)

t.end_fill()


t.color('red')
t.begin_fill()
t.fillcolor('red')
for _ in range(2):
    t.fd(600)
    t.lt(90)
    t.fd(150)
    t.lt(90)
t.end_fill()

t.pu()
t.goto(-250,80)
t.pd()

t.color('white')
t.begin_fill()
t.fillcolor('white')
for _ in range(5):
   t.fd(40)
   t.lt(72)
   t.fd(40)
   t.rt(144)

t.end_fill()

sleep(2)
t.clear()

# Bandeira Gana (50XP)

inicio()
bandeira()

ret2('green')
t.pu()
t.goto(-300,-50)
t.pd()
ret2('yellow')
t.pu()
t.goto(-300,50)
t.pd()
ret2('red')

t.pu()
t.goto(-50,10)
t.pd()
t.color('black')
t.begin_fill()
t.fillcolor('black')
for _ in range(5):
   t.fd(40)
   t.lt(72)
   t.fd(40)
   t.rt(144)

t.end_fill()

sleep(2)
t.clear()

# Bandeira Botswana (50XP)

inicio()

t.color('#0099CC')
t.begin_fill()
t.fillcolor('#0099CC')
for _ in range(2):
    t.fd(600)
    t.lt(90)
    t.fd(300)
    t.lt(90)
t.end_fill()

t.lt(90)
t.fd(120)
t.rt(90)
t.color('white')
t.begin_fill()
t.fillcolor('white')

for _ in range(2):
    t.fd(600)
    t.lt(90)
    t.fd(60)
    t.lt(90)
t.end_fill()

t.lt(90)
t.fd(10)
t.rt(90)
t.color('black')
t.begin_fill()
t.fillcolor('black')

for _ in range(2):
    t.fd(600)
    t.lt(90)
    t.fd(40)
    t.lt(90)
t.end_fill()

sleep(2)
t.clear()

# Bandeira Myanmar (50XP)

inicio()
bandeira()

ret2('#EE2737')
t.pu()
t.goto(-300,-50)
t.pd()
ret2('#43B02A')
t.pu()
t.goto(-300,50)
t.pd()
ret2('#FFCD00')

t.pu()
t.goto(-100,20)
t.pd()
t.color('white')
t.begin_fill()
t.fillcolor('white')
for _ in range(5):
   t.fd(80)
   t.lt(72)
   t.fd(80)
   t.rt(144)
t.end_fill()

sleep(2)
t.clear()
# Bandeira Panama (50XP)

inicio()
bandeira()

t.color('#072357')
t.begin_fill()
t.fillcolor('#072357')
for _ in range(2):
    t.fd(300)
    t.lt(90)
    t.fd(150)
    t.lt(90)
t.end_fill()

t.pu()
t.goto(0,0)
t.pd()

t.color('red')
t.begin_fill()
t.fillcolor('red')
for _ in range(2):
    t.fd(300)
    t.lt(90)
    t.fd(150)
    t.lt(90)
t.end_fill()

t.pu()
t.goto(-200,85)
t.pd()

t.color('#072357')
t.begin_fill()
t.fillcolor('#072357')
for _ in range(5):
   t.fd(40)
   t.lt(72)
   t.fd(40)
   t.rt(144)
t.end_fill()

t.pu()
t.goto(100,-70)
t.pd()

t.color('red')
t.begin_fill()
t.fillcolor('red')
for _ in range(5):
   t.fd(40)
   t.lt(72)
   t.fd(40)
   t.rt(144)
t.end_fill()

sleep(2)
t.clear()

# Bandeira Finlândia (50XP) 

inicio()
bandeira()
t.lt(90)
t.fd(110)
t.rt(90)

t.color('#002F6C')
t.begin_fill()
t.fillcolor('#002F6C')
for _ in range(2):
    t.fd(600)
    t.lt(90)
    t.fd(80)
    t.lt(90)
t.end_fill()

inicio()

t.fd(120)
t.color('#002F6C')
t.begin_fill()
t.fillcolor('#002F6C')
for _ in range(2):
    t.fd(80)
    t.lt(90)
    t.fd(300)
    t.lt(90)
t.end_fill()

sleep(2)
t.clear()

mainloop()
