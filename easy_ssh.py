##################################################################################
#  ©2017 Synthx                                                                  #
#  You may not redistribute as yours unless you have written consent from Synthx #
#  Twitter: @_synthx                                                             #
#  Email: synthx@protonmail.com or synthx01@gmail.com                            #
##################################################################################

import readline # arrow keys
import os # This imports your OS.
exit = False
ssh = ['ssh', 'SSH']
color = {
    'RED'             : '\033[1;91m',
    'UNDERLINE_PURPLE' : '\033[4;34m',
    'GREEN'           : '\033[1;92m',
    'YELLOW'          : '\033[1;33m',
    'CYAN'            : '\033[0;36m',
    'PURPLE'            : '\033[0;34m',
    'MAGENTA'         : '\033[0;35m',
    'DEFAULT'         : '\033[0m',
    'TWITTER_BLUE'            : '\033[38;5;33m',
}
exitSentence = color['RED'] + '[Now Exiting!] ' + color['DEFAULT'] + 'Easy SSH\n'
credits = '©2017 Synthx\n' + color['TWITTER_BLUE'] + 'Twitter: @_Synthx' + color['DEFAULT'] + '\n@danbatiste\n@NyteLife26'
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
''' + color['DEFAULT'] + '''                        +-----------------------+\n                        |  Created by ''' + color['TWITTER_BLUE'] + '''@_Synthx''' + color['DEFAULT'] + '''  |\n                        +-----------------------+
'''
os.system('clear')
print(header + 'Type "help" to begin!')
def Main():
	global exit
	mainInput = input(color['RED'] + 'Easy SSH> ' + color['DEFAULT'])
	if mainInput.lower() == 'help':
		os.system('clear')
		print(printHelp)
		Main()
	elif mainInput == '':
		Main()
	elif mainInput.lower() == 'exit':
		os.system('clear')
		print(exitSentence)
		exit = True
	elif 'ssh' in mainInput or 'SSH' in mainInput:
		os.system('clear')
		print(header + 'Enter IP of device you would like to SSH into. (e.x. 100.234.857.85)')
		sshStart()
	elif mainInput.lower() == 'info':
		os.system('clear')
		print(credits)
		Main()
	elif mainInput.lower() == 'clear':
		os.system('clear')
		print(header)
		Main()
	else:
		print(color['RED'] + '[ERROR] COMMAND "' + mainInput + '" NOT FOUND\n' + color['DEFAULT'] + 'PLEASE USE A PROPER COMMAND!\n')
		Main()
def sshStart():
	global exit
	mainInputSSH = input(color['RED'] + 'IP> ' + color['DEFAULT'])
	if mainInputSSH.lower() == '':
		sshStart()
	elif mainInputSSH.lower() == 'cancel':
		os.system('clear')
		print(header + 'Type "help" to begin!')
		Main()
	else:
		os.system('clear')
		print(header + 'Please specify what user to login as!')
		sshUser(mainInputSSH)
def sshUser(SSH_IP):
	global exit
	mainInputUser = input(color['RED'] + 'User> ' + color['DEFAULT'])
	if mainInputUser.lower() == '':
		sshUser(SSH_IP)
	elif mainInputUser.lower() == 'cancel':
		os.system('clear')
		print(header + 'Type "help" to begin!')
		Main()
	else:
		os.system('clear;' + 'ssh ' + mainInputUser + '@' + SSH_IP)
		print(header)
		Main()
while exit == False:
    Main()





