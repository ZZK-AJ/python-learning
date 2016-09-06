import sys
text = sys.stdin.read()
words = text.split()
wordcount = len(words)
print 'wordcount:',wordcount

#cat somefiles.txt|python count-sysstdin-wordnumbers.py

