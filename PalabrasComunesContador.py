#PALABRAS COMUNES
#Encuentra o crea algunos textos que te gustaría analizar.
#Copia el texto sin formato desde tu navegador en un archivo de 
#texto en tu computadora (o descarga los archivos). Averigua 
#cuántas veces aparece una palabra o frase en el texto 
#(puedes usar el método count()).

def contar_palabras(archivo, palabra):

    with open(archivo, "r") as file:
        texto = file.read()
        contador = texto.count(palabra)
        return contador

archivo = "Colores.txt"
palabra_contar = "Verde"

a = contar_palabras(archivo, palabra_contar)
print(f"La palabra {palabra_contar} aparece {a} veces en el texto")