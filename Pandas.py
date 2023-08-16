import numpy as np
import pandas as pd

df = pd.DataFrame([["Python", "multi", "Guido van Rossum", 1995, 3],
                   ["Lisp", "multi", "John McCarthy", 1958, 33],
                   ["C++", "multi", "Bjarne Stroustrup", 1985, 4],
                   ["Java", "multi", "James Gosling", 1996, 1],
                   ["Haskell", "functional", "Lennart Augustsson", 1990, 40],
                   ["Prolog", "logic", "Alain Colmerauer", 1972, 36]],
                  columns=["name", "paradigm", "creator", "year", "popularity_rank"])

print(df)

seri = pd.Series(['pytho', 'multi', '1995'])
print(seri)

# df = pd.DataFrame(np.arange(70 * 90).reshape(70, 90))
# with pd.option_context("display.max_rows", 100, "display.max_columns", 100):
#     display(df)

# Setting index
df2 = pd.DataFrame([["multi", "Guido van Rossum", 1995, 3],
                    ["multi", "John McCarthy", 1958, 33],
                    ["multi", "Bjarne Stroustrup", 1985, 4],
                    ["multi", "James Gosling", 1996, 1],
                    ["functional", "Lennart Augustsson", 1990, 40],
                    ["logic", "Alain Colmerauer", 1972, 36]],
                   columns=["paradigm", "creator", "year", "popularity_rank"],
                   index=["Python", "Lisp", "C++", "Java", "Haskell", "Prolog"])
print(df2)

# Or:
df.set_index("name", inplace=True)
print(df)

# Remove the index
df.reset_index()

# Initializing series or dataframe from a dictionary
# {key:single value} can be used to initialize series
# {key:same-length iterable of values} can be used to initialize dataframes

mydict = {
    'name': ['Python',
             'Lisp',
             'C++',
             'Java',
             'Haskell',
             'Prolog'],
    'creator': ['Guido van Rossum',
                'John McCarthy',
                'Bjarne Stroustrup',
                'James Gosling',
                'Lennart Augustsson',
                'Alain Colmerauer'],
    'year': [1995, 1958, 1985, 1996, 1990, 1972],
}

df = pd.DataFrame(mydict)
seri = pd.Series(mydict)

print(seri)

# Accessing columns, rows, cells, slices
# Depending on what parts of a data frame we access, we get different types of objects:
#   accessing columns or rows -> pd.Series
#   accessing a cell -> whatever type that particular cell is
#   accessing 2D parts of the data frame -> pd.DataFrame

# The first and last n rows (the default is 5) of a data frame or series can be quickly inspected by the head and tail
# methods:
print(df.head(2))
print(df.tail(2))

# The column labels of a dataframe can be accessed by .columns (NO parentheses!)
print(df2.columns)

# Column values can be also set:
df2.columns = ['paradigm', 'creator', 'year', 'tiobe_idx']

# The row labels with .index
print(df2.index)

# Series only have index, no columns

# Accessing columns -> Can be accessed by label df["creator"]
print(df2["creator"])

# With appropriate column labels (string without spaces) a dotted syntax also works:
print(df2.creator)

# Multiple columns can be accessed using list :
print(df[["creator", "year"]])
print(type(df2["creator"]), type(df[["creator", "year"]]))

# Values also can be set, even new column values
df2["constant"] = 'some value'
df2["id"] = np.arange(len(df2))
print(df2)

# Accessing rows
# The same logic applies as with columns, but they must be accessed using .loc[] instead of simple square brackets
print(df2.loc["Python"])

# .loc[] and .iloc[]
print(df2.loc[["Lisp", "Java"], ["creator", "tiobe_idx"]])
print(df2.iloc[[1, 3], [1, 3]])

# .loc[] and .iloc[] multiple rows and single column = series
print(df2.loc[["Lisp", "Java"], "creator"])
print(df2.iloc[[1, 3], 1])

# .loc[] and .iloc[] multiple rows and single column as a list = dataframe
print(df2.loc[["Lisp", "Java"], ["creator"]])
print(df2.iloc[[1, 3], [1]])

# .loc[] and .iloc[] single row and single column = cell
print(df2.loc["Python", "year"])
print(df2.iloc[0, 0])

# loc can also be used to access 2-dimensional ranges using Python's slicing syntax extended to two dimensions:
print(df2.loc["Lisp":"Java", "creator":"tiobe_idx"])
print(df2.iloc[:3, 1:4])

# Conditions and boolean masks
d2 = pd.DataFrame([[3, 'two', 1], [3, 3, 3]],
                  columns=[f'col{i}' for i in range(3)],
                  index=[f'row{i}' for i in range(2)])

print(d2 == 3)
print(d2[d2 == 3])
print(d2[(d2 == 3) | (d2 == 'two')])

print((d2 == 3).all())
print((d2 == 3).all(axis=1))
print(d2[(d2 == 3).all(axis=1)])

# Descriptive
print(df2.describe())

# If there are numerical columns then only those columns' statistics are included by default --
# the include parameter can be used to produce all:
print(df2.describe(include="all"))
print(df["year"].describe())

# .min(), .max(), .mean(), .median(), .std(), .count()
print(df2.count())
print(df2.count(axis=1))
# print(df2.mean()) & ...

# Unique values and value counts .unique() .nunique() .value_counts()
colname = "paradigm"
print(colname, "has", df2[colname].nunique(), "values:")
print(df2[colname].unique())
print(df2[colname].value_counts())

# Types
print(df2.info())  # This method is not available for series
print(df2.dtypes)  # Gives the types of the columns
print(df2['year'].dtype)  # For series

# DataFrame and Series manipulation
# Making a copy
d = pd.DataFrame(np.arange(6).reshape(2, 3))
d2 = d.copy()
d2.loc[0, 0] = 100
print(d)
print(d2)

# DataFrame Concatenation
# By default, as always, axis=0 is assumed = concatenation of rows:
d = pd.DataFrame(np.arange(15).reshape(3, 5))
d2 = pd.DataFrame(np.arange(100, 110).reshape(2, 5), index=[1, 2])
d3 = pd.concat([d, d2])
print(d3)

# To concatenate along columns
d3 = pd.concat([d, d2], axis=1)
print(d3)

# Elementwise operations
d = pd.DataFrame(np.ones(6).reshape(2, 3))
print(d + 1)
d.iloc[0, 1:] = -2
print(d)
print(d.abs())

# Aggregation/Reduction methods and mapping values
d = pd.DataFrame(np.arange(15).reshape(3, 5))
print(d.sum(1))  # Axis = 1, sum columns = one value per row
print(d.mean())  # Axis = 0, function apply to rows
print(d.mean().mean())

s = pd.Series([1, 1, 10, 3, 3])
print(s.unique(), s.nunique())

# MAP
# Series -> .map()
# DataFrames -> .applymap() to apply a function to each cell
#               .apply() -> axis = 0 apply a function to each column
#                           axis = 1 apply a function to each row

s = pd.Series(['one', 'two', 'three', 'go'])
s2 = s.map(lambda x: x[:2])
print(s2)

d = pd.DataFrame(np.arange(15).reshape(5, 3), columns=["col1", "col2", "col3"])
d2 = d.apply("sum",axis=0)
print(d2)

# .dt. and .str.
s3 = s.str.cat(sep= '+')
print(s3)