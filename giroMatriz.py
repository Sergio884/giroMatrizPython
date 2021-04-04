figura = [["-","X","X"],
           ["X","-","-"],
           ["X","-","-"],
           ["-","X","X"]]

figura2 = [["O","-","X","X"],
           ["-","X","+","X"],
           ["X","+","X","-"],
           ["X","X","-","Q"]]

flecha1 = [["-","-","-","-","-","-","X","X"],
           ["-","-","-","-","-","X","X","-"],
           ["X","-","-","-","X","X","-","-"],
           ["X","-","-","X","X","-","-","-"],
           ["X","-","X","X","-","-","-","-"],
           ["X","X","X","-","-","-","-","-"],
           ["X","X","-","-","-","-","-","-"],
           ["X","X","X","X","X","X","-","-"]]

def girar(flecha,giros):
    nuevaFlecha = []
    for i in range(len(flecha[0])):
        nuevaFlecha.append([])
        for s in range(len(flecha)):
            nuevaFlecha[i].append(flecha[len(flecha)-(s+1)][i])

    print("======================================")
    for fila in nuevaFlecha:
        print(fila)

    if giros<=1:
        return 0
    else:
        girar(nuevaFlecha,giros-1)

def girarFlecha(flecha,cantidadGiros):
    for fila in flecha:
        print(fila)
    girar(flecha,cantidadGiros)

girarFlecha(figura,3)