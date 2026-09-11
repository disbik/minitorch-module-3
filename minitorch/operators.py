"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul

def mul(x: float, y: float) -> float:
    return float(x * y)

# - id

def id(x: float) -> float:
    return float(x)

# - add

def add(x: float, y: float) -> float:
    return float(x + y)

# - neg

def neg(x: float) -> float:
    return float(-x)

# - lt

def lt(x: float, y: float) -> float:
    if x < y: return 1.0
    return 0.0

# - eq

def eq(x: float, y: float) -> float:
    if x == y: return 1.0
    return 0.0

# - max

def max(x: float, y: float) -> float:
    if x > y: return float(x)
    return float(y)

# - is_close

def is_close(x: float, y: float) -> float:
    return abs(x - y) < 1e-2

# - sigmoid

def sigmoid(x: float) -> float:
    if x >= 0:
        return 1 / (1 + math.exp(-x))
    return math.exp(x) / (1 + math.exp(x))

# - relu

def relu(x: float) -> float:
    return x if x > 0.0 else 0.0

# - log

def log(x: float) -> float:
    return math.log(x)

# - exp

def exp(x: float) -> float:
    return math.exp(x)

# - log_back

def log_back(x: float, d: float) -> float:
    return d / x

# - inv

def inv(x: float) -> float:
    return 1 / x

# - inv_back

def inv_back(x: float, d: float) -> float:
    return -d / (x**2)

# - relu_back

def relu_back(x: float, d: float) -> float:
    if x > 0: return d
    return 0

#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map

# и тут мне стало лень прописывать классы, потому да, без них
def map(fn, ls):
    return [fn(x) for x in ls]

# - zipWith

def zipWith(fn, ls1, ls2):
    return [fn(x, y) for x, y in zip(ls1, ls2)]

# - reduce

def reduce(fn, ls, el):
    res = el
    for x in ls:
        res = fn(res, x)
    return res

# Use these to implement
# - negList : negate a list

def negList(ls):
    return map(neg, ls)

# - addLists : add two lists together

def addLists(ls1, ls2):
    return zipWith(add, ls1, ls2)

# - sum: sum lists

def sum(ls):
    return reduce(add, ls, 0.0)

# - prod: take the product of lists

def prod(ls):
    return reduce(mul, ls, 1.0)

# TODO: Implement for Task 0.3.
