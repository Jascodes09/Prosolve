'''arr=[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]
for i in range(3):
    print(arr[1][0][i])'''

arr=[
     [1,2,3,4,5,6,7],
     [8,9,10,11,12,13,14],
     [15,16,17,18,19,20,21],
     [22,23,24,25,26,27,28],
     [29,30,31,32,33,34,35]
     ]
top=0
bottom=len(arr)-1
left=0
right=len(arr[0])-1
result=[]
#traverse from left to right
while top<= bottom and left <= right:
    for i in range(left,right+1):
        result.append(arr[top][i])
    top+=1
    #traverse from top to bottom
    for i in range(top,bottom+1):
        result.append(arr[i][right])
    right-=1
    #traverse from right to left
    if top<=bottom:   
       for i in range(right,left-1,-1):
        result.append(arr[bottom][i])
    bottom-=1
    #traverse from bottom to top
    if left<=right:
       for i in range(bottom,top-1,-1):
        result.append(arr[i][left])
    left+=1
print(result)
