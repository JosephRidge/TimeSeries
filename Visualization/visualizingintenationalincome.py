# Import seaborn and matplotlib
import seaborn as sns
import matplotlib.pyplot as plt

# Print the summary statistics for income
print(income.describe())

# Plot a basic histogram of income per capita


sns.distplot(income['Income per Capita'], hist=True, kde=False, rug=False)

# Show the plot
plt.show()

# Plot a rugplot
sns.distplot(income['Income per Capita'], hist=False, kde=False,bins=50, rug=True)

# Show the plot
plt.show()