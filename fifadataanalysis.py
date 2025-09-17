import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def load_data(file):
    try:
        data = pd.read_csv(file)
        print(data.head())
        return data
    except FileNotFoundError:
        print("File not found")

# loading our data and setting bins
fifa = load_data('../data files/fifa_data.csv')
bins = [40,50,60,70,80,90,100]


#Skill level of players
plt.hist(fifa.Overall, bins = bins)
plt.xlabel('Skill Level')
plt.ylabel('Number of Players')
plt.show()

#Player and the foot they play with
left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0]
right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0]

#getting labels and color ready
labels = ['Left', 'Right']
colors = ['grey', 'blue']
fifa.Weight = [int(x.strip('lbs')) if type(x) == str else x for x in fifa.Weight]
plt.style.use('ggplot')

#Creating Weights
light = fifa[fifa.Weight < 125].count()[0]
light_medium = fifa[(fifa.Weight < 150) & ( fifa.Weight >= 125)].count()[0]
medium = fifa[(fifa.Weight >= 150) &(fifa.Weight < 175)].count()[0]
medium_heavy = fifa[(fifa.Weight >= 175) & (fifa.Weight < 200)].count()[0]
heavy = fifa[(fifa.Weight >= 200) & (fifa.Weight < 250)].count()[0]

#data to plot using pie() method
#weights = [light, light_medium, medium, medium_heavy, heavy]
#labels = ['Under 125', '125-150', '150-175', '175-200', 'Over 200']
#explode = [.4,0,0,0,.4]
#plt.title('Weight Distribution of FIFA Players (in lbs)')
#plt.pie([left, right], labels = labels, colors = colors, autopct = '%.2f %%')
#plt.pie(weights, labels = labels, autopct = '%.2f %%', pctdistance = 0.8, explode = explode)

# 2nd graph, creating labels
plt.style.use('default')
labels = ['FC Barcelona', 'Real Madrid', 'NE Revolution']

# Preparing data
barcelona = fifa.loc[fifa['Club'] == 'FC Barcelona']['Overall']
madrid = fifa.loc[fifa['Club'] == 'Real Madrid']['Overall']
revs = fifa.loc[fifa['Club'] == 'New England Revolution']['Overall']

#setting figure size and plotting it as box
plt.figure(figsize = (8,5))
boxes = plt.boxplot([barcelona, madrid, revs], labels = labels, patch_artist = True, medianprops = {'linewidth' : 2})

#looping through boxes the variable and setting colors to each box
for box in boxes['boxes']:
    #set edge color
    box.set(color = 'black', linewidth = 2, facecolor = 'grey')

#title and y-label
plt.title('Professional Soccer Team comparison')
plt.ylabel('FIFA Overall Rating')
plt.show()





