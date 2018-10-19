# proofAndEditMarkdown

import collections
import re

#phase 1

def writeHeader(inputFile, outPutReportFile):
	reportFile = open(outPutReportFile, 'w')
	reportFile.write('Proofreading Report\n')
	reportFile.write('Input File: ' + (open(inputFile, 'r')).name + '\n')
	reportFile.write('Report File: ' + reportFile.name + '\n\n\n\n')


def identifyRequestExamples(inputFile, outputReportFile):
	# check string for URL; 
	# print line to output to a line in output

	inExample = False
	headingLevel = 0
	exampleHeadingLevel = 0
	inCodeSample = False
	inHtml = False
	
	reportFile = open(outputReportFile, 'a')
	reportFile.write('\n')
	reportFile.write('--- checking for HTML requests ---\n')
	for i, line in enumerate(open(inputFile, 'r')):

		# detect an 'Example' heading
		if line.startswith('#'):

			#identify the heading level
			characterCount = collections.defaultdict(int)
			for c in line:
				characterCount[c] += 1
			headingLevel = characterCount['#']
			#reportFile.write(str(i+1) + ' heading level is ' + str(headingLevel) + '\n')

			if 'Example' in line:
				inExample = True
				exampleHeadingLevel = headingLevel
				#reportFile.write(str(i+1) + ' example heading level is ' + str(exampleHeadingLevel) + '\n')

			else:
				if inExample:
					if headingLevel < exampleHeadingLevel:
						inExample = False

		if inExample:
		# detect the start of a code sample
			if line.startswith('```'):
				if inCodeSample:
					if inHtml:
						inHtml = False # if in HTML, the HTML has ended
						print '\n'
						reportFile.write('\n')
					inCodeSample = False # code sample has ended
					
				else:
					inCodeSample = True # this line starts a code sample

			# detect the start of an HTML sample
			if inCodeSample and line.startswith('GET'):
				if inHtml == False:
					inHtml = True
					print str(i+1) + '   ' + line
					reportFile.write(str(i+1) + '   ' + line)
					#reportFile.write('   under example heading level ' + str(exampleHeadingLevel))
			elif inCodeSample and line.startswith('POST'):
				if inHtml == False:
					inHtml = True
					print str(i+1) + '   ' + line
					reportFile.write(str(i+1) + '   ' + line)
					#reportFile.write('   under example heading level ' + str(exampleHeadingLevel))


def identifyUniqueIds(inputFile, uniqueIdFields, outputReportFile):
	# check string for values of fields passed in IdFields parameter
	# if found, print field name and value to a line in output
	inCodeSample = False
	inJson = False
	
	reportFile = open(outputReportFile, 'a')
	reportFile.write('\n')
	reportFile.write('--- checking for unique IDs ---\n')
	for i, line in enumerate(open(inputFile, 'r')):
		
		# detect the start of a code sample
		if line.startswith('```'):
			if inCodeSample:
				if inJson:
					inJson = False # if in JSON, the JSON has ended
					print '\n'
					reportFile.write('\n')
				inCodeSample = False # code sample has ended
				
			else:
				inCodeSample = True # this line starts a code sample
				#print str(i+1) + ': starting code sample'

		# detect the start of a JSON sample
		if inCodeSample and line.startswith('{'):
			if inJson == False:
				inJson = True
				#print str(i+1) + ': now in JSON'
		elif inCodeSample and line.startswith('['):
			if inJson == False:
				inJson = True
				#print str(i+1) + ': now in JSON'

		# detect JSON fields that contain unique IDs			
		if inJson:
			
			for uniqueIdFieldName in uniqueIdFields:
				if uniqueIdFieldName in line:

					fieldValueType = ''

					if ':' in line:
						#print str(i+1) + ': checking for unique ID field in line with ":"'

						splitString = line.split(':')
						fieldName = splitString[0].strip()
						fieldName = fieldName.strip('"')

						fieldValue = splitString[1].strip() #strip leading & trailing whitespace
						fieldValue = fieldValue.rstrip(',') #strip trailing comma
						fieldValue = fieldValue.strip('"') #strip leading & trailing double-quotes

						if '"' in splitString[1]:
							# print value with double-quotes if it is a string
							print str(i+1) + '   "' + fieldName + '": ' + '"' + fieldValue + '"'
						else:
							print str(i+1) + '   "' + fieldName + '": ' + fieldValue

						for uniqueIdFieldName in uniqueIdFields:
							if fieldName == uniqueIdFieldName:
								reportFile.write(str(i+1) + ' ' + fieldName + ': ' + fieldValue + '\n')


def findHrefsInJsonSamples(inputFile, outputReportFile):
	# check string for values of fields passed in IdFields parameter
	# if found, print field name and value to a line in output
	inCodeSample = False
	inJson = False
	
	reportFile = open(outputReportFile, 'a')
	reportFile.write('\n')
	reportFile.write('---  checking for hrefs with unique IDs ---\n')
	for i, line in enumerate(open(inputFile, 'r')):
		
		# detect the start of a code sample
		if line.startswith('```'):
			if inCodeSample:
				if inJson:
					inJson = False # if in JSON, the JSON has ended
					print '\n'
					reportFile.write('\n')
				inCodeSample = False # code sample has ended
				
			else:
				inCodeSample = True # this line starts a code sample

		# detect the start of a JSON sample
		if inCodeSample and line.startswith('{'):
			if inJson == False:
				inJson = True

		elif inCodeSample and line.startswith('['):
			if inJson == False:
				inJson = True

		# detect JSON fields that contain unique IDs			
		if inJson:
			
			if 'href' in line:

					fieldValueType = ''

					if ':' in line:

						splitString = line.split(':',1)
						fieldName = splitString[0].strip()
						fieldName = fieldName.strip('"')

						fieldValue = splitString[1].strip() #strip leading & trailing whitespace
						fieldValue = fieldValue.rstrip(',') #strip trailing comma
						fieldValue = fieldValue.strip('"') #strip leading & trailing double-quotes

						if '"' in splitString[1]:

							print str(i+1) + '   "' + fieldName + '": ' + '"' + fieldValue + '"'
							reportFile.write(str(i) + ' ' + fieldName + ': ' + fieldValue + '\n')
						else:
							print str(i+1) + '   "' + fieldName + '": ' + fieldValue
							reportFile.write(str(i) + ' ' + fieldName + ': ' + fieldValue + '\n')
								



def findDuplicateRowsInTables(inputFile, outputReportFile):
	# identify each table in Markdown file
	# and for each table,
	# check each row to determine if it is duplicates another row,
	# if so, print line to output identifying the duplicate row by line number

	linesSeen = set()
	inTable = False
	reportFile = open(outputReportFile, 'a')

	reportFile.write('\n')
	reportFile.write('--- finding duplicate rows in tables ---\n')

	for i, line in enumerate(open(inputFile, 'r')):
		
		if line.startswith('|'):
			lineRStripped = line.rstrip()  #remove whitespace from eol, esp. newline
			lineRStripped = lineRStripped.rstrip('| ') #remove pipe or space from eol

			#print 'checking line ' + str(i) + ':   ' + lineRStripped
			inTable = True
			if lineRStripped not in linesSeen:
				linesSeen.add(lineRStripped)
			else:
				reportFile.write('row on line ' + str(i+1) + ' is a duplicate\n')
				reportFile.write('     ' + lineRStripped + '\n')
		else:
			if inTable == True:
				inTable = False 
				linesSeen = set() # table has ended; clear the set
	reportFile.close()


def spellcheckFile(inputFile, englishWordsList, specializedWordsList, outputReportFile):
	# check inputFile for words not in the reference list
	# if found, print line number and word to output

	# import the reference list of English words and put it in a list
	#  with newlines removed
	wordsFile = open(englishWordsList, 'r')
	englishWords = wordsFile.read().splitlines()
	wordsFile.close()

	specializedWordsFile = open(specializedWordsList, 'r')
	specializedWords = specializedWordsFile.read().splitlines()
	print(specializedWords)
	print('\n')
	
	reportFile = open(outputReportFile, 'a')
	reportFile.write('\n')
	reportFile.write('--- Spell-checking file ---\n')
	reportFile.write('   - asterisk (*) after line # indicates case mismatch -\n')
	for i, line in enumerate(open(inputFile, 'r')):
		line = line.rstrip() # remove newline and other whitespace from end of line
		line = line.rstrip('.,;:')
		line = line.lstrip()
		#reportFile.write(str(i) + ' ' + line + '\n')
		#print str(i+1), ' ', line
		
		lineIsEmpty = False
		lineHasOneCharacterNTimes = False

		lineCharacters = ['`', '-', '{', '}']

		if line == '':
			lineIsEmpty = True
		elif len(set(line)) == 1:
				lineHasOneCharacterNTimes = True

				if [c for c in lineCharacters if c in line]:
					lineHasOneDesignatedCharacter = True

		else:
			words = re.split('[ :/<>()*,."|;]+', line)
		
			print(str(i+1) + ' ' + str(words))

			caseMismatch = False

			for word in words:
				if not word.isdigit() and word != '#' and word != '##' and word != '###' and word != '####' and word != '---' and word != '```' and word != '|' and word != '-':
					word = word.strip('[')
					word = word.strip(']')
					if word != '':
						if word.lower() not in englishWords:
							if word not in specializedWords:
								if word.lower() not in specializedWords:
									#print('   "' + word + '" is not in reference list: ' + str(specializedWords))
									reportFile.write(str(i+1) + ' ' + word + '\n')
								else:
									caseMismatch = True
									reportFile.write(str(i+1) + '* ' + word + '\n')
		
	reportFile.close()



	
#phase 2

def obfuscateUniqueIds(inputFile, uniqueIdFields, uniqueIdFieldValueMap, outputReportFile):
	#use dictionary (sorted?) of unique IDs and the field value to write for each field,
	# to search for and obfuscate each field
	# NOTE: should include unique IDs in hrefs also
	pass



def testRequestURLObfuscation(urlString):
	# check if URL is obfuscated
	# return true or false
	pass

def testUniqueIdObfuscation(iDString):
	# check if URL is obfuscated
	# return true or false
	pass

#phase 3

def obfuscateRequestExamples(urlString):
	# check string for request URL;
	pass 