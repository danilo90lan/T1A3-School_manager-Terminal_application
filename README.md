# T1A3 - School Management Application

## Installation requirements

### Prerequisites
- Python 3.10 or higher installed 
  (https://installpython3.com/)
- Pyhton3 virtual environment (venv) installed 
  (https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)

### Step by step installation
1. Open the terminal
2. Navigate to the project directory:
```
cd ./src/T1A3-School_manager
```
3. Run the executable
```
./run.sh
```

## GitHub Repository
[Link to my GitHub Repository](https://github.com/danilo90lan/T1A3-School_manager-Terminal_application)

## Introduction
This application is designed to help manage student and teacher records in a school system.  
It provides a range of features to add, display, search, and filter records, making it easy to keep track of important information.   
It is built with Python and uses JSON files to store data, making it simple to update and access records.

## Who Is This App For?
This application is primarily designed for school administrators and other staff involved in the management of student and teacher records.  
With this app is possible to:
- Keep track of what subject each teacher is teaching or what course each student is enrolled to
- Filter and export data
-  Adding, delete and update record using a simple and user-friendly interface
- View all records in alphabetical order for quick reference.

## List of features

### 1. Load Data from JSON file
- Load student and teacher records from a JSON file.
- Initialize ID system to ensure each record has a unique ID.

### 2. Add New Records
- Add new teacher and new student records.
- Ensure each new record is assigned a unique ID.

### 3. Display Records
- Display all teacher and students records in alphabetical order.

### 4. Search Records
- Search for a student or for a techer by ID or name.

### 5. Filter Records
- Filter teachers by subject and students by course

### 6. List Subjects and Courses
- List all subjects taught in the school.
- List all courses available in the school.

### 7. Export Data
- Export lists of filtered teachers or students to a different new JSON file.
- Save new records to the JSON file after adding them and sort them alphabetically.

## Code style guide
This application adheres to the PEP 8 style guide.
- Use 4 spaces per indentation level.
- Limit all lines to a maximum of 79 characters.
- Surround top-level function and class definitions with two blank lines.
- Method definitions inside a class are surrounded by a single blank line.
- Imports are always put at the top of the file, just after any module comments and docstrings, and before module globals and constants.
- Use meaningful variable and function names.
- Include docstrings for all modules, classes, and functions.
- Modules should have short, all-lowercase names.
- Function names should be lowercase, with words separated by underscores as necessary to improve readability, as well as method names
- Constants are usually defined on a module level and written in all capital letters with underscores separating words

###### Source reference
https://peps.python.org/pep-0008/