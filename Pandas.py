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

#df = pd.DataFrame(np.arange(70 * 90).reshape(70, 90))
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

