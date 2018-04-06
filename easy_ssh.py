# -*- coding: utf-8 -*-

##################################################################################
#  ©2017 Synthx                                                                  #
#  You may not redistribute as yours unless you have written consent from Synthx #
#  Twitter: @_synthx                                                             #
#  Email: synthx@protonmail.com or synthx01@gmail.com                            #
##################################################################################

import os           # This imports the OS module.
if os.name != "nt": # readline is not a thing on Windows
	import readline # arrow keys
import subprocess   # No more spawning a new shell.

alias = {"cancel": ["cancel", "back", "return"], "help": ["help", "?", "/help"], "quit": ["exit", "stop", "quit"]} # Command aliases

def clear():
	if os.name == "nt":
		subprocess.call("cls", shell=True) # CLS in Windows actually clears, not print newlines
	else:
		print("\n" * 80)

exit = False
color = {
	'RED'             : '\033[1;91m',
	'UNDERLINE_PURPLE': '\033[4;34m',
	'GREEN'           : '\033[1;92m',
	'YELLOW'          : '\033[1;33m',
	'CYAN'            : '\033[0;36m',
	'PURPLE'          : '\033[0;34m',
	'MAGENTA'         : '\033[0;35m',
	'DEFAULT'         : '\033[0m',
	'TWITTER_BLUE'    : '\033[38;5;33m',
}
exitSentence = color['RED'] + '[Now Exiting!] ' + color['DEFAULT'] + 'Easy SSH\n'
credits = '©2017 Synthx\n' + color['TWITTER_BLUE'] + 'Twitter: @_Synthx' + color['DEFAULT'] + '\n@danbatiste\n@Nytelife26'
printHelp = color['PURPLE'] + '''
+-------+----------------------------+
| help  | Prints this dialog         |
+-------+----------------------------+
| SSH   | Will begin ssh selection   |
+-------+----------------------------+
| clear | Clears the screen          |
+-------+----------------------------+
| exit  | Exits Easy SSH :/          |
+-------+----------------------------+
| info  | Shows credits for Easy SSH |
+-------+----------------------------+
'''
header = color['PURPLE'] + '''
                  _____                  _____ _____ _   _ 
                 |  ___|                /  ___/  ___| | | |
                 | |__  __ _ ___ _   _  \ `--.\ `--.| |_| |
                 |  __|/ _` / __| | | |  `--. \`--. \  _  |
                 | |__| (_| \__ \ |_| | /\__/ /\__/ / | | |
                 \____/\__,_|___/\__, | \____/\____/\_| |_/
                                  __/ |
                                  |___/
''' + color['DEFAULT'] + '''                        +-----------------------+\n	                       |  Created by ''' + color['TWITTER_BLUE'] + '''@_Synthx''' + color['DEFAULT'] + '''  |\n	                        +-----------------------+'''
clear()
print(header + 'Type "help" to begin!')
def Main():
	global exit
	mainInput = ""
	while not mainInput: # checking a string as bool returns False if the string is "", so mainInput == "" can just be replaced with boolean mainInput
		mainInput = input(color['RED'] + 'Easy SSH> ' + color['DEFAULT']).lower() # .lower'd automatically for efficiency
	if mainInput in alias["help"]:
		clear()
		print(printHelp)
		Main()
	elif mainInput in alias["quit"]: # changed to accept multiple inputs
		clear()
		print(exitSentence)
		exit = True
	elif 'ssh' in mainInput:
		clear()
		print(header + 'Enter IP of device you would like to SSH into. (e.x. 100.234.857.85)')
		sshStart()
	elif mainInput == 'info':
		clear()
		print(credits)
		Main()
	elif mainInput == 'clear':
		clear()
		print(header)
		Main()
	else:
		print(color['RED'] + '[ERROR] COMMAND "' + mainInput + '" NOT FOUND\n' + color['DEFAULT'] + 'PLEASE USE A PROPER COMMAND!\n')
		Main()
def sshStart():
	global exit
	mainInputSSH = ""
	while not mainInputSSH:
		mainInputSSH = input(color['RED'] + 'IP> ' + color['DEFAULT']).lower()
	if mainInputSSH in alias["cancel"]:
		clear()
		print(header + 'Type "help" to begin!')
		Main()
	else:
		clear()
		print(header + 'Please specify what IP to connect to!')
		sshUser(mainInputSSH)
def sshUser(SSH_IP):
	global exit
	mainInputUser = ""
	while not mainInputUser:
		mainInputUser = input(color['RED'] + 'User> ' + color['DEFAULT']).lower()
	if mainInputUser in alias["cancel"]:
		clear()
		print(header + 'Type "help" to begin!')
		Main()
	else:
		clear()
		subprocess.call('ssh {}@{}'.format(mainInputUser, SSH_IP))
		print(header)
		Main()
if __name__ == "__main__": # Check if we're being run normally or imported
	while not exit:
		Main()
