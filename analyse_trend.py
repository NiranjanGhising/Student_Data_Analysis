import numpy as np
import matplotlib.pyplot as plt

def analyse_trends(total_marks, students):
    years = np.arange(total_marks.shape[1])[::-1]  # number of years (columns), reversed
    for i, student in enumerate(students):
        student_marks = total_marks[i]  # marks for this student (length matches years)
        coefficients = np.polyfit(years, student_marks, deg=1)
        trend = coefficients[0]
        trend_direction = "upward" if trend > 0 else "downward"
        print('The trend of', student, 'is', trend_direction)
        plt.plot(years, student_marks, marker='o', label=student)
    plt.title("Trend of Total Marks for All Students")
    plt.xlabel("Year")
    plt.ylabel("Marks")
    plt.legend(bbox_to_anchor=(1.0, 1.0))
    plt.xticks(years)
    plt.show()