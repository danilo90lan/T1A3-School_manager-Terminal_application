# T1A3 - School Management Application

## Installation requirement

### Prerequisites
- Python 3.10 or higher
- Pyhton3 virtual environments (venv)

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