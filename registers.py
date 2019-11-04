assign={'eax':'32#reg1','ecx':'32#reg2','edx':'32#reg3','ebx':'32#reg4','esi':'32#reg5','edi':'32#reg6','esp':'32#reg7','ebp':'32#reg8','ax':'16#reg1','cx':'16#reg2','dx':'16#reg3','bx':'16#reg4','si':'16#reg5','di':'16#reg6','sp':'16#reg7','bp':'16#reg8','al':'8#reg1','cl':'8#reg2','dl':'8#reg3','bl':'8#reg4','ah':'8#reg1','ch':'8#reg2','dh':'8#reg3','bh':'8#reg4'}


inst=['mov','add','sub','mul','div','xor','jmp','jnz','jz','printf','scanf','pusha','popa','push','pop','call','inc','dec','cmp','jnz','jle','jge','fld','fstp','fmul','fild','loop','fild','fchs','fadd','fsqrt','fldz']
sections=['section','global','extern','.data','.text','.bss','main','printf','scanf','printf,scanf']
reg=['eax','ecx','edx','ebx','esi','edi','esp','ebp','ax','cx','dx','bx','si','di','sp','bp','al','ah','cl','ch','dl','dh','bl','bh']

word=['qword','dword','bword','word',]
err=[]
err_line=[]
err_name=[]
err_spec=[]
mac_name=[]
mac_para=[]
mac_def=[] 
