import numpy as np
import pandas as pd

df = pd.DataFrame([["Python", "multi", "Guido van Rossum", 1995, 3],
                   ["Lisp", "multi", "John McCarthy", 1958, 33],
                   ["C++", "multi", "Bjarne Stroustrup", 1985, 4],
                   ["Java", "multi", "James Gosling", 1996, 1],
                   ["Haskell", "functional", "Lennart Augustsson", 1990, 40],
                   ["Prolog", "logic", "Alain Colmerauer", 1972, 36]],
                  columns=["name", "paradigm", "creator", "year", "popularity_rank"])
#
# print(df)
#
# seri = pd.Series(['pytho', 'multi', '1995'])
# print(seri)
#
# # df = pd.DataFrame(np.arange(70 * 90).reshape(70, 90))
# # with pd.option_context("display.max_rows", 100, "display.max_columns", 100):
# #     display(df)
#
# # Setting index
# df2 = pd.DataFrame([["multi", "Guido van Rossum", 1995, 3],
#                     ["multi", "John McCarthy", 1958, 33],
#                     ["multi", "Bjarne Stroustrup", 1985, 4],
#                     ["multi", "James Gosling", 1996, 1],
#                     ["functional", "Lennart Augustsson", 1990, 40],
#                     ["logic", "Alain Colmerauer", 1972, 36]],
#                    columns=["paradigm", "creator", "year", "popularity_rank"],
#                    index=["Python", "Lisp", "C++", "Java", "Haskell", "Prolog"])
# print(df2)
#
# # Or:
# df.set_index("name", inplace=True)
# print(df)
#
# # Remove the index
# df.reset_index()
#
# # Initializing series or dataframe from a dictionary
# # {key:single value} can be used to initialize series
# # {key:same-length iterable of values} can be used to initialize dataframes
#
# mydict = {
#     'name': ['Python',
#              'Lisp',
#              'C++',
#              'Java',
#              'Haskell',
#              'Prolog'],
#     'creator': ['Guido van Rossum',
#                 'John McCarthy',
#                 'Bjarne Stroustrup',
#                 'James Gosling',
#                 'Lennart Augustsson',
#                 'Alain Colmerauer'],
#     'year': [1995, 1958, 1985, 1996, 1990, 1972],
# }
#
# df = pd.DataFrame(mydict)
# seri = pd.Series(mydict)
#
# print(seri)
#
# # Accessing columns, rows, cells, slices
# # Depending on what parts of a data frame we access, we get different types of objects:
# #   accessing columns or rows -> pd.Series
# #   accessing a cell -> whatever type that particular cell is
# #   accessing 2D parts of the data frame -> pd.DataFrame
#
# # The first and last n rows (the default is 5) of a data frame or series can be quickly inspected by the head and tail
# # methods:
# print(df.head(2))
# print(df.tail(2))
#
# # The column labels of a dataframe can be accessed by .columns (NO parentheses!)
# print(df2.columns)
#
# # Column values can be also set:
# df2.columns = ['paradigm', 'creator', 'year', 'tiobe_idx']
#
# # The row labels with .index
# print(df2.index)
#
# # Series only have index, no columns
#
# # Accessing columns -> Can be accessed by label df["creator"]
# print(df2["creator"])
#
# # With appropriate column labels (string without spaces) a dotted syntax also works:
# print(df2.creator)
#
# # Multiple columns can be accessed using list :
# print(df[["creator", "year"]])
# print(type(df2["creator"]), type(df[["creator", "year"]]))
#
# # Values also can be set, even new column values
# df2["constant"] = 'some value'
# df2["id"] = np.arange(len(df2))
# print(df2)
#
# # Accessing rows
# # The same logic applies as with columns, but they must be accessed using .loc[] instead of simple square brackets
# print(df2.loc["Python"])
#
# # .loc[] and .iloc[]
# print(df2.loc[["Lisp", "Java"], ["creator", "tiobe_idx"]])
# print(df2.iloc[[1, 3], [1, 3]])
#
# # .loc[] and .iloc[] multiple rows and single column = series
# print(df2.loc[["Lisp", "Java"], "creator"])
# print(df2.iloc[[1, 3], 1])
#
# # .loc[] and .iloc[] multiple rows and single column as a list = dataframe
# print(df2.loc[["Lisp", "Java"], ["creator"]])
# print(df2.iloc[[1, 3], [1]])
#
# # .loc[] and .iloc[] single row and single column = cell
# print(df2.loc["Python", "year"])
# print(df2.iloc[0, 0])
#
# # loc can also be used to access 2-dimensional ranges using Python's slicing syntax extended to two dimensions:
# print(df2.loc["Lisp":"Java", "creator":"tiobe_idx"])
# print(df2.iloc[:3, 1:4])
#
# # Conditions and boolean masks
# d2 = pd.DataFrame([[3, 'two', 1], [3, 3, 3]],
#                   columns=[f'col{i}' for i in range(3)],
#                   index=[f'row{i}' for i in range(2)])
#
# print(d2 == 3)
# print(d2[d2 == 3])
# print(d2[(d2 == 3) | (d2 == 'two')])
#
# print((d2 == 3).all())
# print((d2 == 3).all(axis=1))
# print(d2[(d2 == 3).all(axis=1)])
#
# # Descriptive
# print(df2.describe())
#
# # If there are numerical columns then only those columns' statistics are included by default --
# # the include parameter can be used to produce all:
# print(df2.describe(include="all"))
# print(df["year"].describe())
#
# # .min(), .max(), .mean(), .median(), .std(), .count()
# print(df2.count())
# print(df2.count(axis=1))
# # print(df2.mean()) & ...
#
# # Unique values and value counts .unique() .nunique() .value_counts()
# colname = "paradigm"
# print(colname, "has", df2[colname].nunique(), "values:")
# print(df2[colname].unique())
# print(df2[colname].value_counts())
#
# # Types
# print(df2.info())  # This method is not available for series
# print(df2.dtypes)  # Gives the types of the columns
# print(df2['year'].dtype)  # For series
#
# # DataFrame and Series manipulation
# # Making a copy
# d = pd.DataFrame(np.arange(6).reshape(2, 3))
# d2 = d.copy()
# d2.loc[0, 0] = 100
# print(d)
# print(d2)
#
# # DataFrame Concatenation
# # By default, as always, axis=0 is assumed = concatenation of rows:
# d = pd.DataFrame(np.arange(15).reshape(3, 5))
# d2 = pd.DataFrame(np.arange(100, 110).reshape(2, 5), index=[1, 2])
# d3 = pd.concat([d, d2])
# print(d3)
#
# # To concatenate along columns
# d3 = pd.concat([d, d2], axis=1)
# print(d3)
#
# # Elementwise operations
# d = pd.DataFrame(np.ones(6).reshape(2, 3))
# print(d + 1)
# d.iloc[0, 1:] = -2
# print(d)
# print(d.abs())
#
# # Aggregation/Reduction methods and mapping values
# d = pd.DataFrame(np.arange(15).reshape(3, 5))
# print(d.sum(1))  # Axis = 1, sum columns = one value per row
# print(d.mean())  # Axis = 0, function apply to rows
# print(d.mean().mean())
#
# s = pd.Series([1, 1, 10, 3, 3])
# print(s.unique(), s.nunique())
#
# # MAP
# # Series -> .map()
# # DataFrames -> .applymap() to apply a function to each cell
# #               .apply() -> axis = 0 apply a function to each column
# #                           axis = 1 apply a function to each row
#
# s = pd.Series(['one', 'two', 'three', 'go'])
# s2 = s.map(lambda x: x[:2])
# print(s2)
#
# d = pd.DataFrame(np.arange(15).reshape(5, 3), columns=["col1", "col2", "col3"])
# d2 = d.apply("sum", axis=0)
# print(d2)
#
# # .dt. and .str.
# s3 = s.str.cat(sep='+')
# print(s3)
#
# # Convert the index of a series into a column of a dataframe
# mylist = list('abcedfghijklmnopqrstuvwxyz')
# myarr = np.arange(26)
# mydict = dict(zip(mylist, myarr))
# ser = pd.Series(mydict)
# df = ser.to_frame().reset_index()
# print(df.head())
#
# # Combine many series to form a dataframe
# ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
# ser2 = pd.Series(np.arange(26))
# # solution 1
# df1 = pd.concat([ser1, ser2], axis=1)
# # solution 2
# df2 = pd.DataFrame({'col1': ser1, 'col2': ser2})
#
# # Assign name to the series index
# ser = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
# ser.name = 'Alphabets'
# print(ser.head())
#
# # Get the items of series A not present in series B
# ser1 = pd.Series([1, 2, 3, 4, 5])
# ser2 = pd.Series([4, 5, 6, 7, 8])
# not_in_a = ser1[~ser1.isin(ser2)]
# print(not_in_a)
#
# # Get the items not common to both series A and series B
# ser1 = pd.Series([1, 2, 3, 4, 5])
# ser2 = pd.Series([4, 5, 6, 7, 8])
# ser_u = pd.Series(np.union1d(ser1, ser2))
# ser_i = pd.Series(np.intersect1d(ser1, ser2))
# print(ser_u[~ser_u.isin(ser_i)])
#
# # Get the minimum, 25th percentile, median, 75th, and max of a numeric series
# state = np.random.RandomState(100)
# ser = pd.Series(np.random.normal(10, 5, 25))
# ans = np.percentile(ser, q=[i * 25 for i in range(5)])
# print(ans)
#
# # Keep only top 2 most frequent values as it is and replace everything else as ‘Other’
# np.random.RandomState(100)
# ser = pd.Series(np.random.randint(1, 5, [12]))
# most_frq = ser[~ser.isin(ser.value_counts().index[:2])] = 'other'
# print(ser)
#
# # Bin a numeric series to 10 groups of equal size
# ser = pd.Series(np.random.random(20))
# new_ser = pd.qcut(ser, q=[0, .10, .20, .3, .4, .5, .6, .7, .8, .9, 1],
#         labels=['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th']).head()
# print(new_ser)
#
# # convert a numpy array to a dataframe of given shape
# ser = pd.Series(np.random.randint(1, 10, 35))
# df = pd.DataFrame(ser.values.reshape(7,5))
# print(df)
#
# # Advanced pandas
# df = pd.DataFrame([["Python", "multi", "Guido van Rossum", 1994, 3],
#                    ["Lisp", "multi", "John McCarthy", 1958, 33],
#                    ["C++", "multi", "Bjarne Stroustrup", 1985, 4],
#                    ["Java", "multi", "James Gosling", 1996, 1],
#                    ["Haskell", "functional", "Lennart Augustsson", 1990, 40],
#                    ["Prolog", "logic", "Alain Colmerauer", 1972, 36]],
#                   columns=["name", "paradigm", "creator", "year", "popularity_rank"])
# df.set_index("name", inplace=True)
# print(df)
#
# # Index/Axis manipulation
# # Index/axis manipulation
# #
# # Caveat: "index" is ambiguous when it comes to pandas:
# #
# #     it can refer to the ordered sequence of values that are the row names (contrast with columns)
# #     it can refer to pd.Index type objects, which includes, among other things, both the index and columns of a
# #     dataframe (but can of course be standalone objects, as well, not to mention the index of pandas series)
# #
# # Here, we talk about the manipulation of index objects.
# #
# #     As such, in most cases, the axis or index/columns will need to be specified.
# #         As usual, the default is axis=0 (rows).
# #     As may by now be familiar, many functions and methods accept and inplace argument to control whether a new object
# #     should be returned (False, default), or the modifications should be made on the original object (True).
#
# # Dropping lables
# # You can drop = remove = delete = exclude rows/columns from a dataframe (or series) by specifying one (string) or more
# # (list-like) labels along that axis.
# # (In the following examples, you could specify inplace=True to apply changes to the original df instead of returning a
# # new df.)
# df.drop("Lisp")  # The default is axis = 0
# df.drop("creator", axis=1)  # drop from columns
# df.drop(columns="creator")  # alternative to specifying axis
# df.drop(["Lisp", "Haskell"])  # dropping several rows
#
# # When using columns and index instead of axis, we can simultaneously drop labels from the index and from the columns:
# df.drop(columns="creator", index=["Lisp", "Haskell"])
#
# # Renaming labels: .rename()
# # Column and index labels can be renamed using the .rename method
# # The axis should be specified either via axis, or via either index or columns (the default is index, as usual, but not
# # being explicit can be a source of trivial mistakes)
# # Either a dictionary or a renaming function must be given as mapper
# #    => lists do not work!
# df.rename(columns={"popularity_rank": "tiobe_idx"},
#           index=lambda x: x + "programming language")
#
# # Renaming axis: .rename_axis()
# # The columns and the index of a dataframe (and the index of a series) can have a name (by default, None).
# # This name can be changed --- note to be confused with rename, which changes the labels on an axis (index or column),
# # not the name of the axis itself!
# # as usual, axis, or index/columns can be specified
# df.rename_axis("language_name")
# df.rename_axis(columns="variable", index="language_name")
#
# # Replacing values: .replace()
# df.replace("logic", "LOGICAL")
#
# # Using dictionary and list and RegExes
# df.replace({"logic": "LOGICAL", "functional": "Functional"})
# df.replace(["logic", "functional"], "NON-MULTI")
# df.replace(["logic", "functional"], ["LOGICAL", "FUNCTIONAL"])
# df.replace(r"[A-Z][\w]+ ([\w ]+)", r"\1", regex=True)  # remove uppercase words and retain the rest of the sentence
#
# # Using dict in to_replace or value, but specifying both = column-specific replace.
# df.replace(r"^[mJ][\w ]+", r"STARTING with m or J", regex=True)  # It will change the values in all columns
# df.replace({"creator": r"^[mJ][\w ]+"}, r"STARTING with m or J", regex=True)  # This change the values of creator column
#
# # Or specifying columns in value
# df.replace(r"^[mJ][\w ]+",
#            {"creator": r"CREATOR STARTING with m or J",
#             "paradigm": r"PARADIGM STARTING with m or J"}, regex=True)
#
# # .where() method
# df["year"].where(df["year"] >= 1980, other="a long time ago")
#
# # The default other value is NaN
# df["year"].where(df["year"] >= 1980)
#
# # .where() differs from boolean indexing, because it doesn't drop the rows where condition is False!
# # Boolean indexing will not keep those datapoints that do not match condition
# new_df = df["year"][df["year"] >= 1980]
#
# # Using values from a different series
# df["creator"].where(df["year"] >= 1980, other=df["popularity_rank"])
#
# # Keep values where number of characters is at least 4 characters long
# df.where(df.applymap(lambda x: len(str(x)) >= 4))
#
# # Merging, Concatenating
# df2 = pd.Series({"Python": "easy", "C++": "difficult", "BASIC": "medium"}, name="difficulty").to_frame()
# df2["popularity_rank"] = ["totes great!", "cool!", "hard-core!"]
#
# # pd.concat()
# #    Blindly concatenate, even if it results in duplicate labels along concatenated axis
# #    But finds the corresponding labels on the other axis.
# pd.concat([df, df2])
#
# # Along columns
# pd.concat([df, df2], axis=1)
#
# # We can concatenate series too
# pd.concat([df, df2["difficulty"]], axis=1)
# pd.concat([df["popularity_rank"], df2["difficulty"]], axis=1)
#
# # Concatenation is by default outer, but we can specify "inner" (mutual):
# pd.concat([df["popularity_rank"], df2["difficulty"]], axis=1, join="inner")
#
# # pd.merge()
# pd.merge(df, df2, left_index=True, right_index=True)
#
# # specify suffixes
# pd.merge(df, df2, left_index=True, right_index=True, suffixes=("", "_unofficial"))
#
# # specify kind of join
# pd.merge(df, df2, left_index=True, right_index=True, suffixes=("", "_unofficial"), how="outer")
# pd.merge(df, df2, left_index=True, right_index=True, suffixes=("", "_unofficial"), how="right")
#
# # Merge on column values
# df3 = pd.DataFrame([["first web page", 1991],
#                     ["launch of the Hubble Space Telescope", 1990],
#                     ["beginning of the Human Genome Project", 1990],
#                     ["release of Microsoft Windows", 1985],
#                     ], columns=["notable_scientific_events", "year"])
#
# pd.merge(df.reset_index(), df3, on="year", how="outer")

# # Grouping: .groupby()
# # Perhaps one of the most useful tools of pds is its ability to group dataframe values on one or more columns,and either
# #     aggregate group values, or
# #     transform values based on group values (e.g., to percentage of by-group maximum), or
# #     filter values based on group values (e.g., keep only rows where a column value is above a group mean), or
# #     apply some function to groups
# np.random.seed(10)
df["random_value"] = np.random.randint(2, size=len(df))
# print(df.groupby("paradigm").agg(lambda x: x.mean()))
#
# # Or:
# print(df.groupby("paradigm").agg("mean"))
#
# print(df.groupby("paradigm")[["year", "creator", "popularity_rank"]].agg("mean"))
#
# # Restricting to a single column returns a series, as expected:
# print(df.groupby("paradigm")["year"].agg("mean"))
#
# # The "span" of a group: the max-min (recall that we are talking about a function over a series corresponding to a
# # column restricted to a group):
# print(df.groupby("paradigm")[["year"]].agg(lambda g:g.max() - g.min()).rename(columns = lambda c:c+" span"))

# # .transform()
# # Basically the same syntax as .agg(), but the function doesn't need to output an aggregate value: instead, it has to
# # transform the group.
# print(df.groupby("paradigm").transform("max").rename(columns=lambda c: c + " max value"))
#
# # To transform into % of the group max:
# print(df.groupby("paradigm").transform(lambda g: g / g.max() * 100)
#       .round(2).rename(columns=lambda c: c + ": % of max in group"))

# # .apply()
# # To apply a function to the entire group dataframe: i.e., it's not a by-column application of the function: the
# # function applies to a dataframe useful when more complex, trans-column functions are needed
# print(df.groupby("paradigm")["year", "popularity_rank"].apply(lambda g: g / g.max().max() * 100))

# # Grouping on multiple columns
# print(df.groupby(["paradigm", "random_value"]).max())

# # Grouping using different functions
# # 1 Dictionaries : column-specific function
# print(df.groupby(["paradigm", "random_value"]).agg({"creator": "count",
#                                               "year": "mean",
#                                               "popularity_rank": "median"}))

# # 2 Lists : multiple functions to apply
# print(df.groupby(["paradigm","random_value"]).agg["count","max"])

# # 3 Dictionaries and lists combined
dfmulti = df.groupby(["paradigm", "random_value"]).agg({"creator": "count",
                                                        "year": ["min", "mean", "max"],
                                                        "popularity_rank": ["mean", lambda x: x.max() - x.min()]})
# print(dfmulti)

# # Multi indexes
# #    have levels numbered from 0
# #    have names (not name)
# # The values at a specific can be accessed
# #     .get_level_values(i) for the ith level values = the same length as the index
# #     .levels[i] for the unique ith level values = the same as number of unique values at the ith level
# print(dfmulti.columns)
# print(dfmulti.index)
# print(dfmulti.index.names)
# print(dfmulti.index.get_level_values(0))
# print(dfmulti.index.levels[0])

# Indexing and selection
# You can use the well-known indexing methods with multi indexes
#   "partial" labels are allowed: using 0th level keys will drop that level and return the part of the series/dataframe
#   under that key
print(dfmulti["creator"])
print(dfmulti.loc["multi"])
print(dfmulti.loc["multi", "year"])
print(dfmulti.loc["multi", "year"]["mean"])
print(dfmulti.loc[("multi", 1)])
print(dfmulti.loc[("multi", 1), "year"])
print(dfmulti.loc["logic":("multi", 0)])
print(dfmulti.loc[["functional", "multi"]])

