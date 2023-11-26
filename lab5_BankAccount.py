class BankAccount:

    __current_id = 0

    def __new__(cls, *args, **kwargs):
        cls.__current_id += 1
        return super().__new__(cls)

    def __init__(self, owner_name, balance = 0.0):
        self.__id = self.check_id(self.get_id())
        self.__owner_name = self.check_owner_name(owner_name)
        self.__balance = self.check_money(balance)

    def __str__(self):
        return f'Account {self.__id}: Owner name - {self.__owner_name}, Balance: {self.__balance}'

    @classmethod
    def get_id(cls):
        return cls.__current_id

    def deposit(self, money):
        self.__balance += self.check_money(money)
        print(f'You have successfully topped up your account by {money}')

    def withdraw(self, money):
        if money > self.__balance:
            raise Exception("you don't have that much money")
        self.__balance -= self.check_money(money)
        print(f'you have successfully withdrawn {money} from your account')

    @property
    def owner_name(self):
        return self.__owner_name

    @owner_name.setter
    def owner_name(self, new_name):
        self.__owner_name = self.check_owner_name(new_name)

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        self.__balance = self.check_money(new_balance)

    @staticmethod
    def check_id(id):
        if type(id) is not int:
            raise TypeError('id should be of type int')
        elif len(str(id)) >= 10:
            raise ValueError('id should contain 10 digits or less')
        else:
            return id

    @staticmethod
    def check_owner_name(owner_name):
        if type(owner_name) is not str:
            raise TypeError('owner_name should be of type str')
        elif not owner_name.replace(" ", "").isalpha():
            raise ValueError('owner_name should consist of only letters')
        elif len(owner_name.split()) != 3:
            raise ValueError('owwner_name should consist of three words')
        else:
            return owner_name

    @staticmethod
    def check_money(balance):
        if type(balance) not in (int, float):
            raise TypeError('amount of money should be of type int or float')
        if balance < 0:
            raise ValueError('amount of money should be positive')
        else:
            return balance
