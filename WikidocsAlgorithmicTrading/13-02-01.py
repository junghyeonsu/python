from pandas import Series, DataFrame

daeshin = {'open':  [11650, 11100, 11200, 11100, 11000],
           'high':  [12100, 11800, 11200, 11100, 11150],
           'low' :  [11600, 11050, 10900, 10950, 10900],
           'close': [11900, 11600, 11000, 11100, 11050]}

day = ['2020.02.27','2020.02.28','2020.02.29','2020.03.01','2020.03.02']

daeshin_day = DataFrame(daeshin,columns=['open','low','high','close'],index=day)
print(daeshin_day)
