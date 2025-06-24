import numpy as np

def display_record(studentArray, subjectArray, marksArray):
    # Defensive checks
    if len(subjectArray) != marksArray.shape[1]:
        print("Error: Number of subjects does not match marks per student.")
        print("Subjects:", subjectArray)
        print("Marks shape:", marksArray.shape)
        return

    # calculate total, average, and pass/fail
    totalArray = np.sum(marksArray, axis=1)
    avgArray = np.mean(marksArray, axis=1)
    resultArray = np.where(np.all(marksArray >= 40, axis=1), 'Pass', 'Fail')
    
    # build the header and column widths
    headerArray = np.hstack(('Student/Subject', subjectArray, ['Total', 'Average', 'Result']))
    lengthArray = np.array([max(len(str(name)), 7) for name in headerArray])  # min width 7 chars for clarity
    
    # print header
    header = "|".join(f"{title:<{lengthArray[i]}}" for i, title in enumerate(headerArray))
    print(header)
    
    # print separator
    separator = "+".join(["-" * l for l in lengthArray])
    print(separator)
    
    # print each student's row
    # this stop from getting valueerror: rebound . Even if the studentArray have 5 students and marksArray has 4 rows. This loop goes through each students and their respective marks ONLY as long as they exit.
    for i in range(min(len(studentArray), marksArray.shape[0])): 
        student = studentArray[i]
        row = f"{student :<{lengthArray[0]}}"
        row += ''.join(f"|{mark:<{lengthArray[col+1]}}" for col, mark in enumerate(marksArray[i]))
    # add Total, Average and Pass result for each student
        row += "|" + f"{totalArray[i]:<{lengthArray[-3]}}"   
        row += "|" + f"{avgArray[i]:<{lengthArray[-2]}}" 
        row += "|" + f"{resultArray[i]:<{lengthArray[-1]}}" 
        print(row)
    print(separator)