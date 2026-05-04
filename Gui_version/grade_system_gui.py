"""Overall Project Explanation (GUI Version)

This is a Grade Management System with a Graphical User Interface (GUI) built using CustomTkinter. It helps manage student records, scores, and performance in a simple visual way instead of using the terminal.

 -----What the system does-----

This application allows the user to:

Add new students (name and roll number)
Add and update student scores (test and exam)
View all students in a list
Search and view individual student details
Generate full report cards
Analyze overall class performance
Store all data permanently using a JSON file"""


# ---------------- IMPORTS ----------------
# Import CustomTkinter for modern GUI
import customtkinter as ctk

# Used for popup error/info messages
from tkinter import messagebox

# Used for saving/loading JSON data (database)
import json

# Used to check if file exists
import os

# ---------------- FILE CONFIG ----------------
#FILE_NAME
"""This is a variable name.
It is written in uppercase by convention, which usually means:
“This value is a constant or should not change often in the program.”
It does not have special meaning in Python, it's just a name you chose.

"students.json"
This is a string (text).
It represents a file name.
.json means the file is expected to be in JSON format, which is commonly used to store structured data like"""
FILE_NAME = "students.json"


# ---------------- DATA HANDLING ----------------
"""This function is used to load student data from a JSON file safely.
First, it checks if the file exists using os.path.exists(FILE_NAME).
If the file exists, it tries to open it in read mode ("r").
It reads the file content and converts the JSON data into a Python dictionary using json.load(f).
If the file is empty, broken, or has invalid JSON, the program will not crash. Instead, it returns an empty dictionary {}.
If the file does not exist at all, it also returns an empty dictionary {}.

In simple terms:
This function safely loads student data from a file, and if anything goes wrong, it returns an empty dataset instead of crashing the program."""
def load_data():
    # Check if file exists
    if os.path.exists(FILE_NAME):
        try:
            # Open and read file
            with open(FILE_NAME, "r") as f:
                return json.load(f)  # Convert JSON → Python dictionary
        except:
            # If file is broken or empty, return empty data
            return {}
    return {}  # If file doesn't exist

#--------------Save File-----------------
"""This function is used to save student data into a JSON file.
The function save_data(data) takes a parameter called data, which is usually a Python dictionary containing student information.
It opens the file defined by FILE_NAME in write mode ("w"). This means it will create the file if it does not exist or overwrite it if it already exists.
The with open(...) statement ensures the file is properly closed after writing.
json.dump(data, f, indent=4) converts the Python dictionary into JSON format and writes it into the file.
The indent=4 makes the JSON file neatly formatted and easier to read.

In simple terms:
This function saves student data into a JSON file in a clean, structured format"""
def save_data(data):
    with open(FILE_NAME, "w") as f:
        # Convert Python dictionary → JSON format
        json.dump(data, f, indent=4)

"""This line calls the function load_data().
The function reads student data from the JSON file (if it exists) and returns it as a Python dictionary.
The returned data is then stored in the variable students.

In simple terms:
This line loads all saved student data from the file and stores it in the variable students so it can be used in the program."""
students = load_data()


# ---------------- UI HELP FUNCTION ----------------
"""This defines a function called clear_frame().
form_frame.winfo_children() gets all widgets (buttons, labels, entries, etc.) inside form_frame.
The for loop goes through each widget one by one.
widget.destroy() removes each widget from the screen (deletes it from the frame).

In simple terms: This function clears everything inside form_frame by deleting all the UI elements inside it, so the frame becomes empty and ready for new content"""
def clear_frame():
    for widget in form_frame.winfo_children():
        widget.destroy()


# ---------------- ADD STUDENT SCREEN ----------------
"""This defines a function called add_student().
Inside the function, it calls clear_frame().
clear_frame() removes all existing widgets (buttons, labels, entries, etc.) from the frame.

In simple terms:
This function prepares the interface for adding a new student by first clearing everything currently shown on the screen"""
def add_student():
    clear_frame()

    # -----------Title label-------------
    """    ctk.CTkLabel(...) creates a label (text display) using CustomTkinter.
    form_frame is the container where this label will be placed.
    text="Add Student" sets what will be shown on the screen.
    font=("Arial", 18) sets the font style and size (Arial, size 18).
    .pack(pady=10) places the label on the screen and adds vertical spacing (10 pixels) above and below it.

    In simple terms:
    This line creates and displays a title label that says "Add Student" at the top of the form, with a nice font and spacing"""
    ctk.CTkLabel(form_frame, text="Add Student", font=("Arial", 18)).pack(pady=10)

    # --------------Input fields--------------------
    """ctk.CTkEntry(...) creates an input box (text field) using CustomTkinter.
    form_frame is where the input box will appear.
    placeholder_text="Add Roll Number" shows faint hint text inside the box before the user types anything.
    roll is the variable that stores this input box.
    .pack(pady=5) places the entry box on the screen and adds vertical spacing.

    In simple terms:
    This creates an input box where the user can type a student's roll number."""
    roll = ctk.CTkEntry(form_frame, placeholder_text="Add Roll Number")
    roll.pack(pady=5)
    
    #This creates another input box using ctk.CTkEntry.
    """It is also placed inside form_frame.
    The placeholder text "Student Name" shows a hint inside the box.
    The variable name stores this input box.
    .pack(pady=5) places it on the screen with spacing.

    In simple terms:
    This creates an input box where the user can type the student’s name"""
    name = ctk.CTkEntry(form_frame, placeholder_text="Student Name")
    name.pack(pady=5)

        # ------------Function that runs when button is clicked----------------
    """This function runs when the submit button is clicked.
        def submit(): defines a function that handles form submission.
        r = roll.get().strip() gets the value entered in the roll number input field and removes any extra spaces at the beginning or end.
        n = name.get().strip() gets the value entered in the student name input field and also removes extra spaces.

        In simple terms:
        This function collects and cleans the user’s input (roll number and name) so it is ready to be checked or saved."""
    def submit():
        r = roll.get().strip()  # Get roll input
        n = name.get().strip()  # Get name input


        # ------------Validate empty inputs-----------
        """This checks if the user left any input empty.
        if not r or not n: checks whether the roll number (r) or name (n) is empty.
        If any field is empty, messagebox.showerror(...) shows an error message saying "All fields required".
        return stops the function so nothing else runs.
        
        In simple terms:
        This part makes sure the user fills in all fields before the data can be saved."""
        if not r or not n:
            messagebox.showerror("Error", "All fields required")
            return

        # -----------Check duplicate student-------------
        """This checks if the student already exists in the system.
        if r in students: checks if the roll number already exists in the students data.
        If it exists, messagebox.showerror("Error", "Student exists") shows an error message.
        return stops the function so no duplicate data is added.

        In simple terms:
        This part prevents adding a student with a roll number that already exists"""
        if r in students:
            messagebox.showerror("Error", "Student exists")
            return

        # Save student into dictionary
        """This adds a new student and saves the data.

        students[r] = {"name": n, "subjects": {}} adds the student to the dictionary using the roll number as the key.
        "name": n stores the student’s name.
        "subjects": {} creates an empty space for subjects and scores.
        save_data(students) saves the updated student data into the JSON file.

        In simple terms:
        This part adds the new student to the system and saves it permanently in the file."""
        students[r] = {"name": n, "subjects": {}}
        save_data(students)

        #------message box------------
        """messagebox.showinfo("Success", "Student added") shows a pop-up message to the user.
        "Success" is the title of the message box.
        "Student added" is the message displayed inside the pop-up.

        👉 In simple terms:
        This shows a confirmation message telling the user that the student was added successfully"""
        messagebox.showinfo("Success", "Student added")

    # Save button
    """ctk.CTkButton(...) creates a button using CustomTkinter.
    form_frame is where the button will appear.
    text="Save" sets the button label to Save.
    command=submit makes the button run the submit() function when clicked.
    .pack(pady=10) places the button on the screen and adds vertical spacing.

    In simple terms:
    This creates a Save button that runs the submit function when clicked."""
    ctk.CTkButton(form_frame, text="Save", command=submit).pack(pady=10)


# ---------------- ADD SCORE SCREEN ----------------
"""This function creates a screen for adding student scores.

def add_score(): defines a function that shows the “Add Score” form.
clear_frame() removes all existing widgets so the new form can appear.

 In simple terms:
This function shows a form where the user can enter a student’s roll number, subject, test score, and exam score."""
def add_score():
    clear_frame()

    # Title
    """
    ctk.CTkLabel(...) displays the title "Add Score" on the screen."""
    ctk.CTkLabel(form_frame, text="Add Score", font=("Arial", 18)).pack(pady=10)

    # Input fields
    """--- Input fields---
    These create text boxes for user input:
    roll → input for student roll number
    subject → input for subject name
    test → input for test score
    exam → input for exam score
    Each .pack(pady=5) places the input box on the screen with spacing."""
    roll = ctk.CTkEntry(form_frame, placeholder_text="Student Roll Number")
    roll.pack(pady=5)

    subject = ctk.CTkEntry(form_frame, placeholder_text="Subject")
    subject.pack(pady=5)

    test = ctk.CTkEntry(form_frame, placeholder_text="Test Score")
    test.pack(pady=5)

    exam = ctk.CTkEntry(form_frame, placeholder_text="Exam Score")
    exam.pack(pady=5)

    # Submit logic
    """This function handles adding a student’s score.

    def submit() runs when the user clicks the button.
    r gets the roll number and s gets the subject name (formatted properly)"""
    def submit():
        r = roll.get().strip()  # roll number
        s = subject.get().strip().title()  # subject name formatted

        # Check student exists
        """Student check
        If the roll number is not found in students, it shows an error message and stops"""
        if r not in students:
            messagebox.showerror("Error", "Student not found")
            return

        # Convert input to numbers
        """Convert scores
        t and e convert test and exam inputs into numbers.
        If conversion fails, it shows an error message."""
        try:
            t = float(test.get())
            e = float(exam.get())
        except:
            messagebox.showerror("Error", "Enter valid numbers")
            return

        # Validation: negative values
        """
        Ensures scores are not negative.
        """
        if t < 0 or e < 0:
            messagebox.showerror("Error", "Scores cannot be negative")
            return

        # Validation: max limits
        # Ensures test score is not above 30 and exam score is not above 70.
        # If any rule is broken, it shows an error and stops
        if t > 30 or e > 70:
            messagebox.showerror("Error", "Score exceeds allowed limit")
            return

        # Save score
        """Stores test, exam, and total score in the student’s record.
        Saves everything to the JSON file using save_data(students)."""
        students[r]["subjects"][s] = {
            "test": t,
            "exam": e,
            "total": t + e
        }

        #Shows “Score added” when everything is successful.
        save_data(students)
        messagebox.showinfo("Success", "Score added")

    # Button
    "click button that perform the command submit for the above defined function"
    ctk.CTkButton(form_frame, text="Save Score", command=submit).pack(pady=10)
    
#Show Student Info
"""This function shows a student’s full profile and scores.

def show_student_info() creates a screen for viewing student details.
clear_frame() clears the screen before showing new content.
A title label "Student Profile" is displayed"""
def show_student_info():
    clear_frame()

    #Label
    ctk.CTkLabel(form_frame, text="Student Profile", font=("Arial", 18)).pack(pady=10)

    #Entry
    """Input field
    roll_entry is an input box where the user enters a student roll number."""
    roll_entry = ctk.CTkEntry(form_frame, placeholder_text="Enter Student Roll Number")
    roll_entry.pack(pady=5)

    #Output
    """🔹 Output box
    output = ctk.CTkTextbox(...) creates a large text area to display results like name, subjects, and scores"""
    output = ctk.CTkTextbox(form_frame, height=350)
    output.pack(pady=10, fill="both", expand=True)


    #search function
    """
    def search() runs when the button is clicked"""
    def search():
        roll = roll_entry.get().strip()

        #Student Check
        """
        Gets roll number from input.
        If the student is not found, it shows an error message."""
        if roll not in students:
            messagebox.showerror("Error", "Student not found")
            return

        #Call out student from database using roll number
        student = students[roll]

        output.delete("1.0", "end")

        # HEADER
        #Display student info
        """Clears previous text in the output box.
        Shows:
        Student name
        Roll number
        Header formatting"""
        output.insert("end", "=========================\n")
        output.insert("end", "     STUDENT PROFILE\n")
        output.insert("end", "=========================\n")
        output.insert("end", f"Name: {student['name']}\n")
        output.insert("end", f"Roll: {roll}\n")
        output.insert("end", "-------------------------\n\n")

        # If no subjects
        if not student["subjects"]:
            output.insert("end", "No subjects recorded.\n")
            return
        
        #Display subject info(exam, text and total)
        output.insert("end", f"{'SUBJECT':<12}{'TEST':<8}{'EXAM':<8}{'TOTAL':<8}\n")
        output.insert("end", "-" * 40 + "\n")

        # SUBJECT DETAILS
        """Displays a table of:

        Subject name
        Test score
        Exam score
        Total score"""
        for subject, score in student["subjects"].items():
            output.insert(
                "end",
                f"{subject:<12}{score['test']:<8}{score['exam']:<8}{score['total']:<8}\n"
            )

        # SUMMARY
        """Calculates:
        Total score of all subjects
        Number of subjects
        Average score
        Displays them at the bottom."""
        total = sum(score["total"] for score in student["subjects"].values())
        count = len(student["subjects"])

        output.insert("end", "-" * 40 + "\n")
        output.insert("end", f"Subjects: {count}\n")
        output.insert("end", f"Total Score: {total}\n")
        output.insert("end", f"Average: {total/count:.2f}\n")


    #Button
    """
    Creates a View Profile button
    When clicked, it runs the search() function"""
    ctk.CTkButton(form_frame, text="View Profile", command=search).pack(pady=5)


# ---------------- VIEW ALL STUDENTS ----------------
"""def show_all_students() creates a screen to display all students.
clear_frame() clears the current screen before showing new content.
"""
def show_all_students():
    clear_frame()

    #A title label "All Students" is displayed
    ctk.CTkLabel(form_frame, text="All Students", font=("Arial", 18)).pack(pady=10)

    # Output box
    #output = ctk.CTkTextbox(...) creates a large text area where student data will be shown
    output = ctk.CTkTextbox(form_frame, height=350)
    output.pack(pady=10, fill="both", expand=True)

    # If no students exist
    """if not students: checks if there are no students in the system.
    If empty, it shows "No students available." and stops the function"""
    if not students:
        output.insert("end", "No students available.")
        return

    # Header
    """Prints column titles:
    ROLL
    NAME
    Adds a line separator for better readability"""
    output.insert("end", "ROLL\tNAME\n")
    output.insert("end", "-" * 30 + "\n")

    # Display all students
    """Loops through the students dictionary.
    For each student:
    Shows the roll number
    Shows the student's name"""
    for roll, info in students.items():
        output.insert("end", f"{roll}\t{info['name']}\n")


# ---------------- REPORT CARD SCREEN ----------------
"""
def show_report() creates a screen for generating a report card.
clear_frame() clears the screen first.
A title label "Student Report Card" is displayed."""
def show_report():
    clear_frame()

    ctk.CTkLabel(form_frame, text="Student Report Card", font=("Arial", 18)).pack(pady=10)

    # Input roll number
    # Enter student roll number
    roll_entry = ctk.CTkEntry(form_frame, placeholder_text="Enter Student Roll Number")
    roll_entry.pack(pady=5)

    # Output box
    #output = ctk.CTkTextbox(...) is used to display the full report card
    output = ctk.CTkTextbox(form_frame, height=350)
    output.pack(pady=10, fill="both", expand=True)

    #Generate function runs the button is clicked
    def generate():
        roll = roll_entry.get().strip()

        # Validate student
        """Gets roll number from input.
        If student is not found, it shows an error message"""
        if roll not in students:
            messagebox.showerror("Error", "Student not found.")
            return

        student = students[roll]

        # Check subjects exist
        #If the student has no subjects, it shows an info message and stops
        if not student["subjects"]:
            messagebox.showinfo("Info", "No subjects recorded for this student.")
            return

        output.delete("1.0", "end")

        # HEADER SECTION
        """Clears old output.
        Displays:
        Report title
        Student name
        Roll number
        Table headings"""
        output.insert("end", "==============================\n")
        output.insert("end", "        STUDENT REPORT CARD\n")
        output.insert("end", "==============================\n")
        output.insert("end", f"Name: {student['name']}\n")
        output.insert("end", f"Roll: {roll}\n")
        output.insert("end", "------------------------------\n")

        output.insert("end", f"{'SUBJECT':<12}{'TEST':<8}{'EXAM':<8}{'TOTAL':<8}\n")
        output.insert("end", "-" * 40 + "\n")

        grand_total = 0
        count = 0
        subject_averages = {}

        # LOOP THROUGH SUBJECTS
        """Goes through each subject and gets:
        test score
        exam score
        total score
        Displays them in a table format.
        Calculates:
        grand_total (sum of all scores)
        count (number of subjects)"""
        for subject, score in student["subjects"].items():
            test = score["test"]
            exam = score["exam"]
            total = score["total"]

            output.insert("end", f"{subject:<12}{test:<8}{exam:<8}{total:<8}\n")

            subject_averages[subject] = total
            grand_total += total
            count += 1

        # SUBJECT AVERAGES
        """Stores each subject's total score.
        Displays each subject's average score."""
        
        output.insert("end", "-" * 40 + "\n\n")
        output.insert("end", "SUBJECT AVERAGES\n")

        for subject, total in subject_averages.items():
            output.insert("end", f"{subject}: {total:.2f}\n")

        # OVERALL AVERAGE + GRADE
        overall_avg = grand_total / count
        grade = grade(overall_avg)


        #Shows
        """Overall average,
        Grade,
        Closing line"""
        output.insert("end", "\n------------------------------\n")
        output.insert("end", f"OVERALL AVERAGE: {overall_avg:.2f}\n")
        output.insert("end", f"GRADE: {grade}\n")
        output.insert("end", "==============================\n")

    # Button
    """Creates a Generate Report button.
    Runs generate() when clicked.
    In simple terms:
    --This function creates a full report card for a student, showing all subjects, total scores, average, and final grade"""
    ctk.CTkButton(form_frame, text="Generate Report", command=generate).pack(pady=5)


# ---------------- CLASS PERFORMANCE ----------------
def show_class_performance():
    clear_frame()

    """def show_class_performance() creates a screen to display class statistics.
    clear_frame() removes everything on the screen first.
    A title "CLASS PERFORMANCE" is displayed in bold"""
    ctk.CTkLabel(
        form_frame,
        text="CLASS PERFORMANCE",
        font=("Arial", 20, "bold")
    ).pack(pady=10)

    #output = ctk.CTkTextbox(...) creates a text area to show results.
    output = ctk.CTkTextbox(form_frame, height=300)
    output.pack(pady=10, fill="both", expand=True)

    #Store data
    """totals = {} stores total scores for each subject.
    counts = {} stores how many students took each subject"""
    totals = {}
    counts = {}

    # Collect data
    """Loops through all students.
    For each subject:
    Adds total score to totals
    Counts how many students took that subject"""
    for student in students.values():
        for sub, sc in student["subjects"].items():
            totals[sub] = totals.get(sub, 0) + sc["total"]
            counts[sub] = counts.get(sub, 0) + 1

    #If no data exists, it shows "No class data available." and stops
    if not totals:
        output.insert("end", "No class data available.\n")
        return

    #Header
    """Shows table headings:
    Subject
    Average score
    Number of students"""
    output.insert("end", "SUBJECT\tAVERAGE\tSTUDENTS\n")
    output.insert("end", "-" * 40 + "\n")

    # Show averages + student count per subject
    for sub in totals:
        avg = totals[sub] / counts[sub]
        output.insert("end", f"{sub}\t{avg:.2f}\t{counts[sub]}\n")
"""In simple terms:
This function calculates and displays how the whole class performed in each subject, 
showing the average score and how many students took each subject"""
        
    

# ---------------- MAIN UI ----------------
"""ctk.set_appearance_mode("dark") sets the app theme to dark mode.
ctk.set_default_color_theme("blue") sets the main color theme to blue."""
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#app = ctk.CTk() creates the main application window
app = ctk.CTk()

"""app.geometry("800x600") sets the window size:
Width = 800 pixels
Height = 600 pixels"""
app.geometry("800x600")


#app.title("Grade System (Dynamic UI)") sets the title shown at the top of the window
app.title("Grade System (Dynamic UI)")

#Leo Icon
import os
import sys
import tkinter as tk
from PIL import Image, ImageTk

# ==================== ICON SETUP FUNCTION ====================
def setup_icon(app):
    """Setup icon for both window and taskbar."""
    
    # Get script directory
    if getattr(sys, 'frozen', False):
        script_dir = os.path.dirname(sys.executable)
    else:
        script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Check for ICO file FIRST (best for Windows taskbar)
    ico_path = os.path.join(script_dir, "tttt.ico")
    png_path = os.path.join(script_dir, "leo.png")
    
    if os.path.exists(ico_path):
        icon_path = ico_path
        use_ico = True
    elif os.path.exists(png_path):
        icon_path = png_path
        use_ico = False
    else:
        print("Warning: No icon file found!")
        return
    
    try:
        if use_ico:
            # Use ICO format for Windows taskbar
            app.iconbitmap(icon_path)
            print(f"Loaded ICO icon: {icon_path}")
        else:
            # Convert PNG to PhotoImage for window icon
            img = Image.open(icon_path)
            icon = ImageTk.PhotoImage(img)
            app.iconphoto(True, icon)
            print(f"Loaded PNG icon: {icon_path}")
    except Exception as e:
        print(f"Error loading icon: {e}")

# ==================== CALL THE FUNCTION ====================
# Place this AFTER app = ctk.CTk() and BEFORE app.mainloop()
setup_icon(app)

# ---------------- TITLE HEADER ----------------
#This displays a big bold title at the top of the app: “GRADE MANAGEMENT SYSTEM”
title = ctk.CTkLabel(
    app,
    text="GRADE MANAGEMENT SYSTEM",
    font=("Arial", 28, "bold")
)
title.pack(pady=10)

# ---------------- LEFT MENU ----------------
# This creates a vertical left menu panel where buttons and navigation options will be placed
menu_frame = ctk.CTkFrame(app, width=200)
menu_frame.pack(side="left", fill="y")

# Buttons (navigation)
"""Each line does the same thing:
Creates a button using ctk.CTkButton
Places it inside menu_frame (left menu)
Connects it to a function using command=...
Adds spacing using .pack(pady=10)"""
ctk.CTkButton(menu_frame, text="Add Student", command=add_student).pack(pady=10)
ctk.CTkButton(menu_frame, text="Add Score", command=add_score).pack(pady=10)
ctk.CTkButton(menu_frame, text="View Students", command=show_all_students).pack(pady=10)
ctk.CTkButton(menu_frame, text="Show Student Info", command=show_student_info).pack(pady=10)
ctk.CTkButton(menu_frame, text="Report Card", command=show_report).pack(pady=10)
ctk.CTkButton(menu_frame, text="Class Performance", command=show_class_performance).pack(pady=10)
"""Buttons explained
Add Student → opens the form to add a new student (add_student)
Add Score → opens the form to add scores (add_score)
View Students → shows all students in the system (show_all_students)
Show Student Info → displays a single student's details (show_student_info)
Report Card → generates a student report card (show_report)
Class Performance → shows overall class statistics (show_class_performance)"""

# ---------------- RIGHT PANEL ----------------
"""Creates a frame (container) inside the main window.
This is where all forms, tables, and outputs will be displayed."""
form_frame = ctk.CTkFrame(app)
"""Places the frame on the right side of the window.
fill="both" makes it expand in both width and height.
expand=True allows it to take all remaining space."""
form_frame.pack(side="right", fill="both", expand=True)

# Start app
"""Starts the Tkinter event loop.
Keeps the window open and running.
Listens for user actions like button clicks.

This runs the app and keeps it active until the user closes it"""
app.mainloop()