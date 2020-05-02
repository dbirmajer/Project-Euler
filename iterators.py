#!/usr/bin/env python3

class Fibs:
    def __init__(self, a = 0, b = 1 ):
        self.a = a
        self.b = b
    def __next__(self):
        aux = self.a
        self.a, self.b = self.b, self.a + self.b
        return aux
    def __iter__(self):
        return self





