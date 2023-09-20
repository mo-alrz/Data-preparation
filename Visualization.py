# Ready-made plots using Pandas
# .plot.<kind> or .plot(kind)
#     bar( or barh) for bar plots
#     hist for histogram
#     box for boxplot
#     scatter for scatter plots
#     pie for pie plots

# As dedicated methods with different interfaces:
#     .hist()
#     .boxplot()

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Prepare some dataframe to plot
# A data frame
df = pd.DataFrame(np.arange(24).reshape(-1, 4), columns=['A', 'B', 'C', 'D'])

# A dataframe with vastly different value columns
dfb = df.iloc[:, :-1].copy()
dfb["B"] = dfb["B"] * 100
dfb["C"] = dfb["C"] * (-1)

# A dataframe with a datetime index (tri-monthly frequency, starting from 1 Jan 2020)
dfd = df.copy()
dfd.index = pd.date_range("2020-01-01", periods=len(dfd), freq="3MS")

# A series
s = df["A"].copy()

# A series with  different indexes
s2 = s.copy()
s2.index = range(100, 100 + len(s))
s2.name = "A2"

# Another dataframe
df2 = pd.DataFrame({"From normal distribution": np.random.randn(1000),
                    "From uniform distribution": np.random.rand(1000)})

# A dataframe with non-numerical values only
df3 = pd.DataFrame({"name": ["rabbit", "tree", "flower", "wolf", "bird"],
                    "type": ["animal", "plant", "plant", "animal", "animal"]})

# Another dataframe
df3b = df3.copy()
df3b["popularity"] = [98, 11, 25, 2, 18]
df3b["difficulty"] = [29, 21, 8, 99, 24]

# Line plots -> Suitable for continuous variables,good for detecting general trends,Not for categorical Data
s.plot()
s2.plot()
plt.legend()
plt.show()

df.plot()
plt.show()

dfd.plot()
plt.show()

# When specifying subplots=True:
df.plot(subplots=True)
plt.show()

# A line plot is also generally not very useful for numerical variables without a trend, but it can still help to
# get an overview:
df2.plot()
plt.show()

# To plot columns against each other, rather than against the index, specify (either as positional or keyword args)
# * one x and * optionally one or more y arguments (a string or a list of strings from the dataframe's columns)
df.plot("A", "B")
plt.show()
df.plot("A", ["B", "C"])
plt.show()

# Specfiying only x -> plot all other columns against it:
df.plot("A")
plt.show()

# Specify y = plot only that column against the index:
df.plot(y="A")
plt.show()

# Scatter plots -> .plot.scatter() or .plot(kind='scatter),needs x andy arguments,Suitable when you need to plot
# variables against each other, and detect if there are any relationships, correlations between them
df.plot.scatter("A","B") # scatter column A against column B
plt.show()

df2.plot(df2.columns[0],df2.columns[1],kind="scatter")
plt.show()

# A line plot would be unsuitable here:
df2.plot(x=df2.columns[0],y=df2.columns[1])
plt.show()

# Histogram -> suitable for exploring the values of a single variable (a series / a column of a dataframe)
#              makes sense for numerical variables with a large number of values
#              bin values into a specified number of bins (default = 10), and plot the number of elements in the bins
#              suitable for comparing distribution shapes
df2.plot.hist()
plt.show()

# Generate by-column histograms in subplots
df2.plot.hist(subplots=True)
plt.show()

# generate by-column histograms --- note that by-column subplots are generated!
df2.hist()
plt.show()

# Setting number of bins using bins (and either method)
for nbins in [3, 20]:
    df2.hist(bins=nbins)
    plt.suptitle(f"{nbins} bins")
    plt.show()

# To plot histograms by groups: by arg for the dedicated .hist() method only.
df2_groups = list(map( lambda x: f"group {x}", np.random.randint(1,3,size=len(df2)) ))
df2.hist(by=df2_groups,legend=True, bins=20)
plt.show()

# To plot only certain columns: column(str or list-like to specify the column names to plot)for dedicated .hist()
# method only.
df2.hist(column=df2.columns[0],legend=True,bins=20)
plt.show()

