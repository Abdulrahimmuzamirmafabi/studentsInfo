print('Enter your academic details')
print('\n')
"""An empty dictionary to hold the details of the students"""
student_details = {}
size = int(input('Enter the size of the dictionary: '))
for i in range(size):
    name = str(input('Enter student name: '))
    regNo = str(input('Enter student registration number: '))
    age = int(input('Enter student age: '))
    program = str(input('Enter student program: '))
    year_of_study = int(input('Enter student year of study: '))
    subjects = {}
    for i in range(1):
        subject1 = str(input('Enter first subject: '))
        subject2 = str(input('Enter second subject: '))
        subject3 = str(input('Enter third subject: '))
        subjects['subject1'] = subject1
        subjects['subject2'] = subject2
        subjects['subject3'] = subject3
    scores = {}
    for i in range(1):
         marks1 = int(input('Enter marks for subject1: '))
         marks2 = int(input('Enter marks for subject2: '))
         marks3 = int(input('Enter marks for subject3: '))
         scores['marks1'] = marks1
         scores['marks2'] = marks2
         scores['marks3'] = marks3
    grades = {}
    for i in range(1):
        grade1 = str(input('Enter grade for marks1: '))
        grade2 = str(input('Enter grade for marks2: '))
        grade3 = str(input('Enter grade for marks3: '))
        grades['grade1'] = grade1
        grades['grade2'] = grade2
        grades['grade3'] = grade3        
        student_details[regNo] = {
            'Name' : name,
            'Age' : age,
            'Program' : program,
            'Year Of Study' : year_of_study,
            'Subjects' : subjects,
            'Scores' : scores,
            'Grade' : grades
        }
        # Function to find the maximum and minimum marks
def find_max_min_marks(values):
    max_mark = max(values)
    min_mark = min(values)
    return max_mark, min_mark

# Iterate through student details and calculate max and min marks for each student
for regNo, student in student_details.items():
    max_marks, min_marks = find_max_min_marks(student['Scores'].values())
    print(f"Student: {student['Name']}, Max Marks: {max_marks}, Min Marks: {min_marks}")

print(student_details)