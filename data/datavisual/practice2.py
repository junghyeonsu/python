import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

df = pd.read_csv('https://raw.githubusercontent.com/cranberrygame/data_analysis/master/StudentsPerformance.csv')

# 수학점수 + 읽기점수 + 쓰기점수 평균!
df['average'] = (df['math score'] + df['reading score'] + df['writing score']) / 3

sns.catplot(x='lunch',y='math score',data=df,hue='gender',kind='box')
plt.show()