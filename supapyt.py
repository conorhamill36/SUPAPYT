#Program written for SUPAPYT course
#C. B. Hamill to be submitted 07/02/2020
#conor.hamill@ed.ac.uk

import math, statistics
import csv

#Function finds the year at the start of a decade for a year
def year_to_decade(year):
	decade = year - (year % 10)
	return decade
	
def date_breakdown(date):
		year = date[:4]
		month = date[5:7]
		day = date[-2:]
		return day, month, year
	

def main():
	
	#Opening cvs file
	input_file = open('small-body-db.txt','r')
	input_file_lines = input_file.readlines()
	
	#Printing out lines to check it's working
	for line in input_file_lines:
		#print(line)
		continue #command to avoid indented line issue
	input_file.seek(0) #Going to top of file again
	del input_file_lines
	input_file_lines = input_file.readlines()

	'''
	1) The names of the objects with the smallest and largest 
	minimum orbit intersection distance (MOID) to Earth (the "moid" column). 
	Not all entries have a "moid" value - those without one should be ignored.
	'''
	print("Columns names are {}".format(input_file_lines[0]))
	
	# print(input_file_lines[0].split(',').index("moid"))
	# print(input_file_lines[0].split(',').index("full_name"))
	
	#Make array of MOID values
	moid_array = []
	smallest_moid = 100000
	largest_moid = 0
	for line in input_file_lines:
		#Breaking up text with commas as delimiters
		line_split = line.split(',')
		
		if line_split[11] != '' and line_split[11] != 'moid': #Skips empty entries and first line
			#Check if smaller than smallest
			if(float(line_split[11]) < smallest_moid): #new smallest moid found
				smallest_moid = float(line_split[11]) 
				smallest_moid_name = line_split[0]
			#Check if largest than largest	
			if(float(line_split[11]) > largest_moid): #new largest moid found
				largest_moid = float(line_split[11]) 
				largest_moid_name = line_split[0]
				
	print("\nQuestion 1:")	
	print("smallest_moid is {}, smallest moid name is {}".format(smallest_moid, smallest_moid_name))
	print("largest_moid is {}, largest moid name is {}".format(largest_moid, largest_moid_name))
	
	
	'''2) The mean and standard deviation of the diameters of the 
	objects (the "diameter" column).'''
	
	print(input_file_lines[0].split(',').index("diameter"))


	diameter_list = [] #defining list to put all diameter values in to
	
	for line in input_file_lines:
		line_split = line.split(',')
		#avoids empty diameter values and the first line with the column names
		if line_split[4] and line_split[4] != 'diameter':  
			diameter_list.append(float(line_split[4]))
	
	mean_diameter = statistics.mean(diameter_list)
	stddev_diameter = statistics.stdev(diameter_list)
	
	print("\nQuestion 2:")
	print("Standard deviation of diameters of	 objects is {}".format(stddev_diameter))
	print("Mean of diameters of objects is {}".format(mean_diameter))

	
	'''3) The min, max, mean and standard deviation of the MOID to Earth for 
	objects with the Near-Earth Object flag = Y ("neo" column), and separately 
	for objects with the Potentially Hazardous Asteroid flag = Y ("pha" column).'''

	print(input_file_lines[0].split(',').index("neo"))
	print(input_file_lines[0].split(',').index("pha"))
	print(input_file_lines[0].split(',').index("moid"))

	moid_neo_array = [] #initialising array of moids for near earth objects
	moid_pha_array = []	#initialising array of moids for potentially hazardous asteroids
	
	input_file.close()
	
	#Trying using csv reader 	
	with open('small-body-db.txt', newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		#This is much easier...
		
		for row in reader: 
			#picking out moids for neo
			if row['neo'] == 'Y':
				#print(row['moid'])
				moid_neo_array.append(float(row['moid']))
				
			#picking out moids for phas
			if row['pha'] == 'Y':
				#print(row['moid'])
				moid_pha_array.append(float(row['moid']))
			
		
		#Min, max, mean of moid_neo_array
		print("\nQuestion 3:")
		print("Moid_neo_array - Min:{} Max:{} Mean:{}".format(min(moid_neo_array), max(moid_neo_array), statistics.mean(moid_neo_array)))
		print("Moid_pha_array - Min:{} Max:{} Mean:{}".format(min(moid_pha_array), max(moid_pha_array), statistics.mean(moid_pha_array)))
	
		
	'''4) How many objects have been found by each person/group/institution ("producer" column).'''

		
	#print("Producer column is {}".format(input_file_lines[0].split(',').index("producer")))
		
	
	#Setting up list of unique producers
	producers_unique_list = []
	with open('small-body-db.txt', newline='') as csvfile:	
		reader = csv.DictReader(csvfile)
		for row in reader:			
			#if row['neo'] == 'Y':
			#print(row['producer'])
			if(row['producer']):
				if row['producer'] not in producers_unique_list:
					producers_unique_list.append(row['producer'])
				
		#print(producers_unique_list)
	
	#Setting up dictionary for counting each of the unique producers 
	producers_dict = {}
	#Initialising producers_dict with zeroes
	for item in producers_unique_list:
		producers_dict[item] = 0
	#print(producers_dict)	
	
	#Iterating through data and counting the number of observations by each producer
	with open('small-body-db.txt', newline='') as csvfile:	
		reader = csv.DictReader(csvfile)
		for row in reader:
			if row['producer']: #Checking if a producer is listed
				#print(row['producer'])
				dummy_variable = producers_dict[row['producer']]
				producers_dict[row['producer']] = dummy_variable + 1
	print("\nQuestion 4:")
	#print(producers_dict)
	print("Producers \t No. observations")
	for item in producers_dict:
		print(item," ", producers_dict[item])
	
	'''5) The names of the objects with the earliest and latest 
	first observation ("first_obs" column).'''
	#Shall attempt this a slightly different way from question 1
	
	#Initialising list of observations
	first_obs_list = []
	name_list = []
	with open('small-body-db.txt', newline='') as csvfile:	
		reader = csv.DictReader(csvfile)
		for row in reader:
			# print(row['first_obs'])
			first_obs_list.append(row['first_obs'])
			name_list.append(row['full_name'])
			
	#Initilaising variables to use
	earliest_year = earliest_month = earliest_day = 10000
	latest_year = latest_month = latest_day = 0
	
	for date in first_obs_list:
		# print(date)
		
		#Break up date in to date, month, year
		day, month, year = date_breakdown(date)
		
		# print(year, month, day)		
			
		if(year.isdigit() == 0 or month.isdigit() == 0 or day.isdigit() == 0):
			#print("Digit not found, skipping entry with date{}".format(date)
			continue
		
		year = float(year)
		month = float(month)
		day = float(day)
		
		#Checking if date is earlier than earliest year
		if(year <= earliest_year):
			if(month <= earliest_month):
				if(day < earliest_day):
					earliest_day, earliest_month, earliest_year = day, month, year
					earliest_date = '{}-{}-{}'.format(int(earliest_year), int(earliest_month), int(earliest_day))
					earliest_name = name_list[first_obs_list.index(date)]
					#print("New earliest date of {}, with name {}".format(earliest_date, earliest_name))
	
	#Checking if date is later than latest year
		if(year >= latest_year):
			if(month >= latest_month):
				if(day >= latest_day):
					latest_day, latest_month, latest_year = day, month, year
					latest_date = '{}-{}-{}'.format(int(latest_year), int(latest_month), int(latest_day))
					latest_name = name_list[first_obs_list.index(date)]
					#print("New latest date of {}, with name {}".format(latest_date, latest_name))
	print("\nQuestion 5:")
	print("Earliest first observation is {}, with a name of {}".format(earliest_date, earliest_name))
	print("Latest first observation is {}, with a name of {}".format(latest_date, latest_name))
	
	'''6) The mean absolute magnitude ("H") of objects with first observation in 
	each decade (group the objects according to the decade of their first
	observation and calculate the mean "H" for each group). A decade is defined 
	as, eg, 2000-01-01 to 2009-12-31 inclusive. If there are no entries for a 
	given decade, or no entries with an "H" value, it should be skipped.'''
	
	#print(input_file_lines[0].split(',').index("H"))
	
	with open('small-body-db.txt', newline='') as csvfile:
		#Defining list with start decade and H value
		decade_list = []	
		unique_decades_list = [] #list where each decade only appears once
		reader = csv.DictReader(csvfile)

		for row in reader:
			#First finding which decades are contained in the data set
			#Interested in years for the first observation
			date = row['first_obs']
			day, month, year = date_breakdown(date)
			year = int(year)
			decade = year_to_decade(year)
			# print(decade)
			if row['H']:
				H_value = float(row['H'])
				decade_list.append((decade, H_value))
			
			if row['H'] and decade not in unique_decades_list:
				#print("New date found: {}".format(decade))
				#print(row['full_name'])
				unique_decades_list.append(decade)
		
			
		unique_decades_list.sort() #Arranges list of decades in increasing size
		print("Unique decades list:")
		print(unique_decades_list)
		#Initialsing sorted decade list
		sorted_H_decade_list = []
		
		# print(len(decade_list))
		# print(decade_list[0])
		
		# for item in decade_list: #Testing to check matching of decades works
			# #print(item[0])
			# if(1890 == item[0]):
				# print("1890 found")
				
		print("\nQuestion 6:")
		decade_index = 0
		for decade in unique_decades_list: #Iterating over each decade that's been found
			#print(decade)
			for item in decade_list:
				#print(item[0], decade)
				#print(type(item[0]), type(decade))
				if item[0] == decade:
					sorted_H_decade_list.append(item[1])
					#print(len(sorted_H_decade_list))	
					#print("Decade match found")
					#print(item[0], decade)
					
			decade_mean = statistics.mean(sorted_H_decade_list) #Mean for a particular decade calculated
			# print("For decade starting {}, the mean is {}".format(decade, decade_mean))
			decade_index = decade_index + 1
			print("For decade beginning {}, mean is {}, with {} entries".format(decade, decade_mean, len(sorted_H_decade_list)))
			
			#Empties list so new elements can be added
			sorted_H_decade_list.clear()
	
		#print(unique_decades_list)
		#print(decade_list)
	
	
	
main()	