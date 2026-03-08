# SCRIPTING = set of instructions
# Function = Kaam

# ek kaam karo 2 number input lo aur sum print karao

def sum_of_num(): #function defination (KAAM)
    num1 = int(input("Enter num 1: ")) # steps
    num2 = int(input("Enter num 2: ")) # steps
    print(num1 + num2)

env = input("Enter env: ")

print("user entered env is: ", env)

if env == "prd":
    sum_of_num() # function calling

def take_backup():
    print("Backup script started..")

if day == "Monday":
    take_backup()