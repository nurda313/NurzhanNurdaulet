import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)


# findall	Returns a list containing all matches
# search	Returns a Match object if there is a match anywhere in the string
# split	    Returns a list where the string has been split at each match
# sub	    Replaces one or many matches with a string


#Metacharacters

#Character      Description                                    Example
# []	      A set of characters	                             "[a-m]"	

# \	        Signals a special sequence 
#           (can also be used to escape special characters)	     "\d"	

# .	        Any character (except newline character)	         "he..o"	

# ^	        Starts with	                                         "^hello"	

# $	        Ends with	                                         "planet$"	

# *	        Zero or more occurrences	                         "he.*o"	

# +	        One or more occurrences	                             "he.+o"	

# ?	        Zero or one occurrences	                             "he.?o"	

# {}	    Exactly the specified number of occurrences	         "he.{2}o"	

# |	        Either or	                                         "falls|stays"




#The findall() function returns a list containing all matches.
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

#Return an empty list if no match was found:
import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)



#The search() function searches the string for a match, 
# and returns a Match object if there is a match.

#If there is more than one match, 
# only the first occurrence of the match will be returned:


import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())


#If no matches are found, the value None is returned:
import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)



# The split() function returns a list where the 
# string has been split at each match:
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)


# You can control the number of occurrences by 
# specifying the maxsplit parameter:
import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)



# The sub() function replaces the matches with the text of your choice:
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)


# Replace the first 2 occurrences:
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

# A Match Object is an object containing information 
# about the search and the result.
import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object




# The Match object has properties and methods used to retrieve information about the search, and the result:

# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match




# Print the position (start- and end-position) of 
# the first match occurrence.

# The regular expression looks for any words that 
# starts with an upper case "S":
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())


# Print the string passed into the function:
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)


# Print the part of the string where there was a match.

# The regular expression looks for any words that 
# starts with an upper case "S":


import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())



