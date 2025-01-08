# Personal Finance Tracker

A simple Python application for tracking your income and expenses. This project uses a CSV file to store transaction data and allows users to add transactions, view them within a specified date range, and generate a plot showing income and expenses over time.

## Features

1. **Add New Transaction**: Allows users to enter income or expense details.
2. **View Transactions**: Displays transactions within a specified date range and provides a summary of total income, total expenses, and net savings.
3. **Plot Transactions**: Generates a plot visualizing income and expenses over time.
4. **CSV-based Storage**: Stores all transactions in a CSV file, making it easy to manage and export data.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    ```

2. Navigate into the project directory:
    ```bash
    cd your-repo-name
    ```

3. Make sure you have the required dependencies installed. You can install them using `pip`:
    ```bash
    pip install pandas matplotlib
    ```

4. Ensure you have Python 3.x installed.

## Usage

### Initialize the CSV File
The application will automatically create a `finance_data.csv` file if it doesn't exist.

### Add a New Transaction
Run the script and select the option to add a new transaction. You will be prompted to enter:
- Date (default to today's date if not provided)
- Amount
- Category (Income or Expense)
- Description (optional)

### View Transactions and Summary
Select the option to view transactions within a specific date range. You will need to enter the start and end dates (in dd-mm-yyyy format). A summary of total income, total expenses, and net savings will be displayed.

### View a Plot of Transactions
After viewing the transactions, you can choose to see a plot that visualizes income and expenses over time.

### Example

```bash
1. Add a new transaction
2. View transaction and summary within a date range
3. Exit
Enter your choice (1-3): 1
Enter the date of transaction (dd-mm-yyyy) or Enter for today's date: 01-01-2025
Enter the amount: 1000
Enter the category 'I' for Income 'E' for Expense: I
Enter a description (optional): Salary

Entry added successfully
