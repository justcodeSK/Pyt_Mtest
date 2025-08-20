def Pyramid(int(num)):
    for i in range(num):
        for j in range(10-i):
            print(" ",end=" ")
        for j in range(i):
            print("*",end=" ")
        for j in range(i+1):
            print("*",end=" ")
        print()

num=input( "enter: ")
Pyramid(num)