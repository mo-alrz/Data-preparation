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

val2 = reduce(reduce_function, map(lambda x: int(x), ints))
print(val2)

# RegEx functions:
#   match -> Returns a Match object if there is a match at the beginning of the string
text_to_search = "Lor3m 1psum"
search_pattern = "\d"
result = re.match(search_pattern, text_to_search)
print(result)

text_to_search = "1psum Lor3m"
search_pattern = "\d"
result = re.match(search_pattern, text_to_search)
print(result)

# The methods of the match object :
methods = [x for x in dir(result) if not x.startswith("_")]
print(methods)

# To get back the matched string -> .group()
print(result.group())

#   search -> Returns a Match object if there is a match anywhere in the string and finds the first matching string
text_to_search = "Lor3m 1psum"
search_pattern = "\d"
result = re.search(search_pattern, text_to_search)
print(result)
print(result.group())

text_to_search = "Lor32m 1psum"
search_pattern = "\d\d"
result = re.search(search_pattern, text_to_search)
print(result)
print(result.group())

#   findall -> Returns a list (Not an object) containing all matches
text_to_search = "Lor32m 12psum"
search_pattern = "\d\d"
result = re.findall(search_pattern, text_to_search)
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
result = re.split(search_pattern, text_to_search)
print(result)

# pands .str. methods do allow regular experessions, very useful.
s = pd.Series(["Lor3m", "And 1p5s\dum"])
s1 = s.str.split(r"\d")
print(s1)

# To expand splits into different columns:
s1 = s.str.split(r"\d", expand=True)
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

# RegEx metacharacters - > . ^ $ * + ? { } [ ] \ | ( ) need a backslash to be found
print('a\nb')
print('a\\nb')

# Predefined sets of characters:
# \d = any integer (from 0 to 9) -> \D = any NON-integer
# \w = any alphanumeric character -> \W = any NON-alphanumeric character
#     lowercase letters a-z
#     uppercase letters A-Z
#     integers 0-9
#     underscore _
# \s = any whitespace character -> \S = any non-whitespace character. The most widely-used whitespaces are:
#     = SPACE
#     \t = TAB
#     \r = CR (Carriage Return) = new line character in Mac OS before X
#     \n = LF (Line Feed) = new line character in Unix/Mac OS X
#     (\r\n = CR + LF is the new line character in Windows = two whitespace characters)
# \b = word boundary, so it's not really a character, just matches word boundaries (=sequences of alphanumeric
#      characters). -> \B = NOT a word boundary (again a zero-width match)

# A multiline text to search
#     Note the multiline string (delimiter """ instead of "), so that we don't have to use \n for line breaks
#     Note the r before the delimiter: this tells Python to use raw string notation (so that, e.g., \ stands for \)
#         regular string "\\" ~ raw string r"\"
#         regular string "\\\\section" ~ raw string r"\\section"
#
# You will generally want to use raw string notation for your regexes, as well to keep things readable!

text_to_search = r"""Lor345m 1psum
dolor sit amet, 
consectetur adipiscing 
elit.\Aliquam vel odio
 volutpat, - tempor odio
 nec, fermentum magna?
"""

for search_pattern in ["\d", "\d\d", "\dm", "\s\w", "\s\W", r"\\A"]:
    print("\n-------------")
    print("Our search pattern:", search_pattern)

    matches_found = re.findall(search_pattern, text_to_search)

    print("The matches:")
    print(matches_found)


# Word boundaries
p = "class"
for text_to_search in ["In today's class", "we learn about classified things."]:
    print("\nText:", text_to_search)
    print("Matches:", re.findall(p, text_to_search))

p = r"\bclass\b"
for text_to_search in ["In today's class", "we learn about classified things."]:
    print("\nText:", text_to_search)
    print("Matches:", re.findall(p, text_to_search))

# Other metacharacters
# ^ 	    match beginning of string/line (use re.MULTILINE flag for line)
# $ 	    match end of string/line (use re.MULTILINE flag for line)
# \A 	    match beginning of string
# \Z 	    match end of string
# . 	    match any single character except newline
# [...] 	match any of the single characters in "..."
# [^...] 	match any single characters not in "..."
# x|y 	    match x or y
# a-z 	    match all characters between a and z within []
# * 	    match 0 or more of the preceding
# + 	    match 1 or more of the preceding
# ? 	    match 0 or 1 of the preceding
# {n} 	    match exactly n occurrences of the preceding
# {n,} 	    match at least n occurrences of the preceding
# {n,m} 	match at least n, but at most m of the preceding
# (...) 	group expressions and remember group text
# \1...\9 	matches 1st .... 9th grouped expression

# The wildcard: .
# In the python re module, the period is the wildcard = matches any single character (except for newline).
text_to_search = """Lor3m
1psum"""
p = "."
print(re.findall(p,text_to_search))

# Controlling number of occurrences
