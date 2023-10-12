#Observacion -> no se devera usar metodos como sum(),min(),max().
# se podra usar for, while, insert, split,join,append -> solo los metodos que se vio en clase

# 1. la funcion recibe como parametro un array y devera devolver el numero mayor del array
def numero_mayor(arr):
  mayor_numero=arr[0]
  for numero in arr:
    if numero >mayor_numero:
      mayor_numero=numero
  return mayor_numero
arr=[1,2,3,4,5]
mayor_numero=numero_mayor(arr)
print(mayor_numero)
  
# 2. la funcion recibe un string la funcion devera devolver el string ivertido ejem:entrada=hola, devuleve=aloh
def inverso(txt):
  string_invertido = ''
  for i in range(len(txt) - 1, -1, -1):
      string_invertido += txt[i]
  return string_invertido
print(inverso('hola'))
# 3. la funcion recibe un string y devuelve si la plabara es un palindromo True si no devuelve False: palindromo que se lee igual de derecha a izquierda y viceversa ejm: entrada=reconocer es palindromo se le igual de izquierda a derecha y viciversa
def palindromo(txt):
  for i in range(len(txt)):
    if txt[i] != txt[len(txt) - i - 1]:
      return False
  return True
print(palindromo('reconocer'))

# 4. la funcion recibe como parametro una letra y devuelve si la letra ingresada es vocal o consonante el mensaje devera ser si es vocal = 'es vocal' si es consonante 'es consonante'
def es_vocal(letra):
  vocales = ['a', 'e', 'i', 'o', 'u']
  if letra in vocales:
    return 'es vocal'
  else:
    return 'es consonante'
print(es_vocal('a'))
