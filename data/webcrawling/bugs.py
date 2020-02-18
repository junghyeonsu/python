from bs4 import BeautifulSoup
import requests
import pandas as pd

res = requests.get('https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01')
soup = BeautifulSoup(res.content, 'html.parser')
list = []
for data in soup.select('#CHARTrealtime > table > tbody > tr'):
     # rank = data.select('td')
     # rank = rank[1].find('strong').get_text()
     # name = data.th.p.a.text
     image = data.select('td')
     image = image[2].find('img')
     image = image.get("src")
     # list.append([rank, name])
     print(image)

# print(list)

# df = pd.DataFrame(list, columns=['rank','name'])
# df.to_csv('bugs_real_time_keyword.xls',index = False , encoding= 'cp949')

# df2 = pd.read_csv('daum_real_time_keyword.xls', encoding='cp949')
#
# print(df2)
#
# list2 = []
# for i in range(0,10):
#     list2.append([df2['rank'][i],df2['keyword'][i]])
#
# print(list2)