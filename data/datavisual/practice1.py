import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.DataFrame([
    [100, 200],
    [120, 205],
    [130, 210],
    [140, 220],
    [150, 230],
    [160, 250],
    [170, 270],
    [180, 280],
    [190, 285],
],columns=['height', 'footsize'])

print(data.head(10))
print(data.describe())
corr = data.corr()
print(corr)

# sns.barplot(x=data['height'], y=data['footsize'], data=data)
sns.heatmap(data=corr)
plt.show()

