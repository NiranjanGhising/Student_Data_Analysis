import numpy as np
import matplotlib.pyplot as plt

def cal_correlation(subject, studentArray, marksArray, sub1, sub2):
    subject1Marks = marksArray[:, sub1]
    subject2Marks = marksArray[:, sub2]
    correlation = np.corrcoef(subject1Marks, subject2Marks)[0, 1]
    print("Correlation between", subject[sub1], "and", subject[sub2], ":", correlation)

    # Use scatterplot for correlation
    plt.scatter(subject1Marks, subject2Marks)
    for i, name in enumerate(studentArray):
        plt.text(subject1Marks[i], subject2Marks[i], name, fontsize=8, ha='left')
    plt.xlabel(subject[sub1])
    plt.ylabel(subject[sub2])
    plt.title(f"Marks Correlation: {subject[sub1]} vs {subject[sub2]}")
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.grid(True, linestyle='dotted', alpha=0.6)
    plt.tight_layout()
    plt.show()