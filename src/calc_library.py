import math

def add(a, b):
    return a+b # funkce vraci sectena cisla

def sub(a, b):
    return  a - b # odecte cisla

def mul(a,b):
    return a * b #funkce vynasobi vsechna zadana cisla

def div(a, b):
    return a/b # funkce vydeli dve cisla

def factorial(number):
    return math.factorial(number) # funkce spocita faktorial

def sqr(a, exp):
    return pow(a, 1/exp)

def power(a, exp):
    return pow(a, exp) #umocni cislo exponentem

def comb_num(n , k):
    return math.perm(n ,k) #vypocet kombinacniho cisla (n nad k)
