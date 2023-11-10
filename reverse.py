# Funcion para invertir el string
def inverso(input_str):
    inverso = ""
    for char in input_str:
        inverso = char + inverso
    return inverso
#Ponemos los inputs para poder meter cualquier tipo de palabra
user_input = input("Introduce una palabra ")
resultado = inverso(user_input)
print("Palabra invrtida:", resultado)
