from lab5_BankAccount import BankAccount

class Bank:

    def __init__(self):
        self.__accounts_list = dict()

    def add_account(self, owner_name, balance = 0.0):
        acc = BankAccount(owner_name, balance)
        self.__accounts_list[acc.get_id()] = acc

    def remove_account(self, id):
        if id in self.__accounts_list.keys():
            self.__accounts_list.pop(id, None)
        else:
            raise KeyError('id was not found')

    def sort_accounts(self):
        return sorted(self.__accounts_list.values(), key=lambda x: x.balance, reverse = True)

    @property
    def account_list(self):
        return self.__accounts_list
