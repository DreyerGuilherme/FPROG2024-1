def tabuada(numero):
    
    resultados = ""
    for i in range(1, 11):
        resultados += f"{numero} x {i} = {numero * i}\n"
    return resultados