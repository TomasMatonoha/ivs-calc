
def comp_input(string):
    binar_oper = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": div,
            "^": power,
            "P": comb_num

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

    for sign in ["^", "P"]:
        if sign in string:
            left, right = string.rsplit(sign,1)
            if sign == "^":
                return power(comp_input(left), comp_input(right))
            if sign == "P":
                return comb_num(comp_input(left), comp_input(right))

    for sign, oper in unar_oper.items():
        if sign in string:
            number = string.replace(sign,"")
            return oper(comp_input(number))
  
    return float(string)


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
    if not isinstance(number, int):
        raise TypeError
    elif (number < 0):
        raise ValueError
    else:
        result = 1
        while (number > 0):
            result*= number
            number -= 1
    return result # funkce spocita faktorial

def sqr(a, exp):
    if (a < 0) and (exp%2 == 0):
        raise AssertionError
    else:
        result = a ** (1/exp)
        return result

def power(a, exp):
    if isinstance(exp, int) and exp > 0:
        result = 0
        reuslt = a ** exp
        return result #umocni cislo exponentem
    elif (exp == 0):
        return 1
    else:
        raise AssertionError

def comb_num(n , k):
    if not isinstance(n,int) or not isinstance(k,int):
        raise TypeError
    elif (n < k) or (n < 0) or (k < 0):
        raise ValueError
    else:
        result = factorial(n)//(factorial (n-k) * factorial(k))
        return result #vypocet kombinacniho cisla (n nad k)
