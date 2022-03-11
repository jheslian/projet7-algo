# Problem solving with python algorithm.

## Objectives:

- Given a csv with 20 actions, create a file `brutforce.py` that contains a brutforce algorithm that test all the possible action that fits the budget of 500.00 and that has the best profit
- Given 2 csv files with 1000 actions each, create a file `optimized.py` with an algorithm that optimise the bruforce solution.


## Getting started:
**Note**: Make sure you have python, virtual environment and git on your machine : 
	- `python -V` : command to check the version python if its installed
	- verify that you have the venv module : `python -m venv --help` if not please check https://www.python.org/downloads/. You could also use any other virtual environment to run the program(**if you opted to use other virtual environment the next commands are not suitable to run the program**)
	- `git --version` : to check your git version if its installed or you could download it at https://git-scm.com/downloads
 1. Clone the repository on the terminal or command prompt : `git clone https://github.com/jheslian/projet7-algo.git`
 2. Create a virtual environment with "venv"  
	 - `cd projet7-algo` :  to access the folder 
	 - python -m venv ***environment name*** : to create the virtual environment - exemple: `python -m venv env`
3. Activate the virtual environment:
	for unix or macos:
	- source ***environment name***/bin/activate - ex : `source env/bin/activate` if "env" is used as environment name 
	for windows:
	- ***environment name***\Scripts\activate.bat - ex: `env\Scripts\activate.bat`
4. Install the packages with pip: `pip install -r requirements.txt`	
6. Run the program : 
	for unix or macos: `python3 main.py`
	for windows: `py main.py`


### Directories
**algo** - contains files for the mentioned algorithms(`brutforce.py` and `optimized.py`)

**dataset** - contains the following:
 - csv folder: csv files of the actions needed
 - txt folder: txt files which contains action details(names, prices, total costs, and total profit) which was bought  with  a budget of 500.00
 ***note:*** 1 csv file = to 1 txt file

