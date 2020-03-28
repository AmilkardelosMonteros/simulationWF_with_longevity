#!/usr/bin/python
import sys
import numpy as np
param = sys.argv[1]
Param = int(param)
N = 100.0
#La funcion recibe un vector de parametros [s1,a1] y los demas estan fijos
# Y vamos a seguir a los de tipo1
x1 = 0.5
d1 = 1
#s1 = variable
#a1 = variable
d0 = 1
a0 = 0
s0 = 0
def ganador_wf_long(parametros):
    s1 = parametros[0]
    a1 = parametros[1]
    proceso_x1_I= 0 #x1_I,x0_I,x1_f,x0_f
    proceso_x0_I = 0
    proceso_x1_f = 0.5
    proceso_x0_f = 0.5
    while proceso_x1_f != 0 and proceso_x0_f != 0:
        no_mueren_1 = np.random.binomial(N*proceso_x1_I,1-d1)
        no_mueren_0 = np.random.binomial(N*proceso_x0_I,1-d0)
        envejecen1 = np.random.binomial(N*proceso_x1_f,a1)
        envejecen0 = np.random.binomial(N*proceso_x0_f,a0)
        I =  no_mueren_1 + no_mueren_0 + envejecen1 + envejecen0
        x1F = proceso_x1_f/(proceso_x1_f + proceso_x0_f)
        p = ((1+s1)*x1F)/((1+s1)*x1F + (1+s0)*(1-x1F))
        proceso_x1_I =  (no_mueren_1 + envejecen1)/N
        proceso_x0_I = (no_mueren_0 + envejecen0)/N
        numero = np.random.RandomState().binomial(N-I,p)
        proceso_x1_f =  numero/N
        proceso_x0_f =  1- (numero + ((no_mueren_1 + envejecen1)) + ((no_mueren_0 + envejecen0)))/N
    if proceso_x1_f != 0:
        return 1
    else:
	return 0

#Para que las graficas se puedan leer se fijan 4 parametros: s0,a0,d0,d1 y los demas los variamos en R2 y para cada a1,s1 se estima la probabilidad de fijacion, para cada a1,s1 necesitamos hacer muchas repeticiones y para hacer esto un poco mas rapido u$

def proba_long(s1,a1,repeticiones):
    info  = []
    v = [s1,a1]
    for i in range(repeticiones):
        info.append(ganador_wf_long(v))
    return [s1*((1+d1)/(1+d1+a1)),a1,np.mean(info),np.var(info)]


def puntos(n,m,repeticiones,numero,nombre):
    S = np.linspace(-0.025,0.025,n)
    s_gorro = S[numero]
    A = np.linspace(0,1,m)
    archivo = open(nombre,'a')
    for a1 in A:
        s = s_gorro*((1+d1+a1)/(1+d1))
        WF = proba_long(s,a1,repeticiones)
        archivo.write(str(WF) + ',')
    archivo.close()

def funcion(numero):
    nombre = 'un_archivo_longevidad_sgorro' + str(int(numero)) + '.txt'
    puntos(20,20,5000,numero,nombre)

funcion(Param)
