#!/usr/bin/env python3

import time

# def timing_function(some_function):
#     """
#     Outputs the time a function takes
#     to execute.
#     """
#     def wrapper():
#         t1 = time.time()
#         print(some_function())
#         t2 = time.time()
#         return "Time it took to run the function: " + str((t2 - t1)) + " seconds"
#     return wrapper()

def timing_function(some_function, arg = 1000):
    """
    Outputs the time a function takes
    to execute.
    """

    def wrapper():
        t1 = time.time()
        print(some_function(arg))
        t2 = time.time()
        print("Time it took to run the function is {} seconds".format(str(t2 - t1)))
    return wrapper()
