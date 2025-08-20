num=10
for i in range(num):
    val=i+1
    dec=num-1
    for j in range(i+1):
        print(val,end=" ")
        val=val+dec
    print() 