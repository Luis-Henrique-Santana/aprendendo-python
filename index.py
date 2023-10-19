#codigo de fib

n1 = 0
n2 = 1
aux = 0
cont = 0

while cont<50:
    print(n2,' ')
    aux = n1+n2
    n1 = n2
    n2 = aux
    cont = cont+1