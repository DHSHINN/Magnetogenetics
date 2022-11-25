# Python Environment Setting
import seaborn as sns
sns.set_theme()
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os

'''heatmap parameter'''
vmax=0.012
bw_method=0.08

'''Circle and Letter (text) Positions Parameter'''


# red left circle (왼쪽 - 빨간 테두리) - EMPTY
red_left_circle_x = -27
red_left_circle_y = 16

red_left_letter_x = red_left_circle_x-6
red_left_letter_y = red_left_circle_y-1



# red right circle (오른쪽 - 빨간 테두리) 

red_right_circle_x = 22
red_right_circle_y = red_left_circle_y

red_right_letter_x = red_right_circle_x-4
red_right_letter_y = red_left_circle_y-2




# white left foodzone circle (왼쪽 - 흰색 테두리)
zone_left_circle_x = red_left_circle_x
zone_left_circle_y = red_left_circle_y

zone_left_letter_x = zone_left_circle_x-9
zone_left_letter_y = red_left_circle_y+14



# white right foodzone circle (오른쪽 - 흰색 테두리)

zone_right_circle_x = 22
zone_right_circle_y = red_left_circle_y

zone_right_letter_x = 15
zone_right_letter_y = red_left_circle_y+14


# foodzone size
left_zone_radius = 12
right_zone_radius = 12



# Import Data
pathname = "/Users/Jace/heatmap/221021 social behavior try 3/excel_raw processed/csv/221021 vgat social behavior-Trial2_no.240 vgat Piezo1+m-torquer Empty vs mouse1.csv"

# get sample title
title = os.path.basename(pathname)
fig_title = title[:-4]


dataset = pd.read_csv(
    pathname,
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
background_circle = plt.Circle((0, 0), radius=400, facecolor="#000080", alpha=1, edgecolor="black")

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


'''draw circle over data'''

#circle 1
circle_1 = plt.Circle((red_right_circle_x, red_right_circle_y ), radius=7, facecolor="none", alpha=1, edgecolor="red", linewidth=1)
plt.gca().add_artist(circle_1)
plt.text(red_right_letter_x, red_right_letter_y, "M1", fontsize=18, color = "white", alpha=1)


#circle 2
circle_2 = plt.Circle((red_left_circle_x, red_left_circle_y ), radius=7, facecolor="none", alpha=1, edgecolor="red", linewidth=1)
plt.gca().add_artist(circle_2)
plt.text(red_left_letter_x, red_left_letter_y, "Empty", fontsize=12, color = "white", alpha=1)


# Modifying the 2D density plot (heatmap)

plt.title(fig_title, fontsize=14) # Add the title
plt.grid() # remove gridlines
ax.set_facecolor("white") # edit background color
myaxis = [-50, -25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 50] # set axis points


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
background_circle = plt.Circle((0, 0), radius=400, facecolor="#000080", alpha=1, edgecolor="black")

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


'''draw circle over data'''


#circle 2
circle_2 = plt.Circle((red_left_circle_x, red_left_circle_y ), radius=7, facecolor="none", alpha=1, edgecolor="red", linewidth=1)
plt.gca().add_artist(circle_2)
plt.text(red_left_letter_x, red_left_letter_y, "Empty", fontsize=12, color = "white", alpha=1)

#circle 1
circle_1 = plt.Circle((red_right_circle_x, red_right_circle_y ), radius=7, facecolor="none", alpha=1, edgecolor="red", linewidth=1)
plt.gca().add_artist(circle_1)
plt.text(red_right_letter_x, red_right_letter_y, "M1", fontsize=18, color = "white", alpha=1)



# If the background is an image?
# Image configuration must align with axis setting - use extent function
# edit -x, x, -y, y to axis configuration
# ax.imshow(img, extent=[-x, x, -y, y]) 




'''draw zone circle'''



#zone marker circle 2 - empty zone


fz_circle_2 = plt.Circle((zone_left_circle_x, zone_left_circle_y), radius=left_zone_radius, facecolor="none", alpha=1, edgecolor="white", linewidth=1, linestyle = ':')
plt.gca().add_artist(fz_circle_2)
plt.text(zone_left_letter_x, zone_left_letter_y, "Empty zone", fontsize=10, color = "white", alpha=1)




#zone marker circle 1 - M1 zone
#fz is for zone

left_zone_radius = 12
fz_circle_1 = plt.Circle((zone_right_circle_x, zone_right_circle_y), radius=right_zone_radius, facecolor="none", alpha=1, edgecolor="white", linewidth=1, linestyle = ':')
plt.gca().add_artist(fz_circle_1)
plt.text(zone_right_letter_x, zone_right_letter_y, "M1 zone", fontsize=10, color = "white", alpha=1)





'''draw zone and calculate the time spent inside the zone'''
'''zone Time Calculation'''
#create dataset
x_center = dataset["x_center"]
y_center = dataset["y_center"]

#list coordinates
coords_list = []

for x_value, y_value in zip(x_center, y_center):
    coords_list.append((x_value, y_value))

time_counter_fz1 = 0 # time count for zone 1 - M1
time_counter_fz2 = 0 # time count for zone 2 - empty

for x, y in coords_list:
    if (zone_right_circle_x-x)**2 + (zone_right_circle_y-y)**2 <= right_zone_radius**2:
        time_counter_fz1 = time_counter_fz1 + 0.067
    elif (zone_left_circle_x-x)**2 + (zone_left_circle_y-y)**2 <= left_zone_radius**2:
        time_counter_fz2 = time_counter_fz2 + 0.067
    
print("the time in the 'M1' zone is", time_counter_fz1, "seconds", "and", "the time in the 'empty' zone is", time_counter_fz2, "seconds")

'''print calculated values onto the plot'''
plt.text(-48,-45, 'Time spent in M1 zone = %.2f sec\nTime spent in empty zone = %.2f sec' % (time_counter_fz1, time_counter_fz2), fontsize=10, color = "white", alpha=1)



# Modifying the 2D density plot (heatmap)

plt.title(fig_title, fontsize=14) # Add the title
plt.grid() # remove gridlines
ax.set_facecolor("white") # edit background color
myaxis = [-50, -25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 50] # set axis points


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


