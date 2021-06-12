import requests
from zxcvbn import zxcvbn
import json
import string
import random
import sys
import functions
import re

def main_menu():

  print("MAIN MENU:")
  print("Type 1 for checker")
  print("Type 2 for generator")
  print("Type 3 to exit")

  inputd = input("What is your choice? ")
  inputd = str(inputd)
  if inputd == "1":
    input2 = input("Password: ")
    #functions.checker(input2)
    checkertest2(input2)

  elif inputd == "2":
    functions.gen_simple()
    while True:
      another = input("Would you like another password? [y/n] ")
      if another.lower() == "y":
        functions.gen_simple()
      else:
        functions.main_menu()
  elif inputd == "3":
    sys.exit()
  else:
    sys.exit()

def checkertest2(password:str):
    if len(password) >=  10 \
    and re.search("^[a-zA-Z0-9]+", password) \
    and re.search("[a-z]+", password) \
    and re.search("[A-Z]+", password) \
    and re.search("[0-9]+", password):
        print(password, True)
        return True
    else:
        print(password, False)
        return False

def checker(password):
  results = zxcvbn(password)
  print(results)
  score = results["score"]
  print(score)
  suggestions = results["feedback"]["suggestions"]
  if suggestions == None:
    pass
  for suggest in suggestions:
    print(suggest)
  
def gen_simple():
    typeofpass = input("\nWould you like a password with a random selection of letters, numbers and symbols or just a lettered one? [1/2] ")
    if typeofpass == "1":
      characters = string.ascii_letters + string.punctuation  + string.digits
      password =  "".join(random.choice(characters) for x in range(random.randint(8, 16)))
      print(f"\n{password}\n")
    elif typeofpass == "2":
      characters = string.ascii_letters
      password =  "".join(random.choice(characters) for x in range(random.randint(8, 16)))
      print(f"\n{password}\n")
    else:
      functions.main_menu()

def gen_simple_web():
    characters = string.ascii_letters
    password =  "".join(random.choice(characters) for x in range(random.randint(8, 26)))
    return password

def gen_tough_web():
    characters = string.ascii_letters + string.punctuation  + string.digits
    password =  "".join(random.choice(characters) for x in range(random.randint(8, 26)))
    return password

def checker_web(password:str):
  results = zxcvbn(password)
  score = results["score"]
  suggestions = results["feedback"]["suggestions"]
  send = score
  send = f"{send} "
  if suggestions != None:
    for suggest in suggestions:
      send = f"{send}" + suggest
  return send