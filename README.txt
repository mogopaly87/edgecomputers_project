Follow the instructions below to setup:


***NOTE****:
BEFORE YOU START THIS SETUP, YOU NEED TO HAVE ALREADY SETUP THE DATABASE USING THE 'EdgeComputersDB' SCRIPT THAT COMES WITH THIS PROJECT.



1. Set environment variables for your MySQL username and password. Use the variable names below for username and password respectively:
	a. MYSQL_USER 
	b. MYSQL_PASSWORD 

To set environment variables, use the commands below:

****NOTE: Substitute '<Your username>' for your actual database username and '<Your password>' for your actual database password. *****

 a. For database username:

     [System.Environment]::SetEnvironmentVariable('MYSQL_USER', '<Your username>', [System.EnvironmentVariableTarget]::User)

 b. For database password:

     [System.Environment]::SetEnvironmentVariable('MYSQL_PASSWORD', '<Your password>', [System.EnvironmentVariableTarget]::User)

2. Change directory/folder to the main project directory 'edge_computers'. 

3. Create a virtual environment with the command:

	python -m venv 'environment name'

**Where 'environment name' can be any name you choose for your virtual environment. 

4. Activate your virtual environment with the command(s):

	'environment name'/Scripts/activate (for Linux & MacOS)
	'environment name'\Scripts\activate (for Windows)

5. Install dependencies with the command:
	pip install -r requirements.txt


6. Now you're ready to launch the program. Run the module named 'interface.py' to intialize the application using the command:
	python interface.py

