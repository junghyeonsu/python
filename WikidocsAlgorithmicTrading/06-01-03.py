class BusinessCard:
    def add(self,name,email,number):
        self.name = name
        self.email = email
        self.number = number

    def print(self):
        print('--------------------------------')
        print('name : ',self.name)
        print('email : ', self.email)
        print('phone : ', self.number)
        print('--------------------------------')


person1 = BusinessCard()
person1.add('정현수','jung660317@naver.com','010-6299-7154')
person1.print()

# 06-02
class perfectBusinessCard:
    def __init__(self,name,email,number):
        self.name = name
        self.email = email
        self.number = number
        print('객체가 생성되었습니다.')

    def print(self):
        print('--------------------------------')
        print('name : ',self.name)
        print('email : ', self.email)
        print('phone : ', self.number)
        print('--------------------------------')

person2 = perfectBusinessCard('junghyeonsu','jhs6567154@naver.com','01062997154')
person2.print()
