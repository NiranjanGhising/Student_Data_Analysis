import numpy as np



def insight_datas(studentsArray, subjectArray, marksArray):

    #average marks for each subject
    avgSubject = np.mean(marksArray,axis = 0)

    #deviation and variation of marks
    stdSubject = np.std(marksArray, axis = 0)
    varSubject = np.var(marksArray, axis = 0)
    stdSubjects = np.std(marksArray, axis = 1)
    varSubjects = np.var(marksArray, axis = 1)


    #First and last Performing Student

    FirstPerformer = studentsArray[np.argmax(np.sum(marksArray, axis = 1))]
    LastPerformer = studentsArray[np.argmin(np.sum(marksArray, axis = 1))]

    #subject comparision
    easiestSubject = subjectArray[np.argmax(avgSubject)]
    hardestSubject = subjectArray[np.argmin(avgSubject)]

    #over all performance 
    totalAverage = np.mean(marksArray)
    totalStd = np.std(marksArray)
    totalVar = np.var(marksArray)
    #analysis and Visualization Part
    # total number of students
    
    print('Total Number of students: ', len(studentsArray))

    #average Marks for each subject

    print("-----Average Marks-----")
    for i , subject in enumerate(subjectArray):
        print('\t', subject,':',avgSubject[i])

    #deviation and variation of marks 

    print("------------Standard Deviation and Variance per Subject --------------")
    header = np.array(['Subject Name ', 'Standard Deviation', 'Variance'])
    print('|'.join(header))

    #separator line

    sep = "+".join(['-'*len(items) for items in header])
    print(sep)

    for i , student in enumerate(subjectArray):

        row = f"{student:<{len(header[0])}}" + '|' + f"stdSubject[i] : <{len(header[1])}" + '|' f"varStudents[i] :<{len(header[2])}"
        print(row)

    #Standard deviation and Variance
    print('\n Standard Deviation and Variance per Student')
    print('|'.join(header))
    print(sep)

    for i, student in enumerate(studentsArray):
        row = f"{student :<{len(header[0])}}" +'|'+ f"{stdSubject[i] :<{len(header[1])}}" + '|' + f"{varSubject[i] :<{len(header[2])}}"
        print(row)

    #first and last performing students
    print('\n First Student:',FirstPerformer)
    print('\n last Student:',LastPerformer)

    #subject Comparison
    print('\n Easiest Subject', easiestSubject, '\n Hardest Subject : ',hardestSubject)

    #overall Performance 
    print('\n Metrics across all Students and Subjects')
    print(f"Average Marks: {totalAverage}. \n Standard Deviation : {totalStd}. \n Variance : {totalVar}")


    