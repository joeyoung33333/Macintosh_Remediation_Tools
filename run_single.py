#
# Run Single
# by Joseph Young
# Version 1.0.0
#
#


import class_tools as tools


# run single was created to give the interface an easy one call function for running a command
# the functions are wrapped in try statements to ensure that the program will safely continue to run and not break

def ping(host):
	try:
		# the user is converted into an object
		user = tools.Tools(host)
		# the object is called to run a function and it is checked
		status = user.ping()
		print(status)
		return status
	except:
		return "failed"

def check_file_vault(host):
	try:
		# the user is converted into an object
		user = tools.Tools(host)
		# the object is called to run a function and it is checked
		status = user.check_file_vault()
		print(status)
		return status
	except:
		return "failed"

def check_fire_wall(host):
	try:
		# the user is converted into an object
		user = tools.Tools(host)
		# the object is called to run a function and it is checked
		status = user.check_fire_wall()
		print(status)
		return status
	except:
		return "failed"

def check_os(host):
	try:
		# the user is converted into an object
		user = tools.Tools(host)
		# the object is called to run a function and it is checked
		status = user.check_os()
		print(status)
		return status
	except:
		return "failed"