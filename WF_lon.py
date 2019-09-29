#!/usr/bin/python
import sys
import numpy as np
from multiprocessing import Pool
import time
param = sys.argv[1]
Param = int(param)
N = 100.0
#La funcion recibe un vector de parametros [s1,a1] y los demas estan fijos
# Y vamos a seguir a los de tipo1
def ganador_wf_long(parametros):
    d1 = 1
    s1 = parametros[0]
    a1 = parametros[1]
    d0 = 0
    a0 = 0
    s0 = 0
    proceso_x1_I= 0.25 #x1_I,x0_I,x1_f,x0_f
    proceso_x0_I = 0.25
    proceso_x1_f = 0.25
    proceso_x0_f = 0.25
    while proceso_x1_f != 0 and proceso_x0_f != 0:
        no_mueren_1 = np.random.RandomState().binomial(N*proceso_x1_I,1-d1)
        no_mueren_0 = np.random.RandomState().binomial(N*proceso_x0_I,1-d0)
        envejecen1 = np.random.RandomState().binomial(N*proceso_x1_f,a1)
        envejecen0 = np.random.RandomState().binomial(N*proceso_x0_f,a0)
        I =  no_mueren_1 + no_mueren_0 + envejecen1 + envejecen0
        p = ((1+s1)*proceso_x1_f)/((1+s1)*proceso_x1_f + (1+s0)*proceso_x0_f)
        proceso_x1_I =  (no_mueren_1 + envejecen1)/N 
        proceso_x0_I = (no_mueren_0 + envejecen0)/N 
        numero = np.random.RandomState().binomial(N-I,p)
        proceso_x1_f =  numero/N 
        proceso_x0_f =  1- (numero + ((no_mueren_1 + envejecen1)) + ((no_mueren_0 + envejecen0)))/N
    if proceso_x1_f != 0:
        return 1
    else:
        return 0

#Para que las graficas se puedan leer se fijan 4 parametros: s0,a0,d0,d1 y los demas los variamos en R2 y para cada a1,s1 se estima la probabilidad de fijacion, para cada a1,s1 necesitamos hacer muchas repeticiones y para hacer esto un poco mas rapido usamos la libreria multiprossesing cuidando la aleatoriedad de procesos paralelos, la funcion que hace esto es la siguiente

def proba_long(s1,a1,repeticiones):
    p = Pool()
    v = [s1,a1]
    iter = []
    for i in range(repeticiones):
        iter.append(v)
    informacion = p.map(ganador_wf_long,iter)
    return [s1,a1,np.mean(informacion),np.var(informacion)]


def puntos(n,m,repeticiones,numero,nombre):
    S = np.linspace(-0.025,0.025,n)
    s = S[numero]
    A = np.linspace(0,1,m)
    archivo = open(nombre,'a')
    for a in A:
        WF = proba_long(s,a,repeticiones)
        archivo.write(str(WF) + ',')
    archivo.close()
    
def funcion(numero):
    nombre = 'un_archivo_longevidad' + str(int(numero)) + '.txt'
    puntos(20,20,100,numero,nombre)


funcion(Param)
