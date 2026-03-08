# Get Env from user and print it

for i in range(5): # why range is used here? -> to repeat the block of code for 5 times
    env = input("Enter the env: ")

    print("user entered env is: ",env)

    # conditional statements - simple if else
    if env == "prod":
        print("Never deploy on friday!")
    elif env == "stg":
        print("Test Well,before prod")
    else:
        print("dev is the best env to work on")