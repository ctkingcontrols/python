import os
from pathlib import Path
from time import sleep
import sys
import xlrd 

def func_choice(x): # this function handles most print() and input() functions for the sake of modularity
	if x == 1:
		return input('Enter the file you wish to select (without quotations) search and include the extension. Enter "0" if you wish to quit. Enter "1" if you wish to type a full filepath:  \n \n')
	elif x==2:
		return input('\nEnter the entire file path, including the file extension:  ')
	elif x==3:
		return input('\nYou have chosen ' + f_choose + ' "1" to confirm, "0" to quit  ')
	elif x==4:
		print ('\n \nError: You have selected a file which does not exist ')
		return
	elif x==5:
		print('You\'ve chosen a file that has an extension which is not parameterized for')
		return
	elif x==6:
		return input('\nTo read the contents of the file, type "x.0". Otherwise type the string you wish to search for: ')
	elif x==7:
		return input('\nChoose a name for your output file and type desired extension (e.g .txt): ')			
	elif x==8:
		print('There is a problem with the extension you have chosen')
		return
	elif x==9:
		return input('\nWhat is the extension of the file you wish to READ from? (1= .txt ; 2= .xlsx): ')	
	elif x==10:
		return input('\nWhat is the extension of the file you wish to WRITE to? (1= .txt ; 2= .xlsx): ')
	elif x==11:
		search_term = input('\n You are reading from a .xls file, type in your search term: ').lower()
		column_start = int(input('\n  type in your start column: '))
		column_end = int(input('\n  type in your end column: '))
		row_start = int(input('\n  type in your start row: '))
		row_end = int(input('\n  type in your end row: '))
		return search_term, column_start, column_end, row_start, row_end
	else:
		return 'Error'
	


def func_select():			# This function gets the current directory and asks the user to select a file from the directory, or type full file path of their target file

	cwd = os.getcwd()																			# os function to get current working directory
	print ('\nCurrent directory: \n \n', cwd, '\n') 
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
			f_choose = cwd + "\\" + f_select
			print ('\n You have selected', f_choose, '\n')
			return f_choose
	else:
		func_choice(4)
		sys.exit()																				#exit program
			
			
			
def func_extension_read(file_target, para_extension = '1'):
	
	para_extension = func_choice(9)
	file_name, file_extension = os.path.splitext(file_target)
	
	if (file_extension == '.txt') and (para_extension == '1'):
		return file_target , para_extension
	elif (file_extension == '.xlsx') and (para_extension == '2'):
		return file_target, para_extension
	else:
		print('file name was: ', file_name)
		print('file extension was: ', file_extension)
		print('para extension was: ', para_extension)
		func_choice(5)
		sys.exit()
		
		
def func_read(file_current, para_extension_read ):
	if para_extension_read ==  '1':        # for reading a '.txt' file
		search_term = func_choice(6)
		with open(file_current) as f:   # open the file and automatically close it when this statement is done
	
			if search_term == 'x.0':			#if the user chooses this option by entering 'x.0', the program will print the file and the return False
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
					for k in range(0, (len(current_line) - len(search_term))):			#numeric range -> 0,1,2,3 etc.
						if current_line[k:(k+len(search_term))] == search_term:				#check if string slice is equal to the user input saved at variable 'search_term'
							line_appearances.append(('line',line_count,'index',k))  #append to list *note, tried using a dict at first, but it just overwrote the value of the key rather than adding a new key-value pair*       	
					current_line = f.readline() 									#update the while loop
				print('this is the list which holds the records of the appearances ', line_appearances)
				return line_appearances   											#returns a list of tuples of the form: [ ('line', line_count1 ,'index', k1),('line', line_count2 ,'index', k2) ]
	elif para_extension_read == '2':  												# for reading a '.xls' file
		search_term, column_start, column_end, row_start, row_end = func_choice(11) 
		workbook = xlrd.open_workbook(file_current) 
		sheet = workbook.sheet_by_index(0)
		print(sheet.cell_value(2, 1)) 										######## <------------------------------- need proof of concept of retriving values from cells in the worksheet
		#for i in range(column_start, column_end + 1):
			#for k in range(row_start, row_end + 1):
				#print('Working on row:', k,'column',i)
				#if str(sheet.cell_value(k,i)) == search_term:
					#print('Search term found on row:', k,'column',i)
					#break
			#print('for loop "K" exited')
		#print('for loop "I" exited')
					
			
def func_check_filename(para_extension = '1' ):
	# 1 = '.txt'
	# 2 = '.xls'
	if para_extension == '1':
		compare_extension = '.txt'
	elif para_extension == '2':
		compare_extension = '.xlsx'

	cwd = os.getcwd()									#get current working directory
	entries = os.listdir(cwd)							#put CWD in list format
	name_valid = False									#initialze entry into while loop
	
	while (name_valid == False):					
		name_valid = True									#while loop will exit after first run unless name_valid is toggled false again
		ask_input = func_choice(7)							#user types name of file they want
		file_name, file_extension = os.path.splitext(ask_input)
		if file_extension == compare_extension:
			for i in entries:								#compare name with files in current working directory
				if ask_input == i:
					name_valid = False						#if there is a match, ensure while loop restarts from beginning
		else:
			print('\nyou have chose extension type :', file_extension)
			print('\nthe required format is :', compare_extension)
			func_choice(8)
			name_valid =False
	return ask_input									# return file name inputted by the user
				
	
		
	


def func_output_to_file(input_data, para_extension):
	
	new_name =func_check_filename(para_extension)             		#new_file is given a filename by func_check_filename() where arg ==1 means it will be a .txt file
	print('\n now creating file' , new_name)
	new_file = open(new_name,'w')
	new_file.write(str(input_data))                     #argument of new_file.write(arg) requirement is that arg must be a string and not a list 
	new_file.close()
	

	return True
	


print('Initializing program - you will now select your target file')
sleep(.2)

f_target = func_select()

sleep(.2)
print ('Starting Step 2\n')

f_current, para_extension_read = func_extension_read(f_target, '1')    		#check to see if extension is valid, if so then return the f_target again.

sleep(.2)
print ('Starting Step 3\n')

list_output = func_read(f_current,para_extension_read)
print('Starting Step 4\n')
sleep(2)

func_output_to_file(list_output, para_extension_read)





