class Atm(object):
    def __init__(self, card_number, pin_number):
        self.card_number = card_number
        self.pin_number = pin_number

    def balanceInquiry(self):
        print("Your balance is: $100")

    def cashWithdrawl(self, amount):
        new_amount = 100-amount
        print("You withdrawed: "+ str(amount))
        print("Your remaining balance is: "+ str(new_amount))

def main():
    name = input("Hello! What is your name? ")
    print("Hello "+name)
    card_number = input("Insert you card number: ")
    pin_number = input("Enter you pin: ")
    new_user = Atm(card_number, pin_number)

    print("Choose your activity")
    print("1. Balance Inquiry")
    print("2. Cash Withdrawl")
    activity = int(input("Enter activity choice: "))

    if(activity == 1):
        new_user.balanceInquiry()
    elif(activity == 2):
        amount = int(input("Enter the amount: "))
        new_user.cashWithdrawl(amount)
    else:
        print("Enter a valid number")

if __name__ == "__main__":
    main()
