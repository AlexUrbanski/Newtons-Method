import math 
from sympy import diff, Symbol
from sympy.parsing.sympy_parser import parse_expr
from sympy import *


def convert_func(a):
    '''
    A function to convert user input to the format
    needed for sympy
    '''
    string = []
    for i in range(len(a)):
        string.append(a[i])
    if string[0] == 'x':
        string.insert(0, ' ')            
    new_string = string 
    orig_len = len(string)
    j = 0
    while j <= orig_len-1:      
        if string[j] == 'x' and string[j-1] != ' ' :
            new_string.insert(j, "*")
            j+= 1           
        j+= 1                
    for k in range(len(new_string)):
        if new_string[k] == '^':
            new_string[k] = '**' 
    final_string = ''
    for h in range(len(new_string)):
        final_string = final_string + new_string[h]

    return final_string 


def newtons_method_polynomials():
    print ("Function format example: 3x^2 + 7x - 2\n")
    user_string = str(input("Enter a function: "))
    user_string = convert_func(user_string)
    x = Symbol('x')
    fx = lambdify(x, user_string)
    deriv = diff(user_string,x)
    f1x = lambdify(x, deriv)
    u_xnot = int(input("Enter an xnot value:  "))
    u_xnot_quant = int(input("xnot iterations:  "))
    xnot = u_xnot
    for i in range(u_xnot_quant):
       xnot = xnot - (fx(xnot)/f1x(xnot))
       print (f'X{i+1} = {xnot}') 


newtons_method_polynomials()
