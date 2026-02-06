import numpy as np
import pandas as pd

def load_crime_data(filename: str) -> pd.DataFrame:
    crime_df = pd.read_csv(filename)
    return crime_df

def add_risk_column(crime_df: pd.DataFrame) -> pd.DataFrame:
    crime_df = crime_df.copy()
    high_crime_condition = crime_df["ViolentCrimesPerPop"] >= 0.50
    crime_df["risk"] = np.where(high_crime_condition, "HighCrime", "LowCrime")

    return crime_df

def compute_average_unemployment_by_risk(crime_df: pd.DataFrame) -> pd.DataFrame:
    grouped = crime_df.groupby("risk")
    average_unemployment = grouped["PctUnemployed"].mean()

    return average_unemployment

def main():
    input_filename = "crime.csv"
    crime_df = load_crime_data(input_filename)
    crime_with_risk = add_risk_column(crime_df)
    average_unemployment = compute_average_unemployment_by_risk(crime_with_risk)

    high_crime_unemployment = average_unemployment["HighCrime"]
    low_crime_unemployment = average_unemployment["LowCrime"]

    print(f"Average unemployment (HighCrime): {high_crime_unemployment:.2f}")
    print(f"Average unemployment (LowCrime): {low_crime_unemployment:.2f}")

if __name__ == "__main__":
    main()