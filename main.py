from initilizting_data import initilize_data 
from Std_data_from_user import user_input
from display_records import display_record

def main():
    subject, students, marks = initilize_data() 
    students,marks = user_input(students,subject,marks) 
    display_record(students,subject,mars)
    print(subject)
    print(students)
    print(marks)

if __name__ == "__main__":  
    main()