# Macintosh_Remediation_Tools

The Macintosh Remediation Tool is an application that gives IT admins the ability to remotely send fixes to machines. For my specific purpose I used the tool to re-install security software, send patches, trigger pre-installed packages, run recon, and help manage or re-ernoll systems into JSS/Casper when the systems were unable to report (but could still on the domain). The backend portion of the Application runs on the pexpect library (interacting with Terminal) to SSH into users computers and execute commands. I have taken out most of the functions/information relate to my employer, but I have left the framework, GUI, and logic. Simiply read the comments, notes, and look at my examples. I have left the framework in such a way that all you will need to do is test the commands in terminal to find the correct and incorrect outputs and fill them into a class function. If you would like to use the GUI, then you will need to create buttons for it with TKinter. Again, look at the notes and previous examples, then copy and paste, and fill in the changes. 

# Uses and Automation

I implemented this tool because the Macintosh Management software (JSS/Casper) had lost contact with over 30% of our systems. Instead of manually connecting to the machines one by one, or calling each user to re-enroll themselves through the JSS Prompt/Enrollment package. I was able to remotely trigger the re-enroll package (Cached on all Machines) by SSHing into the Admin account of each user's machine. The single_run.py interacts with the GUI allowing you to run users through it, but it can actually handle multiple users with a "," seperator. The multi_run.py allows you to import a file and automate the run across all of the users. I also opened multiple conosles to run the program similtaneously against a list split into 3. 

The program automates the process of creating a command, opening a terminal prompt, typing in the command, entering the multiple passwords, follow-up commands, and waiting for the program to finish executing. This tool works well for a large number of users connected to the domain, or as a tool for technicans who can use the GUI to remotely repair a users computer without having to see them or call them. 

# Files

#### class_complaince.py

The compliance class was created as a general complaince tool for checking Operating Systems, FireWall, FileVault, and many other things. Using pexpect, the class generate a command for each of the functions. The class has been organized into functions 

#### class_tools.py

The tools class was created with the same framework as the complaince class but uses different password, timers and types of functions. The tools class was created to organize company tools that would allow me to install security software, push patches, and trigger packages.

#### func_features.py
#### interface.py
#### run_multi.py
#### run_single.py
#### results.txt
#### import.txt


