import matplotlib
matplotlib.use("Qt5Agg")

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Suppress warnings
import warnings

warnings.filterwarnings('ignore')

# Optional but changes the figure size
fig = plt.figure(figsize=(12, 8))

df = pd.read_csv('names.csv')

# Filtered as example but not used
filtered = df["Count"] == 5

# Countplot that is not so useful for this data
#sns.countplot(x=df["Child's First Name"], data=df[filtered])
#plt.xticks(rotation=90)

# Barplot
sns.barplot(x="Child's First Name", y="Count", data=df)

# Show the plot
plt.show()
