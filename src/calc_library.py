"""
@file calc_library.py
@brief Implemetation of mathematical functions
@author Marie Patermannova (xpaterm00)
@date 2026-04-28
@version x.x
@details This library provides basic mathematical functions like addition or subtraction in addition to advanced functions like factorial or combinatory number.
"""

"""
@brief Input handling function
@details Main logic function which determines what operation to use and returns the result of that operation.
@param string String of number/s with an operator
@returns Result of the equation.
"""
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

"""
@brief Determines if argument is integer
@param arg Argument to be checked
@returns True or false
"""
def isint(arg):
    return int(arg) == arg

"""
@brief Adds both arguments together
@param a First number
@param b Second number
@returns Added numbers
"""
def add(a, b):
    return a+b # funkce vraci sectena cisla

"""
@brief Subtracts second argument from the first
@param a First number
@param b Second number
@returns Second argument subtracted from the first one
"""
def sub(a, b):
    return  a - b # odecte cisla

"""
@brief Multiplies both arguments between eachother
@param a First number
@param b Second number
@returns Multiplication result between first and second argument
"""
def mul(a,b):
    if isinstance(a, str) or isinstance(b, str):
        raise TypeError
    else:
        return a * b #funkce vynasobi vsechna zadana cisla

"""
@brief Divides first argument by the second argument
@param a First number
@param b Second number
@returns First number divided by the second number
"""
def div(a, b):
    return a/b # funkce vydeli dve cisla

"""
@brief Computes factorial for a given number
@param number Natural number
@returns Factorial for the given number
"""
def factorial(number):
    if not isint(number):
        raise TypeError
    elif (number < 0):
        raise ValueError
    else:
        result = 1
        while (number > 0):
            result*= number
            number -= 1
    return result # funkce spocita faktorial

"""
@brief Computes square of a given number with a given exponent
@param a Number
@param exp Exponent
@returns Result of squaring a number with a given exponent
"""
def sqr(a, exp):
    if (a < 0) and (exp%2 == 0):
        raise AssertionError
    else:
        result = a ** (1/exp)
        return result

"""
@brief Computes a number to a given power
@param a Number
@param exp Exponent
@returns Number to a given power
"""
def power(a, exp):
    if isint(exp) and exp > 0:
        result = 0
        result = a ** exp
        return result #umocni cislo exponentem
    elif (exp == 0):
        return 1
    else:
        raise AssertionError

"""
@brief Computes the maximum number of combinations
@param n Number of distinct elements
@param k Number of elements
@returns Maximum number of combinations
"""
def comb_num(n , k):
    if not isint(n) or not isint(k):
        raise TypeError
    elif (n < k) or (n < 0) or (k < 0):
        raise ValueError
    else:
        result = factorial(n)//(factorial (n-k) * factorial(k))
        return result #vypocet kombinacniho cisla (n nad k)
