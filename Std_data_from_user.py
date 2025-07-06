import numpy as np

def user_input(studentArray, subjectArray, marksArray):
    studentName = input('Student name: ')
    marks = np.empty(len(subjectArray), dtype=int)

    for i in range(len(subjectArray)):
        while True:
            try:
                value = int(input(f'Enter marks for {subjectArray[i]}: '))
                if 0 <= value <= 100:
                    marks[i] = value
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid integer for marks.")

    # Add new student and corresponding marks
    studentArray = np.append(studentArray, studentName)
    marksArray = np.vstack((marksArray, marks))

    return studentArray, marksArray