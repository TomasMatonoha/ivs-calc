
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
    return a+b 

def sub(a, b):
    return  a - b 

def mul(a,b):
    return a * b 

def div(a, b):
    if (b != 0):
        return a/b 
    else:
        raise AssertionError("Cannot be divided by zero")
def factorial(number):
    if not isint(number):
        raise TypeError("It's not an integer")
    elif (number < 0):
        raise ValueError("It's not a positive number")
    else:
        result = 1
        while (number > 0):
            result*= number
            number -= 1
    return result 

def sqr(a, exp):
    if (exp == 0):
        raise AssertionError("Doesn't exists zero square root")
    if (a < 0) and (exp%2 == 0):
        raise AssertionError ("Can't be even square root from negative number")
    else:
        return a ** (1/exp)

def power(a, exp):
    if isint(exp) and exp > 0:
        return a ** exp 
    elif (exp == 0):
        return 1
    else:
        raise TypeError("It's not an integer or exponent is negative")

def comb_num(n , k):
    if not isint(n) or not isint(k):
        raise TypeError("It's not an integer")
    elif (n < k) or (n < 0) or (k < 0):
        raise ValueError("NUmbers aren't positive or n is less than k")
    else:
        result = factorial(n)//(factorial (n-k) * factorial(k))
        return result
