This one pass Assembler includes symbol table, literal table and intermediate code

	symbol table : collectLables.py is for symbol table which can collect all the symbols and lables in the given .asm file.
	literal table: literalTableFinal.py is for literal table which can collects all the literals in the given .asm file.
	intermediate : intermediate.py is for display all the intermediate data of assembler.

How to run:
	python3 intermediate.py filename.asm
	e.g. : python3 intermediate.py fact.asm
