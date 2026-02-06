import pandas as pd

def load_student_data(filename: str) -> pd.DataFrame:
    return pd.read_csv(filename)

def add_grade_band_column(student_df: pd.DataFrame) -> pd.DataFrame:
    conditions = [
        student_df["grade"] <= 9,
        (student_df["grade"] >= 10) & (student_df["grade"] <= 14),
        student_df["grade"] >= 15,
    ]
    bands = ["Low", "Medium", "High"]

    student_df = student_df.copy()
    student_df["grade_band"] = pd.cut(
        student_df["grade"],
        bins = [-1, 9, 14, 20],
        labels = ["Low", "Medium", "High"]
    )
    return student_df

def build_grade_band_summary(student_df: pd.DataFrame) -> pd.DataFrame:
    grouped = student_df.groupby("grade_band")

    number_of_students = grouped.size()
    average_absences = grouped["absences"].mean()
    internet_access_percentage = grouped["internet"].mean() * 100

    summary_df = pd.DataFrame({
        "number_of_students": number_of_students,
        "average_absences": average_absences,
        "internet_access_percentage": internet_access_percentage,
    }).reset_index()

    return summary_df

def main():
    input_filename = "student.csv"
    output_filename = "student_bands.csv"

    student_df = load_student_data(input_filename)

    student_with_bands = add_grade_band_column(student_df)

    summary_df = build_grade_band_summary(student_with_bands)

    summary_df.to_csv(output_filename, index=False)

    print(summary_df)

if __name__ == "__main__":
    main()