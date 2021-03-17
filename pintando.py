#Librerías para el programa
from turtle import *
from freegames import vector
import math

#Dibuja una línea
def line(start, end):
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

#Dibuja un cuadrado
def square(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

# Se tuvo que cambiar el nombre de esta funcion debido a que
# su nombre tenia conflicto con la funcion de `circle` en la
# libreria de turtle
def draw_circle(start, end):
    radius = math.sqrt((end.x - start.x)**2 + (end.y - start.y)**2)
    
    up()
    goto(start.x, start.y - radius)
    down()
    begin_fill()
    circle(radius)
    
    end_fill()

#Dibuja un rectángulo con la dimensión de la línea dibujada y ese lado multiplicado por 1.5
def rectangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    
    side1 = end.x - start.x
    for count in range(2):
        forward(side1*1.5)
        left(90)
        forward(side1)
        left(90)
    end_fill()
    pass

#Crea un triángulo equilátero con las dimensiones de la línea dibujada
def triangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for count in range(2):
        forward(end.x - start.x)
        left(90)
    end_fill()
    pass

#Almacena el punto de inicio o dibuja la figura
def tap(x, y):
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None
        
#llmacena el valor en state[key]
def store(key, value):
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')

#Llamada de funciones
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('pink'), 'P') #NEW COLOR
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', draw_circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
