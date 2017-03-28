#!/usr/bin/python3
# -*- coding: utf-8 -*-


def sort_int():
    """Ordena crecientemente valores enteros"""
    print("Soy un modulo")
    numbers = input("Introduce números separados por comas: ")
    # numbers = map(int, numbers)
    numbers = numbers.split(",")
    numbers.sort(key=lambda x: int(x))
    print(numbers)
