class Account:
    num_Accounts = 0
    def __init__(self, name):
        self.name = name
        Account.num_Accounts += 1
        print('계좌가 생성되었습니다.')

    def __del__(self):
        Account.num_Accounts -= 1
        print('계좌가 삭제되었습니다.')

a1 = Account('hyeonsu')
a2 = Account('kung')
a3 = Account('kwang')

print(Account.num_Accounts)
