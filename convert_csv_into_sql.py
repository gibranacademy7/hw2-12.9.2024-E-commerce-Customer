import sqlite3
import pandas as pd

conn = sqlite3.connect('datab.db')

df = pd.read_csv('commerce-e.csv')
df.to_sql('commerce-e', conn, if_exists='replace', index=False)

conn.commit()
conn.close()