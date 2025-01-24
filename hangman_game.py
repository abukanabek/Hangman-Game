#player accumulates money by winning which he can spend on hints

import random, time
hard_word_list = [
    "adventure", "backyard", "balloon", "basketball", "beautiful", "bedroom", "birthday", "butterfly", "candlelight", "campfire",
    "challenge", "chocolate", "classroom", "clockwise", "computer", "creative", "daydream", "discovery", "distance", "doorbell",
    "elephant", "everywhere", "explosion", "fantastic", "friendship", "grandfather", "grateful", "happiness", "helicopter", "homework",
    "invisible", "jacket", "jewelry", "joyful", "keyboard", "landscape", "language", "laughter", "lifetime", "lightning",
    "motorcycle", "mountains", "mystery", "necklace", "notebook", "oceanic", "optimistic", "painting", "password", "peaceful",
    "pineapple", "playground", "positive", "powerful", "princess", "rainstorm", "sandcastle", "scientist", "shoulders", "snowflake",
    "storybook", "strawberry", "sunflower", "sunshine", "telephone", "together", "tomorrow", "treasure", "umbrella", "universe",
    "vacation", "volleyball", "waterfall", "whisper", "wildflower", "wonderful", "workshop", "yesterday", "zigzagging", "fireworks",
    "adventure", "blossoming", "breakfast", "carousel", "collection", "delicious", "diamonds", "enchanted", "gentleman", "horizon",
    "jellyfish", "landslide", "magazine", "nostalgia", "playhouse", "president", "railroad", "secretive", "silhouette", "volcano"
]
easy_word_list = [
    "apple", "banana", "grape", "orange", "peach", "cherry", "melon", "berry", "lemon", "mango",
    "house", "table", "chair", "couch", "floor", "ceiling", "window", "door", "kitchen", "garden",
    "happy", "sad", "angry", "excited", "scared", "tired", "brave", "calm", "proud", "kind",
    "blue", "green", "red", "yellow", "black", "white", "orange", "purple", "pink", "brown",
    "dog", "cat", "fish", "bird", "horse", "frog", "lion", "bear", "zebra", "whale",
    "ocean", "river", "lake", "mountain", "valley", "forest", "desert", "island", "beach", "jungle",
    "sun", "moon", "star", "cloud", "rain", "snow", "storm", "wind", "light", "shade",
    "jump", "run", "walk", "talk", "laugh", "cry", "sleep", "eat", "drink", "play",
    "school", "teacher", "student", "class", "book", "pen", "pencil", "desk", "paper", "board",
    "car", "bus", "bike", "plane", "train", "boat", "truck", "taxi", "ship", "rocket"
]
dead_man = '''⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣶⣾⣿⣿⣷⣶⣶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⡾⠛⠉⠉⠀⠀⠀⠀⠀⠉⠉⠛⠻⠿⣿⣿⣶⣤⡀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣶⣄⠀⠀⠀
⠀⠀⣰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡄⠀⠀⠀⠀⠙⢿⣿⣧⠀⠀
⠀⣰⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣶⣾⣿⣧⣄⠀⠀⠀⠀⠀⠹⣿⣷⠀
⢠⡿⠀⠀⠀⠀⡀⣠⡤⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠛⠉⠀⠀⠀⠀⠀⠀⢹⣿⡇
⣼⡇⠀⠀⠀⣼⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿
⣿⡇⠀⠀⣰⠟⢿⣿⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿
⣿⣷⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⣸⡏
⢹⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⠿⠿⠿⣿⣿⣿⠇⠀⠀⠀⢠⡿⠀
⠈⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⣴⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⠁⠀
⠀⠘⣿⣿⣦⡀⠀⠀⠀⠀⠀⣼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠀⠀⠀
⠀⠀⠈⠻⣿⣿⣷⣄⡀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⠟⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠙⠿⣿⣿⣷⣦⣤⣄⣀⣀⣀⣀⣀⣤⣴⣾⠿⠋⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⠿⠿⣿⣿⣿⠿⠿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'''

def get_word_hard():
    return random.choice(hard_word_list).upper()

def get_word_easy():
    return random.choice(easy_word_list).upper()

def display_hangman(tries):
    stages = [  # state 6
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # state 5
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # state 4
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # state 3
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # state 2
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # state 1
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # state 0
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]    

def play(word):
    word_completion = '_'*len(word)
    guessed = False
    letters_g = []
    letters_w = []
    letters_used = []
    for i in range(len(word)):
        if not word[i] in letters_w:
            letters_w.append(word[i])
    tries = 6
    
    print()
    print('Your word has been selected. You can start, but use your 6 tries wisely...')
    print('P.S: If you type a word with the same length as the secret word, it will be considered a guess')
    print(display_hangman(tries))
    print()
    print(*word_completion, sep=' ')
    while guessed == False and tries>0:
        l = input()
        if len(l) == len(word):
            if l.upper() == word.upper():
                guessed = True
                break
            else:
                tries -= 1
                if tries==0:
                    break
                else:
                    print(display_hangman(tries))
                    print(f'Wrong guess! You have {tries} tries left')
                    continue
        while len(l)!=1:
            print(f'Did you mean {l[0]}? Retype please.')
            l = input()
        l = l.upper()
        
        tries-=1
        if not l in word:
            if l in letters_used:
                tries+=1
                print(display_hangman(tries))
                print(f'Already guessed this letter! You still have {tries} tries left')
                print(*word_completion, sep=' ')
            else:
                if tries!=0:
                    print(display_hangman(tries))
                    print(f'Wrong letter! You have {tries} tries left.')
                    print(*word_completion, sep=' ')
                else:
                    break
        else:
            if l in letters_used:
                tries+=1
                print(display_hangman(tries))
                print(f'Already guessed this letter! You still have {tries} tries left')
                print(*word_completion, sep=' ')
            else:
                tries += 1
                print(display_hangman(tries))
                print(f'Great job! You still have {tries} tries left')
                word_completion = ''
                letters_g.append(l)
                for i in range(len(word)):
                    if word[i] in letters_g:
                        word_completion += word[i]
                    else:
                        word_completion += '_'
                print(*word_completion, sep=' ')
        if len(letters_g)==len(letters_w):
            guessed = True
            break
        letters_used.append(l.lower())
        letters_used.append(l.upper())
    if guessed == True:
        print()
        print("You win!!! We're so proud of you!")
        print('The word was:', word)
    else:
        print()
        print('He died...')
        time.sleep(2)
        print('Because of you! How dare you!')
        print(dead_man)
        print('The word was:', word)
        
def user_interaction(first):
    if first:
        print("Do you want to play the game of hangman? (yes/no)")
    else:
        print("Do you want to play another game of hangman? (yes/no)")
    a = input().lower()
    while not (a.startswith('y') or a.startswith('n')):
        print("Incorrect input. Try again.")
        a = input().lower()
    if a.startswith('y'):
        print("Okay, type difficulty: (hard/easy)")
        b = input().lower()
        while not(b.startswith('h') or b.startswith('e')):
            print('Incorrect input. Try again.')
            b = input().lower()
        print('Great! Just wait a second...')
        time.sleep(2)
        if b.startswith('h'):
            play(get_word_hard())
        else:
            play(get_word_easy())
        
        return True
    else:
        print('Come back anytime!')
        return False


a = user_interaction(True)
while a==True:
    a = user_interaction(False)