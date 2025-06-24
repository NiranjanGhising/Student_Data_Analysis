import numpy as np

def cal_correlation(marksArray, subject1, subject2):
    subject1Marks = marksArray[:,subject1]
    subject2Marks = marksArray[:,subject2]

    correlation = np.corrcoef(subject1Marks,subject2Marks)[0,1]
    print(correlation)
    correlation = np.corrcoef(subject2Marks,subject1Marks)[0,1]
    print(correlation)
    
    
