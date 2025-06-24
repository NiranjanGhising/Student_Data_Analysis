import numpy as np


def user_input(studentArray,subjectArray,marksArray):


    studentName = input('Student name: ')

    #empty array for adding marks as same length as subject
    marks = np.empty(len(subjectArray), dtype =int)

    # Getting input marks from users, as same as subject length
    for i in range(len(subjectArray)):
        marks[i] = int(input(f'Enter marks for {subjectArray[i]}: '))

    #adding new studnets to studentArray
    studentArray = np.append(studentArray,studentName)
    #adding marks to marksArray
    marksArray = np.vstack((marksArray,marks))

    return studentArray, marksArray