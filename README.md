# Macintosh_Remediation_Tools

The Macintosh Remediation Tool is an application that gives IT admins the ability to remotely send fixes to machines. For my specific purpose I used the tool to re-install security software, send patches, trigger pre-installed packages, run recon, and help manage or re-ernoll systems into JSS/Casper when the systems were unable to report (but could still on the domain). The backend portion of the Application runs on the pexpect library (interacting with Terminal) to SSH into users computers and execute commands. I have taken out most of the functions/information relate to my employer, but I have left the framework, GUI, and logic. Simiply read the comments, notes, and look at my examples. I have left the framework in such a way that all you will need to do is test the commands in terminal to find the correct and incorrect outputs and fill them into a class function. If you would like to use the GUI, then you will need to create buttons for it with TKinter. Again, look at the notes and previous examples, then copy and paste, and fill in the changes. 

# Uses and Automation

I implemented this tool because the Macintosh Management software (JSS/Casper) had lost contact with over 30% of our systems. Instead of manually connecting to the machines one by one, or calling each user to re-enroll themselves through the JSS Prompt/Enrollment package. I was able to remotely trigger the re-enroll package (Cached on all Machines) by SSHing into the Admin account of each user's machine. The single_run.py interacts with the GUI allowing you to run users through it, but it can actually handle multiple users with a "," seperator. The multi_run.py allows you to import a file and automate the run across all of the users. I also opened multiple conosles to run the program similtaneously against a list split into 3. 

The program automates the process of creating a command, opening a terminal prompt, typing in the command, entering the multiple passwords, follow-up commands, and waiting for the program to finish executing. This tool works well for a large number of users connected to the domain, or as a tool for technicans who can use the GUI to remotely repair a users computer without having to see them or call them. 

# Files

#### class_tools.py

The tools class was created as a general tool for checking Operating Systems, FireWall, FileVault, Pinging and many other things. For differnt outputs I reccomend creating different classes for the OS, FireWall, and FileVault so it can return On or OFF. Using pexpect, the class generates a command for each of the functions. The class has been organized into functions. By editing the tools class and creating new classes you can remotely install security software, push patches, and trigger packages.

#### func_features.py

Extra functions to help with organizations/presentation of data. These including importing, parsing, exporting, and displaying data functions. There is an additional delay function to help with time zone differences.

#### interface.py



#### run_multi.py

run_multi.py runs any number of hostnames from an imported text file. The program parses based on "\n" and ony accepts text files like .txt or .tsv. Run the program main() and it will first ask you to import a file name, and input the column number starting with 0. It then parses the file and creates a list of hostname objects to be run into the tools class. The host objects will be iterated and have the given command ran on them. The progam will keep track of successful, failed, and other records. At the end of the program, it will export and print the results. 

#### run_single.py

run_single.py contatins functions calling each of the tool class function. It first converts the hostname into an object, then runs the given command. This was created to give the interface program an easy one call function. Every tool duplicated within the class_tools.py will also need to be duplicated here.

#### results.txt

The results.txt file will be exported as a result of the export function. This file has the succcessfuly, failed, and other data for the given commands that were ran. Be sure to save the file in another location/name becuase the program write over the file.

#### import.txt

Import is a arbitrary name given to a file that you will import. This file will only be used when running the run_multi.txt. The python console will ask you to input a file name. Make sure this is a text file like a .txt or .tsv. 


