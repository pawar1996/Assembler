section .data
	b dd 10
	a dd 2
	c dd 3
	msg db "addition %f",10,0
section .bss
	Mfirst resq 1
	Msecond resd 1
	four resw 1
section .text
	global main
	extern printf,scanf
main:
	mov dword[four],4
	fld qword[b]
	fmul qword[b]
	fstp qword[Mfirst]
	fld qword[a]
	loop aa
	jmp aa
	fmul qword[c]
aa:	fild dword[four]
	fmul st1
	fchs
	fadd qword[Mfirst]
	fsqrt
	sub esp,8
	fstp qword[esp]
	push msg
	call printf
	add esp,12
