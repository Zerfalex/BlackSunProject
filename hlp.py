#Explanations and error messages about how the program should be used

def fullHelp():
	return explanation() + usage()

def explanation():
	text =  "Program explanation:\n"
	text += "grep searches the named input files (or standard input if no files are named) "
	text += "for lines containing a match to the given pattern. "
	text += "By default, grep highlights the matching text.\n"
	text += "More options can be used depending on the situation.\n\n"
	return text

def usage():
	text =  "Program usage:\n"
	text += "grep.py [PATTERN] [SEARCH OPTIONS] [OUTPUT OPTIONS]\n\n"
	text += "[PATTERN]    - A regular expression that will be searched.\n\n"
	text += "[SEARCH OPTIONS] - Seaches for pattern in stdin for each line if blank, else:\n"
	text += "    [-S]         - Seaches for pattern in stdin, but only after end of file.\n"
	text += "    [-F <files>] - Seaches for pattern in given files.\n\n"
	text += "[OUTPUT OPTIONS] - Outputs whole text with highlighted pattern if blank, else:\n"
	text += "    [-f]         - Outputs each phrase the pattern is found on.\n"
	text += "    [-p]         - Outputs each paragraph the pattern is found on.\n\n"

	return text

def notEnoughArgs():
	return "Error: Need more arguments\n\n"

def noSearchOptions():
	return "Reading each line from input:"

def usingF():
	return "Reading from file(s):"

def usingS():
	return "Reading from input until end of file:"

def noOutputOptions():
	return "Outputting whole text caught:"

def usingf():
	return "Outputting each phrase caught:"

def usingp():
	return "Outputting each paragraph caught:"