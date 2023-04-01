from matplotlib import pyplot as plt
import math as m
import os

def func(a, b, c):
    f_sin = []
    for i in range(a, b, c):
        f_sin.append(m.sinh(i/2))
    return f_sin

print("function is sinh(x/2)")

if os.path.exists("data4/inp.txt"):
    f = open('data4/inp.txt', 'r')
else:
    print("couldn`t find input file, please parameters below")
    a = int(input("start = "))
    b = int(input("stop = "))
    c = int(input("step = "))

if os.path.exists("data4/outp.txt"):
    f1 = open('data4/outp.txt', 'w')
    f1.write("")
else:
    f1 = open('data4/outp.txt', 'a')

l = f.readline()

inp = l.split(" ")

if len(inp) == 0:
    print("file do not cotain parameters, please, write parameters below")
    a = int(input("start = "))
    b = int(input("stop = "))
    c = int(input("step = "))
elif len(inp) == 1:
    print("Found only start point, please write parameters below")
    a = int(inp[0])
    b = int(input("stop = "))
    c = int(input("step = "))
elif len(inp) == 2:
    print("Couldn`t find step parameter, please write parameters below")
    a = int(inp[0])
    b = int(inp[1])
    c = int(input("step = "))
else:
    if not(inp[0].isdigit()):
        print("Couldn`t find start parameter, please, enter below")
        a = int(input("start = "))
    
    if not(inp[1].isdigit()):
        print("Couldn`t find stop parameter, please, enter below")
        b = int(input("stop = "))
    
    if not(inp[2].isdigit()):
        print("Couldn`t find step parameter, please, enter below")
        a = int(input("step = "))
    
    if inp[0].isdigit() and inp[1].isdigit() and inp[2].isdigit():
        a, b, c = int(inp[0]), int(inp[1]), int(inp[2])

res = func(a, b, c)
xis = [i for i in range(a, b, c)]


for i in range(len(res)):
    f1.write("for x = " + str(xis[i]) + ", sinh(x/2) = " + str(res[i]) + "\n")


plt.plot(xis, res)
plt.title("Sinh(x/2)")
plt.ylabel("sinh(x/2)")
plt.xlabel("args")
plt.savefig("data4/Output.svg")
plt.show()

f.close