from initilizting_data import initilize_data 
from Std_data_from_user import user_input
from display_records import display_record
from Insight_data import insight_datas
from Relation_betw_2_sub import cal_correlation
from analyse_trend import analyse_trends

import numpy as np
def main():
    subject, students, marks = initilize_data() 
    
    while(True):
        print('-'*75)
        try:
            choice = int(input('1. Press 1 to Display Student Results\n2. Press 2 to Add a new Student Record\n3. Press 3 to Display Analyzed Results\n4. Press 4 to Calculate the correlation \n5. Press 5 to analysis trend over 4 years: \n6.Press 6 to exit: '))
        except ValueError:
            print("Please Enter the Number between (1-5):")
            continue



        if (choice == 1 ):
            display_record(students,subject,marks)
        elif(choice == 2):
            students,marks = user_input(students, subject, marks)
        elif(choice == 3):
            insight_datas(students, subject, marks)
        elif(choice == 4):
            try:

                sub = int(input("enter 1. english, 2.Nepali, 3.Math, 4.Science,5.Social :"))
                sub2= int(input("enter 1. english, 2.Nepali, 3.Math, 4.Science,5.Social :"))
                cal_correlation(subjects, students, marks, sub1, sub2)

            except:
                print("ERROR!!Please,Enter the Number between (1-5) :")
                continue
        elif(choice == 5):
            #random total marks of 4 years
            total_marks = np.array([[382, 298, 364, 292],
                            [390, 305, 380, 298],
                            [410, 320, 392, 310],
                            [375, 290, 368, 280],
                            [375, 290, 368, 280]])
            for index, student in enumerate(students):
                analyse_trends(total_marks, students)

        elif(choice == 6 ):
            break
        else:
            print('Invalid Choice')


if __name__ == "__main__":  
    main()