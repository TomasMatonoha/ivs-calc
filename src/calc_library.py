import math

def add(a, b):
    return a+b # funkce vraci sectena cisla

def sub(a, b):
    return  a - b # odecte cisla

def mul(a,b):
    if isinstance(a, str) or isinstance(b, str):
        raise TypeError
    else:
        return a * b #funkce vynasobi vsechna zadana cisla

def div(a, b):
    return a/b # funkce vydeli dve cisla

def factorial(number):
    return math.factorial(number) # funkce spocita faktorial

def sqr(a, exp):
    if (a < 0) and (exp%2 == 0):
        raise AssertionError
    else:
        return pow(a, 1/exp)

def power(a, exp):
    if isinstance(exp, int):
        return pow(a, exp) #umocni cislo exponentem
    else:
        raise AssertionError

def comb_num(n , k):
    return math.comb(n ,k) #vypocet kombinacniho cisla (n nad k)
