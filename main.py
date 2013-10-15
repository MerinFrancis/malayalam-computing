# -*- coding: utf-8 -*-
#!/usr/bin/python

import os,sys,codecs,string
import hyphen,punctn,plural,mysql

#read the input
def getInput(inputFile):
	inpt=codecs.open(inputFile,encoding='utf-8', errors='ignore').read()
	return inpt

#write the output to a file
def writeOutput(outputFile,words):
	op=open(outputFile, "w")
	for index in range(len(words)):
		words[index]=unicode(words[index],encoding='utf-8', errors='ignore')
		op.write(words[index].encode("UTF-8"))
		op.write(" ")


#remove hyphenation
inputFile=getInput('input.txt')
partOp1=hyphen.hyphenRem(inputFile)
writeOutput('afterHyph.txt',partOp1)

#remove punctuation
inputFile=getInput('afterHyph.txt')
partOp2=punctn.punctnRem(inputFile)
writeOutput('aftrPunctn.txt',partOp2)

# mark Valid Words
inputFile=getInput('aftrPunctn.txt')
words = inputFile.split()
f=open('valid.txt', "w")
for index in range(len(words)):
	count = mysql.valid(words[index])
	if(count>0):	
		f.write("+")
	f.write(words[index].encode("UTF-8"))
	f.write(" ")
f.close()
		
	
#convert plural to singular
inputFile=getInput('valid.txt')
words = inputFile.split()
f=open('aftrPluralRem.txt', "w")
words=plural.toSingular(words)
for index in range(len(words)):
	f.write(words[index].encode("UTF-8"))
	f.write(" ")




