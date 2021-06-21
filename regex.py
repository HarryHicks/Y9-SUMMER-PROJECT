import re

password = input("Enter the password: ")

score = 0

if len(password) >= 8 and len(password) <= 26:
  score += 6
  print("BETWEEN")

if bool(re.search("((?=.*[a-z]))", password)) == True:
  score += 6
  print("a-z")

if bool(re.search("((?=.*[A-Z]))", password)) == True:
  score += 6
  print("0-9")

if bool(re.search("((?=.*[0-9]))", password)) == True:
  score += 6
  print("A-Z")

if bool(re.search("((?=.*[!,$,%,^,&,*,(,),-,_,=,+]))", password)) == True:
  score += 1
  print("SYMBOLS")

for password in password:
  if password.isdigit():
    score += 1

  if password.isupper():
    score += 1

  if password.islower():
    score += 1

score = score * 2

print(score)
"""
if(len(v)>=8):
    if(bool(re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,30})',v))==True):
        print("The password is strong")
    elif(bool(re.match('((\d*)([a-z]*)([A-Z]*)([!@#$%^&*]*).{8,30})',v))==True):
        print("The password is weak")
else:
    print("You have entered an invalid password.")
"""

"""
100 total

10 for a-z
10 for A-Z
10 for ! $ % ^ & * ( ) - _ = +
1 for islower
1 for isupper
1 for digit
"""