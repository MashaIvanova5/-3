
# Online Python - IDE, Editor, Compiler, Interpreter

import numpy as np
import math


def RotationMatrix(x, y, alpha): # пункт А
    M1 = np.array([[math.cos(alpha), math.sin(-1*alpha), 0], [math.sin(alpha), math.cos(alpha), 0], [0, 0, 1]])
    M2 = np.array([[1, 0, x], [0, 1, y], [0, 0, 1]])
    M3 = np.array([[1, 0, -1*x], [0, 1, -1*y], [0, 0, 1]])
    rotation = M2.dot(M1)
    rotation = rotation.dot(M3)
    return rotation


def GetNormal(xa, ya, za, xb, yb, zb, xc, yc, zc): # пункт Б

    vectorAB = np.array([xa-xb,ya-yb,za-zb])
    vectorAC = np.array([xa-xc,ya-yc,za-zc])
    norm_vector = np.cross(vectorAB,vectorAC)
    return norm_vector


def PointInFlat(xa, ya, za, xb, yb, zb, xc, yc, zc, x, y): # пункт Б
    First = (xa - x) * (yb - ya) -  (xb-xa) * (ya - y)
    Second = (xb - x) * (yc - yb) - (xc - xb) * (yb - y)
    Third = (xc - x) * (ya - yc) - (xa - xc) * (yc - y)
    if ((First < 0) and (Second < 0) and (Third < 0)) or((First >0) and (Second > 0) and (Third > 0)):
        return True
    else:
        return False

if name == 'main':
    #входные данные
    x = 1
    y = 10
    xa, ya, za = 5, 6, 9
    xb, yb, zb = 10, 13, 4
    xc, yc, zc = 14, 7, 8
    alpha = math.pi/3
    
    print ('Пункт а:') #Пункт А
    matr = RotationMatrix(x,y,alpha)
    print('Матрица преобразований:\n {0}'.format(matr))
    print('Пункт б:')  #Пункт Б
    normal = GetNormal(xa, ya, za, xb, yb, zb, xc, yc, zc)
    print('Вектор нормали будет иметь следующие координаты: {0}'.format(normal))
    
    print('Пункт в:') #Пункт В
    if PointInFlat(xa, ya, za, xb, yb, zb, xc, yc, zc,x,y):
        print('Точка с координатами: ({0},{1}) лежит в проекции треугольника ABC на плоскость xOy.'.format(x,y))
    else:
        print('Точка с координатами: ({0},{1}) не лежит в проекции треугольника ABC на плоскость xOy.'.format(x,y))