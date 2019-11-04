from collectLables2 import *
from  literalTablefinal import *
from registers import*
import sys
str2=[]

def intermediate(filename):
	litval=literalTable(filename)
	symbolTable=collectLables(filename)
	nasm_list=[]
	f=open(filename,"r")
	for str1 in f.readlines():
		if not str1.isspace():
			str2=str1
			nasm_list=str1.split()
			sym_list=symbolTable
			lit_list=litval
			for x in range(0,len(nasm_list)-1):
				for i in range(0,len(sym_list)):
					if sym_list[i]==sym_list[2]or sym_list[i]==sym_list[0]:
						for j in range(0,len(sym_list[i])):
							if nasm_list[0]==sym_list[2][j]:
								str1=(str1.replace(nasm_list[0],('sym#'+str(sym_list[0][j]))))
											
							if nasm_list[x] in inst:
								p=nasm_list[x+1].split(",")
								for y in p:
									if y in reg:
										#print ("Value : %s" %  assign.get(y))
										str1=(str1.replace(y,assign.get(y)))
									elif y in sym_list[2][j]:
										str1=(str1.replace(y,('sym#'+str(sym_list[0][j]))))
									else:
										for w in word:
											if w in y:
												lst=y.strip(w)
												if sym_list[2][j]in lst:
													str1=(str1.replace(sym_list[2][j],('sym#'+str(sym_list[0][j]))))
												else:
													for r in reg:
														str1=(str1.replace(r,assign.get(r)))
				for i in range(0,len(lit_list)):
					if lit_list[i]==lit_list[2]or lit_list[i]==lit_list[0]:
						for j in range(0,len(lit_list[i])):
							if nasm_list[x] in inst:
								p=nasm_list[x+1].split(",")
								if p[-1]==lit_list[2][j]:
									str1=(str1.replace(p[-1],('lit#'+str(lit_list[0][j]))))
								
								
			print(str1)	
												
filename= sys.argv[1]
intermediate(filename)
