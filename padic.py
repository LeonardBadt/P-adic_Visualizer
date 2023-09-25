import numpy as num
import matplotlib.pyplot as plt
import math
import random

plt.axis([-1, 1, -1, 1])


colors = ("black", "white", "red", "orange", "yellow")

#initial starting points for equilateral trianngle(Some error b/c of irr. #)
Triangle = ((0.5, 0), (-0.5, 0), (0, math.sqrt(0.75)))
Square = ((0.5, 0.5), (0.5, -0.5), (-0.5, -0.5), (-0.5, 0.5))

#curtesy of wolframalpha : ..... add link to pentagon explanation
c_1 = (5**(1/2)-1)/4
c_2 = (5**(1/2)+1)/4
s_1 = ((10+2*5**(1/2))**(1/2))/4
s_2 = ((10-2*5**(1/2))**(1/2))/4
ratio = (1+5**(1/2))/2
Pentagon = ((0, 1), (-s_1, c_1), (s_1, c_1), (-s_2, -c_2), (s_2, -c_2))

A = Triangle
P = 3
e = 1/3

#To change Shape, make A = Shape name(i.e. Triangle, Square, Pentagon), P = # edges in shape
#To make sierpisnki shape, make e = 1/2
#To make piadic fractal, make e = 1/P

for i in range(P) :
    plt.plot(A[i][0], A[i][1], marker = "o", markersize = 5, markeredgecolor="red", markerfacecolor="green")


Q = [A[random.randint(0, P-1)]]

for i in range(1, 100000):
    #Chosing random intial points
    AR = A[random.randint(0, P-1)]

    while (AR == Q[0] and i == 1) :
        AR = A[random.randint(0, P-1)]

    delta = math.hypot(Q[i-1][0] - AR[0], Q[i-1][1] - AR[1])

    dist = e * delta

    x = (1-(dist / delta)) * AR[0] + ((dist / delta) * Q[i-1][0])
    y = (1-(dist / delta)) * AR[1] + ((dist / delta) * Q[i-1][1])

    plt.plot(x, y, color = "black", marker=",", markersize = 2)


    Q.append((x, y))

plt.show()