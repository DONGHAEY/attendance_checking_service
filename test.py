import pandas as pd

df = pd.read_csv('C:/Users/오동현/Desktop/check/ChurchMember.csv', engine='python', encoding='cp949')

a = df['name']
b = df['role']