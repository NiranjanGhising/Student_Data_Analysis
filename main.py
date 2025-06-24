from initilizting_data import initilize_data 
from Std_data_from_user import user_input
from display_records import display_record
from Insight_data import insight_datas
from Relation_betw_2_sub import cal_correlation

import numpy as np
def main():
    subject, students, marks = initilize_data() 
    
    while(True):
        print('-'*75)
        try:
            choice = int(input('1. Press 1 to Display Student Results\n2. Press 2 to Add a new Student Record\n3. Press 3 to Display Analyzed Results\n4. Press 4 to Calculate the correlation \n5. Press 5 to Exit: '))
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
                cal_correlation(marks,sub,sub2)

            except:
                print("Enter the Number between (1-5) :")
                continue
        elif(choice == 5):
            break
        else:
            print('Invalid Choice')


if __name__ == "__main__":  
    main()