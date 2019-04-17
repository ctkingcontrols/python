import os
from pathlib import Path
from time import sleep
import sys


def func_choice(x): # this function handles most print() and input() functions for the sake of modularity
	if x == 1:
		return input('Enter the file you wish to select (without quotations) search and include the extension. Enter "0" if you wish to quit. Enter "1" if you wish to type a full filepath:  \n \n')
	elif x==2:
		return input('\n Enter the entire file path, including the file extension:  ')
	elif x==3:
		return input('\n You have chosen ' + f_choose + ' "1" to confirm, "0" to quit  ')
	elif x==4:
		print ('\n \n Error: You have selected a file which does not exist ')
		return
	elif x==5:
		print('You\'ve chosen a file that has an extension which is not ".txt"')
		return
	elif x==6:
		return input('To read the contents of the file, type "x.0". Otherwise type the string you wish to search for: ')
	else:
		return 'Error'
	


def func_select():			# This function gets the current directory and asks the user to select a file from the directory, or type full file path of their target file

	cwd = os.getcwd()																			# os function to get current working directory
	print ('\n Current directory: \n \n', cwd, '\n') 
	entries = os.listdir(cwd)																	#os function to list all file objects inside a directory
	print('This is a list of what is in your current working directory: \n \n', entries, '\n')
		
	f_select = func_choice(1)
	if f_select == '1':
		f_choose = func_choice(2)
		f_confirm = func_choice(3)
		if f_confirm == '1':
			return f_choose
		else:
			sys.exit()																			#exit program
	elif f_select == '0':
		sys.exit()																				#exit program	
	elif f_select in entries:
			new_dir = cwd + "\\" + f_select
			print ('\n You have selected', new_dir, '\n')
			return new_dir
	else:
		func_choice(4)
		sys.exit()																				#exit program
			
			
			
def func_extension(file_target):

	file_name, file_extension = os.path.splitext(file_target)
	if file_extension == '.txt':
		return file_target		
	else:
		func_choice(5)
		sys.exit()
		
		
def func_read(file_current, choice ):

	detect = func_choice(choice)
	with open(file_current) as f:   # open the file and automatically close it when this statement is done
	
		if detect == 'x.0':			#if the user chooses this option by entering 'x.0', the program will print the file and the return False
			for i in f:
				print(i)
			return False			
		else:																	#if the user chooses a string other than 'x.0'
			line_appearances = [] 												# declare empty list
			line_count = 0        												# initialize line count
			current_line = f.readline() 										#initialize while loop
			while ( current_line != ''):				
				line_count += 1 												#update line count
				print ('Working on' ,current_line)								
				sleep(.2)														#create a pause in the program for user's eyes
				for k in range(0, (len(current_line) - len(detect))):			#numeric range -> 0,1,2,3 etc.
					if current_line[k:(k+len(detect))] == detect:				#check if string slice is equal to the user input saved at variable 'detect'
						line_appearances.append(('line',line_count,'index',k))  #append to list *note, tried using a dict at first, but it just overwrote the value of the key rather than adding a new key-value pair*       	
				current_line = f.readline() 									#update the while loop
			print(line_appearances)
			return line_appearances   #returns a list of tuples of the form: [ ('line', line_count1 ,'index', k1),('line', line_count2 ,'index', k2) ]



print('Initializing program - you will now select your target file')
sleep(.2)

f_target = func_select()

sleep(.2)
print ('Starting Step 2\n')

f_current = func_extension(f_target)

sleep(.2)
print ('Starting Step 3\n')

func_read(f_current,6)
print('Starting Step 4\n')
sleep(2)



