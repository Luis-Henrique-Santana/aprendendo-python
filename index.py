#codigo de fib

n1 = 1
n2 = 1
aux = 0
cont = 0

while cont<5:
    print(n2,' ')
    aux = n1+n2
    n1 = n2
    n2 = aux
    cont = cont+1