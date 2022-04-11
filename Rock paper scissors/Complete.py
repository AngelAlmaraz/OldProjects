from graphics import *
import random as randy
from time import sleep

v = GraphWin('Rock Paper Scissors Lizard Spock',1000,800, autoflush = True)
v.setCoords(0,0,100,80)
v.setBackground('black')

def Texto(x,y,texto,color):
    t = Text(Point(x,y), texto)
    t.setFill(color)
    t.setSize(20)
    t.draw(v)
def Textox(x,y,texto,color):
    t = Text(Point(x,y), texto)
    t.setFill(color)
    t.setSize(20)
    t.draw(v)
    time.sleep(1.2)
    t.undraw()
def DialogoFinal(x,y,texto,color):
    t = Text(Point(x,y), texto)
    t.setFill(color)
    t.setSize(20)
    t.draw(v)
    time.sleep(2)
    t.undraw()
def Mano(image):
    mano = Image(Point(30,39),image)
    mano.draw(v)
    time.sleep(.5)
    mano.undraw()
def Manoj(image):
    mano = Image(Point(70,39),'h' + image +'.png')
    mano.draw(v)
    time.sleep(1)
    mano.undraw()
def quitarVidaPlayer(vidap):
    x = 17.7177
    rect = Rectangle(Point(x,49.1614),Point(x + 2.8 * (10 - vidap),51.1638))
    rect.setFill('red')
    rect.setOutline('red')
    rect.draw(v)
def quitarVidaJerry(vidaj):
    x = 81.7817
    rect = Rectangle(Point(x,49.1614),Point(x - 2.8 * (10 - vidaj),51.1638))
    rect.setFill('red')
    rect.setOutline('red')
    rect.draw(v)
reglas = {'rock':{'rock':'ties','paper':'loses','scissors':'wins','lizard':'wins','spock':'loses'},
          'paper':{'rock':'wins','paper':'ties','scissors':'loses','lizard':'loses','spock':'wins'},
          'scissors':{'rock':'loses','paper':'wins','scissors':'ties','lizard':'wins','spock':'loses'},
          'lizard':{'rock':'loses','paper':'wins','scissors':'loses','lizard':'ties','spock':'wins'},
          'spock':{'rock':'wins','paper':'loses','scissors':'wins','lizard':'loses','spock':'ties'}}

title = Image(Point(50,70),'logo.png')
title.draw(v)
blob = Rectangle(Point(1,55),Point(99,40))
blob.setFill('black')
blob.draw(v)
testo = Text(Point(50,50),"Type your name to begin")
testo.setFill('white')
testo.setSize(30)
testo.draw(v)
entry = Entry(Point(50,40),20)
entry.draw(v)
v.getMouse()
nombre = entry.getText()
print('ok')
def Boton(x,y,texto):
    rect = Rectangle(Point(x,y),Point(x+12,y+5))
    rect.setFill('white')
    rect.draw(v)
    texto = Text(Point(x+6,y+2.5),texto)
    texto.draw(v)
Boton(20,35,'Give up')
Boton(70,35,'Challenge Jerry')
pussy = True
while pussy:
    maus = v.getMouse()
    print(maus.getX(),maus.getY())
    if 20 <= maus.getX() <= 32 and 35 <= maus.getY() <= 40:
        for i in range(5):
            p = Text (Point(randy.randint(1,99),randy.randint(1,40)), 'Pussy')
            p.setFill('white')
            p.setSize(30)
            p.draw(v)
            time.sleep(.3)
            p.undraw()
    elif 70 <= maus.getX() <= 82 and 35 <= maus.getY() <= 40:
        p = Text (Point(50,30), 'Huzzah!, a man of quality!')
        p.setFill('white')
        p.setSize(30)
        p.draw(v)
        time.sleep(2)
        p.undraw()
        break
entry.undraw()
dare = Image(Point(50,40),'dare.png')
dare.draw(v)
cara1 = Image(Point(89,60.6),'Jerry1.png')
cara1.draw(v)
t = Text(Point(69,58), "Oh, you're approaching me?")
t.draw(v)
time.sleep(1.5)
t.undraw()
t = Text(Point(69,58), """Después de tu horrible examen
         de 8 horas?""")
t.draw(v)
time.sleep(1.5)
t.undraw()
carah = Image(Point(89,62),'headphoness.png')
carah.draw(v)
t = Text(Point(69,58), """Guys, hold on a second,
I've got some loser's
ass to flunk""")
t.draw(v)
time.sleep(1.5)
t.undraw()
carah.undraw()
ojo1 = Image(Point(86.6866,61.1764),'glowx.png')
ojo1.draw(v)
ojo2 = Image(Point(90.9909,61.3767),'glowx.png')
ojo2.draw(v)
t = Text(Point(69,58), """お前はもう死んでいる!!
You are already dead!!""")
t.draw(v)
time.sleep(1.5)
t.undraw()
cara1.undraw()
carah.undraw()
dare.undraw()
ojo1.undraw()
ojo2.undraw()

title.undraw()

## combate

fondo = Image(Point(50,31),'back.GIF')
fondo.draw(v)

rock = Image(Point(10,70),'rock.png')
rock.draw(v)
Texto(10,58,'Rock','white')
paper = Image(Point(30,70),'4.png')
paper.draw(v)
Texto(30,58,'Paper','white')
sc = Image(Point(50,70),'tijera.png')
sc.draw(v)
Texto(50,58,'Scissors','white')
liz = Image(Point(70,70),'lizard.png')
liz.draw(v)
Texto(70,58,'Lizard','white')
spock = Image(Point(90,70),'spock.png')
spock.draw(v)
Texto(90,58,'Spock','white')
#nombre = 'lalito'
Texto(25,54,'Xx_' + nombre + '_xX','red')
Texto(25,47,'Ryu','red')
Texto(75,54,'Jerrinsky_69','red')
Texto(75,47,'Guile','red')
barra = Image(Point(50,50),'bars.png')
barra.draw(v)
player = Image(Point(10,50),'player.png')
player.draw(v)
player2 = Image(Point(90,50),'player2.png')
player2.draw(v)

fight = Image(Point(50,30),'fight.png')
fight.draw(v)
time.sleep(1)
fight.undraw()

ryu = Image(Point(30,20),'ryu.gif')
ryu.draw(v)

guile = Image(Point(70,20),'guiled.gif')
guile.draw(v)

hado = Text(Point(30,36),'Hadouken!')
hado.setSize(20)
hado.setFill('white')
Sb = Text(Point(70,36),'Sonic Boom!')
Sb.setSize(20)
Sb.setFill('white')
vidaj,vidap = 10,10
while vidaj > 0 and vidap > 0:
    maus = v.getMouse()
    x = maus.getX()
    y = maus.getY()
    cual = randy.choice(list(reglas.keys()))
    if 0 <= x <= 20 and 60 <= y <= 80:
        juegas = 'rock'
        Mano('hrock.png')
        Manoj(cual)
        rule = reglas[juegas][cual]
    elif 20 < x <= 40 and 60 <= y <= 80:
        juegas = 'paper'
        Mano('hpaper.png')
        Manoj(cual)
        rule = reglas[juegas][cual]
    elif 40 < x <= 60 and 60 <= y <= 80:
        juegas = 'scissors'
        Mano('hscissorsi.png')
        Manoj(cual)
        rule = reglas[juegas][cual]
    elif 60 < x <= 80 and 60 <= y <= 80:
        juegas = 'lizard'
        Mano('hlizardi.png')
        Manoj(cual)
        rule = reglas[juegas][cual]
    elif 80 < x <= 100 and 60 <= y <= 80:
        juegas = 'spock'
        Mano('hspock.png')
        Manoj(cual)
        rule = reglas[juegas][cual]
    else:
        juegas = 'nada'
        rule = 'nada'
  
    Textox(50,3,juegas + ' ' + rule + ' against ' + cual,'white')

    if rule == 'wins':
        vidaj -= 1
        ryu.undraw()
        guile.undraw()
        ryu = Image(Point(30,20),'ryuh.png')
        ryu.draw(v)
        had = Image(Point(45,24),'ha.png')
        had.draw(v)
        hado.draw(v)
        guile = Image(Point(70,20),'guilered.gif')
        guile.draw(v)
        quitarVidaJerry(vidaj)
        time.sleep(.5)
        ryu.undraw()
        had.undraw()
        hado.undraw()
        guile.undraw()
        ryu = Image(Point(30,20),'ryu.gif')
        ryu.draw(v)
        guile = Image(Point(70,20),'guiled.gif')
        guile.draw(v)
        print('vida de jerry ', vidaj)
    elif rule == 'ties':
        pass
    elif rule == 'loses':
        vidap -= 1
        ryu.undraw()
        guile.undraw()
        ryu = Image(Point(30,20),'ryured.gif')
        ryu.draw(v)
        guile = Image(Point(70,20),'Guiled2.png')
        guile.draw(v)
        Sb.draw(v)
        quitarVidaPlayer(vidap)
        time.sleep(.5)
        ryu.undraw()
        guile.undraw()
        Sb.undraw()
        ryu = Image(Point(30,20),'ryu.gif')
        ryu.draw(v)
        guile = Image(Point(70,20),'guiled.gif')
        guile.draw(v)
        print('vida del jugador ', vidap)
    else:
        pass
    
ko = Image(Point(50,40),'ko.png')
ko.draw(v)
time.sleep(2)

if vidap == 0:
    dop = Image(Point(50,40),'antidop.png')
    dop.draw(v)
    DialogoFinal(50,70,'Ja Ja Ja, y todavía te atreves a perder...','black')
    DialogoFinal(50,70,'Por favor pasa con Escoto para que te hagamos un antidopping...','black')
    DialogoFinal(50,70,'Progra no será lo único que repruebes hoy','black')
    gameOver = Image(Point(50,40),'gameover.png')
    gameOver.draw(v)
    time.sleep(5)
elif vidaj == 0:
    print('ganaste')
    dop = Image(Point(50,40),'grad.png')
    dop.draw(v)
    jer = Image(Point(41.54,59.07),'Jerryx.png')
    jer.draw(v)
    DialogoFinal(50,20,'Muy bien, me has vencido joven Padawan...','white')
    DialogoFinal(50,20,'Felicidades, te has graduado crack','white')
    win = Image(Point(50,40),'win.png')
    win.draw(v)
    time.sleep(5)



