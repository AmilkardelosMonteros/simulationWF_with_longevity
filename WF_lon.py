from matplotlib import pyplot as plt
import numpy as np
import random 
from math import floor
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
N = 5000
S0 = 0
S1 = 0
def grafica(x,y):
    plt.plot(x,y,color='blue')
    plt.xlabel('t')
    plt.ylabel('Xt')
    plt.title('Wright Fisher')
    plt.show()

def graficaC(x,y,pasos,rep):
    plt.plot(x,y,color = 'navy')
    plt.xlabel('t')
    plt.ylabel('Wt')
    plt.xlim(0, 1)
    plt.ylim(0,1)
    plt.title('Caminata aleatoria_de_'+str(pasos)+ '_pasos en dxa con_'+ str(rep)+'_repeticiones')
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
        p = ((1+S1)*proceso_x1_f[-1])/((1+S1)*proceso_x1_f[-1] + (1+S0)*proceso_x0_f[-1])
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
        p = ((1+S1)*proceso_x1_f[-1])/((1+S1)*proceso_x1_f[-1] + (1+S0)*proceso_x0_f[-1])
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
        #print(proceso_x1_f[-1])
        no_mueren_1 = np.random.binomial(N*proceso_x1_I[-1],1-d1)
        no_mueren_0 = np.random.binomial(N*proceso_x0_I[-1],1-d0)
        envejecen1 = np.random.binomial(N*proceso_x1_f[-1],a1)
        envejecen0 = np.random.binomial(N*proceso_x0_f[-1],a0)
        I =  no_mueren_1 + no_mueren_0 + envejecen1 + envejecen0
        p = ((1+S1)*proceso_x1_f[-1])/((1+S1)*proceso_x1_f[-1] + (1+S0)*proceso_x0_f[-1])
        proceso_x1_I[-1] = (no_mueren_1 + envejecen1)/N
        proceso_x0_I[-1] = (no_mueren_0 + envejecen0)/N
        numero = (np.random.binomial(N-I,p))
        proceso_x1_f[-1] = numero/N
        proceso_x0_f[-1] = 1- (numero + ((no_mueren_1 + envejecen1)) + ((no_mueren_0 + envejecen0)))/N
    if proceso_x1_f[-1] == 0:
        return 0
    else:
        return 1

def ganador1(d1,a1,s1,d0,a0,s0):
    proceso_x1_I= [0.25] #x1_I,x0_I,x1_f,x0_f
    proceso_x0_I = [0.25]
    proceso_x1_f = [0.25]
    proceso_x0_f = [0.25]
    while proceso_x1_f[-1] != 0 and proceso_x0_f[-1] != 0:
        #print(proceso_x1_f[-1])
        no_mueren_1 = np.random.binomial(N*proceso_x1_I[-1],1-d1)
        no_mueren_0 = np.random.binomial(N*proceso_x0_I[-1],1-d0)
        envejecen1 = np.random.binomial(N*proceso_x1_f[-1],a1)
        envejecen0 = np.random.binomial(N*proceso_x0_f[-1],a0)
        I =  no_mueren_1 + no_mueren_0 + envejecen1 + envejecen0
        p = ((1+s1)*proceso_x1_f[-1])/((1+s1)*proceso_x1_f[-1] + (1+s0)*proceso_x0_f[-1])
        proceso_x1_I[-1] = (no_mueren_1 + envejecen1)/N
        proceso_x0_I[-1] = (no_mueren_0 + envejecen0)/N
        numero = (np.random.binomial(N-I,p))
        proceso_x1_f[-1] = numero/N
        proceso_x0_f[-1] = 1- (numero + ((no_mueren_1 + envejecen1)) + ((no_mueren_0 + envejecen0)))/N
    if proceso_x1_f[-1] == 0:
        return 0
    else:
        return 1



def distribucion(v,mu1,mu2):
        return[v[-1][0]+ mu1*np.random.uniform(-1,1,1), v[-1][1] + mu2*np.random.uniform(-1,1,1)]
    
def Mutacion1(n,mu1,mu2):
    trayectoria =  [[0.5,0.5]]
    for i in range(n):
        retador = distribucion(trayectoria,mu1,mu2)
        if abs(trayectoria[-1][0]) >= 1 or abs(trayectoria[-1][1]) >= 1:  
            return trayectoria
        elif abs(retador[0]) >=1 or abs(retador[1]) >= 1:
                return trayectoria
        elif ganador(float(trayectoria[-1][0]),float(trayectoria[-1][1]),float(retador[0]),float(retador[1])) == 1:
            trayectoria.append([trayectoria[-1][0],trayectoria[-1][1]])
        else:
            trayectoria.append([retador[0],retador[1]])
    return trayectoria


def dibuja_mutacion1(trayectoria):
        x = []
        y = []
        repeticiones = 0
        pasos = len(trayectoria)
        for i in range(pasos):
                if i > 0:
                        if trayectoria[i][0] == trayectoria[i-1][0] and trayectoria[i][1] == trayectoria[i-1][1]:
                                repeticiones += 1
                v = trayectoria[i]
                x.append(v[0])
                y.append(v[1])
        graficaC(x,y,pasos,repeticiones)
        
#C = Mutacion1(600,0.01,0.03)
#dibuja_mutacion1(C)

def distribucion2(v,mu1,mu2,mu3):
        return[v[-1][0]+ mu1*np.random.uniform(-1,1,1), v[-1][1] + mu2*np.random.uniform(-1,1,1), v[-1][2] + mu3*np.random.uniform(-1,1,1)]
    
def Mutacion_triple(n,mu1,mu2,seleccion):
    mu3 = seleccion
    trayectoria =  [[0.5,0.5,0]]
    for i in range(n):
        print(i)
        retador = distribucion2(trayectoria,mu1,mu2,mu3) 
        if abs(trayectoria[-1][0]) >= 1 or abs(trayectoria[-1][1]) >=1 or abs(trayectoria[-1][2]) >= 1:  
            return trayectoria
        elif abs(retador[0]) >=1 or abs(retador[1])>=1 or abs(retador[2])>=1:
                return trayectoria
        elif ganador1(float(trayectoria[-1][0]),float(trayectoria[-1][1]),float(trayectoria[-1][2]),float(retador[0]),float(retador[1]),float(retador[2])) == 1:
            trayectoria.append([trayectoria[-1][0],trayectoria[-1][1],trayectoria[-1][2]])
        else:
            trayectoria.append([retador[0],retador[1],retador[2]])
    return trayectoria

def dibuja_mutacion_triple(trayectoria):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = []
    y = []
    z = []
    repeticiones = 0
    pasos = len(trayectoria)
    for i in range(pasos):
        if i > 0:
            if trayectoria[i][0] == trayectoria[i-1][0] and trayectoria[i][1] == trayectoria[i-1][1]:
                repeticiones += 1
        v = trayectoria[i]
        x.append(v[0])
        y.append(v[1])
        z.append(v[2])
    ax.plot(x,y,z)
    ax.set_xlabel('Death rate')
    ax.set_ylabel('Rate of aging')
    ax.set_zlabel('Selection')
    plt.show()

C = Mutacion_triple(700,0.001,0.03,0.001)
dibuja_mutacion_triple(C)
