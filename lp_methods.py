#Sebastian Gonzalez
import math
print("Please enter your x values separated by a space")
xlist= [int(x) for x in input().split()]
print("Please enter your y values separated by a space")
ylist= [int(x) for x in input().split()]
print("Please enter your value for alpha")
alpha = int(input("Alpha: "))
print("Please enter your value for E; E > 0")
e = int(input("E: "))

#each funtion will provide our values for getting a and b and new W

# W list is initialized to 1
def initialize_W(xlist):
    wlist = []
    for i in range(len(xlist)):
        wlist.append(1)
    return wlist

# x_bar = sigma(Wi*Xi)
def x_bar(xlist,wlist):
    sum = 0
    for i in range(len(xlist)):
        sum+= xlist[i] * wlist[i]
    return sum

# x_bar * y_bar = sigma(Wi*Xi*Yi)
def xy_bar(xlist,ylist,wlist):
    sum = 0
    for i in range(len(xlist)):
        sum+= xlist[i] * ylist[i] * wlist [i]
    return sum

#y_bar = sigma(Wi*Yi)
def y_bar(wlist,ylist):
    sum = 0
    for i in range(len(wlist)):
        sum += wlist[i] * ylist[i]
    return sum

# x^2_bar = sigma(Wi*(Xi^2))
def x_square_bar(wlist,xlist):
    sum = 0
    for i in range(len(wlist)):
        sum += wlist[i] * (xlist[i])**2
    return sum

# I_bar = Sigma(Wi)
def I_bar(wlist):
    sum = 0
    for i in range(len(wlist)):
        sum += wlist[i]
    return sum

# Wk = |Yk - (a * Xk + b)| ^ -(2-alpha)
def new_W(xlist,ylist,a,b,alpha):
    newList = []
    for i in range(len(xlist)):
        w = abs(ylist[i] - (a * xlist[i] + b))**(-(2-alpha))
        newList.append(w)
    return newList

def lp_robust(xlist,ylist,alpha,e):
    wlist =[1,2,1] # initialize_W(xlist)
    count = 0
    a,b = 0,0

    while count < e:
        a_top = xy_bar(xlist, ylist, wlist) * I_bar(wlist) - x_bar(xlist, wlist) * y_bar(wlist, ylist)
        a_down = x_square_bar(wlist, xlist) * I_bar(wlist) - ((x_bar(xlist, wlist)) ** 2)
        a = a_top / a_down
        b_top = y_bar(wlist,ylist) - (a * x_bar(xlist,wlist))
        b_bottom = I_bar(wlist)
        b = b_top/b_bottom

        print("I bar should be 4: ", I_bar(wlist))
        print("x bar should be 8: ", x_bar(xlist,wlist))
        print("y bar should be 7: ", y_bar(wlist,ylist))
        print("xy bar should be 15: ", xy_bar(xlist,ylist,wlist))
        print("xsquare bar should be 18: ", x_square_bar(wlist,xlist))

        #wlist = new_W(xlist,ylist,a,b,alpha)
        count+=1


    print("Final a value", a,"\nFinal b value: ",b)



# calling main function
lp_robust(xlist,ylist,alpha,e)
