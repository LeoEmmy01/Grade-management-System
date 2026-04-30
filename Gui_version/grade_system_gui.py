


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
# JSON file where all student data is stored
FILE_NAME = "students.json"


# ---------------- DATA HANDLING ----------------
# Load student data from JSON file
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


# Save student data to JSON file
def save_data(data):
    with open(FILE_NAME, "w") as f:
        # Convert Python dictionary → JSON format
        json.dump(data, f, indent=4)


# Load existing students into memory
students = load_data()


# ---------------- UI HELP FUNCTION ----------------
# Clear the right-side frame before loading new UI screen
def clear_frame():
    for widget in form_frame.winfo_children():
        widget.destroy()


# ---------------- ADD STUDENT SCREEN ----------------
def add_student():
    clear_frame()

    # Title label
    ctk.CTkLabel(form_frame, text="Add Student", font=("Arial", 18)).pack(pady=10)

    # Input fields
    roll = ctk.CTkEntry(form_frame, placeholder_text="Add Roll Number")
    roll.pack(pady=5)

    name = ctk.CTkEntry(form_frame, placeholder_text="Student Name")
    name.pack(pady=5)

    # Function that runs when button is clicked
    def submit():
        r = roll.get().strip()  # Get roll input
        n = name.get().strip()  # Get name input

        # Validate empty inputs
        if not r or not n:
            messagebox.showerror("Error", "All fields required")
            return

        # Check duplicate student
        if r in students:
            messagebox.showerror("Error", "Student exists")
            return

        # Save student into dictionary
        students[r] = {"name": n, "subjects": {}}
        save_data(students)

        messagebox.showinfo("Success", "Student added")

    # Save button
    ctk.CTkButton(form_frame, text="Save", command=submit).pack(pady=10)


# ---------------- ADD SCORE SCREEN ----------------
def add_score():
    clear_frame()

    # Title
    ctk.CTkLabel(form_frame, text="Add Score", font=("Arial", 18)).pack(pady=10)

    # Input fields
    roll = ctk.CTkEntry(form_frame, placeholder_text="Student Roll Number")
    roll.pack(pady=5)

    subject = ctk.CTkEntry(form_frame, placeholder_text="Subject")
    subject.pack(pady=5)

    test = ctk.CTkEntry(form_frame, placeholder_text="Test Score")
    test.pack(pady=5)

    exam = ctk.CTkEntry(form_frame, placeholder_text="Exam Score")
    exam.pack(pady=5)

    # Submit logic
    def submit():
        r = roll.get().strip()  # roll number
        s = subject.get().strip().title()  # subject name formatted

        # Check student exists
        if r not in students:
            messagebox.showerror("Error", "Student not found")
            return

        # Convert input to numbers
        try:
            t = float(test.get())
            e = float(exam.get())
        except:
            messagebox.showerror("Error", "Enter valid numbers")
            return

        # Validation: negative values
        if t < 0 or e < 0:
            messagebox.showerror("Error", "Scores cannot be negative")
            return

        # Validation: max limits
        if t > 30 or e > 70:
            messagebox.showerror("Error", "Score exceeds allowed limit")
            return

        # Save score
        students[r]["subjects"][s] = {
            "test": t,
            "exam": e,
            "total": t + e
        }

        save_data(students)
        messagebox.showinfo("Success", "Score added")

    # Button
    ctk.CTkButton(form_frame, text="Save Score", command=submit).pack(pady=10)
    
def show_student_info():
    clear_frame()

    ctk.CTkLabel(form_frame, text="Student Profile", font=("Arial", 18)).pack(pady=10)

    roll_entry = ctk.CTkEntry(form_frame, placeholder_text="Enter Student Roll Number")
    roll_entry.pack(pady=5)

    output = ctk.CTkTextbox(form_frame, height=350)
    output.pack(pady=10, fill="both", expand=True)

    def search():
        roll = roll_entry.get().strip()

        if roll not in students:
            messagebox.showerror("Error", "Student not found")
            return

        student = students[roll]

        output.delete("1.0", "end")

        # HEADER
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

        output.insert("end", f"{'SUBJECT':<12}{'TEST':<8}{'EXAM':<8}{'TOTAL':<8}\n")
        output.insert("end", "-" * 40 + "\n")

        # SUBJECT DETAILS
        for subject, score in student["subjects"].items():
            output.insert(
                "end",
                f"{subject:<12}{score['test']:<8}{score['exam']:<8}{score['total']:<8}\n"
            )

        # SUMMARY
        total = sum(score["total"] for score in student["subjects"].values())
        count = len(student["subjects"])

        output.insert("end", "-" * 40 + "\n")
        output.insert("end", f"Subjects: {count}\n")
        output.insert("end", f"Total Score: {total}\n")
        output.insert("end", f"Average: {total/count:.2f}\n")

    ctk.CTkButton(form_frame, text="View Profile", command=search).pack(pady=5)


# ---------------- VIEW ALL STUDENTS ----------------
def show_all_students():
    clear_frame()

    ctk.CTkLabel(form_frame, text="All Students", font=("Arial", 18)).pack(pady=10)

    # Output box
    output = ctk.CTkTextbox(form_frame, height=350)
    output.pack(pady=10, fill="both", expand=True)

    # If no students exist
    if not students:
        output.insert("end", "No students available.")
        return

    # Header
    output.insert("end", "ROLL\tNAME\n")
    output.insert("end", "-" * 30 + "\n")

    # Display all students
    for roll, info in students.items():
        output.insert("end", f"{roll}\t{info['name']}\n")


# ---------------- REPORT CARD SCREEN ----------------
def show_report():
    clear_frame()

    ctk.CTkLabel(form_frame, text="Student Report Card", font=("Arial", 18)).pack(pady=10)

    # Input roll number
    roll_entry = ctk.CTkEntry(form_frame, placeholder_text="Enter Student Roll Number")
    roll_entry.pack(pady=5)

    # Output box
    output = ctk.CTkTextbox(form_frame, height=350)
    output.pack(pady=10, fill="both", expand=True)

    def generate():
        roll = roll_entry.get().strip()

        # Validate student
        if roll not in students:
            messagebox.showerror("Error", "Student not found.")
            return

        student = students[roll]

        # Check subjects exist
        if not student["subjects"]:
            messagebox.showinfo("Info", "No subjects recorded for this student.")
            return

        output.delete("1.0", "end")

        # HEADER SECTION
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
        for subject, score in student["subjects"].items():
            test = score["test"]
            exam = score["exam"]
            total = score["total"]

            output.insert("end", f"{subject:<12}{test:<8}{exam:<8}{total:<8}\n")

            subject_averages[subject] = total
            grand_total += total
            count += 1

        # SUBJECT AVERAGES
        output.insert("end", "-" * 40 + "\n\n")
        output.insert("end", "SUBJECT AVERAGES\n")

        for subject, total in subject_averages.items():
            output.insert("end", f"{subject}: {total:.2f}\n")

        # OVERALL AVERAGE + GRADE
        overall_avg = grand_total / count
        grade = grade(overall_avg)

        output.insert("end", "\n------------------------------\n")
        output.insert("end", f"OVERALL AVERAGE: {overall_avg:.2f}\n")
        output.insert("end", f"GRADE: {grade}\n")
        output.insert("end", "==============================\n")

    # Button
    ctk.CTkButton(form_frame, text="Generate Report", command=generate).pack(pady=5)


# ---------------- CLASS PERFORMANCE ----------------
def show_class_performance():
    clear_frame()

    ctk.CTkLabel(
        form_frame,
        text="CLASS PERFORMANCE",
        font=("Arial", 20, "bold")
    ).pack(pady=10)

    output = ctk.CTkTextbox(form_frame, height=300)
    output.pack(pady=10, fill="both", expand=True)

    totals = {}
    counts = {}

    # Collect data
    for student in students.values():
        for sub, sc in student["subjects"].items():
            totals[sub] = totals.get(sub, 0) + sc["total"]
            counts[sub] = counts.get(sub, 0) + 1

    if not totals:
        output.insert("end", "No class data available.\n")
        return

    output.insert("end", "SUBJECT\tAVERAGE\tSTUDENTS\n")
    output.insert("end", "-" * 40 + "\n")

    # Show averages + student count per subject
    for sub in totals:
        avg = totals[sub] / counts[sub]
        output.insert("end", f"{sub}\t{avg:.2f}\t{counts[sub]}\n")
        
    

# ---------------- MAIN UI ----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("800x600")
app.title("Grade System (Dynamic UI)")

# ---------------- TITLE HEADER ----------------
title = ctk.CTkLabel(
    app,
    text="GRADE MANAGEMENT SYSTEM",
    font=("Arial", 28, "bold")
)
title.pack(pady=10)

# ---------------- LEFT MENU ----------------
menu_frame = ctk.CTkFrame(app, width=200)
menu_frame.pack(side="left", fill="y")

# Buttons (navigation)
ctk.CTkButton(menu_frame, text="Add Student", command=add_student).pack(pady=10)
ctk.CTkButton(menu_frame, text="Add Score", command=add_score).pack(pady=10)
ctk.CTkButton(menu_frame, text="View Students", command=show_all_students).pack(pady=10)
ctk.CTkButton(menu_frame, text="Show Student Info", command=show_student_info).pack(pady=10)
ctk.CTkButton(menu_frame, text="Report Card", command=show_report).pack(pady=10)
ctk.CTkButton(menu_frame, text="Class Performance", command=show_class_performance).pack(pady=10)


# ---------------- RIGHT PANEL ----------------
form_frame = ctk.CTkFrame(app)
form_frame.pack(side="right", fill="both", expand=True)

# Start app
app.mainloop()