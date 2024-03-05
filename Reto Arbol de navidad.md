## Reto Arbol de navidad.

'''
A continuación, se detalla el patrón esperado para generar un árbol de 
Navidad utilizando asteriscos. Tu tarea es diseñar una función que 
acepte como parámetro tree_height, representando 
la cantidad de líneas que conformarán la altura del árbol de Navidad. 
Para cualquier árbol con una altura mayor o igual a 5, la función deberá 
añadir un tronco de tamaño 2 al final del árbol, de lo contrario un tronco
de tamaño 1.
Este enfoque permite crear una representación visual dinámica de un árbol 
de Navidad, adaptada a diferentes tamaños, 
manteniendo una base consistente para el tronco en árboles de 
tamaño considerable.
'''

## Recuerda utilizar el argumento de palabra clave end=""
## Considera la cantidad de espacios y asteriscos

# si tree_height = 2
# * |## 1 espacio, 1 asterisco
#***|## 0 espacios, 3 asteriscos
# * |

# si tree_height = 3
#  *  |## 2 espacios, 1 asterisco
# *** |## 1 espacio, 3 asteriscos
#*****|## 0 espacios, 5 asteriscos
#  *

# si tree_height = 4
#   *   |## 3 espacios, 1 asterisco
#  ***  |## 2 espacios, 3 asteriscos
# ***** |## 1 espacio, 5 asteriscos
#*******|## 0 espacio, 7 astericos
#   *   

# si tree_height = 5
#    *    |## 4 espacios, 1 asterisco
#   ***   |## 3 espacios, 3 asteriscos
#  *****  |## 2 espacios, 5 asteriscos
# ******* |## 1 espacio,  7 astericos
#*********|## 0 espacio,  9 asteriscos
#    *
#    *