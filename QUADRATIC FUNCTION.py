import math
import matplotlib.pyplot as plt 
import numpy as np

class color:

    RED = '\033[91m'
    ENDC = '\033[0m'

def quadratic_function(a,b,c):
    #-------------------------CALCULATING ROOTS----------------------------
    #----------POSITIVE-------------------
    step1=round((b**2)-(4*a*c))
    step2=round(-(b)+(math.sqrt(step1)),3)
    positive=round(step2/(2*a),3)
    #----------NEGATIVE-------------------
    step2negative=round(-(b)-(math.sqrt(step1)),3)
    negative=round(step2negative/(2*a),3)
    #----------VERTEX--------------------
    xvertex=-(b)/(2*a)
    yvertex=((4*a*c)-(b**2))/(4*a)


    print("\nPOSITIVE ROOT\nStep n°1: "+ str(step1) + "\nStep n°2: " + str(step2) + "\nResult: " + str(positive) + "\n")
    print("NEGATIVE ROOT\nStep n°1: "+ str(step1) + "\nStep n°2: " + str(step2negative) + "\nResult: " + str(negative))
    print("\nVERTEX AXIS" + "\nX Axis : " + str(xvertex) + "\nY Axis : " + str(yvertex))


    #------------PLOT---------------------
    x = np.linspace(b,c,20)
    y = (a*x**2) + (b*x) +c

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    plt.plot(x,y, 'c')
    plt.annotate("|-------------------------[Vertex]"+"\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n!",(xvertex, yvertex),color="red")
    plt.annotate("|---[Root-1]\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n!", (positive, 0),color="purple")
    plt.annotate("|---[Root-2]\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n!", (negative, 0),color="blue")
    plt.annotate("--------------------------[Y-intercept]", (0, c),color="green")
    plt.show()  

#------------------------ TEST --------------------------------------

quadratic_function(2,4,-6)
