#variable scope = where variables are accessible and visible
#scope resoultion = (LEGB) Local -> Enclosing function -> Global -> Built-in

from math import e

def func1():
    print(e)



e=3

func1()