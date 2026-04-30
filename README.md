# Grade Management System Overview

**GradeFlow** is a Python-based Grade Management System that helps manage student records, subjects, scores, and performance analytics.

This project includes --Two versions--:

GUI Version – Built with CustomTkinter (modern interface)
CLI Version – Terminal-based (lightweight and simple)

Both versions use a shared **JSON database** for persistent storage.

---

##  Features

###  Student Management

Add new students (Name & Roll Number/Matric Numbers)
Prevent duplicate entries
View all students

###  Score Management

 Add/Edit scores per subject
 Supports:

   Test score (max 30)
   Exam score (max 70)
*Automatic total calculation

###  Report System

Generate student report cards
Displays:

   Subject scores
   Totals
   Subject averages
   Overall average
   Grade (A–F)

### Analytics

Class performance per subject
Average score per subject
Number of students per subject

### Student Profile View

View a single student's:

  Name
  Subjects
  Scores
  Total & average

---

## GUI Version (CustomTkinter)

Modern interface with:

Sidebar navigation
Dynamic forms
Real-time updates
Styled report output

### Run GUI:

```bash
python grade_system_gui.py
```

##  CLI Version

Simple terminal-based interaction.

### Features:

Menu-driven interface
Fast and lightweight
Same core functionality as GUI

### Run CLI:

```bash
python grade_system_cli.py
```

---

##  Project Structure

```bash
GradeFlow/
│
├── grade_system_cli.py              # Cli Version
├── grade_system_gui.py              # GUI version (CustomTkinter)
├── students.json       # Database (auto-generated)
├── README.md           # Project documentation
```

---

##  Data Storage

All student data is stored in:

```bash
students.json
```

### Format Example:

```json
{
  "101": {
    "name": "John Doe",
    "subjects": {
      "Math": {
        "test": 25,
        "exam": 60,
        "total": 85
      }
    }
  }
}
```

---

##  Installation

### 1. Clone repository

```bash
git clone https://github.com/LeoEmmy01/Grade Management.git
cd Grade Management System
```

### 2. Install dependencies

```bash
pip install customtkinter
```

---

## Future Improvements

Graphs & charts (performance visualization)
Ranking system
Export report card as PDF
Web-based version (Flask/Django)
User authentication (Admin/Teacher login)

---

##  Contribution

Feel free to fork this project and improve it.

---

##  License

This project is open-source and available under the MIT License.

---

##  Author

Developed by **Leo**

---

##  Support

If you like this project, consider giving it a ⭐ on GitHub!
