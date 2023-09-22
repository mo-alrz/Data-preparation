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
#   match -> Returns a match object if there is a match at the beginning of the string
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

#   search -> Returns a match object if there is a match anywhere in the string and finds the first matching string
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

# pands .str. methods do allow regular expressions, very useful.
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
print(re.findall(p, text_to_search))

# Controlling number of occurrences
# The asterisk (Kleene star) allows for the preceding character or group to occur any number of times, incl. zero:
text_to_search = "Lor321m 1psum"
p = r"\d*"
print(re.findall(p, text_to_search))

# To exclude zero occurrences:
text_to_search = "Lor321m 1psum"
p = r"\d+"
print(re.findall(p, text_to_search))

# If you want only 0 or 1 occurrences:
text_to_search = "Lor321m 1psum"
p = r"\d?"
print(re.findall(p, text_to_search))

# This is equivalent to {0,1} = at least 0, at most 1 occurrences:
text_to_search = "Lor321m 1psum"
p = r"\d{0,1}"
print(re.findall(p, text_to_search))

# If you want to find exactly 2 occurrences:
text_to_search = "Lor321m 1psum"
p = r"\d{2}"
print(re.findall(p, text_to_search))

# Disjunctions ("OR"): fine-tuning sets of characters to search for
# Often the predefined sets of characters are not enough,and you need to finetune the characters you want to search for.
# For that, you can use
#     [...] for a list of characters
#     | for two characters or groups
#     - for a range of characters (within [])

text_to_search = "This is a date: 21-12-03"
p = r"[\d\-]+"
print(re.findall(p, text_to_search))

# To find strings of smaller-case letters only (in the range between a-z, inclusive!):
text_to_search = "This iz a date: 21-12-03"
p = r"[a-z]+"
print(re.findall(p, text_to_search))

# To find strings of characters that are neither smaller-case letters, nor space: use caret after opening square
# bracket to negate the set of characters searched for:
text_to_search = "This iz a date: 21-12-03"
p = r"[^a-z]+"
print(re.findall(p, text_to_search))

# To find all integers or hyphens
text_to_search = "This is a date: 21-12-03"
p = r"\d|\-"
print(re.findall(p, text_to_search))

# Use | for longer string, as well:
text_to_search = "Lisp, C++ and Python are all programming languages."
p = r"Python|Lisp"
print(re.findall(p, text_to_search))

# The ambiguity of the caret:
# Beware special metacharacters, which can sometimes --- in [...] --- behave as non-special characters. Beware
# especially the caret ^ which can be ambiguous!
#     outside of [...]: match beginning of string/line
text_to_search = "^This is a^caret."
p = r"^\w"
print(re.findall(p, text_to_search))

text_to_search = "This is a^caret."
p = r"^\w"
print(re.findall(p, text_to_search))

# inside of [^...] as first character: functions as negation ([^...] matches any character not inside it)
text_to_search = "^This is a^caret."
p = r"[^\w]"
print(re.findall(p, text_to_search))

#     inside of [...^] when NOT first character: matches carets!
text_to_search = "^This is a^caret."
p = r"[\w^]"
print(re.findall(p, text_to_search))

# Ambiguity of metacharacters
# inside [], most metacharacters function as non-meta characters
text_to_search = r"(Th)|is$ is a\lot*of+me-ta?char{}act^ers."
p = r"[*+?(){}.^|$]"
print(re.findall(p, text_to_search))

# But \ and of course [] remain special and have to be escaped:
text_to_search = r"This\is something[] different."
p = r"[\ ]"
print(re.findall(p, text_to_search))

text_to_search = r"This\is something[] different."
p = r"[\\ \[\]]"
print(re.findall(p, text_to_search))

# The hyphen - functions as a normal character if it is initial or final:
text_to_search = r"Beware the hy-phen."
p = r"[-a]"
print(re.findall(p, text_to_search))

text_to_search = r"Beware the hy-phen."
p = r"[a-]"
print(re.findall(p, text_to_search))

# But functions as a metacharacter in between others:
text_to_search = r"Beware the hy-phen."
p = r"[a-h]"
print(re.findall(p, text_to_search))

# Your safest bet is to always escape special characters, even if it is superfluous:
text_to_search = r"(Th)|i-s$ is a\lot*of+me-ta?c[h]ar{}act^ers."
p = r"[ \*\+\?\(\)\{\}\.\^\|\$\[\]\-]"
print(re.findall(p, text_to_search))

# Grouping
# We can also use () to group patterns
#     We can then search for a specific pattern within the entire search pattern.
#         use .group() method integer argument numbered from 1 to get the nth group.
#     We can also refer back to groups within the regex
#         use \1, \2..., etc.
text_to_search = "apple apple apple worm apple"
p = r"(\w+ )\1+"
res = re.search(p, text_to_search)
print(res.group())  # -> return entire match (same if argument 0 given)
print(res.group(1))  # -> return value of the first group (first parentheses)

# findall returns the group, not the entire match:
text_to_search = "apple apple apple worm apple"
p = r"(\w+ )\1+"
print(re.findall(p, text_to_search))

# if you have more than one groups (parentheses), then findall returns a list of group tuples:
text_to_search = "Python: 1990, Java: 1995, Go: 2009"
p = r"(\w+): (\d+)"
print(re.findall(p, text_to_search))

# You can also use named groups via (?P<name>...)
#     refer back to group not just using \1, etc., but also via (?P=name)
#     useful if you modify a complex search pattern, introducing and deleting groups

text_to_search = """Go: 2009, Java: 1995, Java: James Gosling, Python: 1990, Python: Guido van Rossum."""
p = r"(?P<language>\w+): (\d+)\b.*(?P=language): ([\w ]+)\b"
print(re.findall(p, text_to_search))

# Compilation flags
# These are NOT part of the search pattern, but arguments to the re search functions modifying the way the patterns are
# searched -> can be specified either in full-fledged names, or single-letter short versions.
# The most widely used flags:
# full flag 	  short flag               meaning
# re.IGNORECASE  	 re.I 	    perform case-Insensitive matches
# re.MULTILINE 	     re.M 	    ^ and $ match start/end of the lines, not of the entire string
# re.VERBOSE 	     re.X 	    enable verbose regexes, for cleaner human overview
# re.DOTALL 	     re.S 	    . matches newline characters, too
# re.ASCII 	         re.A 	    make \w, \d, etc. match only on ASCII characters, not unicode ones

# re.IGNORECASE, re.I
text_to_search = """Go: 2009, Java: 1995, Java: James Gosling, Python: 1990, Python: Guido van Rossum."""
p = r"python: (\d+)"
print(re.findall(p, text_to_search))

p = r"python: (\d+)"
print(re.findall(p, text_to_search, re.I))

# re.MULTILINE, re.M: beginning/end of line/string
text_to_search = """Lor3mus
1psum"""
print(text_to_search)

# Caret ^ matches only beginning of string by default:
p = r"^\w"
print(re.findall(p, text_to_search))

# But caret ^ can match beginning of line with re.MULTILINE flag:
p = r"^\w"
re.findall(p, text_to_search, re.MULTILINE)

# \A can only match beginning of string:
p = r"\A\w"
print(re.findall(p, text_to_search))

p = r"\A\w"
print(re.findall(p, text_to_search, re.MULTILINE))

# The same holds for $ matching end of string...
p = r"\w$"
print(re.findall(p, text_to_search))

p = r"\w$"
print(re.findall(p, text_to_search, re.MULTILINE))

# \Z can only match end of string:
p = r"\w\Z"
print(re.findall(p, text_to_search))

# re.VERBOSE, re.X (x for Extended)
# For complex patterns, it can help us structure and write in a more human-friendly way:
text_to_search = """Go: 2009, Java: 1995, Java: James Gosling, Python: 1990, Python: Guido van Rossum."""
p = r"(?P<language>\w+): (\d+)\b.*(?P=language): ([\w ]+)\b"
print(re.findall(p, text_to_search))

# With re.X, we can split it into multiple lines, adding Python-like comments using #. -> Note that we need to
# explicitly add \s where needed (after first colon in this case), since spaces are ignored in this case!
p = r"""(?P<language>\w+):\s    # first the named group of the programming language followed by : and whitespace
        (\d+)\b                 # then the year = integers followed by a word boundary
        .*                      # then any character(s)
        (?P=language):          # again the language repeated
        ([\w ]+)\b              # finally the developer: alphanumeric characters with space, followed by word boundary
      """

print(re.findall(p, text_to_search, re.X))

# Advanced
# Non-greedy *,+,?
# We have seen that * (like other such operators) is greedy, but in some cases, this would mean that it "eats up" too
# much of the string.
# -> An example: the final ">" is matched, and all interim ">" are "eaten up" by ".*":
text_to_search = "<html><head><title>Title</title>"
p = r"<.*>"
print(re.findall(p, text_to_search))

# In such cases, we can use *?, adding a ? to make it non-greedy, so that the first time it sees a ">", and can thus
# match the entire pattern, it will stop:
text_to_search = "<html><head><title>Title</title>"
p = r"<.*?>"
print(re.findall(p, text_to_search))

# Look ahead, look behind
# Useful if we only want to match patterns followed/preceded by specific patterns (or, to the contrary, NOT
# followed/preceded by specific patterns).
# (?=...) = positive lookahead (?!...) = negative lookahead
text_to_search = "Isaac Newton physicist, Isaac Asimov writer, Albert Einstein physicist"
p = r"Isaac \w+\b(?= physicist)"  # --> Isaac something, which is followed by physicist
print(re.findall(p, text_to_search))   # --> will only return Isaac something, but not the physicist part

text_to_search = "Isaac Newton physicist, Isaac Asimov writer, Albert Einstein physicist"
p = r"Isaac \w+\b(?! physicist)"  # --> Isaac something, which is NOT followed by physicist
print(re.findall(p, text_to_search))   # --> will only return Isaac something, but not the lookahead part

# (?<=...) = positive lookbehind (?<!...) = negative lookbehind
text_to_search = "physicist Isaac Newton, writer Isaac Asimov, and physicist Albert Einstein"
p = r"(?<=physicist )Isaac \w+\b"  # --> Isaac something, which is preceded by physicist
print(re.findall(p, text_to_search))

text_to_search = "physicist Isaac Newton, writer Isaac Asimov, and physicist Albert Einstein"
p = r"(?<!physicist )Isaac \w+\b"  # --> Isaac something, which is NOT preceded by physicist
print(re.findall(p, text_to_search))

# Pre-compiled RegEx objects: re.compile()
# Pre-compiling a regex pattern using re.compile(YOURPATTERN) resulted in better performance when doing a lot of regex
# lookups (especially in earlier Python versions).
# -> then the well-known functions can be called as methods on the regex object.
text_to_search = "Hello world!"
pattern = 'Hello'

# First, compile regex object from pattern, then call method on it
h = re.compile(pattern)
print(h.match(text_to_search).group())

# the non-precompiled way: pattern is an argument of the re function
print(re.match(pattern, text_to_search).group())

# If you precompile the pattern, then the lookup itself will be faster, since the compilation was done earlier
# Also, you can directly specify flags in your precompiled pattern, which you don't have to remember to include in
# future searches:
h = re.compile(pattern,re.I)
print(h.match(text_to_search).group())
