

"""
Regular Expression
(Re/Regax): Re is a tiny programming lanuage which is interfaced with other language ,using Re we can create patterns of special characters
 used to find string or strings from other strings(occurancess from strings).special character used in Re are called Mera character and 
 pattern made to find the occurances is called meta pattterns.

Meta characters used in regular expression:
^ $ .*? +{}[]()\|

Type of basic patterns made using Meta character ..
1.Single character matching
2.Quantity matching
3.Location Matching

First in First : if we are creating  a normal pattern using character without any meta character, then that pattern is directly Searched .
if 5 character in a normal pattern then they will be searched character by chracter in the main string.
Findall method will return a list having all occurances of occurances 

"""
# import re
# s="Welcome to cetpa ,Cetpa is a award winning company**123"
# p="cetpa"
# res=re.findall(p,s)
# print(res)

'''
1.character class"[] this meta character search single character mentioned inside character class.



'''
# s="cetp\na" # Raw String  
# s=r"cetp\na"
# print(s)
# s="Welcome to cetpa.**123"
# p="[abcdjklmjhg2]"   # To search individual character put all the character in square bracket
# r=re.findall(p,s)
# print(r)

# s="Welcome to cetpa.**123"
# p="[abcdefghijklmopqrstuvwxyz]"
# res=re.findall(p,s,flags=re.IGNORECASE)
# print(res)

#New Program
# s="Welcome to cetpa.**123"
# l="[a-zA-Z]"
# r=re.findall(l,s)
# print(r)

#New Program
# import re
# s="Welcome to cetpa.**123"
# l="[a-zA-Z0-9]"
# r=re.findall(l,s)
# print(r)
import re
# s="Welcome to cetpa.**1_23"
# p="[a-zA-Z0-9_]"
# r=re.findall(p,s)
# print(r)

# s="Welcome to cetpa.cetpa is no1."
# p="cetpa"
# r=re.findall(p,s)
# print(r)

# s="Welcome to cetpa.cetpa is no1."
# p="[abc][opq]"  # Will Search combination of 2 characters
# r=re.findall(p,s)
# print(r)

# s="Welcome to cetpa.cetpa is no1."
# p="[a-z][a-z]"  # Will Search combination of 2 characters
# r=re.findall(p,s)
# print(r)

# s="Welcome to cetpa.cetpa is no1."
# p="[a-z][a-z][a-z]"  # Will Search combination of 3 characters
# r=re.findall(p,s)
# print(r)

# s="Welcome to cetpa.cetpa is no1."
# p="[0-9]"  # Will Search combination of 1 characters
# r=re.findall(p,s)
# print(r)

# s="Welcome to cetpa.cetpa is no1."
# p="[0-9][0-9]"  # Will Search combination of 2 characters
# r=re.findall(p,s)
# print(r)

# s="Welcome to cetpa.cetpa is no1."
# p="[0-9][0-9][0-9]"  # Will Search combination of 3 characters
# r=re.findall(p,s)
# print(r)

'''
[0-9]        or \d :Digits
\D                 : all single character other than digits
[a-zA-Z0-9_] or \w :alphanumeric single character
\W                 : All non alphanumeric characters
\s                 : allwhitespaces
\S                 : all characters other than white sapaces

'''

# s="Welcome to cetpa.cetpa is no1123976y9787865."
# p="\d"  
# r=re.findall(p,s)
# print(r)

# s="Welcome to cetpa.cetpa is no1."
# p="\D"  
# r=re.findall(p,s)
# print(r)

# s="Welcome to cetpa.cetpa is no1."
# p="\W"  
# r=re.findall(p,s)
# print(r)

# s="Welcome to cetpa.cetpa is no1."
# p="\w"  
# r=re.findall(p,s)
# print(r)

# s="Welcome to cetpa.cetpa is no1."
# p="\s"  
# r=re.findall(p,s)
# print(r)

# s="Welcome to cetpa.cetpa is no1."
# p="\S"  
# r=re.findall(p,s)
# print(r)

'''NEW PROGRAM'''
# s="devesh upadhyay is a very 88nboy 1872mmb."
# k="\d\d\d"
# r=re.findall(k,s)
# print(r)

'''
Quantity Matching:{}
{n}:will search exact n occurance
ex: will search all  3 digits in a sequence
{m,n}:will search occurances having min m character and max n character
{m,}:will search occurances having min m character ore more than m character
{,n}:will search occurances   having 0 to n character ie maximum n character
'''
# s="devesh upadhyay is a very 88nboy 1872mmb."
# k="\d{3}"
# r=re.findall(k,s)
# print(r)

# s='Welcome9889232425 abcd *8957232425'
# p="\d{10}"
# r=re.findall(p,s)
# print(r)

# s='Welcome988 9 23 2425 abcd *8957 232425'
# p="\d{3,}"                          # 3 ya 3 se jada digit
# r=re.findall(p,s)
# print(r)

# s='Welcome988 9 23 2425 abcd *8957 232425'
# p="\d{3,5}"                          # 3 to 5 digit
# r=re.findall(p,s)
# print(r)

# s='Welcome988 9 23 2425 abcd *8957 232425'
# p="\d{,2}"                          # 3 to 5 digit
# r=re.findall(p,s)
# print(r)

'''
To Nullify the Effect of meta characters,we can put the metacharacter inside character class[] or after back slash \
meta character: .Dot:Search all characters other than new line 
'''
# s="Welcome to cetpa.\ncetpa is no 1"
# p="."
# r=re.findall(p,s)
# print(r)

# s="Welcome to cetpa.\ncetpa is no 1"
# p="[.]"
# r=re.findall(p,s)
# print(r)

# s="Welcome to cetpa.\ncetpa is no 1"
# p="\."
# r=re.findall(p,s)
# print(r)

'''Find all 3 digits combinations starting with # OR $'''

# s="#234 78 $678 &567"
# p="[#$]\d{3}"
# r=re.findall(p,s)
# print(r)

'''Find all 3 digits combinations starting with # OR $'''
# s="#234 789 $678 &567"
# p="[#$]{,1}\d{3}"
# r=re.findall(p,s)
# print(r)

"""
*: Search 0 or more occurance:{0,}
+: Search 1 or more occurance:{1,0}
?: Search 0 or  1  occurance:{,1}
"""
'''To find gmailid from the data'''
# s="Email:abcd@def.com vk@gamil.com -juj0-8  dev@98gmail.com"
# p="\w+@\w+[.]\w+"
# r=re.findall(p,s)
# print(r)
import re
# s="2344-343-1234 2344-343-1233  2344-343-1111 234-343-1234"
# p="\d{3}-\d{3}-\d{4}"
# r=re.findall(p,s)
# print(r)

# s="2344-343-1234 2344-343-1233  +91-2344-343-1111 +92-234-343-1234"
# p="[+]\d{1,3}-\d{3}-\d{3}-\d{4}"
# r=re.findall(p,s)
# print(r)

# s="2344-343-1234 2344-343-1233  +91-2344-343-1111 +92-234-343-1234"
# p="[+]?\d{0,3}-?\d{3}-\d{3}-\d{4}"
# r=re.findall(p,s)
# print(r)

'''
Locatopn:
^:Starting of string
$:End of string
'''
s="Welcome to cetpa you are most welcome "
p="^cetpa"
r=re.findall(p,s)
print(r)

s="Welcome to cetpa you are most welcome cetpa"
p="cetpa$"
r=re.findall(p,s)
print(r)