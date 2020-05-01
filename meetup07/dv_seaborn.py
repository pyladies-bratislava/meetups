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

# There are 2 csv files with data in this folder
# names_large.csv contains a large amount of data while names.csv is small
df = pd.read_csv('names.csv')

# Basics about the dataframe
# df. head() - show the first 5 rows of dataframe
# df.tail() - show the last 5 rows of dataframe
# df. shape - show number of rows and columns
# df.rename(columns={"Child's First Name":'Child_name'}, inplace=True) - rename inappropriate names of column
# df.col_name.nunique() - number of unique values in column / unique - show list of unique values in column
# df.dtypes - shows the data type of each column

# Filtered as example but not used
filtered = df["Count"] == 5

# Countplot that is not so useful for this data
#sns.countplot(x=df["Child's First Name"], data=df[filtered])
#plt.xticks(rotation=90)

# Barplot
sns.barplot(x="Child's First Name", y="Count", data=df)

# Create df top 50
df_top_50 = df.groupby("Child's First Name")["Count"].sum().sort_values(ascending=False).reset_index()
df_top_50 = df_top_50.head(50)

# Plot
plt.figure(figsize=(20, 10))
sns.barplot(x="Child's First Name", y="Count", data=df_top_50)
plt.xticks(rotation=90)

# Show the plot
plt.show()
