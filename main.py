def intro():
  answer = input('Welcome to Mad Libs! Do you know the rules of this game? (y/n) ')
  if answer != 'y':
    print('''All good! From www.madlibslive.com: One player acts as the “reader" and asks the other players, who haven't seen the story, to fill in the blanks with adjectives, nouns, exclamations, colors, adjectives, and more. These words are inserted into the blanks and then the story is read aloud to hilarious results. There are no winners or losers, only laughter. In this game, you will be the player and the computer will be the reader.''')
  noun1 = input('Please enter a name. ')
  verb = input('Please enter a verb. ')
  adjective = input('Please enter a adjective. ')
  adverb = input('Please enter an adverb. ')
  verb2 = input('Please enter a verb ending in -ing. ')
  noun2 = input('Please enter a location. ')
  noun3 = input('Please enter a noun. ')
  adverb2 = input('Please enter an adverb. ')
  print("Generating story..."
  )
  print("On a quiet, sleepy day in the Cohon University Center,", noun1, "was spotted sitting at", noun2 + '.' + '\n')
  print("Then,", noun1, 'saw an opportunity. The', adjective, 'matchbox was just dangling there – so delightfully tempting. Just thinking about it made', noun1, verb, adverb + '...')
  print('\n')
  print('Before long, the entropy worker began to look rather', adverb2, 'at', noun1 + '.', 'He stared from', noun1 + "'s hand to the match, mouthing: NOOOOO!" + '\n')
  print('But it was too late. The fire was quickly spreading, and the', noun3, 'was', verb2 + '.' + '\n')
  print('Nevertheless, the hackathon was a success - disruption and chaos was truly the theme of the night as the judges fanned out the flames from their scoresheets.', noun1, 'was pronounced the winner as the sole survivor of the fire.')
  

  
  
intro()



