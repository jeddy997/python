import pandas as pd
import matplotlib.pyplot as plt

marks_data = [45, 67, 78, 56, 89, 90, 34, 76, 88, 54,
              69, 73, 81, 47, 92, 60, 71, 84, 58, 77]

def load_marks():
    # Convert list into pandas Series
    marks_series = pd.Series(marks_data)
    return marks_series

def calculate_statistics(marks):
    mean = marks.mean()
    median = marks.median()
    mode = marks.mode()[0]
    std_dev = marks.std()
    variance = marks.var()
    
    return mean, median, mode, std_dev, variance


def generate_charts(marks):
    
    
    plt.figure()
    plt.hist(marks, bins=5)
    plt.title("Histogram of Student Marks")
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.show()
    
    
    plt.figure()
    plt.boxplot(marks)
    plt.title("Boxplot of Student Marks")
    plt.ylabel("Marks")
    plt.show()

def main():
    marks = load_marks()
    
    mean, median, mode, std_dev, variance = calculate_statistics(marks)

    print("===== STUDENT MARKS ANALYSIS =====")
    print("Highest Mark:", marks.max())
    print("Lowest Mark:", marks.min())
    print("Range:", marks.max() - marks.min())
    print("Number of students scoring above 70:", len(marks[marks > 70]))
    
    print("\nCalculated Statistics:")
    print("Mean:", mean)
    print("Median:", median)
    print("Mode:", mode)
    print("Standard Deviation:", std_dev)
    print("Variance:", variance)
    generate_charts(marks)

if __name__ == "__main__":
    main()
