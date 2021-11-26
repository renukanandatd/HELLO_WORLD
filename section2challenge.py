
while True:
    print("Please choose your option from the below:\n1.Learn Python\n2.Learn JAVA\n"
"3.Learn C\n4.Learn C++\n0.EXIT")
    choice=int(input("Enter your choice: "))
    if choice==0:
        print("EXIT")
        break
    elif choice in range(1,5):
        print("All the best")

    else:
        print("Invalid choice")