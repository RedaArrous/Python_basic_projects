class BalanceException(Exception):
    pass


class Bankaccount:
    def __init__(self, inintialAmount, acctName):
        self.balance = inintialAmount
        self.name = acctName
        print(
            f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print(f"\n--Deposit complete:", end='')
        self.getBalance()

    def transactionCheck(self, amount):
        if self.balance - amount < 0:
            raise BalanceException(
                f"\nDear {self.name}, you don't have enough money to withdraw\nyou currently have ${self.balance:.2f}")

    def withdraw(self, amount):
        try:
            self.transactionCheck(amount)
            self.balance -= amount
            print(f"\n--Withdraw complete:", end="")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

    def transfer(self, acc2, amount):
        try:
            self.transactionCheck(amount)
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")
        else:
            self.balance -= amount
            acc2.balance += amount
            print("\n--Transfer complete:", end="")
            print(
                f"\n${amount} from Account '{self.name}' has been transfered to Account '{acc2.name}'", end='')
            self.getBalance()
            acc2.getBalance()


class InterestRewardsAcct(Bankaccount):
    def deposit(self, amount):
        self.balance += (amount * 1.05)
        print(f"\n--Deposit complete:\nYou recieved an extra ${amount * 0.05} as a reward", end='')
        self.getBalance()


class savingsAcct(InterestRewardsAcct):
    def __init__(self, inintialAmount, acctName):
        super().__init__(inintialAmount, acctName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.transactionCheck(amount)
            self.balance -= amount + self.fee
            print(f"\n--Withdraw complete:", end="")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")
