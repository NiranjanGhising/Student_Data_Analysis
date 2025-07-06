import numpy as np

def display_record(studentArray, subjectArray, marksArray):
        if len(subjectArray) != marksArray.shape[1]:
            print("Error: Number of subjects does not match marks per student.")
            print("Subjects:", subjectArray)
            print("Marks shape:", marksArray.shape)
            return

    # Calculate total, average, and pass/fail
        totalArray = np.sum(marksArray, axis=1)
        avgArray = np.mean(marksArray, axis=1)
        resultArray = np.where(np.all(marksArray >= 40, axis=1), 'Pass', 'Fail')
    
    # Build header and column widths
        headerArray = np.hstack(('Student/Subject', subjectArray, ['Total', 'Average', 'Result']))
        lengthArray = np.array([max(len(str(title)), 7) for title in headerArray])

    # Print header
        header = "|".join(f"{title:<{lengthArray[i]}}" for i, title in enumerate(headerArray))
        print(header)
        separator = "+".join(["-" * l for l in lengthArray])
        print(separator)
    
    # Print each student's row
        for i in range(min(len(studentArray), marksArray.shape[0])): 
            student = studentArray[i]
            row = f"{student:<{lengthArray[0]}}"
            row += ''.join(f"|{marksArray[i][col]:<{lengthArray[col+1]}}" for col in range(marksArray.shape[1]))
            row += "|" + f"{totalArray[i]:<{lengthArray[-3]}}"
            row += "|" + f"{avgArray[i]:<{lengthArray[-2]}.2f}"
            row += "|" + f"{resultArray[i]:<{lengthArray[-1]}}"
            print(row)
        print(separator)