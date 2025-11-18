#!/usr/bin/env python3

import csv
import os

grades = []

file_header = ["Assignment", "Category", "Grade", "Weight"]
file_name = "grades.csv"


total_available_weight = 100
def validate_grade(grade):
    if 0 <= grade <= 100:
        return True
    else:
        return False
    
def is_postive(input_number):

    if input_number > 0:
        return True
    else:
        return False

def is_unique(assignment_name, grades):
    for grade in grades:
        if grade["assignment_name"].lower() == assignment_name.lower():
            return False
    return True

def is_empty(input_character):
    if input_character.strip() != "":
        return False
    else:
        return True
    
while True:
    if total_available_weight == 0:
        print("No more available weight left.")
        break
    
    while True:

        assignment_name = input("enter assignment name:")
        if is_empty(assignment_name):
            print("Assignment name cant be empty.")
        else:
            if is_unique(assignment_name, grades):
                break
            else:
                print("Assignment name must be unique. Enter a different name.")


    
    total_weight_formative = sum(grade["assignment_weight"] for grade in grades if grade["category_name"] == "FA")
    total_weight_summative = sum(grade["assignment_weight"] for grade in grades if grade["category_name"] == "SA")

    while True:
        category_name = input("enter category FA or SA:").upper()
        if category_name in ("FA", "SA"):
            if category_name == "FA":
                total_remaining_weight_category = 60 - total_weight_formative
        
            else:
                total_remaining_weight_category = 40 - total_weight_summative

            if category_name == "FA":
                if total_remaining_weight_category == 0:
                    print("No more available weight left in FA category.")
                    continue
                else:
                    break
            else:
                if total_remaining_weight_category == 0:
                    print("No more available weight left in SA category.")
                    continue
                else:
                    break
        else:
            print("Category must be FA or SA.")
            

        

    while True:
        assignment_grades = float(input("enter grades:"))
        if validate_grade(assignment_grades):
            break
        else:
            print("The grades must be between 0 and 100.")

    print(f"Total remaining weight for {total_remaining_weight_category}")
    print(f"Total available weight {category_name}: {total_available_weight}")
    

    while True:
        assignment_weight = int(input("enter weight:"))
        if is_postive(assignment_weight):
            if assignment_weight > total_available_weight:
                print(f"The weight must not exceed the total available weight")
            else:
                if assignment_weight > total_remaining_weight_category:
                    print(f"The weight must not exceed the remaining weight for {category_name}:")
                else:
                    break
        else:
            print("The weight must be a only a positive number.")

    total_available_weight -= assignment_weight
    weighted_grade = (assignment_grades / 100) * assignment_weight

    grades.append({
        "assignment_name": assignment_name,
        "category_name": category_name,
        "assignment_grades": assignment_grades,
        "assignment_weight": assignment_weight,
        "weighted_grade": weighted_grade
    })

    other_assignments = input("Are there any other assignments? (y or n):").lower()
    if other_assignments == 'y':
        if total_available_weight == 0:
            print(f"There is no weight available left.")
            break
        else:
            continue
    else:
        if total_available_weight > 0:
            print(f"There is still  weight available left. It is {total_available_weight}")
            continue
        else:
            break
    

total_formative = 0
total_summative = 0

for grade in grades:
    if grade["category_name"] == "FA":
        total_formative += grade["weighted_grade"]
    else:
        total_summative += grade["weighted_grade"]

total_grades = total_formative + total_summative

gpa = (total_grades / 100) * 5

if total_formative > total_summative >= 20:
    
    status = "Passed"
    
else:

    status = "Failed"

formative_assignments = [g for g in grades if g["category_name"] == "FA"]
formative_assignments.sort(key=lambda x: x["assignment_weight"], reverse=True)
resubmit = []
checked_weights = set()

for formative_assignment in formative_assignments:

    formative_assignment_weight = formative_assignment["assignment_weight"]
    if  formative_assignment_weight in checked_weights:
        continue
    same_weight = [z for z in formative_assignments if z["assignment_weight"] == formative_assignment_weight]
    to_resubmit = [low_graded_assignment  for low_graded_assignment in same_weight if low_graded_assignment ["assignment_grades"] < 50]

    if to_resubmit:
        resubmit.extend(to_resubmit)
        break

    checked_weights.add(formative_assignment_weight)
if resubmit:
    resubmission = ", ".join(a["assignment_name"] for a in resubmit)
else:
    resubmission = "none"



print(f"""
=================== RESULTS ==========================
      
= Total Formative Grades: {total_formative:.2f} / 60 =
= Total Summative Grades: {total_summative:.2f} / 40 =
= Grades: {total_grades:.2f} / 100                   =
= GPA: {gpa:.4f} / 5                                 =
= Status: {status}                                   =
= Resubmission: {resubmission}                       =

======================================================
""")

if os.path.exists(file_name):
    print(f"{file_name} already exists. Overwiting....")

with open(file_name, mode="w", newline="") as CSVFile:
    writer = csv.DictWriter(CSVFile, fieldnames=file_header)

    writer.writeheader()
    for g in grades:
        writer.writerow({
            "Assignment": g["assignment_name"],
            "Category": g["category_name"],
            "Grade": g["assignment_grades"],
            "Weight": g["assignment_weight"]
        })
print("CSV file generated successfully.")