import math
from math import log10, floor
import numpy
import decimal
from decimal import Decimal

# =============== QUESTION 1 ===============

binary_num = "010000000111111010111001"
cur_power = 10
c = 0

while cur_power >= 0:
    if binary_num[11-cur_power] == '1':
        c += 2 ** cur_power
    cur_power -= 1

f = 0.0
cur_power = 1

for i in range(12, len(binary_num)):
    if(binary_num[i] == '1'):
        f += 0.5 ** cur_power
    cur_power += 1

decimal_num = (2 ** (c - 1023)) * (1 + f)

if binary_num[0] == '1': decimal_num *= -1

print(f'{decimal_num:.4f}', "\n")

# =============== QUESTION 2 =============== 

# New truncate function that rounds to
# specified amount of significant figures

def truncate(num, sigFigs):
    
    count = 0
    trunc_str = str(num)
    trunc_str2 = ''
    length = len(trunc_str)
    
    for i in range(0, length):
    
        if count < sigFigs:
            trunc_str2 = trunc_str2 + trunc_str[i]
            count += 1
            if trunc_str[i] == '.':
                count -= 1
            continue
        
        elif trunc_str[i] == '.':
            trunc_str2 = trunc_str2 + '.'
            continue
        
        trunc_str2 = trunc_str2 + '0'
        
        return float(trunc_str2)

trunc_num = truncate(decimal_num, 3)

print(trunc_num, "\n")

# =============== QUESTION 3 ===============

def round_sig(num, sigFigs):
    return round(num, sigFigs - int(floor(log10(abs(num)))) - 1)

round_num = round_sig(decimal_num, 3)

print(round_num, "\n")

# =============== QUESTION 4 ===============

abs_error = abs(decimal_num - round_num)
rel_error = str(abs(Decimal(decimal_num) - Decimal(round_num))/abs(Decimal(decimal_num)))

print(abs_error)
print(f'{Decimal(rel_error):.31f}', "\n")

# =============== QUESTION 5 ===============

def check_for_alternating(function_we_got: str):
    term_check = check_for_negative_1_exponent_term(function_we_got)
    return term_check
    
def check_for_decreasing(function_we_got: str, x: int) -> bool:
    k = 1
    starting_val = abs(eval(function_we_got))
    for k in range(2, 10):
        result = abs(eval(function_we_got))
        if starting_val <= result:
            return False
        starting_val = result
    return True
    
def check_for_negative_1_exponent_term(function: str) -> bool:
    if "-1**k" in function:
        return True
    return False

def minTerms(power, errorExp):
    # Solved formula for finding min terms needed for error
    return math.floor((10 ** (errorExp/power)))
    
summation5 = "(-1**k)*((x**k)/(k**3))"

alternating = check_for_alternating(summation5)
decreasing = check_for_decreasing(summation5, 1)

if alternating and decreasing:
    numTerms = minTerms(3, 4)
    print(numTerms, "\n")
    
# =============== QUESTION 6 ===============

def bisection_method(left: float, right: float, given_function: str, tolerance: float):
    x = left
    intial_left = eval(given_function)
    x = right
    intial_right = eval(given_function)
    if intial_left * intial_right >= 0:
        return
    diff: float = right - left
    
    iteration_counter = 0
    while (diff >= tolerance and iteration_counter <= 20):
        iteration_counter += 1
        mid_point = (left + right) / 2
        x = mid_point
        evaluated_midpoint = eval(given_function)
        if evaluated_midpoint == 0.0:
            break
        
        x = left
        evaluated_left_point = eval(given_function)
        
        first_conditional: bool = evaluated_left_point < 0 and evaluated_midpoint >0
        second_conditional: bool = evaluated_left_point > 0 and evaluated_midpoint < 0
        if first_conditional or second_conditional:
            right = mid_point
        else:
            left = mid_point
        
        diff = abs(right - left)
    
    return iteration_counter

function6 = "(x**3) + 4*(x**2) - 10"

print(bisection_method(-4, 7, function6, 0.0001), "\n")

# Newton Raphson

def custom_derivative(value):
    return (3 * value* value) - (2 * value)
    
def newton_raphson(initial_approximation: float, tolerance: float, sequence: str,):
    iteration_counter = 0
    x = initial_approximation
    f = eval(sequence)
    f_prime = custom_derivative(initial_approximation)
    approximation: float = f / f_prime
    
    while(abs(approximation) >= tolerance):
        x = initial_approximation
        f = eval(sequence)
        f_prime = custom_derivative(initial_approximation)
        approximation = f / f_prime
        initial_approximation -= approximation
        iteration_counter += 1
        
    return iteration_counter
        
print(newton_raphson(1.3652 , 0.0001, function6), "\n")

