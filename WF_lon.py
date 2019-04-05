#Gazque Espinosa de lo Monteros Edgar Amilkar
from matplotlib import pyplot as plt
import numpy as np
import random 
from math import floor
import matplotlib.pyplot as plt
frecuencia_inicial = [0.25,0.25,0.25,0.25]
N = 100
s1 = 0.01
s2 = 0.03
def grafica(x,y):
	plt.plot(x,y,color='blue')
	plt.xlabel('t')
	plt.ylabel('Xt')
	plt.title('Wright Fisher')
	plt.show()


def WF_lon(d1,a1,d0,a0,n):
    proceso_x1_I= [0.25] #x1_I,x0_I,x1_f,x0_f
    proceso_x0_I = [0.25]
    proceso_x1_f = [0.25]
    proceso_x0_f = [0.25]
    for i in range(n):
        no_mueren_1 = np.random.binomial(floor(N*proceso_x1_I[-1]),1-d1)
        no_mueren_0 = np.random.binomial(floor(N*proceso_x0_I[-1]),1-d0)
        envejecen1 = np.random.binomial(floor(N*proceso_x1_f[-1]),a1)
        envejecen0 = np.random.binomial(floor(N*proceso_x0_f[-1]),a0)
        I =  no_mueren_1 + no_mueren_0 + envejecen1 + envejecen0
        p = ((1+s1)*proceso_x1_f[-1])/((1+s1)*proceso_x1_f[-1] + (1+s2)*proceso_x0_f[-1])
        proceso_x1_I.append((no_mueren_1 + envejecen1)/N)
        proceso_x0_I.append((no_mueren_0 + envejecen0)/N)
        proceso_x1_f.append((1/(N-I))*np.random.binomial(N-I,p))
        proceso_x0_f.append(1 -(no_mueren_1 + envejecen1)/N + (no_mueren_0 + envejecen0)/N + (1/(N-I))*np.random.binomial(N-I,p))
    return [proceso_x1_I,proceso_x0_I,proceso_x1_f,proceso_x0_f] 

W = WF_lon(0.2,0.3,0.4,0.1,200)
Y = W[1]
X= np.linspace(0,len(Y),len(Y))
grafica(X,Y)
