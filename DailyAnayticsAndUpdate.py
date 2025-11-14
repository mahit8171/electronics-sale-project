import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

from dateutil.utils import today

df = pd.read_csv("https://raw.githubusercontent.com/mahit8171/electronics-sale-project/refs/heads/main/Sales(in).csv")
df['date'] = pd.to_datetime(df['date'])
# print(df['date'][0])
today = datetime.today().date()
df['date'] = df['date'].dt.date
# print(df['date'][0])
# print(today)

df = df.loc[df['date'] == today]
# print(df.head())
df = df.groupby('product').agg(total_sales = ('sales', 'sum')).reset_index()
# print(df)
df.to_csv(f'{today} report.csv')
plt.bar(df['product'], df['total_sales'])
plt.savefig(f'{today}report.png')

