balance = 0

# declaring constants
BANK_NAME = "Equitas Bank"

def deposit(n):
    global balance
    balance += n

def withdraw(n):
    global balance
    balance += n

def main():
    print(f"Balance: {balance}")

    deposit(100)
    withdraw(20)

    print(f"Balance: {balance}")

if __name__ == "__main__":
    main()