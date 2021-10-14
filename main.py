import colorama
from colorama import Fore, Style, Back
colorama.init()
import random
from wyr_questions import wyr_list
from btb_questions import btb_list

name = input("Hello! What's your name? \n???: ")
print()
print(f"That's a nice name! Do you have a favorite {Fore.RED}c{Fore.YELLOW}o{Fore.GREEN}l{Fore.BLUE}o{Fore.MAGENTA}r{Fore.RESET}?\nOptions:\n {Fore.MAGENTA}'purple',\n {Fore.RED}'red',\n {Fore.YELLOW}'yellow',\n {Fore.BLUE}'blue',\n {Fore.GREEN}'green'{Fore.RESET}")

color = input(f"{name}: ")
print()

if color.lower() == 'purple':
  text = Fore.MAGENTA
if color.lower() == 'red':
  text = Fore.RED
if color.lower() == 'yellow':
  text = Fore.YELLOW
if color.lower() == 'blue':
  text = Fore.BLUE
if color.lower() == 'green':
  text = Fore.GREEN

print(f"{Fore.RED}N{Fore.YELLOW}i{Fore.GREEN}c{Fore.BLUE}e {Fore.MAGENTA}c{Fore.BLUE}h{Fore.GREEN}o{Fore.YELLOW}i{Fore.RED}c{Fore.MAGENTA}e{Fore.RESET}! I like {text}{color}{Fore.RESET} too!\nShould I introduce myself now?\nHey there {name}! {Fore.RED}I'm C.B{Fore.RESET},  \ndesigned to entertain you! \nyou can type in:\n{Fore.YELLOW}'wyr'{Fore.RESET},\nor \n{Fore.GREEN}'beat the bot'{Fore.RESET}, \nType in: \n{Fore.CYAN}'info'{Fore.RESET} to learn about the different options! \nOr click the {Fore.MAGENTA}'x'{Fore.RESET} to leave the chat!\n")

def user_input():
    inputs = input(f"{name}:{text} ")
    
    if inputs.lower() == "beat the bot":
      print(beat_the_bot())
    if inputs.lower() == "wyr":
        print(wyr())
    if inputs.lower() ==  "info":
      print(information ())
    else:
      print (f"Sorry, I only understand simple answers, such as: \n{Fore.RESET}'wyr' 'beat the bot' 'info' {text}or{Fore.RESET} click the x{text} to leave the chat \n")
      print (user_input())   
     
 
def information():
    print(f"{Fore.RESET}Beat the bot{text} ----- A series of random questions which you and the bot must take turns answering \n{Fore.RESET}Wry{text} ----- Play 'would you rather'") 
    print(user_input())
  
#Would You Rather Function 
def wyr():

  #randomly picking questions from wyr_questions file
  question = random.choice(wyr_list)

  #displaying question and choices
  print(f"\n{Fore.RESET}{question}{text}" + "\n")
  print()
  print("'left' or 'right'\n")

  #allowing user's response
  input(f"{name}: ")

  #Randomlt picking a response
  list = ["Really?!", "Haha no way!", "Me too!", "That's crazy!!", "what are you thinking?!", "that was a tough question!"]
  response = random.choice(list)
  print()
  print(f"{Fore.RESET}{response}{text}")

  ###
  print("Would you like another question?\n 'yes' or 'no'")
  again = input(f"{name}: ")

  #Determining wether to continue or end the game
  if again.lower() == 'yes':
      print(wyr())
  if again.lower() == "no":
      print()
      print("What would you like to do?\n")
      print(user_input())
  else:
      print("Sorry didn't understand! Type in 'yes' or 'no' ")
      again = input(f"{name}: ")



#Beat the Bot Function
def beat_the_bot():

  #randomly selecting a question from btb_questions file 
  choose = random.choice(btb_list)
  print(choose)

    
  def abc(answer):
    #randomly selecting a response for the bot
    bot_list = ["a", "b", "c", "b"]
    bot = random.choice(bot_list)


    #deciding if bot response and user responses is correct
    if player == answer:
      print(f"\nBot: {Fore.WHITE}OK! I choose...{bot}{text}!\n")
      print(f"Good job that was {Fore.GREEN}right{text}!\n")
      if bot == answer:
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

    #Asking if the user wants to play another round
    print("Another question?\nOptions: 'yes' 'no' ")
    again = input("Your answer: ")
    if again.lower() == "yes":
      print()
      print(beat_the_bot())
    if again.lower() == "no":
      print()
      print("What would you like to do?\n")
      print(user_input())
    else:
      print("Sorry didn't understand! Type in 'yes' or 'no' ")
      again = input("Your answer: ")

#User's input nb


  #where the user answers the question     
  if choose == btb_list[0]:
    player = input("Your answer: ")
    #sending it to the function above
    print(abc("b"))

  if choose == btb_list[1]:
    player = input("Your answer: ")
    print(abc("c"))
 
  if choose == btb_list[2]:
    player = input("Your answer: ")
    print(abc("a"))
 
  if choose == btb_list[3]:
    player = input("Your answer: ")
    print(abc("b"))
 
  if choose == btb_list[4]:
    player = input("Your answer: ")
    print(abc("a"))
 
  if choose == btb_list[5]:
    player = input("Your answer: ")
    print(abc("b"))
 
  if choose == btb_list[6]:
    player = input("Your answer: ")
    print(abc("c"))
 
  if choose == btb_list[7]:
    player = input("Your answer: ")
    print(abc("a"))

  if choose == btb_list[8]:
    player = input("Your answer: ")
    print(abc("b"))
 
  if choose == btb_list[9]:
    player = input("Your answer: ")
    print(abc("b"))
 
  if choose == btb_list[10]:
    player = input("Your answer: ")
    print(abc("c"))
 
  if choose == btb_list[11]:
    player = input("Your answer: ")
    print(abc("b"))
    
  if choose == btb_list[12]:
    player = input("Your answer: ")
    print(abc("c"))
 
  if choose == btb_list[13]:
    player = input("Your answer: ")
    print(abc("a"))
 
  if choose == btb_list[14]:
    player = input("Your answer: ")
    print(abc("b"))
 
  if choose == btb_list[15]:
    player = input("Your answer: ")
    print(abc("c"))
 
  if choose == btb_list[16]:
    player = input("Your answer: ")
    print(abc("b"))
 
  if choose == btb_list[17]:
    player = input("Your answer: ")
    print(abc("a"))

  if choose == btb_list[18]:
    player = input("Your answer: ")
    print(abc("c"))

  if choose == btb_list[19]:
    player = input("Your answer: ")
    print(abc("b"))
 
  if choose == btb_list[20]:
    player = input("Your answer: ")
    print(abc("a"))
 
  if choose == btb_list[21]:
    player = input("Your answer: ")
    print(abc("c"))
 
  if choose == btb_list[22]:
    player = input("Your answer: ")
    print(abc("b"))
 
 
  if choose == btb_list[23]:
    player = input("Your answer: ")
    print(abc("b"))





print (user_input())