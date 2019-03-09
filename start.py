# Script for compressing all files in the folder with TinyJPG
# All libs in requirements.txt

import os
import tinify
import shutil
from colorama import init, Fore, Back, Style
from termcolor import colored

init() # Initialize the colorama

api_key = input('Please, enter your API Key from TinyJPG: ')
ext = ['jpg', 'jpeg','png']

# Create or verify if a folder exist
def create_folder():
	try:
		os.makedirs('Output')
		print( colored('Output folder created!', 'green') )
		return True
	except FileExistsError:
		print(colored('Output folder already!', 'yellow' ) )
		return True
	except:
		return False

# Get path/file from compress() for processing image
def compress_load(pack):
	for r in ext:
		if pack.endswith(r):
			#fullpath = pack[0] + "\\" + f
			#shutil.copy(fullpath, 'Output')
			#print(fullpath)
			source = tinify.from_file(pack)
			source.to_file("Output/"+pack)
			print( colored( '| ' , 'red' ) + pack )

# Search the folder for images available
def compress():
	counter=0
	local = os.getcwd()
	print( colored("Current folder > ", "magenta") + local )
	print( colored("\n+--------------------------------+", "cyan" ) )
	print( colored("| FILES                          |",   "cyan" ) )
	print( colored("+--------------------------------+",   "cyan" ) )

	for pack in os.listdir(local):
		compress_load(pack)
		counter+=1

	print( colored("+--------------------------------+",   "cyan" ) )
	print( colored('| FILES: '+str(counter)+'      |',     "cyan" ) )
	print( colored("+--------------------------------+\n"  "cyan" ) )			

# If want to use a proxy
def proxyMode():
	proxy = input("Use proxy? (Y/N) ")

	if proxy == 'Y' or proxy == 'y' or proxy == 'Yes' or proxy == 'yes':
		proxy = input("Need a authentication?")
		if proxy == 'Y' or proxy == 'y' or proxy == 'Yes' or proxy == 'yes':
			ip = input("Your IP proxy: ")
			port = input("Port: ")
			user = input("Username: ")
			pwd = input("Password: ")
			
			try:
				proxy_load = tinify.proxy = "https://"+user+":"+pwd+"@"+ip+":"+port
				print( colored( "\nConnected!\n" , "green" ) )
			except:
				proxy_load = tinify.proxy = "http://"+user+":"+pwd+"@"+ip+":"+port
				print( colored( "\nConnected!\n" , "green" ) )
		else:
			ip = input("Your IP proxy: ")
			port = input("Port: ")
			
			try:
				proxy_load = tinify.proxy = "https://"+ip+":"+port
				print( colored( "\nConnected!\n" , "green" ) )
			except:
				proxy_load = tinify.proxy = "http://"+ip+":"+port
				print( colored( "\nConnected!\n" , "green" ) )	

# Run script
def main():
	tinify.key = api_key

	proxyMode()

	if create_folder() == False:
		print( colored('Failed to create an output folder...', 'red' ) )
		exit()
	else:
		compress()

if __name__ == '__main__':
	main()