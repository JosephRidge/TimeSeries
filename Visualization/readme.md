# PART 1
### Visualizing international income distribution -> visualization on graph 1
seaborn is a Python visualization library for statistical data visualization based on matplotlib.

By default, the distplot() function in the seaborn package creates a histogram, where data is grouped into ranges and and plotted as bars, and fits a kernel density estimation (KDE), or smoothed histogram. You can also use distplot() to create another kind of graph called a rugplot, which adds markers at the bottom of the chart to indicate the density of observations along the x axis.

seaborn.distplot(a, bins=None, hist=True, kde=True, rug=False, ...)
In previous exercises, you created a quantile plot which provided a fairly granular sense of the level of income per capita at different points of the distribution. Here, you will use distplot() to get the full picture!

pandas has been imported as pd, and the income DataFrame from the previous exercise is available in your workspace.

### Instructions
Import seaborn as sns and matplotlib.pyplot as plt.
Print the summary statistics provided by .describe().
Plot and show a basic histogram of the 'Income per Capita' column with .distplot().
Create and show a rugplot of the same data by setting the additional arguments bins equal to 50, kde to False, and rug to True.

# PART 2
###  Growth rates in Brazil, China, and the US
It's time to extend your analysis beyond the levels of international per capita income to the growth rates. The 'income_growth.csv' file contains the growth rates of per capita income over the last 40 years for Brazil, China, and the US.

You will plot the distribution of the historical growth rates for each country on the same chart using a KDE plot to faciliate visual comparison of the ranges of growth that these markets have experienced over this time period.

From this point in the course onwards, you should always inspect any DataFrame with .info() in your console even if this isn't explicitly in the instructions. pandas as pd, seaborn as sns, and matplotlib.pyplot as plt have been imported.

Instructions
100 XP
Load the file 'income_growth.csv' into the variable growth. Parse the 'DATE' column into dtype datetime64 and set it as the index.
Inspect the summary statistics for these three growth rates using the appropriate function.
Iterate over the growth.columns attribute in a for loop to access their labels. Most of the code has been outlined for you.
In each iteration of distplot(), pass in the iteration variable column to select the respective column, set the keyword hist to False, and set label to column.