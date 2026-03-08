# Get Env from user and print it

env = input("Enter the env: ")

print("user entered env is: ",env)

# conditional statements - simple if else
if env == "prod":
    print("Never deploy on friday!")
elif env == "stg":
    print("Test Well,before prod")
else:
    print("dev is the best env to work on")

a = int(input("Enter the num 1: "))
b = int(input("Enter the num 2: "))


print("Sum of a and b:",a + b)

