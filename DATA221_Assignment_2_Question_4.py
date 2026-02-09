"""
Question 4:
Loads `student.csv` into a pandas DataFrame, filters students with `studytime >= 3`,
`internet == 1`, and `absences <= 5`,
writes the result to `high_engagement.csv`, and prints the number of students and their average grade.

"""

import pandas as pd

def load_student_data(filename: str) -> pd.DataFrame:
    return pd.read_csv(filename)

def filter_high_engagement_students(students_df: pd.DataFrame) -> pd.DataFrame:
    has_high_studytime = students_df["studytime"] >= 3
    has_internet_access = students_df["internet"] == 1
    has_low_absences = students_df["absences"] <= 5

    high_engagement_mask = has_high_studytime & has_internet_access & has_low_absences
    high_engagement_students = students_df[high_engagement_mask]
    return high_engagement_students

def main():
    input_filename = "student.csv"
    output_filename = "high_engagement.csv"

    students_df = load_student_data(input_filename)

    high_engagement_students = filter_high_engagement_students(students_df)

    high_engagement_students.to_csv(output_filename, index=False)

    number_of_students = len(high_engagement_students)
    average_grade_of_high_engagement_students = high_engagement_students["grade"].mean()
    print(f"Number of students saved: {number_of_students}")
    print(f"Average grade: {average_grade_of_high_engagement_students:.2f}")

if __name__ == "__main__":
    main()

