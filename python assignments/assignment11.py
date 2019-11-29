def wallet(balance):
    def deposit(amount):
        nonlocal balance
        balance = balance + amount
        print(amount," added to wallet. New Balance: ",balance)

    def spent(amount):
        nonlocal balance
        if amount <= balance:
            balance = balance - amount
            print(amount, " deducted from wallet. New Balance: ", balance)
        else:
            print("Insufficient Balance")

    def show():
        print("Available Balance: ", balance)
    li = [deposit, spent, show]
    return li

l1=wallet(1000)
deposit = l1[0]
spent = l1[1]
show = l1[2]
show()
deposit(500)
spent(1200)
show()