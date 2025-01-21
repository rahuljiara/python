str1 = "String"
str2 = 'String'
str3 = """String"""
print("Data Type Of str1", type(str1))
print("Data Type Of str2", type(str2))
print("Data Type Of str3", type(str3))



print()
name = "Rahul Ji Ara"
# INDEXING - varName[indexNum]
print(name[0]) 
print(name[7])




# NEGATIVE INDEXING
print()
'''
  0     1     2     3    4   --> Positive Index starts from begining (0)
  A     P     P     L    E
 -5    -4    -3    -2   -1   --> Negative Index starts from end (-1)
'''

print(name[-1]) 
print(name[-9])

# SLICING - varName[startingIndexNum : endIndexNum]
print()
print("SLICING")
print(name[7:11])
print(name[-10:-5])

#String Method 
name= 'rahuljiara'
print()
print("Strings Method ".upper( ),end="\n")
print(name.title())
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name,"is digit -> ",name.isdigit())
print(name,"is only alphabet -> ",name.isalpha())
print(name,"is  alphanumeric character -> ", name.isalnum())
print(name,"contains only whitespace -> ",name.isspace())

'''
    Method	                      Description
    
  capitalize()    	Converts the first character to upper case
  casefold()	      Converts string into lower case
  center()	        Returns a centered string
  count()	          Returns the number of times a specified value occurs in a string
  encode()         	Returns an encoded version of the string
  endswith()	      Returns true if the string ends with the specified value
  expandtabs()	    Sets the tab size of the string
  find()	          Searches the string for a specified value and returns the position of where it was found
  format()	        Formats specified values in a string
  format_map()	    Formats specified values in a string
  index()	          Searches the string for a specified value and returns the position of where it was found
  isalnum()	        Returns True if all characters in the string are alphanumeric
  isalpha()	        Returns True if all characters in the string are in the alphabet
  isascii()	        Returns True if all characters in the string are ascii characters
  isdecimal()	      Returns True if all characters in the string are decimals
  isdigit()	        Returns True if all characters in the string are digits
  isidentifier()	  Returns True if the string is an identifier
  islower()	        Returns True if all characters in the string are lower case
  isnumeric()	      Returns True if all characters in the string are numeric
  isprintable()	    Returns True if all characters in the string are printable
  isspace()	        Returns True if all characters in the string are whitespaces
  istitle()	        Returns True if the string follows the rules of a title
  isupper()         Returns True if all characters in the string are upper case
  join()	          Converts the elements of an iterable into a string
  ljust()	          Returns a left justified version of the string
  lower()	          Converts a string into lower case
  lstrip()	        Returns a left trim version of the string
  maketrans()	      Returns a translation table to be used in translations
  partition()	      Returns a tuple where the string is parted into three parts
  replace()	        Returns a string where a specified value is replaced with a specified value
  rfind()	          Searches the string for a specified value and returns the last position of where it was found
  rindex()          Searches the string for a specified value and returns the last position of where it was found
  rjust()	          Returns a right justified version of the string
  rpartition()	    Returns a tuple where the string is parted into three parts
  rsplit()	        Splits the string at the specified separator, and returns a list
  rstrip()	        Returns a right trim version of the string
  split()	          Splits the string at the specified separator, and returns a list
  splitlines()	    Splits the string at line breaks and returns a list
  startswith()	    Returns true if the string starts with the specified value
  strip()	          Returns a trimmed version of the string
  swapcase()	      Swaps cases, lower case becomes upper case and vice versa
  title()	          Converts the first character of each word to upper case
  translate()	      Returns a translated string
  upper()	          Converts a string into upper case
  zfill()	          Fills the string with a specified number of 0 values at the beginning
'''