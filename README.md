# cmsc447-hw2-sp2024-manav-bhatt

How to run:

1. clone the repo
2. install Python 3.6+ and PIP. 
3. install virtualenv (https://pypi.org/project/virtualenv/)  
4. create virtual environment using python -m venv path
5. run .venv\Scripts\Activate.ps1 or Scripts\activate or Scripts\activate.bat
6. install required packages (flask, databases). 
7. pip install flask
8. run create_table.py
9. run flask --app app run  
10. open 127.0.0.1:5000 in your browser
11. should already have pre-loaded table, can add, remove, search, and reset to get to original state


The search uses ID to see if its there
Usage:
- Can add all the values in the text box to:
     - Add
     - Remove (Uses ID)
     - Update
- Reset does a Select all to print out the original table