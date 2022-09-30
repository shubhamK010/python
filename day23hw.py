####################
#Write a code using function for performing above task with same logic as used for printing separators.

#the sentence should be aligned to the centre as in image 
  

def startEndLine():
     a="*"*80
     return a 
def fortext(text):
     b="**"
     d=76
     c=text.center(d)
     return b+c+b 
print(startEndLine())
print( fortext(' Welcome to AIX Version 6.1!'))
print(fortext('Please see the README file in /usr/lpp/bos for information pertinent to'))
print(fortext('this release of the AIX Operating System'))
print(startEndLine())