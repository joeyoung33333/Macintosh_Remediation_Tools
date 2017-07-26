#
# Run Multi
# by Joseph Young
# Version 1.0.0
#
#

import func_features as features
import class_tools as tools

# this function will convert host names into an iterable host object list
def hosts_objects(hostname_list):
	hostname_objects = []

	print("\n" + "Creating Host Objects")
	print("______________________________________________________________________________________\n")

	try:
		for hostname in hostname_list:
			hostname_objects.append(tools.Tools(hostname))
	except:
		print("Unable to create hostname objects")
		print("______________________________________________________________________________________\n")
		return []
	else:
		print("Successfully created hostname objects")
		print("______________________________________________________________________________________\n")
		return hostname_objects


# calls the features func to import files and print in a formatted style
# the function will continue to ask for an input until the correct format is given
def file_import_input():
	index = 9999
	file = "9999"

	print("\n" + " File Loading Information Input")
	print("______________________________________________________________________________________\n")

	while ("." not in file) or (index > 100):
		try:
			file = str(input("Please enter which file you would like to parse (add .txt to the end) "))
			index = int(input("Please enter the the column number (start count with 0) "))
			if ("." not in file) or (index > 100):
				print("Invalid inputs. Try again.")
		except:
			print("Invalid inputs. Try again.")

	print("______________________________________________________________________________________\n")

	try:
		hostname_list = features.load(file, index)
		features.display_data("Hostnames", hostname_list)
	except:
		return []
	else:
		return hostname_list


# calls the features func to export the file to results.txt
# also prints out the data onto the python console
def file_export(failed, completed, other):
	try:
		features.display_data("Completed: " + str(len(completed)), completed)
		features.display_data("Failed: " + str(len(failed)), failed)
		features.export(failed, completed, other)
	except:
		print("Unable to Export/Display Data")


# a callable function wrapped in try statements to ensure the loop continues
# when choosing a function to run change out the ping for a written function in the tools class
def run(host):
	try:
		status = host.ping()
		print(status)
		return status
	except:
		return "failed"


# loops through the entire list to run the host objects through the process
# keeps count of count and current host completed
# keeps tracks of the failed/ completed/ other in a list
def run_all(hostname_objects):
	failed = []
	completed = []
	other = []
	count = 1
	total = len(hostname_objects)

	for index in range(total):
		print('\n' + hostname_objects[index].hostname)
		print(count, "out of", total)
		print("______________________________________________________________________________________\n")
		count += 1

		status = run(hostname_objects[index])
		if "fail" in status:
			failed.append(hostname_objects[index].hostname)
		elif ("success" in status) or ("complete" in status):
			completed.append(hostname_objects[index].hostname)
		else:
			other.append(hostname_objects[index].hostname)
		print("______________________________________________________________________________________\n")

	return failed, completed, other


# main function to run all of the processes
# run main function in the python console to complete the run_multi.py
def main():
	hostname_list = file_import_input()
	hostname_objects = hosts_objects(hostname_list)
	features.delay()
	failed, completed, other = run_all(hostname_objects)
	file_export(failed, completed, other)

main()

