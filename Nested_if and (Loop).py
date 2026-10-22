#Nested If
marks = int(input("Enter marks: "))

if marks >= 35:
    if marks >= 75:
        print("Distinction")
    else:
        print("Pass")
else:
    print("Fail")

    
#Nested Loop
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()

