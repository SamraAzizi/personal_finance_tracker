import pandas as pd
import csv
from datetime import datetime


class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMN = ["date", "amount", "category", "description"]
    

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMN)
            df.to_csv(cls.CSV_FILE,index=False)


    @classmethod
    def addEntry(cls, date, amount, category, description):
        new_entry = {
            "date" : date,
            "amount" : amount,
            "category": category,
            "description": description


        }
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            write =csv.DictWriter()


CSV.initialize_csv()






