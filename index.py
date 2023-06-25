#if 5>3: # comentario se usa con (#) y no afecta el programa
# print('5 es mayor a 3')

x=5
y='techado mecanico' #variable contenido resumido de un texto
email='Minato56lol@gmail.com'

#print(email)
#print(x,y) #print es para ver en el terminal

a, b, c = 'larry', 'Minato', 'Nibba' # la (,) es para seprar varibles y inprimirlas mas rapido
#print(a,b,c)

larry = nibba = minato = 'minecraft'  #distintas variables que significan lo mismo 

#print (larry)
#print(minato)
#print(nibba)

#print (email + minato) el (+) es para juntar variables

palabra = 'hola mundo' # string
oracion = "hola mundo comilla doble" # string

entero = 20 # integer
conDecimales = 20.2 # float
complejo = 1j

# print(palabra, oracion, entero, conDecimales, complejo)

lista = ['Hola', 'Mundo', 'Chanchito feliz'] #una lista jaja
lista2 = lista.copy()
lista.append('Chanchito triste') #el (.append) es para agragar cosas a la lista sin modificarla

#lista.clear()    #el (.clear) es para borrar todo lo que este en la lista 
lista2 = lista.copy() #el (.copy) es para copiar la lista principal sin el (.append)

#print (lista, lista2.count(3)) #el (.count) es para contar cuantas veces se repite un elemento dentro de la lista selecionada (no se muestra la lista)
# print(len(lista), len(lista2)) len es para ver cuantos elementos hay en una lista

#Nombre de variable = len(nombre de lista en este caso lita)
#Nombre de variable = len(nombre de lista en este caso lita2)
#usamos print(nombre de la variable para ver el len de las listas)
#print(lista[numero de elemento de la lista]) el [] es para selecionar el numero del elemento que queremos usar desde 0 a infinito

#lista.pop() es para esliminar el ultimo elemento de la lista
#lista.remove() es para eliminar un elemento en especifico

lista.reverse() #es para modificar la lista y ponerla alrevez
lista.sort() #es para organizar la lista 

rango = range(6)
#Print(rango)

diccionario = {
    "nombre":"jose miguel",
    "apellido":"Marte Chaco",
    "edad": "16"
}
#inportante la coma y .get se puede utilizar tambien
#print(diccionario)
#print(diccionario['edad'])
diccionario['edad'] = '19' #para cambiar el valor de un elemento de el diccionario
#print(len(diccionario))

diccionario['acleta'] = 'Si'
#print(diccionario)
#diccionario.pop('acleta')
diccionario.clear()
diccionario2 = diccionario.copy()
#print(diccionario, diccionario2)

Familia = {
    "Jose": {
        "nombre": "Jose Miguel",
        "edad": 16
    },
    "lisa": {
        "nombre": "Lisa Maria",
        "edad": 17
    }
}
print(Familia)

verdadero = True
falso = False
