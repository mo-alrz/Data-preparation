# Useful in many cases such as
#   searching for strings
#   searching for files or directories
#   scraping
#   cleaning textual data

import re
from functools import reduce
import pandas as pd

text = "Lor3m 1psum"
search_patt = "\d"
ints = re.findall(search_patt, text)
print(ints)  # All the inputs will be list of strings

reduce_function = lambda x, y: x + y
val1 = reduce(reduce_function, ints)
print(val1)

val2 = reduce(reduce_function, map(lambda x: int(x),ints))
print(val2)

# RegEx functions:
#   match -> Returns a Match object if there is a match at the beginning of the string
text_to_search ="Lor3m 1psum"
search_pattern = "\d"
result = re.match(search_pattern,text_to_search)
print(result)

text_to_search ="1psum Lor3m"
search_pattern = "\d"
result = re.match(search_pattern,text_to_search)
print(result)

# The methods of the match object :
methods = [x for x in dir(result) if not x.startswith("_")]
print(methods)

# To get back the matched string -> .group()
print(result.group())

#   search -> Returns a Match object if there is a match anywhere in the string and finds the first matching string
text_to_search ="Lor3m 1psum"
search_pattern = "\d"
result = re.search(search_pattern,text_to_search)
print(result)
print(result.group())

text_to_search ="Lor32m 1psum"
search_pattern = "\d\d"
result = re.search(search_pattern,text_to_search)
print(result)
print(result.group())

#   findall -> Returns a list (Not an object) containing all matches
text_to_search ="Lor32m 12psum"
search_pattern = "\d\d"
result = re.findall(search_pattern,text_to_search)
print(result)

# Non-Overlapping matches are returned = Once a character was used in a preceding match, it cannot be used in a "next"
# match: of the substring "321", only "32" is returned, "21" is not, since "2" was already used in "32":
text_to_search = "Lor321m 1234psum"
search_pattern = "\d\d"
result = re.findall(search_pattern, text_to_search)
print(result)

#   split -> Returns a list where the string has been split at each match
text_to_search = "Lor3m 1psum"
search_pattern = "\d"
result = re.split(search_pattern,text_to_search)
print(result)

# pands .str. methods do allow regular experessions, very useful.
s = pd.Series(["Lor3m","And 1p5s\dum"])
s1 = s.str.split(r"\d")
print(s1)

# To expand splits into different columns:
s1 = s.str.split(r"\d",expand=True)
print(s1)

# Like regular split, the empty strings are returned when more than one character from a sequence on which we split:
text_to_search = "Lor321m 1psum"
search_pattern = "\d"
result = re.split(search_pattern, text_to_search)
print(result)

#   sub -> Replaces one or many matches with a string
text_to_search = "Lor321m 1psum"
search_pattern = "\d"
replacewith = "X"
result = re.sub(search_pattern, replacewith, text_to_search)
print(result)

# Optional count argument to specify number of replacements. E.g., count=1 only replaces first match:
text_to_search = "Lor321m 1psum"
search_pattern = "\d"
replacewith = "X"
result = re.sub(search_pattern, replacewith, text_to_search, count=1)
print(result)
