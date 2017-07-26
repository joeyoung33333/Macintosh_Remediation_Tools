#
# Tools for Macintosh Machines
# by Joseph Young
# Version 1.0.0
#
# This program will SSH into the user's computer
# The program will continue and check for a given instance bellow
#

import pexpect



class Tools:
	def __init__(self, hostname):
		# put in the information for the command, you can take out the self. variables and add them  into the ssh command
		# be sure to leave the hostname, because this is the changing variable
		self.hostname = hostname
		self.admin_account = "<admin>"
		self.domain = "<domain.com>"

		# most commands will use the following format
		# ssh -t admin@hostname.domain.com
		self.ssh_command = "ssh -t " + self.admin_account + "@" + self.hostname + self.domain

	def tool_name(self):
		# see ping bellow for an idea of how the function works, copy and paste to create multiple functions
		# current command takes the ssh command and adds the executable command
		# most commands will use the following format
		# ssh -t admin@hostname.domain.com "sudo <executable command>"
		# unfortunately, pexpect does not work well to send multiple terminal commands in the sendline, but
		# to send multiple commands to run after one another do the following with ";":
		# ssh -t admin@hostname.domain.com "sudo <executable command>; sudo <executable command>; sudo <executable command>"
		curr_command = self.ssh_command + " \"sudo <executable command>\""

		# the succes and fail variable take the terminal output that tell whether or not the executable command
		# was successfully run. You will need to manually run the commands and see what the correct and
		# incorrect outputs are
		success = "Successfully Installed"
		success = "Failed to Instal"

		# the timer is the amount of time given before the program will time out
		# be sure to time your programs and give it enough time to complete
		# the timer unfortunately will not timeout or cancel on a machine it waits to connect to, but run the entire time
		timer = 360

		# the run command will return if the program ran successfully or not
		status = self.run(curr_command, success, success, timer)

		# this will return the Name of the tool and its status to the run_.py
		return "Tool Name " + status

	def ping(self):
		# here is an example of how to ping a user, which can be used to automate the ping on hundreds of users
		# notice the non standard format for ping compared to above. You can edit and add your own
		curr_command = "ping " + self.hostname + ".domain.com"

		# A ping is successful when the program sees the output for "64 bytes..."
		# A ping is unsuccesful when it sees the output for "Request timeout"
		# There may be more fail commands, but in the format I have for the bellow self.run, it only takes one
		# successful and one fail, so for other fail commands it will have to wait and timeout
		ping_success = "64 bytes from"
		ping_fail = "Request timeout"

		# ping is a very quick process and will timeout after 25 seconds
		timer = 25
		status = self.run(curr_command, ping_success, ping_fail, timer)

		# returns if the ping failed or succeeded
		return "Ping " + status

	# here are some more examples
	# originally, i had a seperate class called compliance for the 3 functions bellow to say On/Off instead of Success/Fail
	def check_file_vault(self):
		curr_command = self.ssh_command + " \"sudo fdesetup status\""
		filevault_off = "FileVault is Off"
		filevault_on = "FileVault is On"
		timer = 30
		status = self.run(curr_command, filevault_on, filevault_off, timer)
		return "FileVault " + status

	def check_fire_wall(self):
		curr_command = self.ssh_command + " \"/usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate\""
		firewall_off = "Firewall is not enabled."
		firewall_on = "Firewall is enabled."
		timer = 30
		status = self.run(curr_command, firewall_on, firewall_off, timer)
		return "FireWall " + status

	def check_os(self):
		curr_command = self.ssh_command + " \"sw_vers -productVersion\""
		curr_OS = "10.12"
		old_OS = "10.11"
		timer = 30
		status = self.run(curr_command, curr_OS, old_OS, timer)
		return "Current Operating System " + status

	def run(self, command, success, fail, timer):
		# When SSHing into a users computer they may want you to authenticate
		# The bellow commands handles the expected authentication command and the command to send back in return
		exp_authen = "Are you sure you want to continue*"
		give_authen = "yes"

		# In order to access a user's machine you will need to enter the admin passsword account you are trying to access
		# <admin>@hostname expects the password for the admin
		# the bellow handles the expected prompt to be asked for the password, and the password to send back in return
		exp_mac_pass = "[P-p]assword.*"
		give_mac_pass = "<Password>"

		# when a hostname hasnt connected to the domain in a while or has been removed, you can't resolve the hostname
		# this command will save time by returning a failed instance instead of waiting to timeout
		exp_uh_1 = "cannot resolve"
		exp_uh_2 = "Could not resolve hostname"

		# declaring the index output for send_command, which will return an index starting at 0 for the given list
		# of inputs
		index = 99

		# all the commands are wrapped in try statements to prevent the program from breaking during the middle of a run
		try:
			# send command is the object
			# spawning a command is the equivelent to opening the terminal, typing the command, and hitting enter
			# timer is the amount of time to pass before timing out
			send_command = pexpect.spawn(command, timeout=timer)
		except:
			# exception statement to return if the above command failed to spawn
			print("Unable to spawn command " + command)
			return "failed"
		else:
			# printing step by step to help track when issues arise in the console
			print("Command spawned: " + command)
			print("Please wait for command to run all the way through or timeout!")

			# index 2 and 3 let the program know when it has successfully installed or failed ro install
			while index != 2 and index != 3:
				try:
					# the index will be a number starting with 0
					# when the expected output is recieved from the terminal, the index will output that number
					index = send_command.expect([exp_authen, exp_mac_pass, success, fail, exp_uh_1, exp_uh_2])
				except:
					# if non of the indexes are found for some reason, the timer will timeout
					# be careful becuae if you are installing then the expected output may take a few minutes
					print("Unable to find index.")
					# closes the connection to the terminal
					send_command.close()
					return "failed"
				else:
					# lets the user know which index was found
					print("Index found at: " + str(index))

					# the first index in the list will send the authetication back
					if index == 0:
						send_command.sendline(give_authen)
						print("Authentication sent...")

					# the second index will send the password back
					elif index == 1:
						send_command.sendline(give_mac_pass)
						print("Admin password sent...")

					# the third will see if the successful exp was found
					elif index == 2:
						print(send_command.before)
						print(send_command.after)
						send_command.close()
						return "successful"

					# the fourth will see if the fail exp was found
					elif index == 3:
						print(send_command.before)
						print(send_command.after)
						send_command.close()
						return "failed"

					# the last two indexes check to see if the hostname is resolvable
					elif (index == 4) or (index == 5):
						print(send_command.before)
						print(send_command.after)
						send_command.close()
						return "Unable to Connect to Host"
