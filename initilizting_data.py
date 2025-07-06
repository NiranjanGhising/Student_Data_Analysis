import numpy as np

def initilize_data():
    subject = np.array(['English', 'Nepali', 'Math', 'Science', 'Social'])
    students = np.array(['Niranjan', 'Mukesh', 'tarkari', 'bujiya', 'Naruto'])
    marks = np.array([
        [81, 78, 80, 60, 63],
        [50, 60, 65, 48, 55],
        [30, 83, 97, 79, 75],
        [99, 55, 60, 48, 30],
        [85, 90, 77, 92, 80]
    ])
    return subject, students, marks