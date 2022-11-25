# Python Environment Setting
import seaborn as sns
sns.set_theme()
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os

'''heatmap parameter'''
vmax=0.05
bw_method=0.2




'''foodzone parameter'''

# food zone 표시 (rectangle)
rec_left = -15
rec_bot = -7.5

rec_top = 2.5
rec_right = -9.2

rec_width = abs(rec_right-rec_left)
rec_height = abs(rec_top-rec_bot)


# Import Data
pathname1 = "/Users/Jace/heatmap/220926 on off on/excel/csv/220926 WT -Trial5_ piezo1 m torquer_38-11_off on off_0-10min.csv"
pathname2 = "/Users/Jace/heatmap/220926 on off on/excel/csv/220926 WT -Trial5_ piezo1 m torquer_38-11_off on off_10-20min.csv"
pathname3 = "/Users/Jace/heatmap/220926 on off on/excel/csv/220926 WT -Trial5_ piezo1 m torquer_38-11_off on off_20-30min.csv"




# get sample title
title = os.path.basename(pathname1)
fig_title = title[:-4]


dataset = pd.read_csv(
    pathname1,
    sep=",",  # Separate by ','
    names=["x_center", "y_center", "time_spent"],  # Name of the columns
    header=None,
)

# Check if data is as  expected
head = dataset.head() 
#print(head)



'''plot figure 1 - just the figure itself'''
plt.figure(1) #first figure will be original version without zone time spent calculation

'''plotting settings'''
# Make the Stage
# set axis
plt.axis([-20, 20, -20, 20])
plt.axis("equal")

# create circle with (x, y) coordinates at (0, 0), with radius of 16
# set the color of the stage (lowest color of colorbar scheme)
# color can be picked by using the "Digital Color Meter" Application from Mac OS Launchpad 
# set the color of the edge - Black
background_circle = plt.Circle((0, 0), radius=20, facecolor="#000080", alpha=1, edgecolor="black")

# add circle to plot (gca means "get current axis")
plt.gca().add_artist(background_circle)


# Draw the 2D Density plot using Seaborn KDE plot function
# 2D KDE Plot - but in KDE mode
# Set the colormap to 'jet' (same as raw data)
cmap = matplotlib.cm.jet

# Draw plot
ax = sns.kdeplot(
    data=dataset, #raw data table
    x="x_center", # select the x data column
    y="y_center", # select the y data column
    levels=100, # how many levels of data
    shade=True, # color in the density plots
    thresh=0.067, # anything above the value "0.1" will be colored
    # here we used 0.067 because data is tracked in 0.067 seconds time interval
    # if we see heatmap plot sticking out of the circle edit threshold to higher value
    alpha=None, # Transparency - No transparency
    cbar=True, # Show colorbar
    cbar_kws={'label': 'Time spent', 'ticks': []},
    vmin=0, vmax=vmax,
    bw_method=bw_method, # control bandwidth of plot
    cmap=cmap # colormap is the colormap we set earlier in line 37
)




# Modifying the 2D density plot (heatmap)

plt.title(fig_title, fontsize=14) # Add the title
plt.grid() # remove gridlines
ax.set_facecolor("white") # edit background color
myaxis = [-25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25] # set axis points


# Labels
plt.xlabel("X", fontsize=12) # x axis label
plt.ylabel("Y", fontsize=12) # y axis label
plt.xticks(myaxis) # set the x axis values to specific values
plt.yticks(myaxis) # y axis values
plt.xticks(color='w') # hide axis plot label
plt.yticks(color='w') # hide axis plot label


#save plot
plt.savefig('heatmap/no zone/'+str(fig_title)+'.png', bbox_inches='tight', dpi=1200)




'''--------------------------------------------------------------------------------'''

'''plot figure 2 - zone + time spent calculated'''
plt.figure(2) #second figure includes zone and time spent calculation

'''plotting settings'''
# Make the Stage
# set axis
plt.axis([-20, 20, -20, 20])
plt.axis("equal")

# create circle with (x, y) coordinates at (0, 0), with radius of 16
# set the color of the stage (lowest color of colorbar scheme)
# color can be picked by using the "Digital Color Meter" Application from Mac OS Launchpad 
# set the color of the edge - Black
background_circle = plt.Circle((0, 0), radius=20, facecolor="#000080", alpha=1, edgecolor="black")

# add circle to plot (gca means "get current axis")
plt.gca().add_artist(background_circle)


# Draw the 2D Density plot using Seaborn KDE plot function
# 2D KDE Plot - but in KDE mode
# Set the colormap to 'jet' (same as raw data)
cmap = matplotlib.cm.jet

# Draw plot
ax = sns.kdeplot(
    data=dataset, #raw data table
    x="x_center", # select the x data column
    y="y_center", # select the y data column
    levels=100, # how many levels of data
    shade=True, # color in the density plots
    thresh=0.067, # anything above the value "0.1" will be colored
    # here we used 0.067 because data is tracked in 0.067 seconds time interval
    # if we see heatmap plot sticking out of the circle edit threshold to higher value
    alpha=None, # Transparency - No transparency
    cbar=True, # Show colorbar
    cbar_kws={'label': 'Time spent', 'ticks': []},
    vmin=0, vmax=vmax,
    bw_method=bw_method, # control bandwidth of plot
    cmap=cmap # colormap is the colormap we set earlier in line 37
)




'''draw zone rectangle'''





left, bottom, width, height = (rec_left, rec_bot, rec_width, rec_height)
rect=mpatches.Rectangle((left,bottom),width,height, 
                        fill=False,
                        color="grey",
                        linestyle = ":",
                       linewidth=2)
                       #facecolor="red")
plt.gca().add_patch(rect)





'''draw zone and calculate the time spent inside the zone'''
'''zone Time Calculation'''
#create dataset
x_center = dataset["x_center"]
y_center = dataset["y_center"]

#list coordinates
coords_list = []

for x_value, y_value in zip(x_center, y_center):
    coords_list.append((x_value, y_value))

time_counter = 0

for x, y in coords_list:
    if (rec_left <= x <= rec_right) and (rec_bot <= y <= rec_top):
        time_counter = time_counter + 0.067
    
print("the time in the food zone is", time_counter, "seconds", "or", time_counter//60, "mins and", time_counter%60, "seconds")

'''print calculated values onto the plot'''
plt.text(-25,-23, 'Time spent in food zone = %.2f sec' % (time_counter), fontsize=10, color = "black", alpha=1)



# Modifying the 2D density plot (heatmap)

plt.title(fig_title, fontsize=14) # Add the title
plt.grid() # remove gridlines
ax.set_facecolor("white") # edit background color
myaxis = [-25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25] # set axis points


# Labels
plt.xlabel("X", fontsize=12) # x axis label
plt.ylabel("Y", fontsize=12) # y axis label
plt.xticks(myaxis) # set the x axis values to specific values
plt.yticks(myaxis) # y axis values
plt.xticks(color='w') # hide axis plot label
plt.yticks(color='w') # hide axis plot label


#save plot
plt.savefig('heatmap/zone/'+str(fig_title)+'.png', bbox_inches='tight', dpi=1200)





# Python Environment Setting
import seaborn as sns
sns.set_theme()
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os

'''heatmap parameter'''
#check above 

# Import Data


# get sample title
title = os.path.basename(pathname2)
fig_title = title[:-4]


dataset = pd.read_csv(
    pathname2,
    sep=",",  # Separate by ','
    names=["x_center", "y_center", "time_spent"],  # Name of the columns
    header=None,
)

# Check if data is as  expected
head = dataset.head() 
#print(head)



'''plot figure 3 - just the figure itself'''
plt.figure(3) #first figure will be original version without zone time spent calculation

'''plotting settings'''
# Make the Stage
# set axis
plt.axis([-20, 20, -20, 20])
plt.axis("equal")

# create circle with (x, y) coordinates at (0, 0), with radius of 16
# set the color of the stage (lowest color of colorbar scheme)
# color can be picked by using the "Digital Color Meter" Application from Mac OS Launchpad 
# set the color of the edge - Black
background_circle = plt.Circle((0, 0), radius=20, facecolor="#000080", alpha=1, edgecolor="black")

# add circle to plot (gca means "get current axis")
plt.gca().add_artist(background_circle)


# Draw the 2D Density plot using Seaborn KDE plot function
# 2D KDE Plot - but in KDE mode
# Set the colormap to 'jet' (same as raw data)
cmap = matplotlib.cm.jet

# Draw plot
ax = sns.kdeplot(
    data=dataset, #raw data table
    x="x_center", # select the x data column
    y="y_center", # select the y data column
    levels=100, # how many levels of data
    shade=True, # color in the density plots
    thresh=0.067, # anything above the value "0.1" will be colored
    # here we used 0.067 because data is tracked in 0.067 seconds time interval
    # if we see heatmap plot sticking out of the circle edit threshold to higher value
    alpha=None, # Transparency - No transparency
    cbar=True, # Show colorbar
    cbar_kws={'label': 'Time spent', 'ticks': []},
    vmin=0, vmax=vmax,
    bw_method=bw_method, # control bandwidth of plot
    cmap=cmap # colormap is the colormap we set earlier in line 37
)




# Modifying the 2D density plot (heatmap)

plt.title(fig_title, fontsize=14) # Add the title
plt.grid() # remove gridlines
ax.set_facecolor("white") # edit background color
myaxis = [-25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25] # set axis points


# Labels
plt.xlabel("X", fontsize=12) # x axis label
plt.ylabel("Y", fontsize=12) # y axis label
plt.xticks(myaxis) # set the x axis values to specific values
plt.yticks(myaxis) # y axis values
plt.xticks(color='w') # hide axis plot label
plt.yticks(color='w') # hide axis plot label


#save plot
plt.savefig('heatmap/no zone/'+str(fig_title)+'.png', bbox_inches='tight', dpi=1200)




'''--------------------------------------------------------------------------------'''

'''plot figure 4 - zone + time spent calculated'''
plt.figure(4) #second figure includes zone and time spent calculation

'''plotting settings'''
# Make the Stage
# set axis
plt.axis([-20, 20, -20, 20])
plt.axis("equal")

# create circle with (x, y) coordinates at (0, 0), with radius of 16
# set the color of the stage (lowest color of colorbar scheme)
# color can be picked by using the "Digital Color Meter" Application from Mac OS Launchpad 
# set the color of the edge - Black
background_circle = plt.Circle((0, 0), radius=20, facecolor="#000080", alpha=1, edgecolor="black")

# add circle to plot (gca means "get current axis")
plt.gca().add_artist(background_circle)


# Draw the 2D Density plot using Seaborn KDE plot function
# 2D KDE Plot - but in KDE mode
# Set the colormap to 'jet' (same as raw data)
cmap = matplotlib.cm.jet

# Draw plot
ax = sns.kdeplot(
    data=dataset, #raw data table
    x="x_center", # select the x data column
    y="y_center", # select the y data column
    levels=100, # how many levels of data
    shade=True, # color in the density plots
    thresh=0.067, # anything above the value "0.1" will be colored
    # here we used 0.067 because data is tracked in 0.067 seconds time interval
    # if we see heatmap plot sticking out of the circle edit threshold to higher value
    alpha=None, # Transparency - No transparency
    cbar=True, # Show colorbar
    cbar_kws={'label': 'Time spent', 'ticks': []},
    vmin=0, vmax=vmax,
    bw_method=bw_method, # control bandwidth of plot
    cmap=cmap # colormap is the colormap we set earlier in line 37
)




'''draw zone rectangle'''


# food zone 표시 (rectangle)
# 위에서 만져놨음

left, bottom, width, height = (rec_left, rec_bot, rec_width, rec_height)
rect=mpatches.Rectangle((left,bottom),width,height, 
                        fill=False,
                        color="grey",
                        linestyle = ":",
                       linewidth=2)
                       #facecolor="red")
plt.gca().add_patch(rect)





'''draw zone and calculate the time spent inside the zone'''
'''zone Time Calculation'''
#create dataset
x_center = dataset["x_center"]
y_center = dataset["y_center"]

#list coordinates
coords_list = []

for x_value, y_value in zip(x_center, y_center):
    coords_list.append((x_value, y_value))

time_counter = 0

for x, y in coords_list:
    if (rec_left <= x <= rec_right) and (rec_bot <= y <= rec_top):
        time_counter = time_counter + 0.067
    
print("the time in the food zone is", time_counter, "seconds", "or", time_counter//60, "mins and", time_counter%60, "seconds")

'''print calculated values onto the plot'''
plt.text(-25,-23, 'Time spent in food zone = %.2f sec' % (time_counter), fontsize=10, color = "black", alpha=1)



# Modifying the 2D density plot (heatmap)

plt.title(fig_title, fontsize=14) # Add the title
plt.grid() # remove gridlines
ax.set_facecolor("white") # edit background color
myaxis = [-25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25] # set axis points


# Labels
plt.xlabel("X", fontsize=12) # x axis label
plt.ylabel("Y", fontsize=12) # y axis label
plt.xticks(myaxis) # set the x axis values to specific values
plt.yticks(myaxis) # y axis values
plt.xticks(color='w') # hide axis plot label
plt.yticks(color='w') # hide axis plot label


#save plot
plt.savefig('heatmap/zone/'+str(fig_title)+'.png', bbox_inches='tight', dpi=1200)




# Python Environment Setting
import seaborn as sns
sns.set_theme()
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os

'''heatmap parameter'''
#check above


# Import Data

# get sample title
title = os.path.basename(pathname3)
fig_title = title[:-4]


dataset = pd.read_csv(
    pathname3,
    sep=",",  # Separate by ','
    names=["x_center", "y_center", "time_spent"],  # Name of the columns
    header=None,
)

# Check if data is as  expected
head = dataset.head() 
#print(head)



'''plot figure 5 - just the figure itself'''
plt.figure(5) #first figure will be original version without zone time spent calculation

'''plotting settings'''
# Make the Stage
# set axis
plt.axis([-20, 20, -20, 20])
plt.axis("equal")

# create circle with (x, y) coordinates at (0, 0), with radius of 16
# set the color of the stage (lowest color of colorbar scheme)
# color can be picked by using the "Digital Color Meter" Application from Mac OS Launchpad 
# set the color of the edge - Black
background_circle = plt.Circle((0, 0), radius=20, facecolor="#000080", alpha=1, edgecolor="black")

# add circle to plot (gca means "get current axis")
plt.gca().add_artist(background_circle)


# Draw the 2D Density plot using Seaborn KDE plot function
# 2D KDE Plot - but in KDE mode
# Set the colormap to 'jet' (same as raw data)
cmap = matplotlib.cm.jet

# Draw plot
ax = sns.kdeplot(
    data=dataset, #raw data table
    x="x_center", # select the x data column
    y="y_center", # select the y data column
    levels=100, # how many levels of data
    shade=True, # color in the density plots
    thresh=0.067, # anything above the value "0.1" will be colored
    # here we used 0.067 because data is tracked in 0.067 seconds time interval
    # if we see heatmap plot sticking out of the circle edit threshold to higher value
    alpha=None, # Transparency - No transparency
    cbar=True, # Show colorbar
    cbar_kws={'label': 'Time spent', 'ticks': []},
    vmin=0, vmax=vmax,
    bw_method=bw_method, # control bandwidth of plot
    cmap=cmap # colormap is the colormap we set earlier in line 37
)




# Modifying the 2D density plot (heatmap)

plt.title(fig_title, fontsize=14) # Add the title
plt.grid() # remove gridlines
ax.set_facecolor("white") # edit background color
myaxis = [-25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25] # set axis points


# Labels
plt.xlabel("X", fontsize=12) # x axis label
plt.ylabel("Y", fontsize=12) # y axis label
plt.xticks(myaxis) # set the x axis values to specific values
plt.yticks(myaxis) # y axis values
plt.xticks(color='w') # hide axis plot label
plt.yticks(color='w') # hide axis plot label


#save plot
plt.savefig('heatmap/no zone/'+str(fig_title)+'.png', bbox_inches='tight', dpi=1200)




'''--------------------------------------------------------------------------------'''

'''plot figure 6 - zone + time spent calculated'''
plt.figure(6) #second figure includes zone and time spent calculation

'''plotting settings'''
# Make the Stage
# set axis
plt.axis([-20, 20, -20, 20])
plt.axis("equal")

# create circle with (x, y) coordinates at (0, 0), with radius of 16
# set the color of the stage (lowest color of colorbar scheme)
# color can be picked by using the "Digital Color Meter" Application from Mac OS Launchpad 
# set the color of the edge - Black
background_circle = plt.Circle((0, 0), radius=20, facecolor="#000080", alpha=1, edgecolor="black")

# add circle to plot (gca means "get current axis")
plt.gca().add_artist(background_circle)


# Draw the 2D Density plot using Seaborn KDE plot function
# 2D KDE Plot - but in KDE mode
# Set the colormap to 'jet' (same as raw data)
cmap = matplotlib.cm.jet

# Draw plot
ax = sns.kdeplot(
    data=dataset, #raw data table
    x="x_center", # select the x data column
    y="y_center", # select the y data column
    levels=100, # how many levels of data
    shade=True, # color in the density plots
    thresh=0.067, # anything above the value "0.1" will be colored
    # here we used 0.067 because data is tracked in 0.067 seconds time interval
    # if we see heatmap plot sticking out of the circle edit threshold to higher value
    alpha=None, # Transparency - No transparency
    cbar=True, # Show colorbar
    cbar_kws={'label': 'Time spent', 'ticks': []},
    vmin=0, vmax=vmax,
    bw_method=bw_method, # control bandwidth of plot
    cmap=cmap # colormap is the colormap we set earlier in line 37
)




'''draw zone rectangle'''


# food zone 표시 (rectangle)
# look to the upper side of the code


left, bottom, width, height = (rec_left, rec_bot, rec_width, rec_height)
rect=mpatches.Rectangle((left,bottom),width,height, 
                        fill=False,
                        color="grey",
                        linestyle = ":",
                       linewidth=2)
                       #facecolor="red")
plt.gca().add_patch(rect)





'''draw zone and calculate the time spent inside the zone'''
'''zone Time Calculation'''
#create dataset
x_center = dataset["x_center"]
y_center = dataset["y_center"]

#list coordinates
coords_list = []

for x_value, y_value in zip(x_center, y_center):
    coords_list.append((x_value, y_value))

time_counter = 0

for x, y in coords_list:
    if (rec_left <= x <= rec_right) and (rec_bot <= y <= rec_top):
        time_counter = time_counter + 0.067
    
print("the time in the food zone is", time_counter, "seconds", "or", time_counter//60, "mins and", time_counter%60, "seconds")

'''print calculated values onto the plot'''
plt.text(-25,-23, 'Time spent in food zone = %.2f sec' % (time_counter), fontsize=10, color = "black", alpha=1)



# Modifying the 2D density plot (heatmap)

plt.title(fig_title, fontsize=14) # Add the title
plt.grid() # remove gridlines
ax.set_facecolor("white") # edit background color
myaxis = [-25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25] # set axis points


# Labels
plt.xlabel("X", fontsize=12) # x axis label
plt.ylabel("Y", fontsize=12) # y axis label
plt.xticks(myaxis) # set the x axis values to specific values
plt.yticks(myaxis) # y axis values
plt.xticks(color='w') # hide axis plot label
plt.yticks(color='w') # hide axis plot label


#save plot
plt.savefig('heatmap/zone/'+str(fig_title)+'.png', bbox_inches='tight', dpi=1200)




















# Draw
plt.show() # show plot
plt.close()





