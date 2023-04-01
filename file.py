import os

if os.path.exists("data/app.conf"):
    f = open('data/app.conf', 'r')
else:
    print("couldn`t find app.conf, please write a, b and c below")
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))

if os.path.exists("data/result.dat"):
    f1 = open('data/result.dat', 'w')
    f1.write("")
else:
    f1 = open('data/result.dat', 'a')

l = f.readline()

inp = l.split(" ")

if len(inp) == 0 or not(inp[0].isdigit()):
    print("file do not cotain numbers, please, write your a, b and c below")
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
elif len(inp) == 1:
    print("Couldn`t find b and c, please enter your numbers below")
    a = int(inp[0])
    b = int(input("b = "))
    c = int(input("c = "))
elif len(inp) == 2:
    print("Couldn`t find c, please enter your numbers below")
    a = int(inp[0])
    b = int(inp[1])
    c = int(input("c = "))
else:
    a, b, c = int(inp[0]), int(inp[1]), int(inp[2])

arr = []

for i in range(a):
    arr.append(b*i + c)
    f1.write(str(arr[i]) + ', ')


f.close