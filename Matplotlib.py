# Matplotlib is a widely used Python plotting library which is also used via Pandas to plot dataset histograms, scatter
# plots etc. Since Pandas exposes only a small fragment of Matplotlib's functionality, and its plotting capabilities are
# limited to data held in data frames and series, there are many situations when a direct use of Matplotlib is
# unavoidable. Matplotlib has, in fact, two user-facing APIs -- a simple procedural one called Pyplot which is modeled
# after MATLAB's plotting functionality and a way more sophisticated and versatile object-oriented one. This short
# introduction concentrates on the procedural Pyplot API. The following summary offers an introduction to the use of
# the object-oriented API: https://matplotlib.org/stable/tutorials/introductory/lifecycle.html

# Basic concepts
# Matplotlib is built around a few fundamental concepts:
#     a figure is an independent container for graphical elements which can be presented in a separate GUI window/area
#     when displayed. All Pyplot graphical elements are contained in figures. Pyplot commands either create figures or
#     change them e.g. by adding elements (plots etc.);
#     axes are rectangular areas with a corresponding coordinate system in a figure on which graphical elements can be
#     placed;
#     an axis is one of the axes of an axes (caution with the terms!) object: a number-line like object with associated
#     numerical limits;
#     subplots are sets of axes arranged in a regular grid which can be accessed by their position in the grid;
#     finally, artists are the graphical elements (lines, texts, images etc.) that can be placed on a figure (typically
#     with the help of axes).

# The Pyplot workflow in the context of Jupyter notebooks is to
#     create a figure with one or more axes (often implicitly),
#     place graphical elements on it at locations identified with the help of subplots/axes,
#     and, finally, display/render the figure by calling plt.show().
# During the process pyplot keeps track of the current figure and current axes, which can be queried by the gcf and gca
# functions:

import numpy as np
from matplotlib import pyplot as plt
import math

# plt.figure()  # This creates a figure with the default settings and with associated axes
# print(plt.gcf())  # Get the current figure object and print its parameters
# print(plt.gca())  # Get the current axes object and print its parameters
# plt.show()  # Show the (in essence empty) figure
#
# # As the above example shows axes, by default, already bring visualized axis objects with themselves, that is, the
# # visualization of their boundaries with numbered ticks. This visualization can be configured in various ways, e.g.:
#
# axes = plt.gca()  # This implicitly creates a figure and axes
# axes.spines["top"].set_color("red")  # spines are the displayed boundaries
# axes.spines["right"].set_color("red")
# axes.set_xlim((10, 20))  # Set the horizontal limits
# axes.set_ylim((10, 20))  # Set the vertical limits
# axes.xaxis.set_ticks_position("both")  # Put horizontal ticks to the top as well
# axes.yaxis.set_ticks_position("both")  # Put vertical ticks to the top as well
# plt.show()
#
# # Let's try to use more than one axes regions in a figure.
# plt.axes((.1, .1, .8, .8))  # dimensions are given as left, bottom, width, height in figure-relative coordinates
# # and units, (0,0,1,1) would cover the entire figure
# print(plt.gca())
# plt.axes((0, 0, 0.5, 0.5))
# print(plt.gca())
# plt.show()
#
# # Using subplots we can easily produce axes arranged in a grid
# plt.subplot(2, 3, 2)  # (nrows, ncols, plot_number)
# print(plt.gca())
# plt.subplot(2, 3, 4)  # (nrows, ncols, plot_number)
# print(plt.gca())
# plt.subplot(2, 3, 6)  # (nrows, ncols, plot_number)
# print(plt.gca())
# plt.show()
#
# # As we have seen so far, the procedural API is highly stateful in the sense that it has the notions of "current figure"
# # "current axes" etc. which are often changed implicitly by Pyplot commands. This is useful for relatively simple plots
# # but can be confusing and difficult to handle programatically in the case of complex figures consisting of a high
# # number of subplots axes etc. In these situations it is useful to create figure(s) and axes explicitly in a more
# # transparent, object-oriented style:
# figure, axes = plt.subplots(1, 2)
# ax1, ax2 = axes
# print(ax1, ax2)
# ax1.spines["top"].set_color("red")
# ax1.spines["bottom"].set_color("red")
# plt.show()
#
# # The above 'design pattern' is usable with a single axes object as well
# figure, ax = plt.subplots()  # "grid" with a single cell
# plt.show()

# # Ready-made plot types
# #   Although Matplotlib offers a huge variety of graphical elements ("artists") that can be added to a figure (see the
# #   Artist tutorial, most daily plotting tasks can be accomplished by utilising a few ready made plot types.
# #     The data points for these plots have to bee specified in the form of one or more iterables that are typically
# #     lists, NumPy ndarrays or Pandas dataframe columns.
# # Some ready-made plot types, available from Pandas directly, as well:
# #     scatter
# #     histogram
# #     box plots
#
# xs = np.random.normal(size=100)
# ys = xs * xs
#
# plt.figure(figsize=(12, 4))
#
# plt.subplot(131)
# plt.boxplot(xs)
# plt.title("A boxplot")
#
# plt.subplot(132)
# plt.hist(xs)
# plt.title("A histogram")
#
# plt.subplot(133)
# plt.scatter(xs, ys)
# plt.title("A scatterplot")
#
# plt.show()
#
# # Notice that the axis limits were automatically set to sensible values. In addition to these, Matplotlib also supports
# # simple "elementary school type" line plots:

# xs = np.linspace(start=-2 * math.pi, stop=2 * math.pi, num=100)
# sin_vals = [math.sin(x) for x in xs]
# plt.plot(xs, sin_vals)
# plt.show()

# # Legends, etc. also can be set
# xs = np.linspace(start=-2*math.pi, stop=2*math.pi, num=100)
# sin_vals = [math.sin(x) for x in xs]
# cos_vals = [math.cos(x) for x in xs]
#
# fig, ax = plt.subplots() # We will need the axes, so create a figure and axes object explicitly
#
# # matplotlib automatically plots everything to the current axis
# # and automatically uses different colors for the different plots within the same axis
# plt.plot(xs, sin_vals, label="Sine")    # the "label" will be used in the legend
# plt.plot(xs, cos_vals, label="Cosine")
#
# # Move lower spines to the center
# ax.spines['left'].set_position('center')
# ax.spines['bottom'].set_position('center')
# # Eliminate upper and right axes
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
#
# # Add legend
# plt.legend()
# # Add title
# plt.title("Trigonometric functions")
# plt.show()

# The familiar bar and pie charts are also available, e.g.
data = [13.27, 10.16, 4.73, 3.78, 68.06]  # The numerical values to chart
labels = ["Java", "C", "C++", "Python", "other"]

plt.figure(figsize=(12, 6))  # Set figure size to a reasonable size for the two plots next to each other

plt.subplot(121)
plt.pie(data, labels=labels)
plt.title("A pie plot")

plt.subplot(122)
positions = range(len(data))  # Positions of the bars
plt.bar(positions, data)
plt.xticks(positions, labels)  # set the "xticks" to display the labels at the positions
plt.title("A bar plot")

plt.suptitle("Popularity of programming languages")  # Suptitle sets a title for the whole figure
plt.show()
