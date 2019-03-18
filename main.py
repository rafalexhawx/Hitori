#Python library imports
import os
try:
    import pygame
except ImportError:                  #Cecks to see if pygame is installed, otherwise it installs it
    os.system('pip install pygame')
    import pygame
from pygame.locals import *
import time

#Custom library imports
from generator import * #To generate numbers
