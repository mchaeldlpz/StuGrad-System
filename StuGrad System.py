import os
import csv
from colorama import Fore, Style, init

init(autoreset=True)

FILE_NAME = "student_records.csv"

def save_records_to_file(records):
    try:
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Math", "Science", "English"])
            for name, grades in records.items():
                writer.writerow([name, grades[0], grades[1], grades[2]])
        print(Fore.GREEN + "\nRecords saved successfully!")
    except Exception as e:
        print(Fore.RED + f"Error saving records: {e}")

def load_records_from_file():
    records = {}
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  
                for row in reader:
                    records[row[0]] = (int(row[1]), int(row[2]), int(row[3]))
        except Exception as e:
            print(Fore.RED + f"Error loading records: {e}")
    return records

def display_records(records):
    if not records:
        print(Fore.YELLOW + "\nNo records found.")
        return
    print(Fore.CYAN + "\nStudent Records:")
    print("-" * 55)
    print(f"{'Name':<15} {'Math':<10} {'Science':<10} {'English':<10} {'Average':<10}")
    print("-" * 55)
    for name, grades in records.items():
        avg = sum(grades) / 3
        print(Style.BRIGHT + Fore.YELLOW + f"{name:<15} {grades[0]:<10} {grades[1]:<10} {grades[2]:<10} {avg:.2f}")
    print("-" * 55)

def get_valid_grade(subject):
    while True:
        try:
            grade = int(input(Style.BRIGHT + Fore.YELLOW + f"Enter {subject} grade (0-100): "))
            if 0 <= grade <= 100:
                return grade
            else:
                print(Fore.RED + "Grade must be between 0 and 100. Try again.")
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.")

def add_student(records):
    name = input(Style.BRIGHT + Fore.YELLOW + "Enter student name: ")
    math = get_valid_grade("Math")
    science = get_valid_grade("Science")
    english = get_valid_grade("English")
    records[name] = (math, science, english)
    print(Fore.GREEN + f"\n{name} added successfully!")

def update_student(records):
    name = input(Style.BRIGHT + Fore.YELLOW + "Enter student name to update: ")
    if name in records:
        math = get_valid_grade("Math")
        science = get_valid_grade("Science")
        english = get_valid_grade("English")
        records[name] = (math, science, english)
        print(Fore.GREEN + f"\n{name}'s grades updated successfully!")
    else:
        print(Fore.RED + "Student not found.")

def delete_student(records):
    name = input(Style.BRIGHT + Fore.YELLOW + "Enter student name to delete: ")
    if name in records:
        del records[name]
        print(Fore.GREEN + f"\n{name} deleted successfully!")
    else:
        print(Fore.RED + "Student not found.")

def generate_reports(records):
    if not records:
        print(Fore.YELLOW + "\nNo records available for reports.")
        return
    highest = max(records.items(), key=lambda x: sum(x[1]) / 3)
    lowest = min(records.items(), key=lambda x: sum(x[1]) / 3)
    print(Fore.CYAN + "\nReports:")
    print(Fore.GREEN + f"Highest Average: {highest[0]} with {sum(highest[1]) / 3:.2f}")
    print(Fore.RED + f"Lowest Average: {lowest[0]} with {sum(lowest[1]) / 3:.2f}")

def show_pass_fail(records):
    if not records:
        print(Fore.YELLOW + "\nNo records available to evaluate.")
        return
    passing_score = 75
    passed_students = [name for name, grades in records.items() if all(grade >= passing_score for grade in grades)]
    failed_students = [name for name, grades in records.items() if any(grade < passing_score for grade in grades)]
    
    print(Fore.CYAN + "\nPassed Students:")
    if passed_students:
        for student in passed_students:
            print(Fore.GREEN + f"- {student}")
    else:
        print("None")
    
    print(Fore.CYAN + "\nFailed Students:")
    if failed_students:
        for student in failed_students:
            print(Fore.RED + f"- {student}")
    else:
        print("None")

def main():
    records = load_records_from_file()
    while True:
        print(Style.BRIGHT + Fore.YELLOW + "\n=== Student Grading System ===")
        print("1. Display all records")
        print("2. Add a student")
        print("3. Update a student's grades")
        print("4. Delete a student")
        print("5. Show highest and lowest AVG")
        print("6. Show passed and failed students")
        print("7. Save and Exit")
        choice = input(Style.BRIGHT + Fore.YELLOW + "Enter your choice: ")
        if choice == "1":
            display_records(records)
        elif choice == "2":
            add_student(records)
        elif choice == "3":
            update_student(records)
        elif choice == "4":
            delete_student(records)
        elif choice == "5":
            generate_reports(records)
        elif choice == "6":
            show_pass_fail(records)
        elif choice == "7":
            save_records_to_file(records)
            break
        else:
            print(Fore.RED + "Invalid choice. Please pick again.")

if __name__ == "__main__":
    main()
