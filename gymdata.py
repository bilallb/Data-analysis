import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# loading data function
def load_data(file, quotechar, on_bad_lines):
    try:
        df = pd.read_csv(file, quotechar = quotechar, on_bad_lines = on_bad_lines)
        print(df.head())
        return df
    except FileNotFoundError:
        print('File not found')

# loading data
df = load_data('FitNotes_Export.csv', quotechar='"', on_bad_lines='skip')

#preparing data
category = df['Category']
weight = df['Weight']
exercises = df['Exercise']
Date = df['Date']
volume = df['Weight'] * df['Reps']

#Each muscle and it's exercise
chest = df[df['Category'] == 'Chest']
back = df[df['Category'] == 'Back']
biceps = df[df['Category'] == 'Biceps']
triceps = df[df['Category'] == 'Triceps']
legs = df[df['Category'] == 'Legs']
forearms = df[df['Category'] == 'Forearm']
shoulders = df[df['Category'] == 'Shoulders']
shoulders['Volume'] = shoulders['Weight'] * shoulders['Reps']

# Grouping shoulders exercises by volume
shoulders = shoulders.groupby(shoulders['Exercise'], as_index = False)['Volume'].sum()
print(shoulders)

# setting ticks and showing the graph
plt.yticks(range(0,3200, 500))
x = np.arange(len(Date))                  # numeric range 0..1524
    # plot against numeric x

# fixing the x-axis text
import textwrap

shoulders["Exercise"] = shoulders["Exercise"].apply(lambda var: "\n".join(textwrap.wrap(var, width=15)))

#plt.bar(df['Date'], weight, color = 'red', align = 'center')

plt.figure(figsize = (10,5))
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.5, alpha = 0.2)
plt.title('Volume of shoulder execises', fontsize = 14, fontweight = 'bold', fontstyle = 'italic', color = 'black')
plt.xticks(rotation = 15, fontsize = 8, ha = 'right')
plt.xlabel('Exercises', color = 'blue')
plt.ylabel('Volume (in kgs)', color = 'black', fontweight = 'bold', fontstyle = 'italic')
plt.bar(shoulders['Exercise'], shoulders['Volume'], align = 'center', color = 'black')
plt.savefig('shouldersvolume.jpg')
plt.show()

