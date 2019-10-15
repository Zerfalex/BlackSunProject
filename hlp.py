#Explanations and error messages about how the program should be used

def fullHelp():
	return explanation() + usage()

def explanation():
	text =  'Program explanation:\n'
	text += 'grep searches the named input files (or standard input if no files are named) '
	text += 'for lines containing a match to the given pattern. '
	text += 'By default, grep highlights the matching text.\n'
	text += 'More options can be used depending on the situation.\n\n'
	return text

def usage():
	text =  'Program usage:\n'
	text += 'grep.py [PATTERN] [SEARCH OPTIONS] [OUTPUT OPTIONS]\n\n'
	text += '[PATTERN]	- A regular expression that will be searched.\n\n'
	text += '[SEARCH OPTIONS] - Seaches for pattern in stdin for each line if blank, else:\n'
	text += '    [-S]         - Seaches for pattern in stdin, but only after end of file.\n'
	text += '    [-F <files>] - Seaches for pattern in given files.\n\n'
	text += '[OUTPUT OPTIONS] - Seaches for pattern in stdin for each line if blank, else:\n'
	text += '    [-f]         - Outputs each phrase the pattern is found on.\n'
	text += '    [-p]         - Outputs each paragraph the pattern is found on.\n\n'

	return text

def notEnoughArgs():
	return 'Error: Need more arguments\n\n'