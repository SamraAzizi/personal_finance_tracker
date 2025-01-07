import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_date, get_descriptipn
import matplotlib.pyplot as plt


class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]
    FORMAT = "%d-%m-%Y"

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description,
        }
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully")

    @staticmethod
    def get_transactions(start_date, end_date):
        try:
            # Read the CSV file
            df = pd.read_csv("finance_data.csv")

            # Debugging: Print DataFrame structure
            print("Initial DataFrame:")
            print(df.head())
            print(df.columns)

            # Check if 'data' column exists
            if 'data' not in df.columns:
                raise ValueError("'data' column is missing in the CSV file.")

            # Rename 'data' to 'date' for consistency
            df.rename(columns={'data': 'date'}, inplace=True)

            # Convert 'date' column to datetime
            df['date'] = pd.to_datetime(df['date'], format=CSV.FORMAT, errors='coerce')

            # Drop rows with invalid or missing dates
            df.dropna(subset=['date'], inplace=True)

            # Filter by date range
            start_date = pd.to_datetime(start_date, format=CSV.FORMAT)
            end_date = pd.to_datetime(end_date, format=CSV.FORMAT)
            df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]

            return df

        except FileNotFoundError:
            print("Error: The file 'finance_data.csv' was not found.")
            return pd.DataFrame()
        except Exception as e:
            print(f"An error occurred: {e}")
            return pd.DataFrame()

def add():
    CSV.initialize_csv()
    date = get_date(
        "Enter the date of the transaction (dd-mm-yyyy) or enter for today's date: ",
        allow_default=True,
    )
    amount = get_amount()
    category = get_category()
    description = get_descriptipn()
    CSV.add_entry(date, amount, category, description)

def plot_transactions(df):
    if 'date' not in df.columns:
        print("Error: 'date' column is missing in the DataFrame.")
        return

    # Debugging: Check DataFrame before processing
    print("DataFrame before setting index and plotting:")
    print(df.head())

    # Set 'date' as the index
    df.set_index('date', inplace=True)

    # Separate income and expense
    income_df = df[df["category"] == "Income"].resample("D").sum().reindex(df.index, fill_value=0)
    expense_df = df[df["category"] == "Expense"].resample("D").sum().reindex(df.index, fill_value=0)

    # Debugging: Check resampled data
    print("\nIncome Data:")
    print(income_df.head())
    print("\nExpense Data:")
    print(expense_df.head())

    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(income_df.index, income_df["amount"], label="Income", color="g")
    plt.plot(expense_df.index, expense_df["amount"], label="Expense", color="r")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expense Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()



def main():
    while True:
        print("\n1. Add a new transaction")
        print("2. View transactions and summary within a date range")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add()
        elif choice == "2":
            start_date = get_date("Enter the start date (dd-mm-yyyy): ")
            end_date = get_date("Enter the end date (dd-mm-yyyy): ")
            df = CSV.get_transactions(start_date, end_date)
            if input("Do you want to see a plot? (y/n) ").lower() == "y":
                plot_transactions(df)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Enter 1, 2 or 3.")


if __name__ == "__main__":
    main()