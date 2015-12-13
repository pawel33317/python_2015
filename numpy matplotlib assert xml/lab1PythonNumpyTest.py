# -*- coding: utf-8 -*-
import numpy as np
from timeit import Timer

'''
instalacja modu��w
numpy, scipy, matplotlib jako exe
matpolot potrzebuje jeszcze kilku pakiet�w
instalacja przez pipa:


pip install cycler
pip install pyparsing
(jako root cmd)pip install --upgrade pip
pip install python-dateutil

numpy, scipy, matplotlib nie da si� przez pipa 
zainstalowa� bo co�tam wymagaja
'''


size_of_vec = 1000
def pure_python_version():
    X = range(size_of_vec)
    Y = range(size_of_vec)
    Z = []
    for i in range(len(X)):
        Z.append(X[i] + Y[i])
def numpy_version():
    X = np.arange(size_of_vec)
    Y = np.arange(size_of_vec)
    Z = X + Y
# timer_obj = Timer("x = x + 1", "x = 0")
timer_obj1 = Timer("pure_python_version()", "from __main__ import pure_python_version")
timer_obj2 = Timer("numpy_version()", "from __main__ import numpy_version")
print(timer_obj1.timeit(10))
print(timer_obj2.timeit(10))


