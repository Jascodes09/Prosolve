def flames_game(name1, name2):
    #Step 1: Remove spaces and lowercase the names
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()

   # Step 2: Remove common letters one by one 
    for ch in name1[:]:
        if ch in name2:
            name1 = name1.replace(ch, "", 1)
            name2 = name2.replace(ch, "", 1)

   # Step 3: Count remaining letters 
    count = len(name1) + len(name2)

   # Step 4: Define FLAMES
    flames = ["F", "L", "A", "M", "E", "S"]

   # Step 5: Eliminate letters based on the count
    while len(flames) > 1:
        index = (count % len(flames)) - 1
        if index >= 0:
            right = flames[index+1:]
            left = flames[:index]
            flames = right + left
        else:
            flames = flames[:len(flames)-1]

    # Step 6: Map final letter to meaning
    result_map = {
        "F": "Friends",
        "L": "Love",
        "A": "Affection",
        "M": "Marriage",
        "E": "Enemies",
        "S": "Siblings"
    }

    return result_map[flames[0]]

name1 = input("Enter first name: ")
name2 = input("Enter second name: ")

relationship = flames_game(name1, name2)
print(f"The relationship between {name1} and {name2} is: {relationship}")


'''name1=input("Enter the first name:")
name2=input("Enter the second name:")
name1 = name1.replace(" ", "").lower()
name2 = name2.replace(" ", "").lower()
l1.list(name1)
l2.list(name2)
for i in range(len(l1)):
    for j in range(len(l2)):
        if(l1[i]==l2[j]):
            l1[i]='2'
            l2[j]='2'
print(l1)
print(l2)'''

