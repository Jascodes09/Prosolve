password = input("Enter the password: ")
digit = 0
lowercase = 0
uppercase = 0
special = 0

if len(password) > 7:
    for i in password:
        if i.isupper():
            uppercase += 1
        elif i.islower():
            lowercase += 1
        elif i.isdigit():
            digit += 1    
        else:
            special += 1

    if uppercase >= 1 and lowercase >= 1 and digit >= 1 and special >= 1:
        print("Valid Password")
    else:
        print("Invalid Password")
else:
    print("Password must contain more than 7 characters")
