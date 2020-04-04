# -*- coding: utf-8 -*-
"""Ecuaciones lineales_funcion de numpy.ipynb

"""

import numpy as np

a = np.array([[6,0,-1,0,0],[1,-1,0,0,0],[3,1,0,0,-4],[0,1,8,-11,2],[0,1,-9,0,0]])
b = np.array([50,0,0,0,-160])
x = np.linalg.solve(a,b)
print('la solución es: c1 = {},c2 = {},c3 = {},c4 = {},c5 = {}'.format(x[0],x[1],x[2],x[3],x[4]))
