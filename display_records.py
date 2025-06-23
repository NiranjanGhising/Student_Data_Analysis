from Std_data_from_user import user_input

def display_record(studentArray, subjectArray,marksArray):

    #prints the subjects as table header
    header = f"Student/Subject|"
    header += '|'.join(subjectArray)
    print(header)

    #seprates the data , and make header more clean
    sep = '-'* 16 +"*" + "*".join(['-' * len(sub) for sub in subjectArray])
    print(sep)


    for i , student in enumerate(studnetArray):
        row = f"{student: <{16}}"
        row+= ''.join(f"|{mark: <{len(subjectArray[col])}}" for col, mark in enumerate(marksArray[i]))
        print(row)