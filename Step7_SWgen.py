import os
from pathlib import Path
from time import sleep
import sys
import xlrd 

def func_choice(x): # this function handles most print() and input() functions for the sake of modularity
	if x == 1:
		return input('Enter the file you wish to select (without quotations) search and include the extension. [ 0 = quit ; 1 = type a full filepath ]  \n \n')
	elif x==2:
		return input('\nEnter the entire file path, including the file extension:  ')
	elif x==3:
		return input('\nYou have chosen ' + f_choose + ' [1 = confirm, 0 = Quit]  ')
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
		return input('\nWhat is the extension of the file you wish to READ from? [ 0 = .xlsx ; 1 = .txt  ]: ')	
	elif x==10:
		return input('\nWhat is the extension of the file you wish to WRITE to? [ 0 = .xlsx ; 1 = .txt  ]: ')
	elif x==11:
		user_term = input('\n You are reading from a .xls file, searching for [ 0 = Module Number ]: ')
		if user_term == '0':
			search_term = 'Module Number'
		else:
			sys.exit()
		user_range = input('\n Choose searching range (0 = default, any = custom): ')
		if user_range == '0':
			column_start, column_end, row_start, row_end = 0 , 20, 0 , 20
		else:
			column_start = input('\n  type in your start column: ')
			column_end = input('\n  type in your end column: ')
			row_start = input('\n  type in your start row: ')
			row_end = input('\n  type in your end row: ')
		return str(search_term), int(column_start), int(column_end), int(row_start), int(row_end)
	elif x==12:
		user_range = input('\n Choose the column range of your table (rows will be automatically calculated) [0 = 0 - 14 (default choice]; any_key = custom ')
		if user_range == '0':
			column_start, column_end = 0 , 14
		else:
			column_start = input('\n  type in your start column: ')
			column_end = input('\n  type in your end column: ')
		return int(column_start), int(column_end)
	elif x==13:
		user_ext =  input('\n What type of file do you want to create?  [0 = .txt ]: ')
		if user_ext == '0':
			return '.txt'
		else:
			func_choice(13)	
	elif x==14:
		user_ext =  input('\n What type of output do you want [0 = .txt (generate software blocks) ; 1 = .txt (write a string)]: ')
		if user_ext == '0':
			return 'generate'
		elif user_ext == '1':
			return 'simple'
		else:
			func_choice(14)	
	else:
		return 'Error'

def func_exit(x,y): 		
	if (x == 1) and (y == '1'):
		input('Program is exiting from func_select_file with func_exit(1,"1"),  press any key to exit program  ')
		sys.exit()
	elif (x == 1) and (y == '0'):
		input('Program is exiting from func_select_file with func_exit(1,"0"), press any key to exit program  ')
		sys.exit()
	elif (x == 1) and (y == 'null'):
		input('Program is exiting from func_select_file with func_exit(1,"null"), press any key to exit program  ')
		sys.exit()
	elif (x == 2) and (y == '0'):
		input('Program is exiting from func_extension with func_exit(2,"0"), press any key to exit program  ')
		sys.exit()
	elif (x == 3) and (y == '0'):
		input('Program is exiting from func_draw_xls_table with func_exit(3,"0"), press any key to exit program  ')
		sys.exit()	
	elif (x == 4) and (y == '0'):
		input('Program is exiting from func_read with func_exit(4,"0"), press any key to exit program  ')
		sys.exit()	
	elif (x == 4) and (y == '1'):
		input('Program is exiting from func_read with func_exit(4,"1"), press any key to exit program  ')
		sys.exit()
	elif (x == 5) and (y == '0'):
		input('Program is exiting from func_output_to_file with func_exit(5,"0"), press any key to exit program  ')
		sys.exit()
	elif (x == 5) and (y == '1'):
		input('Program is exiting from func_output_to_file with func_exit(5,"1"), press any key to exit program  ')
		sys.exit()
	else:
		input('Program is exiting through func_exit with no valid arguments, press any key to exit program  ')
		sys.exit()
		

	


def func_select_file():			# This function gets the current directory and asks the user to select a file from the directory, or type full file path of their target file

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
			func_exit(1,'1')
	elif f_select == '0':
		func_exit(1,'0')																				
	elif f_select in entries:
			f_choose = cwd + "\\" + f_select
			print ('\n You have selected', f_choose, '\n')
			return f_choose
	else:
		func_exit(1,'null')																				
			
			
			
def func_extension_read(file_address):
	
	para_extension = func_choice(9)
	file_name, file_extension = os.path.splitext(file_address)
	
	if (file_extension == '.txt') and (para_extension == '1'):
		return file_address , para_extension
	elif (file_extension == '.xlsx') and (para_extension == '0'):
		return file_address, para_extension
	else:
		print('file name was: ', file_name)
		print('file extension was: ', file_extension)
		print('para extension was: ', para_extension)
		func_choice(5)
		func_exit(2,'0')

		
		
def func_draw_xls_table(actual_row_start, actual_row_end,  actual_col_start, actual_col_end,workbook, sheet): 			#workbook is still open from previous function call!
	save1, save2, save3, save4, save5, save6 = actual_row_start, actual_row_end,  actual_col_start, actual_col_end,workbook, sheet
	ret_col_start, ret_col_end = func_choice(12)
	print('\n Column range: ', (range(actual_col_start, ret_col_end)))
	print('\n Row range: ', range(actual_row_start, actual_row_end))
	try:
		module_num = []
		module_type = []
		network_name = []
		hs_rear = []
		hs_front = []
		for c in range(actual_col_start, ret_col_end):	
			for r in range(actual_row_start, actual_row_end):
				print('Working on row:', r,'column', c)
				print(sheet.cell_value(r, c))
				if (c == actual_col_start):																		#module number column
					if type(sheet.cell_value(r,c)) == float:
						module_num.append(int(sheet.cell_value(r,c)))
					else:
						module_num.append((sheet.cell_value(r,c)))
				if (c == (actual_col_start + 1)):																#module type column
					if type(sheet.cell_value(r,c)) == float:
						module_type.append(int(sheet.cell_value(r,c)))
					else:
						module_type.append((sheet.cell_value(r,c)))
				if (c == (actual_col_start + 2)):																#network name column
					network_name.append((sheet.cell_value(r,c)))
				if (c == (actual_col_start + 3)):																#handshake rear column
					if type(sheet.cell_value(r,c)) == float:
						hs_rear.append(int(sheet.cell_value(r,c)))
					else:
						hs_rear.append((sheet.cell_value(r,c)))
				if (c == (actual_col_start + 4)):																#handshake front column
					if type(sheet.cell_value(r,c)) == float:
						hs_front.append(int(sheet.cell_value(r,c)))
					else:
						hs_front.append((sheet.cell_value(r,c)))
								
		else:																									#else statement always executed upon completion of the FOR loop
			if (len(module_num) == len(module_type) == len(network_name) == len(hs_rear) == len(hs_front)):
				multi_list = [module_num, module_type, network_name,hs_rear,hs_front]
				return multi_list
			else:
				print('Error in drawing excel table -- not all columns have the same amount of data')
				func_exit(3,'0')
				
				
	except IndexError:
		print('EXCEPTION (IndexError)- column :', c, 'row: ',r,'  The program has likely detected a column which has no values, try adjusting your column range')
		func_draw_xls_table(save1, save2, save3, save4, save5, save6)
		

			
	
	
		
		
def func_read(file_current, para_extension_read ):
	
	if para_extension_read ==  '1':        											# for reading a '.txt' file
		search_term = func_choice(6)
		with open(file_current) as f:   											# open the file and automatically close it when this statement is done
	
			if search_term == 'x.0':												#if the user chooses this option by entering 'x.0', the program will print the file and the return False
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
	
	elif para_extension_read == '0':  												# for reading a '.xls' file
		search_term, column_start, column_end, row_start, row_end = func_choice(11) 
		print(search_term, column_start, column_end, row_start, row_end)	
		workbook = xlrd.open_workbook(file_current) 
		sheet = workbook.sheet_by_index(0)	
		find_row_start, find_row_end, find_col_start, find_col_end, end_loop, ret_val = False, False, False, False, False, 0
		for c in range(column_start, column_end ):
			for r in range(row_start, row_end ):  
				print('Working on row:', r,'column', c)
				print(sheet.cell_value(r, c)) 				
				if str(sheet.cell_value(r,c)).lower() == search_term.lower():
					print('Search term found on row:', r,'column',c)
					find_row_start, actual_row_start, find_col_start, actual_col_start = True, r, True, c
				if str(sheet.cell_value(r,c)).lower() == '~' + search_term.lower():
					print('Search term END found on row:', r,'column', c)
					find_row_end, actual_row_end, find_col_end, actual_col_end = True, r, True, c
				if find_row_start and find_row_end and find_col_start and find_col_end:
					end_loop = True
					break
			if end_loop:
				break
		if end_loop:																#error handling for the case where someone has improperly configured the module list
			err_val = 1																#error free -> err_val stays as 1
			if actual_col_start != actual_col_end:
				print('actual_col_start: ',actual_col_start ,' is not equal to', ' actual_col_end: ',actual_col_end)
				err_val += 2
			if actual_row_start == actual_row_end:
				print('actual_row_start: ',actual_row_start ,' is equal to', ' actual_row_end: ',actual_row_end)
				err_val += 4
			if (actual_row_end - actual_row_start) <= 0:
				print('actual_row_end: ',actual_row_end ,' minus', ' actual_row_start: ',actual_row_start, ' is equal to ',actual_row_end - actual_row_start )
				err_val += 8
			if err_val == 1 :
				print('No errors in column or row configuration detected')
				return func_draw_xls_table(actual_row_start, actual_row_end,  actual_col_start, actual_col_end, workbook, sheet)
				
			else:
				print('err_val: ',err_val,' - program will exit soon')
				func_exit(4,'0')
	
		if err_val == 0:
			print('There is something wrong with your excel configuration: Check for "~" character to end your selection ; Check for correct row/column search ranges')
			print('err_val: ', err_val)
			func_exit(4,'1')
			
			
																
			

					
			
def func_check_filename(para_extension = '1' ):
	# 1 = '.txt'
	# 0 = '.xls'
	if para_extension == '1':
		compare_extension = '.txt'
	elif para_extension == '0':
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

def func_create_1650(single_dim_list, new_file):
		
		DB_Num = str(single_dim_list[0])
		FB_Num = str(single_dim_list[1])
		NW_name = str(single_dim_list[2])
		Hs_Rear = str(single_dim_list[3])
		Hs_Front = str(single_dim_list[4])

		new_file.write('\n \n')
		new_file.write('  ----- '+ NW_name + ' ----- '   ) 
		new_file.write('\n \n')
		new_file.write('A db' + DB_Num +'.dbw.0 ' + ' = '+ Hs_Rear + ' //   hs_rear' )    #create handshake Rear
		new_file.write('\n')
		new_file.write('A db' + DB_Num +'.dbw.2 ' + ' = '+ Hs_Front + ' //  hs_front' )    #create handshake Front
		new_file.write('\n \n')
		new_file.write('CALL FB '+ FB_Num+ ',  db' + DB_Num  )
		new_file.write('\n \n')
		new_file.write('  ----- '+ NW_name + ' ----- '   ) 
		new_file.write('\n \n')
		
		
		print("\n func_create_1650 created FB", FB_Num," with DB", DB_Num, '\n' )


		return
	
	
	
		
	
		
	


def func_output_to_file(multi_dim_list):
	para_extension_write = func_choice(13)
	para_job_type = func_choice(14)
	
	if (para_extension_write == '.txt') and (para_job_type == 'simple'):
		new_name =func_check_filename('1')             		#new_file is given a filename by func_check_filename() where arg ==1 means it will be a .txt file
		print('\n now creating ".txt" file with para_job_type = simple - > ' , new_name, '\n')
		new_file = open(new_name,'w')
		new_file.write(str(multi_dim_list))                     #argument of new_file.write(arg) requirement is that arg must be a string and not a list 
		new_file.close()
	elif (para_extension_write == '.txt') and (para_job_type == 'generate'):
		new_name =func_check_filename('1')             		
		print('\n now creating ".txt" file with para_job_type = generate - > ' , new_name, '\n')
		new_file = open(new_name,'w')
		if (multi_dim_list[0][0].lower() == 'module number') and (multi_dim_list[1][0].lower() == 'module type') and (multi_dim_list[2][0].lower() == 'network name') and 	(multi_dim_list[3][0].lower() == 'handshake rear') and	(multi_dim_list[4][0].lower() == 'handshake front'):	
			for i in range(1,len(multi_dim_list[0])):
					if multi_dim_list[1][i] == 1650:
						single_dim_list = []
						for k in range(0, len(multi_dim_list)):
							single_dim_list.append(multi_dim_list[k][i])											
						else:
							func_create_1650(single_dim_list, new_file)
				
		else:
			new_file.close()
			func_exit(5,'0')
			
		
		
	else:
		new_file.close()
		func_exit(5,'1')	
	

	return True
	
def func_main():
	


	print('Initializing program - you will now select your target file')
	sleep(.2)
	main_file_address = func_select_file()

	print ('Starting Step 2 - call func_extension_read \n')
	sleep(.2)
	main_file_name, main_file_extension_type = func_extension_read(main_file_address)    		#check to see if extension is valid, if so then return the main_file_address again.

	print ('Starting Step 3 - call func_read\n')
	sleep(.2)	
	main_list_output = func_read(main_file_name,main_file_extension_type)
	
	print('Starting Step 4 - call func_output_to_file\n')
	sleep(2)
	func_output_to_file(main_list_output)

	return True




### call of the main function

func_main()


