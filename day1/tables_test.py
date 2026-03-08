# num = int(input("Enter a number you want table for: "))



# # String Formatting "f"

# name = input("Enter your name: ")
# print(f"Hello {name}, welcome to python for devops class!")
# for i in range(1,11):
#     print(f"{num} x {i} = {num*i}")


# suraj = "chand"

# while suraj == "chand":
#     print("suraj is a good") # infinite loop
#     break

# real world

choice = input("Enter the choice (press q to quit): ")

while choice != "q":
    num = int(input("Enter a number you want table for: "))
    
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")
    choice = input("Enter the choice (press q to quit): ")

 