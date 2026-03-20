import numpy as np
from functions import  load_file

"""Loading data first"""
df = load_file('product_data.csv')

"""Dropping null values"""
df.dropna(inplace = True)


"""Creating new columns that will help us in the process"""
df['profit'] = df['list_price'] - df['cost_price']
df['margin'] = df['profit'] / df['list_price'] * 100
df['cash_cows'] = np.where(df['margin'] > 0, df['margin'], np.nan)
df['money_pits'] = np.where(df['margin'] < 0, df['margin'], np.nan)




