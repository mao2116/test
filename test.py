from pyfiglet import figlet_format
from termcolor import colored
import sys,time
x = 'mao2116'
x = figlet_format(x, 'slant')
x = colored(x, 'cyan')

def EH(z):
  for ww in z + '\n':
    sys.stdout.write(ww)
    sys.stdout.flush()
    time.sleep(0.01)
EH(x)
