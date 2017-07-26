#
# Features
# by Joseph Young
# Additional Features for Scripts
# Version 1.0.0
#


import time

# add the delay function to run commands after a certain amount of time
# helpful for users in different time zones
# add the number of minutes to delay
def delay():
	print("TIMER\n______________________________________________________________________________________\n")
	minutes = float(input("How many minutes do you want to delay? "))
	print("Wait for", minutes, "minute(s)...")
	minute_seconds = minutes * 60
	time.sleep(minute_seconds)
	print("\n______________________________________________________________________________________\n")


# load function to take care of loading and parsing data
def load(file, index):
	print("LOADING FILE\n______________________________________________________________________________________\n")
	try:
		print("Reading file...")
		raw_data = open(file, "r")
		raw_data_values = raw_data.read().strip().split("\n")
		raw_data.close()
	except:
		print("Unable to read file...")
		return []
	else:
		print("Parsing file...")
		final_list = []
		try:
			for line in raw_data_values:
				final_list.append(line.strip().split("\t")[index])
		except:
			print("Unable to parse file - check index!!!")
			print("\n______________________________________________________________________________________\n")
			return []
		else:
			print("List was successfully parsed!!!")
			print("\n______________________________________________________________________________________\n")
			return final_list


# export function to take care of lists and export them into a file
def export(failed, completed, other):
	print("FILE EXPORT\n______________________________________________________________________________________\n")
	try:
		results = open("results.txt", "w")
		results.write("Results\n\n")
		results.write("Completed: " + str(len(completed)) + "\n" + str(completed) + "\n\n")
		results.write("Failed: " + str(len(failed)) + "\n" + str(failed) + "\n\n")
		results.write("Other: " + str(len(other)) + "\n" + str(other) + "\n\n")
	except:
		print("Unable to export results...")
		print("\n______________________________________________________________________________________\n")
		results.close()
	else:
		print("Results have been exported")
		print("\n______________________________________________________________________________________\n")
		results.close()


# an organized way to display data within the console
# uses the same format as the other functions
def display_data(title, data):
	print(title + "\n______________________________________________________________________________________\n")
	print(data)
	print("\n______________________________________________________________________________________\n")

