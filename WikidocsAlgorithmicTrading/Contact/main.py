class Contact:
    def __init__(self,name,phone_number,e_mail,addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print_info(self):
        print("----------------------------------")
        print("Name : " + self.name)
        print("PhoneNumber : " + self.phone_number)
        print("E-mail : " + self.e_mail)
        print("Address : " + self.addr)
        print("----------------------------------")

def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    menu = input("메뉴선택 : ")
    return int(menu)

def set_contact():
    name = input("Name : ")
    phone_number = input("PhoneNumber : ")
    e_mail = input("E-mail : ")
    addr = input("Address : ")
    return Contact(name, phone_number, e_mail, addr)

def del_contact(contact_list,name):
    for i,contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]

def save_contact(contact_list):
    f = open('C:\\Users\\정현수\\Desktop\\contact_list.txt','wt')
    for contact in contact_list:
        f.write(contact.name+'\n')
        f.write(contact.phone_number + '\n')
        f.write(contact.e_mail + '\n')
        f.write(contact.addr + '\n')
    f.close()

def load_contact(contact_list):
    f = open('C:\\Users\\정현수\\Desktop\\contact_list.txt', 'rt')
    lines = f.readlines()
    num = len(lines) / 4
    num = int(num)

    for i in range(num):
        name = lines[4 * i].rstrip('\n')
        phone = lines[4 * i + 1].rstrip('\n')
        email = lines[4 * i + 2].rstrip('\n')
        addr = lines[4 * i + 3].rstrip('\n')
        contact = Contact(name, phone, email, addr)
        contact_list.append(contact)
    f.close()

def run():
    contact_list = []
    load_contact(contact_list)
    while 1:
        menu = print_menu()
        if menu == 4:
            save_contact(contact_list)
            print("안녕히가세요.")
            break;

        if menu == 3:
            name = input("삭제하려는 이름 : ")
            del_contact(contact_list,name)

        if menu == 2:
            print("연락처의 개수는 총",len(contact_list),"개 입니다.")
            for c in contact_list:
                c.print_info()

        if menu == 1:
            contact = set_contact()
            contact_list.append(contact)


if __name__ == "__main__":
    run()

