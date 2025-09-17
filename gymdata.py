import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import textwrap

# loading data function
def load_data(file, quotechar, on_bad_lines):
    try:
        df = pd.read_csv(file, quotechar = quotechar, on_bad_lines = on_bad_lines)
        print(df.head())
        return df
    except FileNotFoundError:
        print('File not found')

# loading data
df = load_data('../data files/FitNotes_Export.csv', quotechar='"', on_bad_lines='skip')

# preparing data
category = df['Category']
weight = df['Weight']
exercises = df['Exercise']
Date = df['Date']
volume = df['Weight'] * df['Reps']

# Each muscle and its exercise
chest = df[df['Category'] == 'Chest']
back = df[df['Category'] == 'Back']
biceps = df[df['Category'] == 'Biceps']
triceps = df[df['Category'] == 'Triceps']
legs = df[df['Category'] == 'Legs']
forearms = df[df['Category'] == 'Forearm']
shoulders = df[df['Category'] == 'Shoulders']

# Creating a volume column
shoulders['Volume'] = shoulders['Weight'] * shoulders['Reps']
chest['Volume'] = chest['Weight'] * chest['Reps']
legs['Volume'] = legs['Weight'] * legs['Reps']
back['Volume'] = back['Weight'] * back['Reps']
triceps['Volume'] = triceps['Weight'] * triceps['Reps']
biceps['Volume'] = biceps['Weight'] * biceps['Reps']
forearms['Volume'] = forearms['Weight'] * forearms['Reps']

# Grouping exercises by volume
chest = chest.groupby(chest['Exercise'], as_index = False)['Volume'].sum()
back = back.groupby(back['Exercise'], as_index = False)['Volume'].sum()
biceps = biceps.groupby(biceps['Exercise'], as_index = False)['Volume'].sum()
triceps = triceps.groupby(triceps['Exercise'], as_index = False)['Volume'].sum()
shoulders = shoulders.groupby(shoulders['Exercise'], as_index = False)['Volume'].sum()
forearms = forearms.groupby(forearms['Exercise'], as_index = False)['Volume'].sum()
legs = legs.groupby(legs['Exercise'], as_index = False)['Volume'].sum()

# Fixing exercise names for readability
chest["Exercise"] = chest["Exercise"].apply(lambda var: "\n".join(textwrap.wrap(var, width=15)))
back['Exercise'] = back['Exercise'].apply(lambda var: "\n".join(textwrap.wrap(var, width=15)))
shoulders['Exercise'] = shoulders['Exercise'].apply(lambda var: "\n".join(textwrap.wrap(var, width=15)))
biceps['Exercise'] = biceps['Exercise'].apply(lambda var: "\n".join(textwrap.wrap(var, width=15)))
triceps['Exercise'] = triceps['Exercise'].apply(lambda var: "\n".join(textwrap.wrap(var, width=15)))
legs['Exercise'] = legs['Exercise'].apply(lambda var: "\n".join(textwrap.wrap(var, width=15)))
forearms['Exercise'] = forearms['Exercise'].apply(lambda var: "\n".join(textwrap.wrap(var, width=15)))

# Creating subplots for different muscle groups
fig, ax = plt.subplots(nrows=3, ncols=3, figsize=(12, 8))  # Reduced width

# Plotting the volume of each exercise for the chest on ax[0,0]
ax[0, 0].bar(chest['Exercise'], chest['Volume'], color='blue')
ax[0, 0].set_title('Chest Exercises Volume')
ax[0, 0].set_ylabel('Volume (kg)')
ax[0, 0].tick_params(axis='x', rotation=45, labelsize=8)  # Reduced label size

# Plotting for back exercises on ax[0,1]
ax[0, 1].bar(back['Exercise'], back['Volume'], color='green')
ax[0, 1].set_title('Back Exercises Volume')
ax[0, 1].set_ylabel('Volume (kg)')
ax[0, 1].tick_params(axis='x', rotation=45, labelsize=8)

# Plotting for biceps exercises on ax[0,2]
ax[0, 2].bar(biceps['Exercise'], biceps['Volume'], color='red')
ax[0, 2].set_title('Biceps Exercises Volume')
ax[0, 2].set_ylabel('Volume (kg)')
ax[0, 2].tick_params(axis='x', rotation=45, labelsize=8)

# Plotting for triceps exercises on ax[1,0]
ax[1, 0].bar(triceps['Exercise'], triceps['Volume'], color='orange')
ax[1, 0].set_title('Triceps Exercises Volume')
ax[1, 0].set_ylabel('Volume (kg)')
ax[1, 0].tick_params(axis='x', rotation=45, labelsize=8)

# Plotting for shoulders exercises on ax[1,1]
ax[1, 1].bar(shoulders['Exercise'], shoulders['Volume'], color='purple')
ax[1, 1].set_title('Shoulders Exercises Volume')
ax[1, 1].set_ylabel('Volume (kg)')
ax[1, 1].tick_params(axis='x', rotation=45, labelsize=8)

# Plotting for legs exercises on ax[1,2]
ax[1, 2].bar(legs['Exercise'], legs['Volume'], color='brown')
ax[1, 2].set_title('Legs Exercises Volume')
ax[1, 2].set_ylabel('Volume (kg)')
ax[1, 2].tick_params(axis='x', rotation=45, labelsize=8)

# Plotting for forearms exercises on ax[2,0]
ax[2, 0].bar(forearms['Exercise'], forearms['Volume'], color='cyan')
ax[2, 0].set_title('Forearms Exercises Volume')
ax[2, 0].set_ylabel('Volume (kg)')
ax[2, 0].tick_params(axis='x', rotation=45, labelsize=8)

# Hide empty subplots (ax[2,1] and ax[2,2])
ax[2, 1].axis('off')
ax[2, 2].axis('off')

plt.tight_layout()  # Ensures the subplots do not overlap
plt.show()

