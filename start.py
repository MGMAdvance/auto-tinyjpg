# Script for compressing all files in the folder with TinyJPG
# All libs in requirements.txt

import os
import tinify
import shutil

api_key = input('Please, enter your API Key from TinyJPG: ')
ext = ['jpg','png','gif']

def create_folder():
	try:
		os.makedirs('Output')
		print('Output folder created!')
		return True
	except FileExistsError:
		print('Output folder already!')
		return True
	except:
		return False

def compress_load(f, pack):
	for r in ext:
		if f.endswith(r):
			fullpath = pack[0] + "\\" + f
			#shutil.copy(fullpath, 'Output')
			#print(fullpath)
			source = tinify.from_file(f)
			source.to_file("Output/"+f)
			print(f)

def compress():
	counter=0
	local = os.getcwd()
	print("Current folder > "+local)
	print("\n+--------------------------------+")
	print("| FILES                          |")
	print("+--------------------------------+")
	for pack in os.walk(local):
		for f in pack[2]:
			compress_load(f, pack)
	print("+--------------------------------+\n")			
				
def main():
	api = tinify.key = api_key
	
	if create_folder() == False:
		print('Failed to create a output folder...')
		exit()
	else:
		compress()

	
main()