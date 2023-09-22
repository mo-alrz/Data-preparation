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
import seaborn as sns

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

# Specifying only x -> plot all other columns against it:
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

# Hexbins
# in a hexagonal grid using gridsize number of grids in x direction for variables x and y, a) counts of the number of
# occurrences or b) a third variable's values in the hexagonal grids.
df2.plot(kind="hexbin",x=df2.columns[0],y=df2.columns[1],gridsize = 15, sharex=False)
plt.show()

# Box plots
#     Has dedicated .boxplot() DataFrame method, which takes somewhat different arguments than the plot.box()
#     (or .plot(kind="box")) method.
#     Useful to visualize the distribution.
#     Also called box-and-whiskers plots
#         The box extends from the Q1 to Q3 quartiles (=25th and 75th percentiles = 25%, resp. 75%, of the values are
#         below that percentile) --- this means that the middle 50% of our data lies in the box
#         The line in the middle is the median = Q2 quartile = 50th percentile.
#         Optionally, a marker for the mean value can be added using showmeans=True.
#         Whiskers extend to the minimal and maximal values excluding outliers=up to 1.5 * IQR from the box boundaries
#         (IQR = inter-quartile range = Q3 - Q1)
#         Outliers are shown by default as separate dots. Can be made excluded from the plot using showfliers = False.
#     As with hist, optional column and by string or list to specify columns to plot / group plots by.
df2.plot.box(title="A boxplot with outliers")
plt.show()

df2.plot.box(showfliers=False,title="A boxplot without outliers")
plt.show()

df2.plot.box(showfliers=False,showmeans=True,title="Addd symbols for means")
plt.grid(True)
plt.show()

df2.plot.box(showfliers=False,showmeans=True,notch=True,widths=0.3,
             title="With confidence intervals around the median\nand 'fatter' boxes")
plt.grid(True)
plt.show()

# Bar plots
# Useful if you have categorical variables: these will be along the x-axis, and numerical variables along the y-axis
df.plot(kind="bar")
plt.show()

df.plot(kind="bar",stacked=True)
plt.show()

# Horizontal
df.plot(kind="barh",stacked=True)
plt.show()

df3b.sort_values(by=["popularity"],ascending=False).plot(x="name",y="popularity",kind="bar")
plt.show()

# Barplots can be used to plot value counts of categorical variables,E.g.the number of occurrences of different types
print(df3b["type"].value_counts())

df3b["type"].value_counts().plot(kind="bar",ylabel="occurrences in types")
plt.show()

# Pie plots
# suitable to visualize ratios
# plot values of variable y against the index -> y or subplots=True must be specified!
# rarely used nowadays, especially when the goal is to get a feel for the data and detect anomalies like outliers.
df3b.set_index("name").plot.pie(y="popularity",legend=False,ylabel="",title="popularity")
plt.show()

# Plot values with vastly different ranges
# # this will look like only B has an upward trend, while A and C are by and large stationary.
dfb.plot()
plt.show()

# specify a secondary y-axis for use for the column(s) with vastly a different data range compared to the first y axis:
dfb.plot(secondary_y=["B"])
plt.show()

# if more than three y-axes were needed, we would have to resort to more advanced matplotlib solutions like twin axes
# (ax.twinx()). Alternative: plot on subplots:
dfb.plot(subplots=True)
plt.show()

# Figure, size and layout
# Especially when using subplots, the default figure size can be unsuitable. We can specify the figure size (in inches)
# with the argument figsize=(horizonalsize_in,verticalsize_in).
dfb.plot(subplots=True, figsize=(5,12))
plt.show()

# To specify the layout, use the layout=(nrows, ncols) argument.
# Tip: as with ndarrays, you can use -1 for automatically determining size along an axis.
dfb.plot(subplots=True, figsize=(12,5), layout=(1,-1))
plt.show()

# Other optional arguments
# Different plots take different kwargs, but the following are generally available (though not for the dedicated
# .boxplot() and .hist() methods, which use a different interface!):
#     title for the title(s), which appears above the plot(s)
#         if stringed, used as a super-title
#         if a list, used as titles for subplots
#     label for a series (this is what will appear in the legend, when the legend is visible)
#     xlabel and/or ylabel to set the name for the entire x (resp. y) axis
#     xticks and/or yticks to set the ticks along the relevant axis
#     rot (integer, in degrees) to rotate xticklabels (useful for long names that overlap)
#     xlim, ylim (take tuples) to set (min, max) limits on the x or y axis.
#     logx, logy to set logarithmic scaling on the axes
#     table to draw a table using the dataframe data below the plot. (You might want to set xticks = [] --- or put the
#     xticks on the top using advanced matplotlib solutions --- in this case to avoid duplication and overlap of the
#     column names in the figure.)
#     and many others (see method documentations, e.g., pandas.DataFrame.plot)...
s.plot(label="my special label",
       xticks=s.index * 10,
       ylabel="my very own ylabel",
       xlabel="the original index times 10",
       title="Showcasing keyword arguments with the help of series s")
plt.legend()  # <- otherwise, the legend is not made visible
plt.show()

df.plot(subplots=True, title="A super title!")
df.plot(subplots=True, title=["one", "two", "three", "four"])
plt.tight_layout()
plt.show()

# rot for rotation of xticklabels (also for .boxplot())
df3b.set_index("name").plot.box(title="Default rotation")
plt.show()
for rot in[45,90]:
    df3b.set_index("name").plot.box(rot=rot,title=f"rot={rot}")
    plt.show()

# Further optional arguments to pass on matplotlib
# Approaching more and more the behind-the-scenes realm of matplotlib, we can give keyword arguments that are passed on
# to the matplotlib methods and objects for which pandas provides the wrappers. These include (sometimes depending on
# the plot type), e.g.,
#     grid (bool): set to True to show light gray grid on the plot
#     marker (str): a string adding and setting the appearance of markers for each datapoint (useful when the number of
#     datapoints is small); for a full list, see documentation, but the most common ones are:
#         "." = point
#         "o" = circle
#         "v" = triangle_down
#         "^" = triangle_up
#         "s" = square
#         "*" = star
#         "+" = plus
#         "x" = x
#         "D" = diamond
#     alpha (float between 0 and 1): the opacity of the plot (default is 1 = 100% opaque; 0 = 100% transparent)
#     ax: matplotlib "axes" object to be used

# marker
for marker in ["o", ".", "x", "s", "D", "v"]:
    df.plot( marker=marker, title=f"Using marker '{marker}'")
    plt.show()

# Alpha
for alpha in [1, 0.7]:
    df2.plot.hist( grid=True, alpha=alpha, title=f"Plot with alpha={alpha}");
    plt.show()

# Visualization in the early stages of the data analysis pipeline
# At the point where we are still before any modelling or proper descriptive analysis of our data, visualization does
# not serve the goal of presenting our insights. However, it can be a useful tool to help us
#     get a better understanding of our data, and
#     to immediately see if there are any anomalies in the data, e.g.,
#         outliers that differ too much from the majority,
#         the opposite, i.e., too homogeneous data,
#         unexpected skewed distributions.

# Understanding data
# Shape of the distribution
# Have already seen how useful histograms are to differentiate between samples from a normal and from a uniform
# distribution:
df2.hist()
plt.show()

# A histogram can also help us detect if there are multiple modes
np.random.seed(10)
df4 = pd.DataFrame({"single-mode sample": np.random.randn(1000)*2,
                    "multi-mode sample": np.concatenate((np.random.randn(500)-2.5,np.random.randn(500)+2.5)),
                    })

# Similar descriptive but different distributions
print(df4.describe())
df4.hist()
plt.show()

# Plotting as a sanity check : The famous example with very similar descriptive statistics, but vastly different
# distributions: Anscombe's quartet: simple scatterplots suffice to see how different the datasets are.
df_ansc = sns.load_dataset("anscombe")
print(df_ansc.groupby("dataset").describe().T.unstack(level=0).swaplevel(0, 1, axis=1).sort_index(axis=1))
fig, axs = plt.subplots(figsize=(10, 10), nrows=2, ncols=2)
for i, dataset in enumerate(df_ansc["dataset"].unique()):
    ax = axs.flatten()[i]
    data = df_ansc[df_ansc["dataset"] == dataset]
    data.plot.scatter("x", "y", ax=ax, marker="o", s=100, c=["b", "orange", "g", "r"][i], title=dataset)
plt.suptitle("Anscombe's quartet")
plt.show()

# Time series: Trend and seasonality
# There are of course statistical tests to check for trend and seasonality features, and even dedicated plotting
# options, but the first step (as well as a sanity check) is always to look at the most basic plots of the time series.
# Take our artificial dataframe with a datetime index, and do some modifications on it.
print(dfd["B"].diff().fillna(0))
dfd2 = dfd.iloc[:, :3].copy()
dfd2["A"] = dfd2["A"].diff().bfill()
dfd2["B"] = dfd2["B"].diff().bfill() * np.array([2, -2] * 3)
print(dfd2)

# If we plot the time series in the dataframe, we can immediately see the difference between the pattern of the
# different series --- while this may be easy to see from the dataframe itself, that is not possible for longer
# timeseries and more complex patterns.
dfd2.plot()
plt.show()

# Data anomalies
# A boxplot can be ideal to detect outliers
s3 = s.replace(12, 100)
s3.plot.box(title="With outliers")
plt.show()
s3.plot.box(showfliers=False, title="Without outliers")
plt.show()

# Using simple plots, we can check what we would get with and without smoothing over the outliers:
iqr = s3.quantile(0.75) - s3.quantile(0.25)
s4 = s3.where((s3 < s3.quantile(0.75) + 1.5*iqr) & (s3 > s3.quantile(0.25) - 1.5*iqr)).interpolate()
df4 = pd.DataFrame({"with outlier": s3, "smoothed over": s4})
df4.plot(subplots=True)
plt.show()
