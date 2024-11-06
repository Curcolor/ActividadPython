palabra_user1 = input('Introduza la palabra a detectar como prefijo: ')
palabraCompleta = print("Escriba la palabra completa")

def detectPrefijo():
    if(palabraCompleta.startwith(palabra_user1)):
        return True
    

if(detectPrefijo):
    print(f'la palabra tiene de prefijo {palabra_user1}')
else:
    print(f'La palabra no tiene el prefijo a {palabra_user1}')

# hay un error de lógica pues simpre da true 