x=1000
y=x

print(x,y,id(x),id(y),sep="\n")

y=1001 #solo se modifica y
print(x,y,id(x),id(y),sep="\n")
y=y-1
print(x,y,id(x),id(y),sep="\n") #apunta a un nuevo objeto, si usásemos 1001-1 si volvería a apuntar al objeto int 1000 que ya había
print(x==y, x is y) #is para saber si las dos variables apuntan al mismo objeto

print(type(x))
print(isinstance(x,int))

imprimir = print
imprimir("Hola")
imprimir(type(print))

