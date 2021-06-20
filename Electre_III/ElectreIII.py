# José Fernando Méndez Torres
# Los métodos Electre son utilizados para la toma de decisiones.
# Dadas alternativas donde no es claro cuál es mejor que otra, 
# el método Electre III nos dará un orden de ellas. 

# Lea el beamer adjunto para mayor información.

import numpy as np   

def Concordancia(G,P,Q,W):
    """La función Concordancia crea la matriz de concordancia \n
    para el método electre III a partir de \n 
    G := 'la matriz de calificaciones',\n
    P := 'El vector de umbral de preferencia para los criterios',\n
    Q := 'El vector de umbral de indiferencia para los criterios',\n
    W := 'El vector de pesos de los criterios'.
    """
    n = len(G[0])           # la cantidad de criterios
    m = int(np.size(G)/n)   # la cantidad de alternativas
    C = np.zeros((m,m))       # Definimos a una matriz de concordancia C vacía
    weight = 0                # Obtenemos la suma de los pesos en este valor
    for i in range(0,n):
        weight += W[i]
        
    for a in range(0,m):      
        for b in range(0,m):
            aux = 0
            for j in range(0,n):
                if G[a][j] + Q[j] >= G[b][j]:
                    aux += W[j]
                elif G[a][j] + P[j] <= G[b][j]:
                    pass
                else:    
                    aux += (P[j] + G[a][j]-G[b][j])/(P[j]-Q[j])
            C[a][b] = aux/weight
    return C

def Credibilidad(G,P,V,C):
    """La función Credibilidad crea la matriz de credibilidad \n
    para el método electre III a partir de \n 
    G := 'la matriz de calificaciones',\n
    P := 'El vector de umbral de preferencia para los criterios',\n
    V := 'El vector de veto para los criterios',\n
    C := 'La matriz de concordancia'.
    """
    n = len(G[0])           # la cantidad de criterios
    m = int(np.size(G)/n)   # la cantidad de alternativas
    S = np.zeros((m,m))       # Definimos a una matriz de concordancia C vacía
    for a in range(0,m):
        for b in range(0,m):
            decision = np.zeros(n)
            d = np.zeros(n)
            for j in range(0,n):
                if G[a][j] + P[j] >= G[b][j]:
                    pass
                elif G[a][j] + V[j] <= G[b][j]:
                    d[j] = 1
                else:    
                    d[j] = (G[b][j] - G[a][j] - P[j])/(V[j]-P[j])
            
            for j in range(0,n):
                if d[j] <= C[a][b]:
                    decision[j] = 0
                else:    
                    decision[j] = 1
                    
            if np.inner(decision,np.ones(n)) == 0:
                S[a][b] = C[a][b] 
            else:     
                S[a][b] = C[a][b]/((1-C[a][b])**(np.inner(decision,np.ones(n))))
                for i in range(0,n):
                    S[a][b] *= (1-d[i]*decision[i])
    return S

def LambdaMax(S):
    """Obtiene Lambda max a partir de la matriz de Credibilidad.
    """                 
    return np.max(S)    

def MatrizT(S, D, LambdaMax, SLambda):
    """Genera la matriz T a partir de los D_k"""
    r = len(S[0])
    T = np.zeros((r,r))
    for a in D:
        for b in D:
            if a == b:
                pass
            else: 
                if S[a][b] > LambdaMax and S[a][b]-S[b][a]>SLambda:
                    T[a][b] = 1
                else:
                    pass
                
    return T
 
def QA(T):
    """Genera el vector Q a partir de T"""
    m = len(S[0])
    Q = np.zeros(m)
    for a in range(0,m):
        aux1 = 0
        aux2 = 0
        for j in range(0,m):
           aux1 += T[a][j]
           aux2 += T[j][a]
        Q[a] = aux1 - aux2
    return Q               
                
def Lambda(S, A):
    """Obtiene Lambda max a partir de la matriz de Credibilidad.
    """   
    L = 0
    for a in A:
        for b in A:
            if a == b:
                pass
            else:    
                L = max(L,S[a][b])  
    return L  
        
    
def s(L, alpha, beta):
    return alpha*L+beta    
    
def LambdaK(L, D, S, alpha, beta):
    ese = s(L, alpha, beta)
    aux = 0
    for a in D:
        for b in D:
            if a == b:
                pass
            else:
                if S[a][b] < L - ese:
                    aux = max(aux,S[a][b])
                else:
                    pass
                
    return aux       
       

def DestiladoAscendente(S, alpha = -0.15, beta = 0.3):
    """Este es el algoritmo de destilamiento, el cual recibe la \n
    matriz de Credibilidad, una constante alpha y una beta; y nos dará \n
    el destilado ascendente de las alternativas.
    """
    n = 0                    #El número de destilación
    m = len(S[0])
    A = list(range(0,m))
    L = Lambda(S,A)
    Alt = []
    Orden = []
    foo = False
    while len(A) != 0: 
        k = 0                #El número de pasos de la destilación
        D = A
        while len(D) != 1 and foo == False and len(A)!= 0:
            L = LambdaK(L, D, S, alpha, beta)
            T = MatrizT(S, D, L, s(L, alpha, beta)) 
            Q = QA(T)
            q = min(Q)
            
            
            if np.max(Q) == 0:
                foo = True
                for i in D:
                    Orden.append(n)
                    Alt.append(i)
                    A.remove(i)
            else:
                pass
                
                
            alternativas = []
            for i in D:
                if Q[i] == q:
                    alternativas.append(i)
                else:
                    pass
                    
            if len(alternativas) == 1:
                Alt.append(alternativas[0])
                Orden.append(n)
                A.remove(alternativas[0])
                k = k+1            
            else:
                k = k+1
                if foo == False:
                    D = alternativas
                else:
                    D = A    
                
            n = n+1
            foo = False
    return dict(zip(Alt,Orden))
	        
	        
	               
    
    
def DestiladoDescendente(S, alpha = -0.15, beta = 0.3):
    """Este es el algoritmo de destilamiento, el cual recibe la \n
    matriz de Credibilidad, una constante alpha y una beta; y nos dará \n
    el destilado ascendente de las alternativas.
    """
    n = 1                    #El número de destilación
    m = len(S[0])
    A = list(range(0,m))
    L = Lambda(S,A)
    Alt = []
    Orden = []
    foo = False
    while len(A) != 0: 
        k = 0                #El número de pasos de la destilación
        D = A
        while len(D) != 1 and foo == False and len(A)!= 0:
            L = LambdaK(L, D, S, alpha, beta)        #Definimos Lambda_k
            T = MatrizT(S, D, L, s(L, alpha, beta))  #Generamos la Matriz T
            Q = QA(T)                                #Generamos el vector Q
            q = max(Q)                               #Obtenemos el máximo de Q
            
            
            if np.max(T) == 0:                       #Vemos si todas las entradas de T son cero.
                foo = True                           #De ser así, definimos el orden n para las alternativas en D_k
                for i in D:
                    Orden.append(n)
                    Alt.append(i)
                    A.remove(i)
            else:
                pass
                
                
            alternativas = []                        #Generamos el conjunto de alternativas
            for i in D:
                if Q[i] == q:                        #Obtenemos el conjunto argmax del problema
                    alternativas.append(i)
                else:
                    pass
                    
            if len(alternativas) == 1:               #En caso de ser un único elemento que maximice Q
                Alt.append(alternativas[0])          #Definimos su orden n.
                Orden.append(n)
                A.remove(alternativas[0])
                k = k+1                              
            else:
                k = k+1
                if foo == False:                     #De no ser así, definimos a D_k como las argmax de Q
                    D = alternativas
                else:
                    pass    
                
            n = n+1
            foo = False
    return dict(zip(Alt,Orden))                      #Juntamos las alternativas con sus órdenes.
    
    


                                     
G = [[-14,90,0,40,100],
	 [129,100,0,0,0],
	 [-10,50,0,10,100],
	 [44,90,0,5,20],
	 [-14,100,0,20,40]]

P = [50,24,1,24,20]

Q = [25,16,0,12,10]

W = [1,1,1,1,1]

V = [100,60,2,48,90]  

A = list(range(0,5))
				
C = Concordancia(G,P,Q,W)
S = Credibilidad(G,P,V,C)
print(C)
print(" ")     
print(S)
DestDes = DestiladoDescendente(S)
print(DestDes)
DestAsc = DestiladoAscendente(S)
print(DestAsc)


