import numpy as np

def insight_datas(studentsArray, subjectArray, marksArray):
    # Average marks for each subject
    avgSubject = np.mean(marksArray, axis=0)

    # Deviation and variation of marks
    stdSubject = np.std(marksArray, axis=0)
    varSubject = np.var(marksArray, axis=0)
    stdStudents = np.std(marksArray, axis=1)
    varStudents = np.var(marksArray, axis=1)

    # First and last performing student
    FirstPerformer = studentsArray[np.argmax(np.sum(marksArray, axis=1))]
    LastPerformer = studentsArray[np.argmin(np.sum(marksArray, axis=1))]

    # Subject comparison
    easiestSubject = subjectArray[np.argmax(avgSubject)]
    hardestSubject = subjectArray[np.argmin(avgSubject)]

    # Overall performance
    totalAverage = np.mean(marksArray)
    totalStd = np.std(marksArray)
    totalVar = np.var(marksArray)

    print('Total Number of students:', len(studentsArray))

    print("-----Average Marks-----")
    for i, subject in enumerate(subjectArray):
        print('\t', subject, ':', avgSubject[i])

    print("------------Standard Deviation and Variance per Subject--------------")
    header = np.array(['Subject Name', 'Standard Deviation', 'Variance'])
    print('|'.join(header))
    sep = '+'.join(['-'*len(items) for items in header])
    print(sep)

    for i, subject in enumerate(subjectArray):
        row = f"{subject:<{len(header[0])}}|{stdSubject[i]:<{len(header[1])}.2f}|{varSubject[i]:<{len(header[2])}.2f}"
        print(row)

    print('\nStandard Deviation and Variance per Student')
    print('|'.join(header))
    print(sep)
    for i, student in enumerate(studentsArray):
        row = f"{student:<{len(header[0])}}|{stdStudents[i]:<{len(header[1])}.2f}|{varStudents[i]:<{len(header[2])}.2f}"
        print(row)

    print('\nFirst Student:', FirstPerformer)
    print('Last Student:', LastPerformer)
    print('\nEasiest Subject:', easiestSubject)
    print('Hardest Subject:', hardestSubject)
    print('\nMetrics across all Students and Subjects')
    print(f"Average Marks: {totalAverage:.2f}\nStandard Deviation: {totalStd:.2f}\nVariance: {totalVar:.2f}")