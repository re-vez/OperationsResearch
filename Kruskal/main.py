from Algoritmo import * 




if __name__=='__main__':
    """Neta si no sabes que es un __main__, has fallado como 100tifico.
    Esto solo hace una grafica y la imprime.
	"""
    graph = Red(6)                 #Se crea una grafica de 5 nodos
    graph.agregarArista(1,2,4)   #Se van agregando aristas (x,y,p)
    graph.agregarArista(1,3,3.4)   #donde x,y son nodos y p es su peso.
    graph.agregarArista(1,4,0.6)
    graph.agregarArista(2,3,1.5)
    graph.agregarArista(2,6,9)
    graph.agregarArista(3,5,0.1)
    graph.agregarArista(4,5,5.1)
    graph.agregarArista(3,4,9)
    graph.agregarArista(2,5,-2)
    tree = graph.Kruskal()      #Aqui se aplica Kruskal.
    print(' ')
    print(graph.aristasConPesos())                 #Aqui imprime el AEPM en la terminalDe aqui en adelante es para imprimir la grafica con plt.

    
    Att = nx.get_edge_attributes(tree.G, 'peso')
    
    
    pos = nx.spring_layout(tree.G)
        
    edge_lables = nx.get_edge_attributes(tree.G,'peso')
         
    nx.draw(tree.G, pos, with_labels=True)
    nx.draw_networkx_edge_labels(tree.G,pos, lables = edge_lables)
    plt.show()
