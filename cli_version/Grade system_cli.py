import json
import os

FILE_NAME = "students.json"

#Data Stroage Functions
#This is where student info(score,name,subject, exam) are stored


#The programme locate the json file and load through os path 
def load_data():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                data = json.load(file)
                
                if data is None:
                    return {}
                
                return data
        except (json.JSONDecodeError, FileNotFoundError):
            return {}
    return {}
    
#student data/info written or dump in json file
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)
 
       
students = load_data() or {}


#Grade Functions
def calculate_grade(avg):
    if avg >= 70:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 45:
        return "D"
    elif avg >= 40:
        return "E"
    else:
        return "F"
    
#Add Student functions
def add_student():
    print("\n" + "="*10)
    print("---------------ADD STUDENT-----------")
    print("="*10)    
    
    roll = input("Enter Roll Number: ")
    
    # it makes sure rolls are not kept empty
    if not roll.strip():
        print("Roll number cannot be empty.")
        return
    
    if roll in students:
        print("Student already exists.")
        return

    name = input("Enter student Name: ")
    
    # It makes sure name are empty
    if not name.strip():
        print("Name cannot be empty.")
        return
    
    #Handle/store inputed data/info
    students[roll] = {
        "name": name,
        "subjects": {}
    }
    
    save_data(students)
    print("Student added successfully.")
    
#Add/Update scores
def add_score():
    
    print("\n==================================")
    print("---------------ADD SCORE-----------")
    print("=====================================")
    
    roll = input("Enter Roll Number: ")
    
    #Checks if student exists
    if roll not in students:
        print("Student not found.")
        return
    
    """.strip()and .title() it breaks down existing data like
    subject name and match it up with existing datas"""
    subject = input("Enter Subject: ").strip().title()
    
    if not subject:
        print("Subject cannot be empty.")
        return
    
    #Error handler
    try:
        test = float(input("Enter Test Score (30): "))
        exam = float(input("Enter Exam Scores (70): "))
    except ValueError:
        print("Invalid input. Please enter numbers.")
        return
    
    #it make sure user don't input negative numbers
    if test < 0 or exam < 0:
        print("Scores cannot be negative.")
        return
    
    #It makes sure test and Exams don't exceeds certain numbers
    if test > 30 or exam > 70:
        print("Score exceeds allowed limit.")
        return
    
    total = test + exam
    
    #print inputed data/scores
    students[roll]["subjects"][subject] = {
        "test": test,
        "exam": exam,
        "total": total
    }
    
    save_data(students)
    print("Score Updated Successfully.")
    
#View all Students

def view_student():

    if not students:
        print("No Student Available.")
        return 
    
    print("\n Students List")
    print("_"*30)
    
    #This print student and it index
    for roll, info in students.items():
        print(f"{roll} | {info['name']}")
        

def report_card():
    roll = input("Enter Roll Number: ")
    
    if roll not in students:
        print("Student not found.")
        return
    
    student = students[roll]
    
    if not student["subjects"]:
        print("No subjects recorded for this student.")
        return
    
    print("\n==============================")
    print("        STUDENT REPORT CARD")
    print("==============================")
    print(f"Name: {student['name']}")
    print(f"Roll: {roll}")
    print("------------------------------")
    
    print(f"{'SUBJECT':<12}{'TEST':<8}{'EXAM':<8}{'TOTAL':<8}")
    print("-" * 40)
    
    grand_total = 0
    count = 0
    
    subject_averages = {}
    
    for subject, score in student["subjects"].items():
        test = score["test"]
        exam = score["exam"]
        total = score["total"]
        
        print(f"{subject:<12}{test:<8}{exam:<8}{total:<8}")
        
        subject_averages[subject] = total
        grand_total += total
        count += 1
    
    print("-" * 40)
    print("\nSUBJECT AVERAGES")
    
    for subject, total in subject_averages.items():
        print(f"{subject}: {total:.2f}")
    
    overall_avg = grand_total / count
    grade = calculate_grade(overall_avg)
    
    print("\n------------------------------")
    print(f"OVERALL AVERAGE: {overall_avg:.2f}")
    print(f"GRADE: {grade}")
    print("==============================")
    
#It calculate the overall subject performance from all student/numbers of student offering the subject
def class_performance():
    subject_totals = {}
    subject_counts = {}
    
    # Collect data
    for student in students.values():
        for subject, score in student["subjects"].items():
            total = score["total"]
            
            if subject not in subject_totals:
                subject_totals[subject] = 0
                subject_counts[subject] = 0
            
            subject_totals[subject] += total
            subject_counts[subject] += 1
    
    if not subject_totals:
        print("No subject data available.")
        return
    
    print("\n--- CLASS PERFORMANCE (ALL SUBJECTS) ---")
    
    # Averages
    for subject in subject_totals:
        avg = subject_totals[subject] / subject_counts[subject]
        print(f"{subject}: {avg:.2f}")
    
    #  Student count section 
    print("\n--- NUMBER OF STUDENTS PER SUBJECT ---")
    
    for subject, count in subject_counts.items():
        print(f"{subject}: {count} student(s)")

#Admin debug/view stored data      
def debug():
    print(json.dumps(students, indent=4))
        
#Menu
def menu():
    while True:
        
        print("""
------------GRADE MANAGMENT ---------------
1 Add Students
2 Add/Update Score
3 View All Students
4 Student Report Card
5 Class performance
6 Exit
              """)
        
        choice = input("Choose Options: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            add_score()
        elif choice == "3":
            view_student()
        elif choice == "4":
            report_card()
        elif choice == "5":
            class_performance()
        elif choice == "6":
            save_data(students)
            print("Data saved. Goodbye.")
        elif choice == "7":
            debug()
            break
        else:
            print("Invalid option.")
            
menu()
