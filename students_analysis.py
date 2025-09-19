import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# function to load the file while handling errors
def load_file(file):
    try:
        df = pd.read_csv(file)
        # pick 5000 random rows
        print(df.head())
        return df
    except FileNotFoundError:
        print('File not found')

# creating the variable that we will use
data = load_file('student_performance.csv')

# printing the columns
print(data.columns.unique())


# creating the whole figure
fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize = (10, 4)) # specifying the figure size and number of columns and rows

# figure title
fig.suptitle('Student Performance Comparison', weight = 'bold',y = 1, style = 'italic', fontsize = 14)

# scatter the first plot
ax[0].scatter(data["total_score"], data["weekly_self_study_hours"])
ax[0].set_title('Score based on weekly self study hours', fontstyle = 'italic') # small figure title

# x, y limits
plt.xlim(0, 120)
plt.ylim(0, 50)
# x, y labels
ax[0].set_xlabel('Total Score', fontweight = 'bold', fontsize = 8) # specifying color, size and weight
ax[0].set_ylabel('Hours spent studying weekly (in hours)', fontweight = 'bold', fontsize = 8) # specifying color, size and weight

# scatter the second plot
ax[1].scatter(data['total_score'], data['attendance_percentage'], color = 'red', linewidth = 0.5)
ax[1].set_title('Score based on attendance percentage', fontstyle = 'italic') # second figure title


# x, y limits
plt.xlim(0, 120)
plt.ylim(40, 110)

# x, y labels
ax[1].set_xlabel('Total Score',fontweight = 'bold', fontsize = 10) # specifying color, size and weight
ax[1].set_ylabel('Attendance (in percentage)', fontweight = 'bold', fontsize = 10) # specifying color, size and weight

plt.subplots_adjust(wspace=0.3) # a small space between the 2 figures

plt.show()