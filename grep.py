import fileinput
import re
import sys
import os
import flags as fg
import hlp

# Functions ##############################################################################################################################################

#Checks if basic arguments are correct
def checkSyntax():
	if(len(sys.argv)<2):
		sys.exit(hlp.notEnoughArgs() + hlp.fullHelp())

#Prints colored text
def printC(line,color, end=''):
	print(colored(line, color),end=end,flush=True)

#Iterates thru a string 
def grep(data):
	#Splits data by phrase, paragraph or gets the entire chunk
	for result in re.finditer(blockMatch, data):
		block = data[result.start():result.end()]

		#For each match prints the text from overture till the match, then the match, overture then gets set to the end of the match.
		overture = 0
		finale = len(block)
		for result in re.finditer(match, block):
			start = result.start()
			end = result.end()
			if(block[overture] == ' '): #Removes initial space if it has one (looks better when printed)
				overture += 1
			print(block[overture:start],end='')
			printC(block[start:end],'red')
			overture = end
		print(block[overture:finale],end='\n',flush=True)

# Checks #################################################################################################################################################

#Checks for windows system
if (os.name == 'nt'):
	from colorama import init
	init()
from termcolor import colored

#Checks for correct syntax
checkSyntax()

# Flags ##################################################################################################################################################

blockFlag = ''		#If a result blocks is a:	-f phrase	-p paragraph			Default: everything
infoFlag = ''		#Additional info:			-l line		-w words				Default: no info
readFlag = ''		#How to read input:			-F file		-S stdin after EOF		Default: stdin, each line

fg.argv = sys.argv[2:]
blockFlag = fg.getFlags('-f','-p')
infoFlag = fg.getFlags('-l','-w')
readFlag = fg.getFlags('-F','-S')

filePaths = fg.getFiles()

# Syntax #################################################################################################################################################



# Match ##################################################################################################################################################

match = sys.argv[1] if (len(sys.argv) >= 2) else ''

if (blockFlag == '-f'):
	blockMatch = r'[^\.:!?]*' + match + r'.*?(\.\.\.|[\.:!?])'		#matches all phrases with match
elif(blockFlag == '-p'):
	blockMatch = r'[^\n]*' + match + r'[^\n]*'						#matches all paragraphs with match
else:
	blockMatch = r'(.|\n)*' + match + r'(.|\n)*'					#matches all text with the match

# Main ###################################################################################################################################################

if (readFlag == '-F'):							# -F data is the file contents
	for filePath in filePaths:
		try:
			with open(filePath, 'r') as file:
				data = file.read()
				grep(data)
		except:
			pass
elif(readFlag == '-S'):							# -S data is all the stdin content until EOF
	for line in sys.stdin.readlines():
		data += line
	grep(data)
else:											# each line is parsed thru grep at a time
	for line in sys.stdin:
		grep(line)