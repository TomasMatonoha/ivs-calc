
def comp_input(string):
    binar_oper = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": div,
            "^": power,
            "C": comb_num

    }

    unar_oper = {
           "√": sqr,
           "!": factorial
    }

    for sign in ["+", "-"]:
        if sign in string:
            left, right = string.rsplit(sign,1)
            if sign == "+":
                return add(comp_input(left), comp_input(right))
            if sign == "-":
                return sub(comp_input(left), comp_input(right))

    for sign in ["*","/"]:
        if sign in string:
            left, right = string.rsplit(sign,1)
            if sign == "*":
                return mul(comp_input(left), comp_input(right))
            if sign == "/":
                return div(comp_input(left), comp_input(right))

    for sign in ["^", "C"]:
        if sign in string:
            left, right = string.rsplit(sign,1)
            if sign == "^":
                return power(comp_input(left), comp_input(right))
            if sign == "C":
                return comb_num(comp_input(left), comp_input(right))

    for sign, oper in unar_oper.items():
        if sign in string:
            number = string.replace(sign,"")
            return oper(comp_input(number))
  
    return float(string)

def isint(arg):
    return int(arg) == arg

def add(a, b):
    return a+b # funkce vraci sectena cisla

def sub(a, b):
    return  a - b # odecte cisla

def mul(a,b):
    return a * b #funkce vynasobi vsechna zadana cisla

def div(a, b):
    if (b != 0):
        return a/b # funkce vydeli dve cisla
    else:
        raise AssertionError(" Nelze dělit nulou")
def factorial(number):
    if not isint(number):
        raise TypeError("Není to celé číslo")
    elif (number < 0):
        raise ValueError("Není to kladné číslo")
    else:
        result = 1
        while (number > 0):
            result*= number
            number -= 1
    return result # funkce spocita faktorial

def sqr(a, exp):
    if (exp == 0):
        raise AssertionError("Neexistuje nultá odmocnina")
    if (a < 0) and (exp%2 == 0):
        raise AssertionError ("Nelze sudá odmocnina ze záporného čísla")
    else:
        return a ** (1/exp)

def power(a, exp):
    if isint(exp) and exp > 0:
        return a ** exp #umocni cislo exponentem
    elif (exp == 0):
        return 1
    else:
        raise TypeError("Není to celé číslo nebo exponent je záporný")

def comb_num(n , k):
    if not isint(n) or not isint(k):
        raise TypeError("Není to celé číslo")
    elif (n < k) or (n < 0) or (k < 0):
        raise ValueError("čísla nejsou kladná nebo je n menší než k")
    else:
        result = factorial(n)//(factorial (n-k) * factorial(k))
        return result #vypocet kombinacniho cisla (n nad k)
