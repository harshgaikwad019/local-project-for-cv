# this is a simple banking program
def show_balance():
    print(f"your current balance is ${balance:.2f}")

def deposit():
    amount = float(input(f"enter an amount to be deposited "))

    if amount < 0:
        print("that is not a vaild amount")
        return 0
    else:
        return amount

def withdraw():
    amount = float(input("enter amount to be withdrawn: "))

    if amount > balance:
        print("insufficient funds")
    elif amount < 0:
        print("the amount must be greater than 0")
    else:
        return amount

balance = 0
is_running = True


while is_running:
    print("banking program")
    print("1. show balance")
    print("2. deposit")
    print("3. withdraw")
    print("4. exit")

    choice = input("enter your choice (1-4)")

    if choice == '1':
        show_balance()
    elif choice == '2':
        balance += deposit()
    elif choice == '3':
        balance -= withdraw()
    elif choice == '4':
        is_running = False
    else:
        print("that is not a valid input that you enter")

print("thank you for join with us...")