import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_date, get_description

class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMN = ["date", "amount", "category", "description"]
    FORMAT = "%d-%m-%Y"
    

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMN)
            df.to_csv(cls.CSV_FILE,index=False)


    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date" : date,
            "amount" : amount,
            "category": category,
            "description": description


        }
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer =csv.DictWriter(csvfile, fieldnames=cls.COLUMN)
            writer.writerow(new_entry)
        print("Entry added successfully")

    
    @classmethod
    def get_transaction(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)

        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print("not transactions found in the given date range")
        else:
            print(f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}")
            print(filtered_df.to_string(index=False, formatters={"date": lambda x:x.strftime(CSV.FORMAT)}))


            total_income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()
            total_expense = filtered_df[filtered_df["category"] == "Expense"]["amount"].sum()
            print("\nSummary:")
            print(f"Total Income : ${total_income:.2f}")
            print(f"Total expense : ${total_expense:.2f}")
            print(f"Net Savings : ${(total_income - total_expense):.2f}")

        return filtered_df
def add():
    CSV.initialize_csv()
    date = get_date("Enter the date of transaction (dd-mm-yyyy) or Enter for today's date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount , category, description)

CSV.initialize_csv()
CSV.add_entry("20-07-2024",12.,"Income","Salary")


def main():
    while True:
        print("\n1. Add a new  transaction")
        print("2. view transaction and summary within a date range")
        print("3. Exit")
        choice = input("Enter you choice (1-3): ")


        if choice == "1":
            add()

        elif choice == "2":
            start_date = get_date("Enter the start date (dd-mm-yyyy): ")
            end_date = get_date("Enter the end date (dd-mm-yyyy): ")
            CSV.get_transaction(start_date, end_date)
            
        

