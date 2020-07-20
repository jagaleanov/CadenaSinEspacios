# Escribir un programa que elimine los blancos de una cadena de caracteres. 
# La cadena original y la transformada deben almacenarse de forma independiente

frase=(input("Introduzca una cadena de texto: "))
frase_fin = ""
for i in frase:
    if i != " ":
        frase_fin = frase_fin + i
 
print("La frase sin blancos es ",frase_fin," y la frase original es ",frase)   