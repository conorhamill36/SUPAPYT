#Program written for SUPAPYT course
#C. B. Hamill 04/02/2020
#conor.hamill@ed.ac.uk

import math, statistics

def main():
	print("hello world")
	
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
	
	print(input_file_lines[0].split(',').index("moid"))
	
	print(input_file_lines[0].split(',').index("full_name"))
	
	#Make array of MOID values
	moid_array = []
	smallest_moid = 100000
	largest_moid = 0
	for line in input_file_lines:
		#Breaking up text with commas as delimiters
		line_split = line.split(',')
		
		if line_split[11] != '' and line_split[11] != 'moid':
			#Check if smaller than smallest
			if(float(line_split[11]) < smallest_moid): #new smallest moid found
				smallest_moid = float(line_split[11]) 
				smallest_moid_name = line_split[0]
				
			if(float(line_split[11]) > largest_moid): #new largest moid found
				largest_moid = float(line_split[11]) 
				largest_moid_name = line_split[0]
				
		#print(line_split)
		
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
	print("Standard deviation is {}".format(stddev_diameter))
	print("Mean is {}".format(mean_diameter))

	
	
	
	
	
	
	
	
	input_file.close()
	
main()	