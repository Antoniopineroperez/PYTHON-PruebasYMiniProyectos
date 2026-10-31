from FuncionesPython.ContarCadaPalabraTexto import contar_cada_palabra

texto = input("Introduce un texto o frase:\n")

resultado = contar_cada_palabra(texto)

#Mostrar los resultados ordenados de mayor a menor frecuencia
print("Lista de palabras de mayor a menor frecuencia:")
for palabra, conteo in resultado.most_common():
    print(f"'{palabra}': {conteo}")