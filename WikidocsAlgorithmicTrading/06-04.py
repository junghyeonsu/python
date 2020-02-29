
class Stock:
    market = 'kospi'

s1 = Stock()
s1_market = s1.market
print(s1_market)
print(Stock.__dict__)
s1.market = "kosdaq"
print(s1.__dict__)