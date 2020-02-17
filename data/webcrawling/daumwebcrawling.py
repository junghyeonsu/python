from bs4 import BeautifulSoup
import requests
import pandas as pd


# 다음

res = requests.get('https://www.daum.net/')
soup = BeautifulSoup(res.text, 'html.parser')
Daumlist = []
for li in soup.select('#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin.hide > div.realtime_part > ol > li'):
    rank = li.div.div.span.span.text
    keyword = li.div.div.a.text
    Daumlist.append([rank, keyword])

print(Daumlist)

# 데이터 입력시키는 법 dataFrame을 통해서 값을 변수에 저장한뒤에 csv파일로 저장시킨다.
df = pd.DataFrame(Daumlist, columns=['rank','keyword'])
df.to_csv('daum_real_time_keyword.xls',index = False , encoding= 'cp949')

df2 = pd.read_csv('daum_real_time_keyword.xls', encoding='cp949')

print(df2)

list2 = []
for i in range(0,10):
    list2.append([df2['rank'][i],df2['keyword'][i]])

print(list2)