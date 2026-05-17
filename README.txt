===============================
Mini Shell in Python - README
===============================

Description:
------------
This project is a simple Linux Mini Shell written in Python.
It can execute basic Linux commands such as:

- ls
- pwd
- cd
- mkdir
- touch
- cat
- echo
- history
- ps
- ping
- ifconfig
- grep
- wc
- and more

A special command called:

    Commands

will display all supported commands inside the shell.


Requirements:
-------------
- Linux Operating System
- Python 3 installed

Check Python version:

    python3 --version


Files:
------
- mini_shell.py
- README.txt


How to Run:
-----------

1) Open the Linux terminal

2) Navigate to the project directory

Example:

    cd ~/Desktop/project_folder

3) Give execution permission to the script

    chmod +x mini_shell.py

4) Run the shell

Option 1:

    python3 mini_shell.py

Option 2:

    ./mini_shell.py


Using the Shell:
----------------

After running the script, you will see:

    Welcome to Python Mini Shell

You can now type Linux commands.

Example:

    pwd
    ls
    mkdir test
    cd test
    touch file.txt
    echo Hello
    history

To display all available commands:

    Commands

To exit the shell:

    exit


Notes:
------
- Some commands depend on Linux tools being installed.
- Certain commands may require sudo/root privileges.
- This project is intended for educational purposes.


Author:
-------
Mini Shell Project in Python
