import nltk
import stemmerr21
f3=open("stem_out","w")
ll1=[]
ll1=stemmerr21.stemmerinput()
#print ll
def stem_malayalam(ll):
	l=[]
	l22=[]
	l=stemmerr21.malayalam_stemmer(ll)
	l22=stemmerr21.malayalam_stemmer(l)
	print l22
	l33=stemmerr21.malayalam_stemmer(l22)
	'''ss=stemmerr.secpass(l33)
	print ss'''
	return l33
l3=stem_malayalam(ll1)
for j in l3:
	f3.write(j.encode('utf-8')+"\n")
	#print j
'''for j in l22:
	
	print j'''
