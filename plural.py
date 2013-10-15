# -*- coding: utf-8 -*-
#This program gives the singular equivalent of a word.
#exceptions:ഞാന്‍-ഞങ്ങള്‍
#നീ-നിങ്ങള്‍ , താന്‍-താങ്കള്‍ ,അവന്‍ -അവര്‍ ,ഇവള്‍ -ഇവര്‍ ,ഇവന്‍-ഇവര്‍ 
#ബ്രാഹ്മണര്‍ = ബ്രാഹ്മണന്മാര്‍ ->former is not handled
#wrong results:	മകള്‍ ,മക്കള്‍ ,കാര്‍
import os,sys,codecs,string


def toSingular(words):
  for index in range(len(words)):
	
	word=words[index]
	if('+' not in word):
	 
		let1=u'ള്‍'
		if(let1 in word):
			lb1=u'കള്‍'
			lb2=u'ക്കള്‍'
			lb3=u'ങ്ങള്‍'
			lb4=u'ം ' 
			print word[-4:]
			if(word.endswith(lb2)):
				word=word.replace(lb2,"")
			else:
				if(word.endswith(lb1)):
					word=word.replace(lb1,"")
				else:
					if(word.endswith(lb3)):
						word=word.replace(lb3, lb4)
		else:
			let2=u'ര്‍'
			if(let2 in word):
				lb5=u'മാര്‍'
				lb6=u'കാര്‍'	
				if(word.endswith(lb5)):
					word=word.replace(lb5, "")

				else:
					if(word.endswith(lb6)):
						word=word.replace(lb6,u'കാരന്‍')
		print word
		words[index]=word
  return words







