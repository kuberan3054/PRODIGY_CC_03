#Task-03

password = input("Enter password : ")


flag = [0,0,0,0]
symbol = ['@','!','$','#','&']

if len(password)>8:
    flag[0]=1 #very weak
    
for character in password:
    
    if character.isdigit():
        flag[1]=1 #weak
        
    elif character in symbol:
        flag[2]=1 #moderate
        
    elif character.isupper():
        flag[3]=1 #strong

strength = 4- flag.count(0)

if strength==0:
    print("Your password is very weak")
elif strength ==1:
    print("Your password is weak")
elif strength ==2:
    print("Your password is Moderate")
elif strength==3:
    print("Your password is strong")
elif strength==4:
    print("Your password is very Strong!")
        
    
