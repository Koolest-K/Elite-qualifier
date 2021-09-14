import colorama
from colorama import Fore, Style, Back
colorama.init()
import random

name = input("Hello! What's your name? \n???: ")
print()
print(f"That's a nice name! Do you have a favorite {Fore.RED}c{Fore.YELLOW}o{Fore.GREEN}l{Fore.BLUE}o{Fore.MAGENTA}r{Fore.RESET}?\nOptions:\n {Fore.MAGENTA}'purple',\n {Fore.RED}'red',\n {Fore.YELLOW}'yellow',\n {Fore.BLUE}'blue',\n {Fore.GREEN}'green'{Fore.RESET}")

color = input(f"{name}: ")
print()

if color == 'purple':
  text = Fore.MAGENTA
if color == 'red':
  text = Fore.RED
if color == 'yellow':
  text = Fore.YELLOW
if color == 'blue':
  text = Fore.BLUE
if color == 'green':
  text = Fore.GREEN

print(f"{Fore.RED}N{Fore.YELLOW}i{Fore.GREEN}c{Fore.BLUE}e {Fore.MAGENTA}c{Fore.BLUE}h{Fore.GREEN}o{Fore.YELLOW}i{Fore.RED}c{Fore.MAGENTA}e{Fore.RESET}! I like {text}{color}{Fore.RESET} too!\nShould I introduce myself now?\nHey there {name}! {Fore.RED}I'm C.B{Fore.RESET},  \ndesigned to entertain you! \nyou can type in:\n{Fore.YELLOW}'wyr'{Fore.RESET},\nor \n{Fore.GREEN}'beat the bot'{Fore.RESET}, \nType in: \n{Fore.CYAN}'info'{Fore.RESET} to learn about the different options! \nOr click the {Fore.MAGENTA}'x'{Fore.RESET} to leave the chat!\n")

def user_input():
    inputs = input(f"{name}:{text} ")
    
    if inputs == "beat the bot":
      print(f"{Fore.RESET}\nRules of the game:\n------------------ \n{text}1. Must type in answer in LOWERCASE, NO SPACES, or it will counted wrong\n{Fore.RESET}Example:\nquestion: pick red\n a.red b.yellow c.green?\nyour input: a{text}\n3. Cross ur fingers and hope you know enough!\n")
      print(beat_the_bot())
    if inputs == "wyr":
        print(wyr())
    if inputs ==  "info":
      print(information ())
    else:
      print (f"Sorry, I only understand simple answers, such as: \n{Fore.RESET}'wyr' 'beat the bot' 'info' {text}or{Fore.RESET} click the x{text} to leave the chat \n")
      print (user_input())   
     
 
def information():
    print(f"{Fore.RESET}Beat the bot{text} ----- A series of random questions which you and the bot must take turns answering \n{Fore.RESET}Wry{text} ----- Play 'would you rather'") 
    print(user_input())
  
  
def wyr():
  a = "Would you rather have the ability to see 10 minutes into the future or 150 years into the future?"
  b = " Would you rather have telekinesis (the ability to move things with your mind) or telepathy (the ability to read minds)?"
  c = "Would you rather team up with Wonder Woman or Captin Marvel"
  d = "Would you rather be forced to sing along or dance to every single song you hear?"
  e = "Would you rather find true love today or win the lottery next year?"
  f = "Would you rather be in jail for five years or be in a coma for a decade?"
  g = "Would you rather have another 10 years with your partner or a one-night stand with your celebrity crush?"
  h = "Would you rather be chronically under-dressed or overdressed?"
  i = "Would you rather have everyone you know be able to read your thoughts or for everyone you know to have access to your Internet history?"
  j = "Would you rather lose your sight or your memories?"
  k = "Would you rather have universal respect or unlimited power?"
  l = "Would you rather give up air conditioning and heating for the rest of your life or give up the Internet for the rest of your life?"
  m = "Would you rather swim in a pool full of Nutella or a pool full of maple syrup?"
  n = "Would you rather labor under a hot sun or extreme cold?"
  o = " Would you rather buy 10 things you don’t need every time you go shopping or always forget the one thing that you need when you go to the store?"
  p = "Would you rather never be able to go out during the day or never be able to go out at night?"
  q = "Would you rather have a personal maid or a personal chef?"
  r = "Would you rather be 11 feet tall or nine inches tall?"
  s = "Would you rather vomit on your hero or have your hero vomit on you?"
  t = "Would you rather communicate only in emoji or never be able to text at all ever again?" 
  u = "Would you rather find a rat in your kitchen or a roach in your bed?"
  v = "Would you rather have a pause or a rewind button in your life?"
  w = "Would you rather solve world hunger or global warming?"
  x = "Would you rather have to wear every shirt inside out or every pair of pants backward?"
  y = "Would you rather be alone all your life or surrounded by really annoying people?"
  z = "Would you rather be in a zombie apocalypse or a robot apocalypse?"


  questions = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
  question = random.choice(questions)
  print(f"\n{Fore.RESET}{question}{text}" + "\n")
  print()
  print("'left' or 'right'\n")
  input(f"{name}: ")
  list = ["Really?!", "Haha no way!", "Me too!", "That's crazy!!", "what are you thinking?!", "that was a tough question!"]
  response = random.choice(list)
  print()
  print(f"{Fore.RESET}{response}{text}")
  print("Would you like another question?\n 'yes' or 'no'")
  again = input(f"{name}: ")
  if again == 'yes':
      print(wyr())
  if again == "no":
      print()
      print("What would you like to do?\n")
      print(user_input())
  else:
      print("Sorry didn't understand! Type in 'yes' or 'no' ")
      again = input(f"{name}: ")
        
 
def beat_the_bot():
  a = "How long is an Olympic swimming pool (in meters)?\n a.100meters b.50meters c.250meters"#50m
  b = "What geometric shape is generally used for stop signs?\n a.hexagon b.heptagon c.octagon"#Octagon
  c = "How many countries still have the shilling as currency?\n a.4 b.2 c.none"#4
  d = "What is the name of the biggest technology company in South Korea?\n a.HYUNDAI MOTOR COMPANY b.SAMSUNG ELECTRONICS c.SK HYNIX."#Samsung
  e = "Worship of Krishna is observed by which Religious Faith?\n a.Hinduism b.Judaism c.Buddhism"#Hinduism
  f = "What is the rarest M&M color? a.purple b.brown c.orange"#Brown
  g = "What is the common name for dried plums?\n a.Raisins b.Dates c.Prunes"#Prunes
  h = "What was the first soft drink in space?\n a.Coca Cola b.Pepsi c.Sprite"#Coca Cola
  i = "What is the most consumed manufactured drink in the world?\n a.Sprite b.Tea c.Coffe"#Tea
  j = "What is the only edible food that never goes bad?\n a.Spam b.Honey c.Raw Spaghetti"#Honey
  k = "Which country invented ice cream?\n a.New Zealand b.United States c.China"#China
  l = "What was the first toy to be advertised on television?\n a.Barbie b.Mr. Potato Head c.Slingers"#Mr. Potato Head
  m = "Who created Sherlock Holmes?\n a.F. Scott Fitzgerald b.Ernest Himingway c.Arthur Conan Doyle"#Arthur Conan Doyle
  n = "Iceland diverted roads to avoid disturbing communities of what?\n a.Elves b.Penguins c.Icelandic Sheep"#Elves
  o = "Which member of the Beatles married Yoko Ono?\n a.Paul McCartney b.John Lennon c.George Harrison"#John Lennon
  p = "How many colors are there in the rainbow?\n a.6 b.8 c.7"#seven
  q = "In the state of Georgia, it’s illegal to eat what with a fork?\n a.Burgers b.Fried chiken c.Pizza"#Fried chicken
  r = "What is Earth's largest continent?\n a.Asia b.Russia c.Canada"#Asia
  s = "Area 51 is located in which state?\n a.Colorado b.Arizona c.Nevada"#Nevada
  t = "What is a duel between three people called?\n a.Triuel b.Truel c.Trupel"# a Truel
  u = "Which country borders 14 nations and crosses 8 time zones?\n a.Russia b.Asia c.not possible"#Russia
  v = "How many hearts does an octopus have?\n a.4 b.8 c.3"#3
  w = "The unicorn is the national animal of which country?\n a.Iceland b.Scotland c.Germany"#Scotland
  x = "A group of ravens is known as?\n a.Herd b.Unkindness c.Cluster"#Unkindness



  list2 = ["a", "b", "c", "b"]
  
  choices = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x]  

  choose = random.choice(choices)
  print(choose)
  bot = random.choice(list2)


  if choose == a:
    player = input("Your answer: ")
    if player == "b":
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Good job that was {Fore.GREEN}right{text}!\n")
      if bot == "b":
        print(f"Bot got it {Fore.GREEN}right{text}!\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    else:
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Oh no that was {Fore.RED}wrong{text}!\n")
      if bot == "b":
        print(f"Bot got it {Fore.GREEN}right!{text}\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    print("Another question?\nOptions: 'yes' 'no' ")
    again = input("Your answer: ")
    if again == "yes":
      print()
      print(beat_the_bot())
    if again == "no":
      print()
      print("What would you like to do?\n")
      print(user_input())
    else:
      print("Sorry didn't understand! Type in 'yes' or 'no' ")
      again = input("Your answer: ")


  if choose == b:
    player = input("Your answer: ")
    if player == "c":
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Good job that was {Fore.GREEN}right{text}!\n")
      if bot == "c":
        print(f"Bot got it {Fore.GREEN}right{text}!\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    else:
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Oh no that was {Fore.RED}wrong{text}!\n")
      if bot == "b":
        print(f"Bot got it {Fore.GREEN}right!{text}\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    print("Another question?\nOptions: 'yes' 'no' ")
    again = input("Your answer: ")
    if again == "yes":
      print()
      print(beat_the_bot())
    if again == "no":
      print()
      print("What would you like to do?\n")
      print(user_input())
    else:
      print("Sorry didn't understand! Type in 'yes' or 'no' ")
      again = input("Your answer: ")

  if choose == c:
    player = input("Your answer: ")
    if player == "a":
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Good job that was {Fore.GREEN}right{text}!\n")
      if bot == "a":
        print(f"Bot got it {Fore.GREEN}right{text}!\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    else:
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Oh no that was {Fore.RED}wrong{text}!\n")
      if bot == "b":
        print(f"Bot got it {Fore.GREEN}right!{text}\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    print("Another question?\nOptions: 'yes' 'no' ")
    again = input("Your answer: ")
    if again == "yes":
      print()
      print(beat_the_bot())
    if again == "no":
      print()
      print("What would you like to do?\n")
      print(user_input())
    else:
      print("Sorry didn't understand! Type in 'yes' or 'no' ")
      again = input("Your answer: ")

  if choose == d:
    player = input("Your answer: ")
    if player == "b":
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Good job that was {Fore.GREEN}right{text}!\n")
      if bot == "b":
        print(f"Bot got it {Fore.GREEN}right{text}!\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    else:
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Oh no that was {Fore.RED}wrong{text}!\n")
      if bot == "b":
        print(f"Bot got it {Fore.GREEN}right!{text}\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    print("Another question?\nOptions: 'yes' 'no' ")
    again = input("Your answer: ")
    if again == "yes":
      print()
      print(beat_the_bot())
    if again == "no":
      print()
      print("What would you like to do?\n")
      print(user_input())
    else:
      print("Sorry didn't understand! Type in 'yes' or 'no' ")
      again = input("Your answer: ")

  if choose == e:
    player = input("Your answer: ")
    if player == "a":
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Good job that was {Fore.GREEN}right{text}!\n")
      if bot == "a":
        print(f"Bot got it {Fore.GREEN}right{text}!\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    else:
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Oh no that was {Fore.RED}wrong{text}!\n")
      if bot == "b":
        print(f"Bot got it {Fore.GREEN}right!{text}\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    print("Another question?\nOptions: 'yes' 'no' ")
    again = input("Your answer: ")
    if again == "yes":
      print()
      print(beat_the_bot())
    if again == "no":
      print()
      print("What would you like to do?\n")
      print(user_input())
    else:
      print("Sorry didn't understand! Type in 'yes' or 'no' ")
      again = input("Your answer: ")

  if choose == f:
    player = input("Your answer: ")
    if player == "b":
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Good job that was {Fore.GREEN}right{text}!\n")
      if bot == "b":
        print(f"Bot got it {Fore.GREEN}right{text}!\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    else:
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Oh no that was {Fore.RED}wrong{text}!\n")
      if bot == "b":
        print(f"Bot got it {Fore.GREEN}right!{text}\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    print("Another question?\nOptions: 'yes' 'no' ")
    again = input("Your answer: ")
    if again == "yes":
      print()
      print(beat_the_bot())
    if again == "no":
      print()
      print("What would you like to do?\n")
      print(user_input())
    else:
      print("Sorry didn't understand! Type in 'yes' or 'no' ")
      again = input("Your answer: ")

  if choose == g:
    player = input("Your answer: ")
    if player == "c":
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Good job that was {Fore.GREEN}right{text}!\n")
      if bot == "c":
        print(f"Bot got it {Fore.GREEN}right{text}!\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    else:
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Oh no that was {Fore.RED}wrong{text}!\n")
      if bot == "b":
        print(f"Bot got it {Fore.GREEN}right!{text}\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    print("Another question?\nOptions: 'yes' 'no' ")
    again = input("Your answer: ")
    if again == "yes":
      print()
      print(beat_the_bot())
    if again == "no":
      print()
      print("What would you like to do?\n")
      print(user_input())
    else:
      print("Sorry didn't understand! Type in 'yes' or 'no' ")
      again = input("Your answer: ")

  if choose == h:
    player = input("Your answer: ")
    if player == "a":
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Good job that was {Fore.GREEN}right{text}!\n")
      if bot == "a":
        print(f"Bot got it {Fore.GREEN}right{text}!\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    else:
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Oh no that was {Fore.RED}wrong{text}!\n")
      if bot == "b":
        print(f"Bot got it {Fore.GREEN}right!{text}\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    print("Another question?\nOptions: 'yes' 'no' ")
    again = input("Your answer: ")
    if again == "yes":
      print()
      print(beat_the_bot())
    if again == "no":
      print()
      print("What would you like to do?\n")
      print(user_input())
    else:
      print("Sorry didn't understand! Type in 'yes' or 'no' ")
      again = input("Your answer: ")

  if choose == i:
    player = input("Your answer: ")
    if player == "b":
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Good job that was {Fore.GREEN}right{text}!\n")
      if bot == "b":
        print(f"Bot got it {Fore.GREEN}right{text}!\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    else:
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Oh no that was {Fore.RED}wrong{text}!\n")
      if bot == "b":
        print(f"Bot got it {Fore.GREEN}right!{text}\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    print("Another question?\nOptions: 'yes' 'no' ")
    again = input("Your answer: ")
    if again == "yes":
      print()
      print(beat_the_bot())
    if again == "no":
      print()
      print("What would you like to do?\n")
      print(user_input())
    else:
      print("Sorry didn't understand! Type in 'yes' or 'no' ")
      again = input("Your answer: ")

  if choose == j:
    player = input("Your answer: ")
    if player == "b":
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Good job that was {Fore.GREEN}right{text}!\n")
      if bot == "b":
        print(f"Bot got it {Fore.GREEN}right{text}!\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    else:
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Oh no that was {Fore.RED}wrong{text}!\n")
      if bot == "b":
        print(f"Bot got it {Fore.GREEN}right!{text}\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    print("Another question?\nOptions: 'yes' 'no' ")
    again = input("Your answer: ")
    if again == "yes":
      print()
      print(beat_the_bot())
    if again == "no":
      print()
      print("What would you like to do?\n")
      print(user_input())
    else:
      print("Sorry didn't understand! Type in 'yes' or 'no' ")
      again = input("Your answer: ")

  if choose == k:
    player = input("Your answer: ")
    if player == "c":
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Good job that was {Fore.GREEN}right{text}!\n")
      if bot == "c":
        print(f"Bot got it {Fore.GREEN}right{text}!\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    else:
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Oh no that was {Fore.RED}wrong{text}!\n")
      if bot == "b":
        print(f"Bot got it {Fore.GREEN}right!{text}\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    print("Another question?\nOptions: 'yes' 'no' ")
    again = input("Your answer: ")
    if again == "yes":
      print()
      print(beat_the_bot())
    if again == "no":
      print()
      print("What would you like to do?\n")
      print(user_input())
    else:
      print("Sorry didn't understand! Type in 'yes' or 'no' ")
      again = input("Your answer: ")

  if choose == l:
    player = input("Your answer: ")
    if player == "b":
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Good job that was {Fore.GREEN}right{text}!\n")
      if bot == "b":
        print(f"Bot got it {Fore.GREEN}right{text}!\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    else:
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Oh no that was {Fore.RED}wrong{text}!\n")
      if bot == "b":
        print(f"Bot got it {Fore.GREEN}right!{text}\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    print("Another question?\nOptions: 'yes' 'no' ")
    again = input("Your answer: ")
    if again == "yes":
      print()
      print(beat_the_bot())
    if again == "no":
      print()
      print("What would you like to do?\n")
      print(user_input())
    else:
      print("Sorry didn't understand! Type in 'yes' or 'no' ")
      again = input("Your answer: ")

  if choose == m:
    player = input("Your answer: ")
    if player == "c":
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Good job that was {Fore.GREEN}right{text}!\n")
      if bot == "c":
        print(f"Bot got it {Fore.GREEN}right{text}!\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    else:
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Oh no that was {Fore.RED}wrong{text}!\n")
      if bot == "b":
        print(f"Bot got it {Fore.GREEN}right!{text}\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    print("Another question?\nOptions: 'yes' 'no' ")
    again = input("Your answer: ")
    if again == "yes":
      print()
      print(beat_the_bot())
    if again == "no":
      print()
      print("What would you like to do?\n")
      print(user_input())
    else:
      print("Sorry didn't understand! Type in 'yes' or 'no' ")
      again = input("Your answer: ")

  if choose == n:
    player = input("Your answer: ")
    if player == "a":
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Good job that was {Fore.GREEN}right{text}!\n")
      if bot == "a":
        print(f"Bot got it {Fore.GREEN}right{text}!\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    else:
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Oh no that was {Fore.RED}wrong{text}!\n")
      if bot == "b":
        print(f"Bot got it {Fore.GREEN}right!{text}\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    print("Another question?\nOptions: 'yes' 'no' ")
    again = input("Your answer: ")
    if again == "yes":
      print()
      print(beat_the_bot())
    if again == "no":
      print()
      print("What would you like to do?\n")
      print(user_input())
    else:
      print("Sorry didn't understand! Type in 'yes' or 'no' ")
      again = input("Your answer: ")

  if choose == o:
    player = input("Your answer: ")
    if player == "b":
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Good job that was {Fore.GREEN}right{text}!\n")
      if bot == "b":
        print(f"Bot got it {Fore.GREEN}right{text}!\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    else:
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Oh no that was {Fore.RED}wrong{text}!\n")
      if bot == "b":
        print(f"Bot got it {Fore.GREEN}right!{text}\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    print("Another question?\nOptions: 'yes' 'no' ")
    again = input("Your answer: ")
    if again == "yes":
      print()
      print(beat_the_bot())
    if again == "no":
      print()
      print("What would you like to do?\n")
      print(user_input())
    else:
      print("Sorry didn't understand! Type in 'yes' or 'no' ")
      again = input("Your answer: ")

  if choose == p:
    player = input("Your answer: ")
    if player == "c":
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Good job that was {Fore.GREEN}right{text}!\n")
      if bot == "c":
        print(f"Bot got it {Fore.GREEN}right{text}!\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    else:
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Oh no that was {Fore.RED}wrong{text}!\n")
      if bot == "b":
        print(f"Bot got it {Fore.GREEN}right!{text}\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    print("Another question?\nOptions: 'yes' 'no' ")
    again = input("Your answer: ")
    if again == "yes":
      print()
      print(beat_the_bot())
    if again == "no":
      print()
      print("What would you like to do?\n")
      print(user_input())
    else:
      print("Sorry didn't understand! Type in 'yes' or 'no' ")
      again = input("Your answer: ")

  if choose == q:
    player = input("Your answer: ")
    if player == "b":
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Good job that was {Fore.GREEN}right{text}!\n")
      if bot == "b":
        print(f"Bot got it {Fore.GREEN}right{text}!\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    else:
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Oh no that was {Fore.RED}wrong{text}!\n")
      if bot == "b":
        print(f"Bot got it {Fore.GREEN}right!{text}\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    print("Another question?\nOptions: 'yes' 'no' ")
    again = input("Your answer: ")
    if again == "yes":
      print()
      print(beat_the_bot())
    if again == "no":
      print()
      print("What would you like to do?\n")
      print(user_input())
    else:
      print("Sorry didn't understand! Type in 'yes' or 'no' ")
      again = input("Your answer: ")

  if choose == r:
    player = input("Your answer: ")
    if player == "a":
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Good job that was {Fore.GREEN}right{text}!\n")
      if bot == "a":
        print(f"Bot got it {Fore.GREEN}right{text}!\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    else:
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Oh no that was {Fore.RED}wrong{text}!\n")
      if bot == "b":
        print(f"Bot got it {Fore.GREEN}right!{text}\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    print("Another question?\nOptions: 'yes' 'no' ")
    again = input("Your answer: ")
    if again == "yes":
      print()
      print(beat_the_bot())
    if again == "no":
      print()
      print("What would you like to do?\n")
      print(user_input())
    else:
      print("Sorry didn't understand! Type in 'yes' or 'no' ")
      again = input("Your answer: ")

  if choose == s:
    player = input("Your answer: ")
    if player == "c":
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Good job that was {Fore.GREEN}right{text}!\n")
      if bot == "c":
        print(f"Bot got it {Fore.GREEN}right{text}!\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    else:
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Oh no that was {Fore.RED}wrong{text}!\n")
      if bot == "b":
        print(f"Bot got it {Fore.GREEN}right!{text}\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    print("Another question?\nOptions: 'yes' 'no' ")
    again = input("Your answer: ")
    if again == "yes":
      print()
      print(beat_the_bot())
    if again == "no":
      print()
      print("What would you like to do?\n")
      print(user_input())
    else:
      print("Sorry didn't understand! Type in 'yes' or 'no' ")
      again = input("Your answer: ")

  if choose == t:
    player = input("Your answer: ")
    if player == "b":
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Good job that was {Fore.GREEN}right{text}!\n")
      if bot == "b":
        print(f"Bot got it {Fore.GREEN}right{text}!\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    else:
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Oh no that was {Fore.RED}wrong{text}!\n")
      if bot == "b":
        print(f"Bot got it {Fore.GREEN}right!{text}\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    print("Another question?\nOptions: 'yes' 'no' ")
    again = input("Your answer: ")
    if again == "yes":
      print()
      print(beat_the_bot())
    if again == "no":
      print()
      print("What would you like to do?\n")
      print(user_input())
    else:
      print("Sorry didn't understand! Type in 'yes' or 'no' ")
      again = input("Your answer: ")

  if choose == u:
    player = input("Your answer: ")
    if player == "a":
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Good job that was {Fore.GREEN}right{text}!\n")
      if bot == "a":
        print(f"Bot got it {Fore.GREEN}right{text}!\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    else:
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Oh no that was {Fore.RED}wrong{text}!\n")
      if bot == "b":
        print(f"Bot got it {Fore.GREEN}right!{text}\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    print("Another question?\nOptions: 'yes' 'no' ")
    again = input("Your answer: ")
    if again == "yes":
      print()
      print(beat_the_bot())
    if again == "no":
      print()
      print("What would you like to do?\n")
      print(user_input())
    else:
      print("Sorry didn't understand! Type in 'yes' or 'no' ")
      again = input("Your answer: ")

  if choose == v:
    player = input("Your answer: ")
    if player == "c":
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Good job that was {Fore.GREEN}right{text}!\n")
      if bot == "c":
        print(f"Bot got it {Fore.GREEN}right{text}!\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    else:
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Oh no that was {Fore.RED}wrong{text}!\n")
      if bot == "b":
        print(f"Bot got it {Fore.GREEN}right!{text}\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    print("Another question?\nOptions: 'yes' 'no' ")
    again = input("Your answer: ")
    if again == "yes":
      print()
      print(beat_the_bot())
    if again == "no":
      print()
      print("What would you like to do?\n")
      print(user_input())
    else:
      print("Sorry didn't understand! Type in 'yes' or 'no' ")
      again = input("Your answer: ")

  if choose == w:
    player = input("Your answer: ")
    if player == "b":
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Good job that was {Fore.GREEN}right{text}!\n")
      if bot == "b":
        print(f"Bot got it {Fore.GREEN}right{text}!\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    else:
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Oh no that was {Fore.RED}wrong{text}!\n")
      if bot == "b":
        print(f"Bot got it {Fore.GREEN}right!{text}\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    print("Another question?\nOptions: 'yes' 'no' ")
    again = input("Your answer: ")
    if again == "yes":
      print()
      print(beat_the_bot())
    if again == "no":
      print()
      print("What would you like to do?\n")
      print(user_input())
    else:
      print("Sorry didn't understand! Type in 'yes' or 'no' ")
      again = input("Your answer: ")


  if choose == x:
    player = input("Your answer: ")
    if player == "b":
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Good job that was {Fore.GREEN}right{text}!\n")
      if bot == "b":
        print(f"Bot got it {Fore.GREEN}right{text}!\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    else:
      print(f"\nBot: OK! I choose...{bot}!\n")
      print(f"Oh no that was {Fore.RED}wrong{text}!\n")
      if bot == "b":
        print(f"Bot got it {Fore.GREEN}right!{text}\n")
      else:
        print(f"Bot got it {Fore.RED}wrong{text}!\n")
    print("Another question?\nOptions: 'yes' 'no' ")
    again = input("Your answer: ")
    if again == "yes":
      print()
      print(beat_the_bot())
    if again == "no":
      print()
      print("What would you like to do?\n")
      print(user_input())
    else:
      print("Sorry didn't understand! Type in 'yes' or 'no' ")
      again = input("Your answer: ")


print (user_input())