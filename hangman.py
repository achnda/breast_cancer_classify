import random

chosen_word_list=[]
word_list=['apple','sausage','pancake','casserole','bagel','sandwich','cereal','omelet','toast','spam']
chosen_word=random.choice(word_list)
for k in chosen_word:
  chosen_word_list.append("_")
chosen_word2=list(chosen_word) #toast, t o a s t
n=2*len(chosen_word)
print(chosen_word)
mistakecount=0
allguess=[]
while True:
  print()
  print()
  cntr=0

  guess=input('GUESS A LETTER:').lower()
  allguess.append(guess)
  for i in allguess:
    if i==guess:
      cntr+=1
  if cntr>1:
    print("YOU GUESSED THIS LETTER BEFORE",end=" ")
  if guess not in chosen_word:
    print('YOUR GUESS IS NOT IN THE CHOSEN WORD. YOU LOSE A LIFE!')
    mistakecount+=1
    if mistakecount==1:
      print('''  +---+
  |   |
  O   |
      |
      |
      |
=========''')
    elif mistakecount==2:
      print('''  +---+
  |   |
  O   |
  |   |
      |
      |
=========''')
    elif mistakecount==3:
      print('''  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''')
    elif mistakecount==4:
      print('''  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''')
    elif mistakecount==5:
      print('''  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''')
    elif mistakecount>5:
      print('''  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''')
      print("UH-OH. YOU LOSE.")
      break
  else:
    print("YOU GUESSED",guess,"RIGHT!")
    for i in range(len(chosen_word2)):  
      if chosen_word2[i]==guess: 
        chosen_word2[i]='*'
    if(["*"]*len(chosen_word2) == chosen_word2):
      print("YOU GUESSED THE WORD RIGHT!")
      for i in chosen_word:
          print(i,end=" ")
      break
  

  for i in range(len(chosen_word2)): 
    if chosen_word2[i]=='*': 
      chosen_word_list[i]=chosen_word[i] 
  for i in chosen_word_list:
    print(i,end=" ")
   
