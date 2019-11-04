def collectLables(fileName):
	symbol_name=[]
	variable_size=[]
	variable_Name=[]
	list1=[]
	finalsymbol=[]
	data_size=[]
	size=[]
	list7=["jz","jnz","jnz","jmp","call"]
	extern_list=[]
	asm_list=[]
	lables_list=[]
	symbol_lable_tag=[]
	addr=[]
	value=[]	
	du=[]
	var=[]
	j=lables_list
	k=0
	cnt=0
	symNo=[]
	asmNo=[]	
	f=open(fileName,"r")
	for str1 in  f.readlines():
		if not str1.isspace():
			asm_list=str1.split()
			k+=1
			#print(k)
			#print(asm_list)
			#print(str1)
			for i in range((len(asm_list))):
				#print(asm_list[i])
				if(asm_list[i]=='dd'):
					cnt+=1
					asmNo.append(k)
					symNo.append(cnt)
					#print(symNo)
					symbol_name.append(asm_list[i-1])
					variable_size.append(2)
					p=asm_list[i+1].strip('[')
					#print("*******************************",p)
					symbol_lable_tag.append("s")
					value.append(p)
					du.append('D')
					z=len(p)-1
					data_size.append(len(p))
					if(z==0):
						size.append(4)
					else:
						size.append((z)*4)
				elif(asm_list[i]=='db'):
					cnt+=1
					symNo.append(cnt)
					asmNo.append(k)
					#print(symNo)
					symbol_name.append(asm_list[i-1])
					variable_size.append(1)
					symbol_lable_tag.append("s")
					p=asm_list[i+1].strip("[")
					value.append(p)
					data_size.append(len(p))
					z=(len(p[0])-2)*1
					size.append(z)
					du.append('D')
				elif(asm_list[i]=='dw'):
					cnt+=1
					symNo.append(cnt)
					asmNo.append(k)
					symbol_name.append(asm_list[i-1])
					variable_size.append(8)
					symbol_lable_tag.append("s")
					p=asm_list[i+1].strip("[")
					value.append(p)
					data_size.append(len(p))	
					du.append('D')
					z=len(p)-1
	               	
					if(z==0):
						size.append(2)
					else:
						size.append(z*2)
				elif(asm_list[i]=='dq'):
					cnt+=1
					symNo.append(cnt)
					asmNo.append(k)
					symbol_name.append(asm_list[i-1])
					variable_size.append(4)
					symbol_lable_tag.append("s")
					p=asm_list[i+1].strip("[")
					#print("*******************************",p)					
					value.append(p)
					du.append('D')
					z=len(p)-1
					data_size.append(len(p))
					if(z==0):
						size.append(8)
					else:
						size.append(z*8)
				elif(asm_list[i]=='resd'):
					cnt+=1
					symNo.append(cnt)
					asmNo.append(k)
					symbol_name.append(asm_list[i-1])
					variable_size.append(2)
					symbol_lable_tag.append("s")
					p=int(asm_list[i+1])*2
					value.append(asm_list[i+1])
					du.append('D')
					data_size.append(int(asm_list[i+1]))
					size.append(asm_list[i+1])
				elif(asm_list[i]=='resb'):
					cnt+=1
					symNo.append(cnt)
					symbol_name.append(asm_list[i-1])
					variable_size.append(1)
					symbol_lable_tag.append("s")
					du.append('D')
					p=int(asm_list[i+1])*1
					value.append(asm_list[i+1])
					size.append(p)
					data_size.append(int(asm_list[i+1]))
				elif(asm_list[i]=='resw'):
					cnt+=1
					symNo.append(cnt)
					asmNo.append(k)
					symbol_name.append(asm_list[i-1])
					variable_size.append(8)
					symbol_lable_tag.append("s")
					p=int(asm_list[i+1])*4
					value.append(p)
					du.append('D')
					data_size.append(int(asm_list[i+1]))
					size.append(p)
				elif(asm_list[i]=='resq'):
					cnt+=1
					symNo.append(cnt)
					asmNo.append(k)
					symbol_name.append(asm_list[i-1])
					variable_size.append(4)
					symbol_lable_tag.append("s")
					p=int(asm_list[i+1])*8
					value.append(p)
					du.append('D')
					data_size.append(int(asm_list[i+1]))
					size.append(p)
				elif(asm_list[i]=='rest'):
					cnt+=1
					symNo.append(cnt)
					asmNo.append(k)
					symbol_name.append(asm_list[i-1])
					variable_size.append(4)
					symbol_lable_tag.append("s")
					p=int(asm_list[i+1])*16
					value.append(p)
					du.append('D')
					data_size.append(int(asm_list[i+1]))
					size.append(p)
				elif(asm_list[i]=='extern'):
					
					extern_list=asm_list[i+1].split(",")
					#print(extern_list)
				elif(asm_list[i]=='global'):
					lables_list.append(asm_list[i+1])
				elif ':' in asm_list[i]:
					
					var=asm_list[i].split(':')
					#print(var)
					#print('******************')
					if var[0]not in symbol_name:
						cnt+=1
						symNo.append(cnt)
						asmNo.append(k)
						symbol_name.append(var[0])
						j.append(var[0])
						#print(j)
						#print('******************')
						symbol_lable_tag.append('L')
						variable_size.append('-')
						data_size.append('-')
						value.append('-')
						if asm_list[i] not in j:
							du.append('U')					
						size.append(0)
				elif(asm_list[i] in list7):
					j.append(symbol_name)
					#print(j)
					#print("*************************")
					if(asm_list[i]not in j):
						cnt+=1
						symNo.append(cnt)
						asmNo.append(k)
						symbol_name.append(asm_list[i+1])
						
						symbol_lable_tag.append('L')
						variable_size.append('-')
						data_size.append('-')
						if asm_list[i] not in j:
							du.append('U')
						size.append(0)
						value.append('-')
				
		
		
	addr.append(0)
	for i in range(1,len(size)):
		addr.append((int(size[i-1])+int(size[i])))
	
	#print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",k)
	'''print ("\nsymbol_no | asm_no   | symbol_name | variable_size| data_size |\t symbol_lable_tag |   du\t|\t addr |\t\t value")
	for x in range(0,(len(symbol_name))):
		
		print ("\n"+str(symNo[x])+"\t\t" +str(asmNo[x])+"\t"+symbol_name[x] +"\t\t" + str(variable_size[x]) +"\t\t"+ str(data_size[x]) + "\t\t" + str(symbol_lable_tag[x]) + "\t\t" + str(du[x])+ "\t\t" + str(addr[x])+ "\t\t" + str(value[x]))
	#print(finalsymbol)'''
	return(symNo,asmNo,symbol_name,variable_size,data_size,symbol_lable_tag,du,addr,value)
	
fileName="demo.asm"
collectLables(fileName)
