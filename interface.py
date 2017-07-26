#
# Interface for Tools Class
# by Joseph Young
# Version 1.0.0
#

from tkinter import *
import tkinter.messagebox
import run_single


class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.hostname_list = Entry(self.master, width=48, relief=SUNKEN)
		self.grid()
		self.executables = {}
		self.content = StringVar()
		self.createMainMenu()
		self.createSearchBar()

		self.ping_var = IntVar()
		self.check_firewall_var = IntVar()
		self.check_filevault_var = IntVar()
		self.check_os_var = IntVar()

		self.createCheckBox()
		self.createButton()

	# creates the main menu in the menu bar, which includes instructions and ability to exit the program
	def createMainMenu(self):
		menu = Menu(self.master)
		self.master.config(menu=menu)

		fileMenu = Menu(menu)
		menu.add_cascade(label="Menu", menu=fileMenu)
		fileMenu.add_command(label="Instructions", command=self.directionsMessageBox)
		fileMenu.add_separator()
		fileMenu.add_command(label="Quit", command=quit)

	# the search bar allows you to input the hostname(s) you would like to run the program against
	def createSearchBar(self):
		self.hostname_list.grid(row=1, columnspan=8, padx=3, pady=3)
		self.content.set("hostname")
		self.hostname_list["textvariable"] = self.content

	# creates the checkboxes for the user to select which Tool class functions they would to run against the hostnames
	def createCheckBox(self):
		padding = 3

		ping = Checkbutton(self.master, text="Ping", variable=self.ping_var,
						   command=self.addExecutable("ping", self.ping_var.get()))
		ping.grid(row=3, column=3, padx=padding, pady=padding, sticky=W)

		check_firewall = Checkbutton(self.master, text="Check FireWall", variable=self.check_firewall_var,
									 command=self.addExecutable("check_firewall", self.check_firewall_var.get()))
		check_firewall.grid(row=4, column=0, padx=padding, pady=padding, sticky=W)

		check_filevault = Checkbutton(self.master, text="Check FileVault", variable=self.check_filevault_var,
									  command=self.addExecutable("check_filevault", self.check_filevault_var.get()))
		check_filevault.grid(row=4, column=1, padx=padding, pady=padding, sticky=W)

		check_os = Checkbutton(self.master, text="Check OS", variable=self.check_os_var,
							   command=self.addExecutable("check_os", self.check_os_var.get()))
		check_os.grid(row=4, column=2, padx=padding, pady=padding, sticky=W)

	# creates the button to quit or run the program
	def createButton(self):
		quit_button = Button(self.master, text="Exit Program", command=quit)
		quit_button.grid(row=5, column=1, padx=5, pady=5)
		run_button = Button(self.master, text="Run Program", command=self.run)
		run_button.grid(row=5, column=0, padx=5, pady=5)
		run_button.bind()

	# executable function that checks self.exectuable dictionary for 1 (run) or 0 (don't run)
	def addExecutable(self, com, var):
		if var == 1:
			self.executables[com] = var
		elif var != 1:
			self.executables[com] = var

	# menu box accessed by the main menu function
	# gives the user a pop up with instructions
	def directionsMessageBox(self):
		title = "Instructions"
		message = "Welcome to the Macintosh Remediation Tool\n" \
				  "Tool Instructions:\n" \
				  "1. Enter the hostname(s) of the user(s) (Note: Separate users with a ,)\n" \
				  "2. Select the actions you would like to perform \n" \
				  "3. Select Run Program\n" \
				  "4. Exit or Quit the program once you are finished"
		tkinter.messagebox.showinfo(title, message)

	# at the start it will refresh the checkboxes and get the list of executables
	def run(self):
		self.createCheckBox()
		print("\nList of Executables")
		print("______________________________________________________________________________________\n")
		print(self.executables)
		print("______________________________________________________________________________________\n")

		# parse the hostnames into a list
		hostnames = self.hostname_list.get().strip().split(",")
		count = 1
		total = len(hostnames)
		output = ""

		# iterate through the hostname list and print the status
		for host in hostnames:
			host = host.strip()
			print('\n' + host)
			print(count, "out of", total)
			print("______________________________________________________________________________________\n")
			# for each host, iterate through the executable dictionary
			for command, status in self.executables.items():
				if status == 1:
					print("\nCurrently working on " + command)
					print("----------------------------------")
					if command == "ping":
						output += host + ": " + run_single.ping(host) + "\n"
					elif command == "check_firewall":
						output += host + ": " + run_single.check_fire_wall(host) + "\n"
					elif command == "check_filevault":
						output += host + ": " + run_single.check_file_vault(host) + "\n"
					elif command == "check_os":
						output += host + ": " + run_single.check_os(host) + "\n"
			print("______________________________________________________________________________________\n")
			count += 1

		# pop up message for the completion status of the program
		tkinter.messagebox.showinfo("Macintosh Remediation Report", output)

# create the root object for TKinter
root = Tk()

# Initial interface setup and placement
root.title("Macintosh Remediation Tools")
label = Message( root, text="Macintosh Remediation Tools by Joseph Young", relief=RAISED, width=800, padx=3, pady=3)
label.grid(row=0, columnspan=8)
help = Message( root, text="*See menu for instructions", width=500, padx=3, pady=3)
help.grid(row=6, columnspan=8, sticky=W)
root.geometry("450x220")

# application class with root object
app = Application(master=root)

# conintuous loop of the program to keep it active
app.mainloop()

# end of program
root.destroy()
