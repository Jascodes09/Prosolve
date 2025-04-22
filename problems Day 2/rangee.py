a=0
for i in range(5):
    for j in range(i+1):
        if(i==j):
            continue
        a+=2
    a+=1
print(a)