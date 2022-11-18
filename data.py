import numpy as np
from numpy import random


def generate(n, m, t): # n milkmen, m factories, t items
    L = random.randint(200, 5000, size=(n))  # amount in litre
    R = random.randint(30, 50, size=(n))  # cost per litre in INR
    D = random.randint(10, 500, size=(n*m)) # distance in kilometre, colunm of n columns of size m
    Q = random.randint(100, 10000, size=(m*t)) # quantity of items, column m columns of size t
    A = random.uniform(0.1, 10, size = (t)) # amount per item in litre
    P = random.randint(1, 10, size = (t)) # production cost per item in INR
    S = random.randint(5, 500, size = (t)) # selling price per item in INR
    M = random.randint(1000, 50000, size = (t)) # minimum quantity per item
    C0 = 200
    l0 = 500
    return L, R, D, Q, A, P, S, M, C0, l0