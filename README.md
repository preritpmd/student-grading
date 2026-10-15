# Student Grading System

A simple Python-based Student Grading System that processes student records, assigns grades based on marks, and displays a student grade report.

## Features

- **Student Records:** Reads student information from a CSV file.
- **Grade Calculation:** Assigns grades according to the grading rules implemented in the program.
- **Input Validation:** Validates grading inputs and handles invalid values.
- **Student Grade Report:** Displays student IDs, names, marks, and grades in a formatted table.
- **Unit Testing:** Includes automated tests to verify grading functionality and boundary cases.
- **CSV Support:** Stores sample student data in `students.csv`.

## Technologies Used

- Python 3
- CSV file handling
- Git and GitHub
- Python `unittest` framework

## Project Structure

```text
student-grading/
├── grading.py
├── students.csv
├── test_grading.py
├── README.md
└── .gitignore
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/preritpmd/student-grading.git
```

### 2. Navigate to the project directory

```bash
cd student-grading
```

### 3. Run the program

```bash
python grading.py
```

On Windows, you can also use:

```powershell
py grading.py
```

### 4. Run the tests

```powershell
py -m unittest discover -s . -p "test_grading.py" -v
```

## Sample Output

```text
ID | Name | Marks | Grade
------------------------------
101 | Aarav | 85.0 | A
102 | Diya | 72.0 | B
103 | Rohan | 91.0 | A
104 | Ananya | 58.0 | C
105 | Vikram | 34.0 | F
```

## Learning Objectives

This project demonstrates practical use of Python functions, conditional logic, input validation, CSV file processing, automated testing, and Git version control.

## Author

**Prerit Devashetti**

Indian Institute of Technology Dharwad (IIT Dharwad)

---

*This project was developed as a hands-on exercise in Python programming, software testing, and version control.*
