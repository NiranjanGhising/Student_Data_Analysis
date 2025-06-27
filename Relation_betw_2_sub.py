def cal_correlation(subject, studentArray, marksArray, sub, sub2):
    subject1Marks = marksArray[:, subject1]
    subject2Marks = marksArray[:, subject2]
    
    correlation = np.corrcoef(subject1Marks, subject2Marks)[0, 1]
    print("Correlation between", subject[subject1], "and", subject[subject2], ":", correlation)

    # Plotting scatter plot
    plt.plot(studentArray, subject1Marks, marker='o', label = subject[sub])
    plt.plot(studentArray, subject2Marks, marker='o', label = subject[sub2])
    plt.xlabel('Students')
    plt.ylabel('Marks')
    plt.title('Plot to show correlation')
    plt.legend(bbox_to_anchor=(1, 1))
    plt.ylim(0, 100)
    plt.show()