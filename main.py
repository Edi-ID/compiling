import marshal
import base64
import sys
import os
import click
from uncompyle6 import main
from time import sleep

top = '\033[0;1m[\033[31m!\033[0;1m]\033[32m'
logo = ('''
    \033[36;1m+\033[33;1m------------------\033[36;1m+\033[33;1m
    \033[33;1m| \033[32mCOMPILE \033[0;1m| \033[32mPYTHON \033[33;1m|\033[33;1m
    \033[36;1m+\033[33;1m------------------\033[36;1m+\033[33;1m
	''')

def menu():
	print ('\033[33;1m-------------------')
	print ('\033[0;1m[\033[31m+\033[0;1m]\033[32m MENU\033[0;1m:          ')
	print ('\033[33;1m-------------------')
	print ('\033[0;1m[\033[31m1\033[0;1m]\033[32m Compile Python ')
	print ('\033[0;1m[\033[31m0\033[0;1m]\033[31m Exit           ')
	print ('\033[33;1m-------------------')
	print ('\033[0;1m[\033[31m+\033[0;1m]\033[32m Enter Number\033[0;1m: ')

def Testing():
	class Compiles:
		def __init__(self,choose,amount):
			self.file=choose
			self.cout=0
			self.jum=amount
			self.marsh(open(choose,'r').read())

		def marsh(self,strg):
			x=compile(strg,'<script>','exec')
			xx=marshal.dumps(x)
			xxx=f'#Python Compile\n#Github  : https://github.com/Edi-ID\n#Facebook: Edi ID\n\nimport marshal\nexec(marshal.loads({xx}))'
			if self.cout == self.jum:
				with open(self.file.replace('.py','_testing.py'),'w') as compiles:
					compiles.write(xxx)
					print(f"\033[0;1m[\033[31m+\033[0;1m]\033[32m File Saved At\033[0;1m:\033[33;1m {self.file.replace('.py','_testing.py')}")
					return True
			self.b64(xxx)

		def b64(self,strg):
			encode=base64.b64encode(bytes(strg,'utf-8'))
			decode=f"#Spirit\n\nimport base64\nexec(base64.b64decode({encode}).decode('utf-8','ignore'))"
			self.cout+=1
			self.marsh(decode)
	os.system('clear')
	print (logo)

	try:
		print ('\033[0;1m[\033[31m?\033[0;1m]\033[32m Enter File Python\033[0;1m: ')
		file_python=input('\033[34m=\033[33;1m>\033[0;1m: ')
		print ('\033[0;1m[\033[31m?\033[0;1m]\033[32m Number of compiles\033[0;1m:')
		amount=int(input('\033[34m=\033[33;1m>\033[0;1m: '))
		if amount > 10:
			click.pause('\033[32mYou enter a number more than \033[0;1m10, \033[32mthis can cause the file size to be slow \033[31mENTER\033[0;1m')
		Compiles(file_python,amount)
		choose=input('\033[0;1m[\033[31m?\033[0;1m]\033[32m Compile to bytes code pyc \033[32m(\033[32my\033[0;1m/\033[32mt)\033[0;1m: ')
		if choose.lower() == 'y':
			main.compile_file(file_python.replace('.py','_testing.py'))
			print ('\033[33;1m-\033[0;1m'*21)
			print ('\033[0;1m[\033[31m+\033[0;1m]\033[32m Successfully\033[0;1m')
			print ('')
		else:
			print ('\033[33;1m-\033[0;1m'*21)
			print ('\033[0;1m[\033[31m+\033[0;1m]\033[32m Created By Edi ID\033[0;1m')
			sys.exit()
	except KeyboardInterrupt:
		print (top + ' \033[31mStopped\033[0;1m')
		print ('')
	except Exception as F:
		print(f'[Error] {str(F)}')

def ex():
	print ('')
	print ('\033[33;1m-----------------\033[0;1m')
	print ('\033[0;1m[\033[31m+\033[0;1m]\033[32m Thank YOU    \033[0;1m')
	sys.exit()

reset = 'y'
while (reset != 't'):
	os.system('clear')
	print (logo)
	menu()
	selection = input('\033[34m=\033[33;1m>\033[0;1m: ')
	if selection == '1':
		Testing()
	elif selection == '0':
		ex()
	else:
		print ('')
		print ('\033[33;1m-----------------')
		print ('\033[0;1m[\033[31m!\033[0;1m]\033[31m Wrong Input  \033[0;1m')
		print ('')
	reset = input('\033[0;1m[\033[31m?\033[0;1m]\033[32m back to menu \033[32m(\033[32my\033[0;1m/\033[32mt)\033[0;1m: ')
	os.system('clear')

if __name__ == '__main__':
	menu()