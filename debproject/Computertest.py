import subprocess
import time
import random
subprocess.run(['sudo', 'apt-get', 'install', 'pygame'])
subprocess.run(['pip', 'install', 'pygame'])
import pygame

pygame.init()

def speak(text):
    print(text)
    subprocess.run(['espeak-ng', text])

    
print("You need espeak-ng for this. if you do not have espeak-ng, please type lowercase n unless you have espeak-ng, then type lowercase y")
espeaknginstalled = input('Do you have espeak-ng? [y/n]: ')
if espeaknginstalled == "n":
    subprocess.run(['sudo', 'apt-get', 'install', 'espeak-ng'])
elif espeaknginstalled == "y":
    speak("This is a test.")


speak('Hello, I am a computer. I have a built in text-to-speech system installed.')
speak('I will now list some things to do')
time.sleep(2)
print('Games')
print('sudo nano')
print('Command line')
speak('Done. Please type lowercase g for games, lowercase s for text editor, and lowercase c for command line. one more thing, lowercase m for music')
while True:
    speak('Please type lowercase g for games, lowercase s for text editor, and lowercase c for command line. one more thing, lowercase m for music.')
    action = input('pick >>')
    if action == 'g':
        randomgame = random.randint(1, 2)
        print('Game 1: Guess the number: Easy 1-50')
        print('Game 2: Guess the number: Hard 100-1,000')
        speak('Lets play game number...')
        if randomgame == 1:
            speak('1. Lets play game number 1.')
            speak('Think of a number, and I will guess it')
            speak('5 chances.')
            speak('I will now guess.')
            randomnumber = random.randint(1, 50)
            randomnumber2 = random.randint(1, 50)
            randomnumber3 = random.randint(1, 50)
            randomnumber4 = random.randint(1, 50)
            randomnumber5 = random.randint(1, 50)
            speak(f"I guess number {randomnumber}. Is this correct?")
            guess = input('>>')
            if guess == 'y':
                speak('Yay, I did it! That was fun! I am going to guess again, yet I am staying at the amount of chances I have, unless of course, this is my last chance.')
            if guess == 'n':
                speak('Well then.')
            speak(f"I guess number {randomnumber2}. Is this correct?")
            guess = input('>>')
            if guess == 'y':
                speak('Yay, I did it! That was fun! I am going to guess again, yet I am staying at the amount of chances I have, unless of course, this is my last chance.')
            if guess == 'n':
                speak('Well then.')
            speak(f"I guess number {randomnumber3}. Is this correct?")
            guess = input('>>')
            if guess == 'y':
                speak('Yay, I did it! That was fun! I am going to guess again, yet I am staying at the amount of chances I have, unless of course, this is my last chance.')
            if guess == 'n':
                speak('Well then.')
            speak(f"I guess number {randomnumber4}. Is this correct?")
            guess = input('>>')
            if guess == 'y':
                speak('Yay, I did it! That was fun! I am going to guess again, yet I am staying at the amount of chances I have, unless of course, this is my last chance.')
            if guess == 'n':
                speak('Well then.')
            speak(f"I guess number {randomnumber5}. Is this correct?")
            guess = input('>>')
            if guess == 'y':
                speak('Yay, I did it! That was fun! I am going to guess again, yet I am staying at the amount of chances I have, unless of course, this is my last chance.')
            if guess == 'n':
                speak('Well then I lost.')
        if randomgame == 2:
            speak('2, lets play game number 2.')
            speak('think of a number between 1-1000.')
            randomnumber = random.randint(1, 1000)
            randomnumber2 = random.randint(1, 1000)
            randomnumber3 = random.randint(1, 1000)
            randomnumber4 = random.randint(1, 1000)
            randomnumber5 = random.randint(1, 1000)
            speak(f"I guess number {randomnumber}. Is this correct?")
            guess = input('>>')
            if guess == 'y':
                speak('Yay, I did it! That was fun! I am going to guess again, yet I am staying at the amount of chances I have, unless of course, this is my last chance.')
            if guess == 'n':
                speak('Well then.')
            speak(f"I guess number {randomnumber2}. Is this correct?")
            guess = input('>>')
            if guess == 'y':
                speak('Yay, I did it! That was fun! I am going to guess again, yet I am staying at the amount of chances I have, unless of course, this is my last chance.')
            if guess == 'n':
                speak('Well then.')
            speak(f"I guess number {randomnumber3}. Is this correct?")
            guess = input('>>')
            if guess == 'y':
                speak('Yay, I did it! That was fun! I am going to guess again, yet I am staying at the amount of chances I have, unless of course, this is my last chance.')
            if guess == 'n':
                speak('Well then.')
            speak(f"I guess number {randomnumber4}. Is this correct?")
            guess = input('>>')
            if guess == 'y':
                speak('Yay, I did it! That was fun! I am going to guess again, yet I am staying at the amount of chances I have, unless of course, this is my last chance.')
            if guess == 'n':
                speak('Well then.')
            speak(f"I guess number {randomnumber5}. Is this correct?")
            guess = input('>>')
            if guess == 'y':
                speak('Yay, I did it! That was fun! I am going to guess again, yet I am staying at the amount of chances I have, unless of course, this is my last chance.')
            if guess == 'n':
                speak('Well then I lost.')
    if action == "s":
        subprocess.run(['sudo', 'nano'])
    if action == "c":
        speak('Before entering, to exit, hold control then press C to exit. Commands are: speak (No args)')
        while True:
            line = input('>>')
            if line == 'speak':
                speaker = input('>>')
                speak(speaker)
    if action == "m":
        speak('Press 1 for red sun in the sky, 2 for never gonna give you up, 3 for everybody wants to rule the world, and 4 for smooth criminal.')
        song = input('1, 2, 3, or 4 >>')
        if song == "1":
            pygame.mixer.music.stop()
            pygame.mixer.music.load('Red sun in the sky.mp3')
            pygame.mixer.music.play()
        if song == "2":
            pygame.mixer.music.stop()
            pygame.mixer.music.load('jocofullinterview41.mp3')
            pygame.mixer.music.play()
        if song == "3":
            pygame.mixer.music.stop()
            pygame.mixer.music.load('EBWTRTW.mp3')
            pygame.mixer.music.play()
        if song == "4":
            pygame.mixer.music.stop()
            pygame.mixer.music.load('Smooth criminal.mp3')
            pygame.mixer.music.play()