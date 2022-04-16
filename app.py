
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



book_data = pd.read_csv('bestsellers.csv')
print(book_data.head())

sns.countplot(book_data['Genre'])
plt.show()
plt.clf()

sns.boxplot(book_data['User Rating'])
plt.show()
plt.clf()

