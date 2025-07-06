from initilizting_data import initilize_data
from Std_data_from_user import user_input
from display_records import display_record
from Insight_data import insight_datas
from Relation_betw_2_sub import cal_correlation
from analyse_trend import analyse_trends

import numpy as np

def main():
    subject, students, marks = initilize_data()

    while True:
        print('-' * 75)
        try:
            choice = int(input(
                '1. Display Student Results\n'
                '2. Add a New Student Record\n'
                '3. Display Analyzed Results\n'
                '4. Calculate the Correlation Between Two Subjects\n'
                '5. Analyze Trend Over 4 Years\n'
                '6. Exit\n'
                'Enter your choice (1-6): '
            ))
        except ValueError:
            print("Please enter a number from 1 to 6.")
            continue

        if choice == 1:
            display_record(students, subject, marks)
        elif choice == 2:
            students, marks = user_input(students, subject, marks)
        elif choice == 3:
            insight_datas(students, subject, marks)
        elif choice == 4:
            try:
                sub1 = int(input("Enter subject 1 (1. English, 2. Nepali, 3. Math, 4. Science, 5. Social): ")) - 1
                sub2 = int(input("Enter subject 2 (1. English, 2. Nepali, 3. Math, 4. Science, 5. Social): ")) - 1
                if 0 <= sub1 < len(subject) and 0 <= sub2 < len(subject):
                    cal_correlation(subject, students, marks, sub1, sub2)
                else:
                    print("Subjects should be numbers between 1 and 5.")
            except Exception:
                print("ERROR! Please enter valid numbers between 1-5.")
        elif choice == 5:
            total_marks = np.array([
                [382, 298, 364, 292],
                [390, 305, 380, 298],
                [410, 320, 392, 310],
                [375, 290, 368, 280],
                [375, 290, 368, 280]
            ])
            analyse_trends(total_marks, students)
        elif choice == 6:
            break
        else:
            print('Invalid Choice')

if __name__ == "__main__":
    main()