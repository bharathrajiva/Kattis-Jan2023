import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
iris = pd.read_csv('iris.csv', names=['sepal_length', 'sepal_width', 'petal_length',
'petal_width', 'class'])
print(iris.head())
wine_reviews = pd.read_csv('winemag-data-130k-v2.csv', index_col=0)
wine_reviews.head()

colors = {'Iris-setosa':'r', 'Iris-versicolor':'g', 'Iris-virginica':'b'}

fig, ax = plt.subplots()

for i in range(len(iris['sepal_length'])):
 ax.scatter(iris['sepal_length'][i], iris['sepal_width'][i],color=colors[iris['class'][i]])

ax.set_title('Iris Dataset')
ax.set_xlabel('sepal_length')
ax.set_ylabel('sepal_width')
plt.show()

columns = iris.columns.drop(['class'])

x_data = range(0, iris.shape[0])

fig, ax = plt.subplots()

for column in columns:
 ax.plot(x_data, iris[column], label=column)

ax.set_title('Iris Dataset')
ax.legend()
plt.show()

fig, ax = plt.subplots()

ax.hist(wine_reviews['points'])

ax.set_title('Wine Review Scores')
ax.set_xlabel('Points')
ax.set_ylabel('FrequencyA')
plt.show()

fig, ax = plt.subplots()

data = wine_reviews['points'].value_counts()

points = data.indexg
frequency = data.values

ax.bar(points, frequency)

ax.set_title('Wine Review Scores')
ax.set_xlabel('Points')
ax.set_ylabel('Frequency')
plt.show()

iris.plot.hist(subplots=True, layout=(2,2), figsize=(10, 10), bins=20)
plt.show()
wine_reviews['points'].value_counts().sort_index().plot.bar()
plt.show()
wine_reviews['points'].value_counts().sort_index().plot.barh()
plt.show()

wine_reviews.groupby("country").price.mean().sort_values(ascending=False)[:5].plot.bar()
plt.show()
corr = iris.corr()
fig, ax = plt.subplots()
im = ax.imshow(corr.values)
ax.set_xticks(np.arange(len(corr.columns)))
ax.set_yticks(np.arange(len(corr.columns)))
ax.set_xticklabels(corr.columns)
ax.set_yticklabels(corr.columns)
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",rotation_mode="anchor")
for i in range(len(corr.columns)):
 for j in range(len(corr.columns)):
  text = ax.text(j, i, np.around(corr.iloc[i, j], decimals=2),
   ha="center", va="center", color="black")
plt.show()
