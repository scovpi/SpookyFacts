import os
import time
import sys
import random

rand_facts = ["There are at least 15 active serial killers.", "95% of the ocean remains unexplored.", "Rabies has a 100% kill rate.",
"Deer can sometimes suffer from 'Chronic Wasting Disease,' causing their bodies to rot.", "Doing bathsalts can drive a user to cannibalism."]

running = True

def clr():
    os.system("clear")

def main():
    global running
    global rand_facts

    try:
        while running:
            clr()
            print("SpookyFacts - A generator of random facts to scare you!")
            print("Developed by scovpi @ GitHub")
            print("=========================================================")
            print(random.choice(rand_facts))
            print("=========================================================")
            input("Press ENTER/RETURN to generate another fact. Press CTRL+C to exit...")
    except KeyboardInterrupt:
        print()
        sys.exit()

main()
