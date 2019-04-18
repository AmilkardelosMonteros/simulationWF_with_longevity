from matplotlib import pyplot as plt
import numpy as np
import random 
from math import floor
import matplotlib.pyplot as plt
N = 2000
s1 = 1/N
s2 = 0
def grafica(x,y):
    plt.plot(x,y,color='blue')
    plt.xlabel('t')
    plt.ylabel('Xt')
    plt.title('Wright Fisher')
    plt.show()

def graficaC(x,y):
    plt.plot(x,y)
    plt.xlabel('t')
    plt.ylabel('Zt')
    plt.title('Caminata aleatoria')
    plt.show()
    
def grafica1(x,y0,y1,y2,y3):
    plt.plot(x,y0,color='cyan')
    plt.plot(x,y1,color='deeppink')
    plt.plot(x,y2,color='steelblue')
    plt.plot(x,y3,color='hotpink')
    plt.xlabel('t')
    plt.ylabel('Xt')
    plt.title('Wright Fisher con eficiencia')
    plt.show()



def WF_lon(d1,a1,d0,a0,n):
    proceso_x1_I= [0.25] #x1_I,x0_I,x1_f,x0_f
    proceso_x0_I = [0.25]
    proceso_x1_f = [0.25]
    proceso_x0_f = [0.25]
    for i in range(n):
        no_mueren_1 = np.random.binomial(N*proceso_x1_I[-1],1-d1)
        no_mueren_0 = np.random.binomial(N*proceso_x0_I[-1],1-d0)
        envejecen1 = np.random.binomial(N*proceso_x1_f[-1],a1)
        envejecen0 = np.random.binomial(N*proceso_x0_f[-1],a0)
        I =  no_mueren_1 + no_mueren_0 + envejecen1 + envejecen0
        p = ((1+s1)*proceso_x1_f[-1])/((1+s1)*proceso_x1_f[-1] + (1+s2)*proceso_x0_f[-1])
        proceso_x1_I.append((no_mueren_1 + envejecen1)/N)
        proceso_x0_I.append((no_mueren_0 + envejecen0)/N)
        numero = (np.random.binomial(N-I,p))
        proceso_x1_f.append(numero/N)
        proceso_x0_f.append(1- (numero + ((no_mueren_1 + envejecen1)) + ((no_mueren_0 + envejecen0)))/N)
    return [proceso_x1_I,proceso_x0_I,proceso_x1_f,proceso_x0_f] 


def WF_lon_completo(d1,a1,d0,a0):
    proceso_x1_I= [0.25] #x1_I,x0_I,x1_f,x0_f
    proceso_x0_I = [0.25]
    proceso_x1_f = [0.25]
    proceso_x0_f = [0.25]
    while proceso_x1_f[-1] != 0 and proceso_x0_f[-1] != 0:
        no_mueren_1 = np.random.binomial(N*proceso_x1_I[-1],1-d1)
        no_mueren_0 = np.random.binomial(N*proceso_x0_I[-1],1-d0)
        envejecen1 = np.random.binomial(N*proceso_x1_f[-1],a1)
        envejecen0 = np.random.binomial(N*proceso_x0_f[-1],a0)
        I =  no_mueren_1 + no_mueren_0 + envejecen1 + envejecen0
        p = ((1+s1)*proceso_x1_f[-1])/((1+s1)*proceso_x1_f[-1] + (1+s2)*proceso_x0_f[-1])
        proceso_x1_I.append((no_mueren_1 + envejecen1)/N)
        proceso_x0_I.append((no_mueren_0 + envejecen0)/N)
        numero = (np.random.binomial(N-I,p))
        proceso_x1_f.append(numero/N)
        proceso_x0_f.append(1- (numero + ((no_mueren_1 + envejecen1)) + ((no_mueren_0 + envejecen0)))/N)
    return [proceso_x1_I,proceso_x0_I,proceso_x1_f,proceso_x0_f] 

    
#W = WF_lon_completo(0.2,0.3,0.4,0.1)
#Y1 = W[0]
#Y2 = W[1]
#Y3 = W[2]
#Y4 = W[3]
#X= np.linspace(0,len(Y1),len(Y1))
#grafica1(X,Y1,Y2,Y3,Y4)

def ganador(d1,a1,d0,a0):
    proceso_x1_I= [0.25] #x1_I,x0_I,x1_f,x0_f
    proceso_x0_I = [0.25]
    proceso_x1_f = [0.25]
    proceso_x0_f = [0.25]
    while proceso_x1_f[-1] != 0 and proceso_x0_f[-1] != 0:
        no_mueren_1 = np.random.binomial(N*proceso_x1_I[-1],1-d1)
        no_mueren_0 = np.random.binomial(N*proceso_x0_I[-1],1-d0)
        envejecen1 = np.random.binomial(N*proceso_x1_f[-1],a1)
        envejecen0 = np.random.binomial(N*proceso_x0_f[-1],a0)
        I =  no_mueren_1 + no_mueren_0 + envejecen1 + envejecen0
        p = ((1+s1)*proceso_x1_f[-1])/((1+s1)*proceso_x1_f[-1] + (1+s2)*proceso_x0_f[-1])
        
        proceso_x1_I[-1] = (no_mueren_1 + envejecen1)/N
        proceso_x0_I[-1] = (no_mueren_0 + envejecen0)/N
        numero = (np.random.binomial(N-I,p))
        proceso_x1_f[-1] = numero/N
        proceso_x0_f[-1] = 1- (numero + ((no_mueren_1 + envejecen1)) + ((no_mueren_0 + envejecen0)))/N
    if proceso_x1_f[-1] == 0:
        return 0
    else:
        return 1

print(ganador(0.1,0.3,0.1,0))
def distribucion(mu):
    x = mu*np.random.uniform(0,1)
    y = mu*np.random.uniform(0,1)
    #x = np.random.beta(2,2)
    #y = np.random.beta(2,2)
    return x,y
    
def caminata(n):
    trayectoria = [[0,0]] #di,ai
    rep = 0 
    for i in range(n):
        retador = distribucion(1)
        if ganador(trayectoria[-1][0],trayectoria[-1][1],retador[0],retador[1]) == 0:
            trayectoria.append([retador[0],retador[1]])
        else:
            rep = rep + 1

        #else:
         #   trayectoria.append([trayectoria[-1][0],trayectoria[-1][1]])
    
        

    return trayectoria,rep


def dibuja_caminata(trayectoria):
        x = []
        y = []
        for i in range(len(trayectoria)):
                v = trayectoria[i]
                x.append(v[0])
                y.append(v[1])
        graficaC(x,y)
        
C = caminata(100)
def color(caminata,rep):
    x_rojo = []
    y_rojo = []
    x_azul = []
    y_azul = []
    j = 0
    n = len(caminata)
    for i in range(n):
        if caminata[i][1] >= caminata[i][0]:
            x_rojo.append(caminata[i][0])
            y_rojo.append(caminata[i][1])
        else:
            x_azul.append(caminata[i][0])
            y_azul.append(caminata[i][1])
    
    plt.plot(x_rojo,y_rojo,'ro')
    plt.plot(x_azul,y_azul,'bo')
    plt.title('caminata con_'+str(n + rep)+'pasos' + str(rep) + '_repeticiones_' + str(len(x_azul))+'_azules y_ '+ str(len(x_rojo))+'_rojos' )
    plt.show()
            
            
color(C[0],C[1])        
#dibuja_caminata(C) 


  
