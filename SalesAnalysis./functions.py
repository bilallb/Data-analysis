import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def load_file(filename):
    try:
        df = pd.read_csv(filename)
        return df
    except pd.errors.EmptyDataError:
        return 'File is Empty.'
    except FileNotFoundError:
        return 'File is not found.'
df = load_file('product_data.csv')

def set_limits(x, y):
    plt.xlim([x[0], x[1]])
    plt.ylim([y[0], y[1]])

def plot(x, y, title, x_label, y_label):
    """Setting the theme"""
    sns.set_theme(style = 'dark')
    plt.grid(visible = True, animated = True)
    plt.title(title, fontweight = 'bold')

    """Plotting"""
    sns.scatterplot(x = x, y = y, c = 'brown')
    plt.ticklabel_format(style='plain', axis='x')

    """Naming axes"""
    plt.xlabel(x_label, fontweight = 'bold')
    plt.ylabel(y_label, fontweight = 'bold')

"""Plotting"""
def margin_suppliers():

    """Plot Margin based on suppliers"""
    sns.set_theme(style = 'dark')
    sns.barplot(data = df, x = df['supplier'], y = df['margin'], color = 'brown')
    plt.grid(visible=True, animated=True)
    plt.title('Margin based on each supplier', fontweight = 'bold')
    plt.xlabel('Supplier', fontweight = 'bold')
    plt.ylabel('Margin', fontweight = 'bold')

def profit_category():

    """Plot Profit of each category"""
    sns.set_theme(style = 'dark')
    sns.barplot(data =df, x = df['category'], y = df['profit'], color='brown')
    plt.title('Profit based on each category', fontweight = 'bold')
    plt.xlabel('Category', fontweight = 'bold')
    plt.ylabel('Profit', fontweight = 'bold')
    plt.grid(visible=True, animated=True)

def profit_cost_rice():

    """Profit based on cost price"""
    sns.set_theme(style = 'dark')
    sns.scatterplot(data = df, x = df['cost_price'], y = df['profit'], color = 'brown')
    plt.title('Profit based on cost price', fontweight = 'bold')
    plt.xlabel('Cost Price', fontweight = 'bold')
    plt.ylabel('Profit', fontweight = 'bold')
    plt.grid(visible=True, animated=True)



"""The main goal of this function is to get rid of the ??? values and replace each product in the right category"""
def smart_impute_categories(db):
    # filling the '???' values with null ones
    db['category'] = db['category'].replace('???', np.nan)
    # grouping category by supplier and filling the null values automatically
    df['category'] = df.groupby('supplier')['category'].transform(
        lambda x : x.fillna(x.mode()[0] if not x.mode().empty else "Unclassified")
    )
    remaining_nulls = db['category'].isna().sum()
    print(f"Data Cleaning Complete. Remaining unknown categories: {remaining_nulls}")

