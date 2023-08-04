# Automation Website
Automation Website [TodoList] with Python

## What will the test do?
- Check Url title
- Add todolist items
- Complete todolist items
- Filter todolist (ALL, ACTIVE, COMPLETED)
- Delete todolist items

## Tech

- [Python] - Python is used successfully in thousands of real-world business applications around the world
- [Allure] - Generated report dashboard
- [Pytest] - The pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries
- [PyCharm] - The Python IDE for Professional Developers

## Installation

Download & Install [Python](https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe) 3.11.4.
Check Python version in cmd
```sh
python --version
Python 3.11.4
```
Download & Install [PyCharm]
Install Python [Pytest] di cmd
```sh
pip install pytest
```
Install Python [Allure] di cmd
```sh
pip install allure-pytest
```
Check Packages Request & Pytest in cmd has been done 
```sh
pip list
```
## Development
1. Open PyCharm
2. Create new project -> pythonToDoList
3. Create New -> Python Package -> locators
4. Create New -> Python Package -> pages
5. Create New -> Python Package -> reports
6. Create New -> Python Package -> testcases
4. Create file .py -> test_todolist.py in testcases package
5. Import packages
6. Create function in python with start name is 'test_'
7. Open terminal in PyCharm 
8. Run scripts with report allure
```sh
pytest testcases\test_todolist.py -- alluredir="./reports" 
```
9. Report will be generated
10. Open cmd and path to folder project python
11. Run Allur serve
```sh
allure serve "./reports" 
```
12. Screen will be open browser and report will be shown

   [Python]: <https://www.python.org/>
   [Request]: <https://pypi.org/project/requests/>
   [Pytest]: <https://pypi.org/project/pytest/>
   [PyCharm]: <https://www.jetbrains.com/pycharm/>
   [ToDoList]: <https://todomvc.com/examples/knockoutjs/>
   [Allure]: <https://pypi.org/project/allure-pytest/>
