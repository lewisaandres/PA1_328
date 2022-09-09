'''
This program is used to run all student submissions in batch and test 
each program against a testcase set saved in a text file.

The program generates report for each submission.

Written by: Arjang Fahim

version: 1.0.0
'''


import os
import subprocess as sp

# This folder contains the submitted assignments from students
assignment_folder = "C://Users//Lewis//Desktop//Fall_2022_Source_Code//New_PA1_328"

# This folder contains reports generated by this program.
# For each submmission the program generated one report
evaluation_folder = "C://Users//Lewis//Desktop//Fall_2022_Source_Code//New_PA1_328"

# A text file contains all test cases.
testcase_file = "C://Users//Lewis//Desktop//Fall_2022_Source_Code//New_PA1_328/testcase.txt"

f = open(testcase_file, "r")
testcases_list = f.readlines()
f.close()

# Filter files to get only python files 
files_list =  [f for f in os.listdir(assignment_folder) if f[len(f)-2:len(f)] == "py"]

counter = 1
passcount = 0
notpasscount = 0
finaloutput = ""
pass_test = ""

for f in files_list:
	if os.path.isfile(evaluation_folder + "\\" + f + ".txt"):
		os.remove(evaluation_folder + "\\" + f + ".txt")
	fh = open(evaluation_folder + "\\" + f + ".txt", "a")
	for tcl in testcases_list:
		tc = tcl.split(":")[0]
		
		correct_output = tcl.split(":")[1]  
		run_command = 'python ' + assignment_folder + "/" + f + " " + tc
		output = sp.getoutput(run_command)
		if output.strip() == correct_output.strip():
			pass_test = "pass"
			passcount += 1
		else:
			pass_test = "Not pass"
			notpasscount += 1

		finaloutput += str(counter) + "\n" + tc.strip() + "\n" 
		finaloutput += "The correct output is: " + correct_output + "Your output is: " + output + "\n"
		finaloutput += "pass\\not pass: " + pass_test + "\n"
		counter += 1
		
	finaloutput += "\n" + "Total correct answers: " + str(passcount) + "\n"
	finaloutput += "Total incorrect answers: " + str(notpasscount) + "\n" 
	print(finaloutput)
	fh.write(finaloutput + "\n")

	fh.close()
	counter = 0
	passcount = 0
	notpasscount = 0
	finaloutput = ""