from lab5_Bank import Bank

def main():
    mono = Bank()
    mono.add_account('Qwerty uiop asd', 666)
    mono.add_account('Nazar Leskiv Romanovich', 1000)
    mono.add_account('Viktor Decrot Viktor')
    mono.remove_account(3)
    mono.account_list[2].withdraw(999)
    mono.account_list[1].deposit(444)
    for i in mono.sort_accounts():
        print(i)


if __name__ == '__main__':
    main()
