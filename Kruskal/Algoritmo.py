import networkx as nx
import matplotlib.pyplot as plt
    
    
    
class Red:
    """ En esta clase definiremos algunos metodos de network x para
    nuestras redes.
    """
    def __init__(self, n):
        """En esta funcion definiremos una red que contenga unicamente
        nodos, por lo que A = []. Los nodos son del 1 al n.
        """
        self.G = nx.Graph() #Inicializamos nuestra grafica
        for i in range(1,n+1):
            self.G.add_node(i)
            
    def copia(self):
        """Esta funcion hara una copia de nuestra red con sus aristas
        ordenadas.
        """
        n = len(self.G)
        Nueva_Red = Red(n)
        m = self.G.number_of_edges()
        L = sorted(self.G.edges(data=True), key=lambda x: x[2]['peso'])
        for i in range(0,m):
            x = L[i][0] 
            y = L[i][1]
            p = L[i][2]['peso']
            Nueva_Red.G.add_edge(x,y, peso = p)

        return Nueva_Red      
            
    def agregarArista(self, p, q, d = 0):
        """Esta funcion sera la encargada de agregar aristas de nodos p
        y q con peso p a la grafica. 
        """
        self.G.add_edge(p,q, peso = d)
        
    def nodos(self):
        """Esta funcion nos regresara una lista de los nodos de la red.
        """
        return self.G.nodes()

    def aristas(self):
        """Esta funcion nos regresara una lista de las aristas de la red
        .
        """		
        return self.G.edges()
        
    def aristasConPesos(self):
        """Esta funcion nos regresara una lista de las aristas de la red
        con sus respectivos pesos.
        """	
        return self.G.edges(data=True)    
        
    def cardN(self):
        """Esta funcion nos regresara la cardinalidad de X.
        """	
        return len(self.G)
        
    def cardA(self):
        """Esta funcion nos regresara la cardinalidad de A.
        """	        
        return self.G.number_of_edges()
        
    def nodo(self,n):
        """Esta funcion nos regresara el nodo n.
        """	
        return self.G.nodes(n+1)
		    
    def aristaDeNodo(self, m):
        """Esta funcion nos regresara la arista m.
        """	    
        return self.G.edges(m)
        
    def pesoDeArista(self, m):
        """Esta funcion nos regresara el peso de la arista m.
        """	
        return Att[self.G.edges(m+1)]
        
    def ordenarAristasPorPeso(self):
        """Esta funcion nos regresara la lista de aristas ordenadas.
        """	
        l = sorted(self.G.edges(data=True), key=lambda x: x[2]['peso'])
        
        return l #self.G.edges(data=True)
               
    def ciclos(self):
        """Esta funcion regresará una lista de ciclos que haya en la
        grafica.
        """	
        return nx.cycle_basis(self.G)
        
    def buscarCiclos(self):
        """Esta funcion detectara si hay ciclos en la grafica. En caso
        de que haya al menos un ciclo, regresara 1. En caso de que no
        haya ciclos, nos regresara el 0.
        """	
        if nx.cycle_basis(self.G) == []:
            return 0
        else:
            return 1
        
    def Kruskal(self):
        """Este algoritmo tiene 3 pasos. El primer paso es guardar en L  
        las arisatas ordenadas por peso, k=j=0. La cardinalidad de X y A
        se guarda en n y m respectivamente. Arbol solo tiene nodos en
        este punto.
        Para el segundo paso, vamos viendo si las aristas que agregamos
        hacen un ciclo en la grafica, x y y son los nodos de la arista 
        de peso p. El if, else preguntará si hacen ciclo. El tercer paso
        es la condicion del while, el cual pregunta si j<m y k<n-1.
        En caso de que L sea vacía, la original gráfica es disconexa.
        En caso contrario, ta tenemos el arbol expandido de peso min.
        Tiene a lo mas m iteraciones.
		"""
        #Paso 1:
        L = sorted(self.G.edges(data=True), key=lambda x: x[2]['peso'])
        k=0                      #Auxiliar k.
        j=0                      #Auxiliar j.
        n = len(self.G)          #Card de X.
        m = len(L)               #Card de A.
        Arbol = Red(len(self.G)) #T = (X,0).
        
        #Paso 3.1:
        while j < m and k<n-1 :
            #Paso 2:
            j=j+1
            Arbol_1 = Arbol.copia() #Arbol sin la arista a_k.
            x = L[0][0]
            y = L[0][1]
            p = L[0][2]['peso']
            Arbol_1.agregarArista(x,y,p)  #Arbol con la arista a_k.
            if Arbol_1.buscarCiclos() == 1:  #Si a_k genera un ciclo.
                pass
            else:                          #e.o.c.
                Arbol = Arbol_1.copia() 
                k=k+1
                
            L.pop(0)    #Sacamos la arista a_k de la lista L.
            
            #Condicion de conexidad:
            if L == []:
                print('No te pases, no es conexa. Tengo cosas más importantes qué hacer >:(')
            else:
                pass            
        return Arbol   
        
            
