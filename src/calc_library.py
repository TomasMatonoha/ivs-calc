"""!
@file calc_library.py
@brief Implemetation of mathematical functions
@author Marie Patermannova (xpaterm00)
@date 2026-04-28
@version x.x
@details This library provides basic mathematical functions like addition or subtraction in addition to advanced functions like factorial or combinatory number.
"""


def comp_input(string):
    """!
    @brief Input handling function
    @details Main logic function which determines what operation to use and returns the result of that operation.
    @param string String of number/s with an operator
    @returns Result of the equation.
    """
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
                return round(add(comp_input(left), comp_input(right)),5)
            if sign == "-":
                return round(sub(comp_input(left), comp_input(right)),5)

    for sign in ["*","/"]:
        if sign in string:
            left, right = string.rsplit(sign,1)
            if sign == "*":
                return round(mul(comp_input(left), comp_input(right)),5)
            if sign == "/":
                return round(div(comp_input(left), comp_input(right)),5)

    for sign in ["^", "C"]:
        if sign in string:
            left, right = string.rsplit(sign,1)
            if sign == "^":
                return round(power(comp_input(left), comp_input(right)),5)
            if sign == "C":
                return round(comb_num(comp_input(left), comp_input(right)),5)

    for sign, oper in unar_oper.items():
        if sign in string:
            number = string.replace(sign,"")
            return round(oper(comp_input(number)),5)
  
    return float(string)


def isint(arg):
    """!
    @brief Determines if argument is integer
    @param arg Argument to be checked
    @returns True or false
    """
    return int(arg) == arg


def add(a, b):
    """!
    @brief Adds both arguments together
    @param a First number
    @param b Second number
    @returns Added numbers
    """
    return a+b # funkce vraci sectena cisla


def sub(a, b):
    """!
    @brief Subtracts second argument from the first
    @param a First number
    @param b Second number
    @returns Second argument subtracted from the first one
    """
    return  a - b # odecte cisla


def mul(a,b):
    """!
    @brief Multiplies both arguments between eachother
    @param a First number
    @param b Second number
    @returns Multiplication result between first and second argument
    """
    return a * b #funkce vynasobi vsechna zadana cisla


def div(a, b):
    """!
    @brief Divides first argument by the second argument
    @param a First number
    @param b Second number
    @returns First number divided by the second number
    """
    if (b != 0):
        return a/b # funkce vydeli dve cisla
    else:
        raise AssertionError("Cannot be divided by zero")


def factorial(number):
    """!
    @brief Computes factorial for a given number
    @param number Natural number
    @returns Factorial for the given number
    """
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


def sqr(a, exp):
    """!
    @brief Computes square of a given number with a given exponent
    @param a Number
    @param exp Exponent
    @returns Result of squaring a number with a given exponent
    """
    if (exp == 0):
        raise AssertionError("Doesn't exists zero square root")
    elif (a < 0) and (exp%2 == 0):
        raise AssertionError("Can't be even square root from negative number")
    else:
        return a ** (1/exp)


def power(a, exp):
    """!
    @brief Computes a number to a given power
    @param a Number
    @param exp Exponent
    @returns Number to a given power
    """
    if isint(exp) and exp > 0:
        return a ** exp #umocni cislo exponentem
    elif (exp == 0):
        return 1
    else:
        raise AssertionError("It's not an integer or exponent is negative")


def comb_num(n , k):
    """!
    @brief Computes the maximum number of combinations
    @param n Number of distinct elements
    @param k Number of elements
    @returns Maximum number of combinations
    """
    if not isint(n) or not isint(k):
        raise TypeError
    elif (n < k) or (n < 0) or (k < 0):
        raise ValueError("Numbers aren't positive or n is less than k")
    else:
        return factorial(n)//(factorial (n-k) * factorial(k)) #vypocet kombinacniho cisla (n nad k)
