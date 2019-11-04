#import pandas as pd 
def literalTable(filename):
	litLineNo=[]
	asmLineNo=[]
	litValue=[]
	litHex=[]
	instruction=["mov","add","sub","cmp"]
	l=0
	f=open(filename,"r")
	for i,line in enumerate(f):
			if not line.isspace():					#or(if not re.search('\s',line):)
				filelist=line.split()
				lineNo=++i
				#print(filelist)
				for j in range(len(filelist)):	
					if filelist[j] in instruction:
						p=filelist[j+1].split(",")
						if(p[1].isnumeric()):
							Hex=hex(int(p[1]))[2:]
							if(len(Hex)==1):
								h=(7-len(Hex))*'0'+str(0)+Hex
							else:
								h=(8-len(Hex))*'0'+Hex
							'''else:
							p= [i.strip("'") for i in p]
							p= [i.strip('"') for i in p]
							Hex=hex(ord(p[1]))[2:]
							h=(8-len(Hex))*'0'+Hex'''
											
							litHex.append(h)
							#print(p,lineNo)
							litValue.append(p[1])
							asmLineNo.append(lineNo)
							litLineNo.append(l)
							l+=1
	
	
 					
	'''print("\n litLineNo \t\t asmLineNo\t\tlitValue\t\tlitHex")
	for x in range(len(litLineNo)):
	
		print("    "+str(litLineNo[x])+"\t\t\t"+str(asmLineNo[x])+"\t\t\t"+str(litValue[x])+"\t\t\t"+str(litHex[x]))'''
	return(litLineNo,asmLineNo,litValue,litHex)
filename="demo.asm"
literalTable(filename)		

