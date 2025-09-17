import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

# function that allows to load files
def load_file(data):
    try:
        data = pd.read_csv(data) # reading the file into a variable
        print('File loaded')
        print(data.head())
        return data
    except FileNotFoundError: # error handling when unable to read the file
        print('File not found')

# loading file
bios = load_file('coffeedata.csv')

# Use regex to extract hours and minutes
bios['Duration_hours'] = bios['Duration'].str.extract(r'(\d+)h\s*(\d+)m').apply(
    lambda x: int(x[0]) + int(x[1]) / 60 if pd.notnull(x[0]) else None, axis=1
)

# sorting items
bios['Duration_hours'] = bios['Duration_hours'].sort_values(ascending = True)

# Plot
plt.figure(figsize = (7, 4)) # figure size
plt.grid(axis = 'y', color = 'grey', linewidth = 0.5, alpha = 0.7) # creating a grid
plt.bar(bios['Date'], bios['Duration_hours'], color='skyblue', edgecolor='black') # creating the graph (bar)

# specifying ticks
plt.xticks(rotation = 45, ha = 'right')
plt.yticks(range(0, 11, 1))

# Use regex to extract hours and minutes
bios['Duration_hours'] = bios['Duration'].str.extract(r'(\d+)h\s*(\d+)m').apply(
    lambda x: int(x[0]) + int(x[1]) / 60 if pd.notnull(x[0]) else None, axis=1
)
bios['Duration_hours'] = bios['Duration_hours'].sort_values(ascending = True)

# setting labels
plt.xlabel('Days')
plt.ylabel('Duration (in hours)')

# setting title and showing the graph
plt.title("My own sleeping data graph")
plt.show()
