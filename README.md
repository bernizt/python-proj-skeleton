# Python Project Skeleton

Kickstart your Python script with this easy to use project structure! The only requirement is to have a working Python 3 interpreter.

It works as follows:
1. Development happens in a Python virtual environment (inside .venv), so no need to mess with global installations
2. A cmd file is provided, which automatically creates the required virtual environment and runs your script

## How To Use

Start by running *example.cmd*. A *.venv* directory, containing a virtual environment, will be created and *src/example.py*, executed. If you are using vscode, the new venv should be detected automatically.

Start writing your script, using *example.py* as a base (or not). It is probably a good idea to rename both this script and the cmd file to whatever name you choose for your script. Edit the cmd file accordingly to point to your python script.

If you need to instal additional Python modules, make sure to keep the *requirements.txt* file updated with the following command:

> .venv\Scripts\pip.exe freeze > requirements.txt

**Note:** if you are using modules such as *autopep8* (only needed during development), you might want to manually remove them from this file.

If someone wants to run your script, they only needs to install Python 3. Executing the cmd file will create the required virtual environment, install the modules specified in *requirements.txt* and run your Python script automatically. You don't need to share the .venv directory.