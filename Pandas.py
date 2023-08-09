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
