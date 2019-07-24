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

#df = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/datasets/mtcars.csv')
#df = pd.read_csv('/home/filipa/Downloads/mtcars.csv')
df = pd.read_csv('/home/filipa/Downloads/Popular_Baby_Names.csv')

# Line
#ax = sns.regplot(x="Child's First Name", y="Count", data=df)

# Histogram
sns.distplot(df.Count, kde=False)

# Show the plot
plt.show()
