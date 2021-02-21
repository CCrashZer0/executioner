import random
import pyfiglet

def titleScreen():
    font = random.choice(pyfiglet.FigletFont.getFonts())
    pyfiglet.print_figlet("Executioner",font)
