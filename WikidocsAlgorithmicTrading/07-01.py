f = open('C:\\Users\\정현수\\Desktop\\buy_list.txt','rt',encoding='UTF-8')

line = f.readlines()

# print(line)

for line in line:
    nline = line.split('\n')[0]
    print(nline)

