def percentage(person):
    tot=sum(person["marks"])
    return tot/4
a=[
    {"name" : "jay", "age" : 23, "marks" : [45,50,40,60]},
    {"name" : "jake", "age" : 22, "marks" : [55,70,80,70]},
    {"name" : "sunghoon", "age" : 22, "marks" : [55,60,75,80]},
    {"name" : "heeseung", "age" : 24, "marks" : [85,70,88,90]}
]
b=sorted(a,key=percentage,reverse=True)
print(b)

l=["fIRST","SECOND","THIRD","FOURTH"]
pos=0
for i in b:
    print("{} has scored {} % -----> stands {}".format(i["name"],percentage(i),l[pos]))
    pos=pos+1





