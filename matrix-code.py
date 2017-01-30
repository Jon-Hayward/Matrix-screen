import time
import termcolor
import colorama
import os
import sys
import random

colorama.init()

colors = ("green", "green", "green", "green", "green", "green", "grey")
attributes = ("bold", "underline", "blink", "reverse")

def get_color():
	global colors
	return colors[random.randint(0,len(colors)-1)]
	
def get_on_color():
	global colors
	return "on_" + colors[random.randint(0,len(colors)-1)]
	
def get_attributes():
	global attributes
	return attributes[random.randint(0,len(attributes)-1)]
	
for i in range(100**3): # 880):
	x = random.randint(0,6)
	the_char = chr(random.randint(33,126))
	if (x%6 == 0):
		print termcolor.colored(the_char, get_color(), get_on_color(), attrs=[get_attributes()]),
	elif (x%6 == 1):
		print termcolor.colored(the_char, get_color(), get_on_color()),
	elif (x%6 == 2):
		print termcolor.colored(the_char, get_color()),
	elif (x%6 == 4):
		print termcolor.colored(the_char, get_color(), attrs=[get_attributes()]),
	elif (x%5 == 5):
		print termcolor.colored(the_char, get_on_color(), attrs=[get_attributes()]),
	else:
		print the_char,
	
	sys.stdout.flush()
#	time.sleep(0.3)
