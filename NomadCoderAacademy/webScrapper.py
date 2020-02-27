import requests
from bs4 import BeautifulSoup
import csv

data = requests.get('https://www.ytn.co.kr/')

soup = BeautifulSoup(data.text, 'html.parser')

# div를 찾는데 attribute를 설정해주는데 id는 area_01을 가진 div를 찾는다.
crawling_data = soup.find("div" , {"id" : "area_01"}).find_all('li')

# print(crawling_data)

result_data = []

for i in crawling_data:
    rank = i.find('span').text
    title = i.find('a')['title']
    link = i.find('a')['href']
    result_data.append({
        'rank': rank,
        'title': title,
        'link': link
    })


# open 함수는 파이썬 기본함수, 첫번째 인자는 파일이름, 두번째는 모드
file = open("news.csv", mode="w", encoding="UTF-8")
# csv = comma seperate values 의 약자로 파일을 만든다.
writer = csv.writer(file)
# file 파일에 첫번째 줄을 입력한다.
writer.writerow(["rank", "title", "link"])

for row in result_data:
    print(row.values())
    writer.writerow(row.values())
