__author__ = 'Chigozie Nnani, cfnnani@unc.edu, Onyen = cfnnani'

import os

def get_filename(prompt):
    filename = input(prompt)
    while not os.path.exists(filename):
        print("Error: File not found. Please enter a valid filename.")
        filename = input(prompt)
    return filename

def get_output_filename(prompt):
    return input(prompt)

def determine_letter_grade(student_type, grade):
    if student_type == "GRAD":
        if 95 <= grade <= 100:
            return "H"
        elif 80 <= grade < 95:
            return "P"
        elif 70 <= grade < 80:
            return "L"
        else:
            return "F"
    elif student_type == "UNDERGRAD":
        if 90 <= grade <= 100:
            return "A"
        elif 80 <= grade < 90:
            return "B"
        elif 70 <= grade < 80:
            return "C"
        elif 60 <= grade < 70:
            return "D"
        else:
            return "F"
    else:
        return "Invalid student type"

def curve_grade(grade, curve_max):
    return min(100, (grade / curve_max) * 100)

def process_grades(input_file, output_file, curve_max=None):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        lines = infile.readlines()
        for i in range(0, len(lines), 3):
            student_type = lines[i].strip()
            student_name = lines[i+1].strip()
            grade = int(lines[i+2].strip())
            if curve_max:
                grade = curve_grade(grade, curve_max)
            letter_grade = determine_letter_grade(student_type, grade)
            outfile.write(f"{student_name}\n{letter_grade}\n")

def main():
    input_filename = get_filename("Please enter the name of the input data file: ")
    output_filename = get_output_filename("Please enter the name of the output data file: ")
    
    curve_choice = input("Would you like to curve the grades? (Y/N) ").strip().lower()
    curve_max = None
    if curve_choice == 'y':
        curve_max = float(input("Please enter the score that should map to a '100%' grade: "))
    
    process_grades(input_filename, output_filename, curve_max)
    print("All data was successfully processed and saved to the requested output file.")

if __name__ == "__main__":
    main()