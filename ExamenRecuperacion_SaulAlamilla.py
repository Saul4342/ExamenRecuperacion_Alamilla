"""
Examen de recuperación Graficacion 3D
Nombre: Saúl Humberto Alamilla Calixto
Fecha: 01/02/2021
NoControl 18390023
Materia: Graficación
"""
import matplotlib.pyplot as plt 
import numpy as np
from math import sin, cos, radians,sqrt
import msvcrt #Importamos esta libreria para poder detectar las teclas que se presionen.

#-----Coordenadas iniciales
xg=[]
yg=[]
zg=[]

#Cordenadas centrales
xc=0
yc=0
zc=0
#

#-----Dibujar el sistema que pide el problema, los triangulos
#def plotPlaneLine(xg,yg,zg,xh,yh,xhg,yhg,hitcolor):
def plotPlaneLine(x,y,z,xg,yg,zg,hitx,hity):

    plt.axis([0,110,100,0])
    plt.axis('on')
    plt.grid(False)
    #Triangulo A o triangulo base
    plt.plot([xg[0],xg[1]],[yg[0],yg[1]],color='k')#Plotear la linea del punto 0 a 1
    plt.plot([xg[1],xg[2]],[yg[1],yg[2]],color='k')#Plotear la linea del punto 1 a 2
    plt.plot([xg[2],xg[0]],[yg[2],yg[0]],color='k')#Plotear la linea del punto 2 a 0
    #Dibujar los otros triangulos teniendo como base el triangulo anterior
    plt.plot([xg[3],xg[0]],[yg[3],yg[0]],color='r', linestyle=':')#Plotear la linea del punto 0 al 3 (hitpoint)
    plt.plot([xg[3],xg[1]],[yg[3],yg[1]],color='r', linestyle=':')#Plotear la linea del punto 1 al 3 (hitpoint)
    plt.plot([xg[3],xg[2]],[yg[3],yg[2]],color='r', linestyle=':')#Plotear la linea del punto 2 al 3 (hitpoint)

    plt.scatter(xg[3],yg[3], s=30,color='r') #Pintar un circulo en el hitpoint

    #-----Etiquetas para mostrar los puntos, 0, 1, 2 y 3 (hitpoint)------
    plt.text(xg[0],yg[0]-1, '0')#Aqui solo le resto 1 para que se vean mejor los puntos
    plt.text(xg[1],yg[1]-1, '1')
    plt.text(xg[2],yg[2]-1, '2')
    plt.text(xg[3],yg[3]-1, '3 (Hitpoint)')
    #--------------------------------------------------------------------

    plt.axes().set_aspect('equal')
    calcularArea(x,y,z)#Llamar a la funcion para calcular distancias y áreas
    plt.show()

#Calcular las distancias entre puntos y areas para determinar si el hitpoint esta fuera o dentro
def calcularArea(x,y,z):
    #CALCULAR DISTANCIAS DEL Y ÁREA DEL TRIANGULO A
    #----Distancia del punto 0 al 1
    a=x[0]-x[1]
    b=y[0]-y[1]
    c=z[0]-z[1]
    d01=sqrt(a*a+b*b+c*c) #Formula para calcular la distancia
    #----Distancia del punto 1 al 2
    a=x[1]-x[2]
    b=y[1]-y[2]
    c=z[1]-z[2]
    d12=sqrt(a*a+b*b+c*c) #Formula para calcular la distancia
    #----Distancia del punto 2 al 0
    a=x[2]-x[0]
    b=y[2]-y[0]
    c=z[2]-z[0]
    d02=sqrt(a*a+b*b+c*c) #Formula para calcular la distancia
    SA=(d01+d12+d02)/2 #Calculamos el Semiperímetro usando la formula de Heron
    A=int(sqrt(SA*(SA-d01)*(SA-d12)*(SA-d02)))#Área del triángulo A usando la formula de Heron

    #--------------------------------------------

    #CALCULAR DISTANCIAS DEL Y ÁREA DEL TRIANGULO A1
    #----Distancia del punto 0 al 1 (Aqui como ya lo habiasmos calculado antes, entonces no hacia falta volverlo a calcular)
    d01=d01
    #----Distancia del punto 1 al 3
    a=x[3]-x[1]
    b=y[3]-y[1]
    c=z[3]-z[1]
    d13=sqrt(a*a+b*b+c*c)
    #----Distancia del punto 3 al 0
    a=x[3]-x[0]
    b=y[3]-y[0]
    c=z[3]-z[0]
    d03=sqrt(a*a+b*b+c*c) #Formula para calcular la distancia
    SA=(d01+d13+d03)/2 #Calculamos el Semiperímetro
    A1=int(sqrt(SA*(SA-d01)*(SA-d13)*(SA-d03)))#Área del triángulo A1

    #--------------------------------------------

    #CALCULAR DISTANCIAS DEL Y ÁREA DEL TRIANGULO A2
    #----Distancia del punto 0 al 3, como ya lo teniamos, no hacia falta volver a calcularlo
    d03=d03
    #----Distancia del punto 0 al 2, de igual manera, ya no hacia falta calcularlo de nuevo
    d02=d02
    #----Distancia del punto 2 al 3
    a=x[2]-x[3]
    b=y[2]-y[3]
    c=z[2]-z[3]
    d23=sqrt(a*a+b*b+c*c) #Formula para calcular la distancia
    SA=(d03+d02+d23)/2 #Calculamos el Semiperímetro
    A2=int(sqrt(SA*(SA-d03)*(SA-d02)*(SA-d23)))#Área del triángulo A2

    #ETIQUETAS
    plt.text(65,23,"Área de los triangulos")
    plt.text(80,30,"A: ",color='b')
    plt.text(84,30,A,color='b')
    plt.text(80,37,"A1: ",color='g')
    plt.text(86,37,A1,color='g')
    plt.text(80,44,"A2: ",color='purple')
    plt.text(86,44,A2,color='purple')
    plt.title("Graficación 3D - Saúl Alamilla") #Titulo para el programa
    plt.xlabel("Eje X")#Etiquetar el eje X
    plt.ylabel("Eje Y")#Etiquetar el eje y
    #plt.show()

    #VALIDAR SI EL HITPOINT ESTA DENTRO O AFUERA UTILIZANDO LAS ÁREAS CALCULADAS ANTERIORMENTE
    if (A1+A2) > A: #Si el área de los triangulos definidos por el hitpoint es mayor al area del triangulo base, el hitpoint esta fuera de los límites
        plt.text(30,80,'HitPoint fuera de los límites')
    if (A1+A2) < A: #Si el área de los triangulos definidos por el hitpoint es menor al area del triangulo base, el hitpoint esta dentro de los límites
        plt.text(30,80,'HitPoint dentro de los límites')

    plt.show()

#--------Pedir al usuario las coordenadas para el hitpoint
while True:
    print ("Pulse ESC para salir o cualquier otra tecla para ingresar el hitpoint:")
    
    #TECLA ESCAPE
    #Aqui ocupe el codigo ASCII transformandolo con la función .encode para que python lo pueda reconocer
    #en este caso el '27' es el código para la tecla ESCAPE y es la misma que ocupo para terminar el programa
    if msvcrt.getch() == chr(27).encode():
        #Aqui busque una manera para que igual detecte una tecla pero era instalando una libreria, pip install keyboard, y quise intentarlo
        #de tal manera que no necesite instalar nada, y es lo que mostre arriba.
        break #Esto termina el programa

    #CUALQUIER OTRA TECLA
    #Si el usuario oprime cualquier otra tecla que no sea el ESCAPE, entonces pasa a pedir el hitpoint
    else:
        #Definimos estas variables para determinar el hitpoint
        hitx=int(input("Digite la coordenada X: "))
        hity=int(input("Digite la coordenada Y: "))

        #---------Definimos las coordenadas incluyendo el hitpoint con las variables anteriores----------
        x=[40,30,80,hitx]
        y=[60,10,60,hity]
        z=[-10,10,10,-10]

        for i in range(len(x)):
            xg.append(x[i]+xc)
            yg.append(y[i]+yc)
            zg.append(z[i]+zc)
        #-------------------------------------------------------------------
        plotPlaneLine(x,y,z,xg,yg,zg,hitx,hity)#LLamamos a la funcion de ploteo incluyendo las variables que el usuario ingreso


