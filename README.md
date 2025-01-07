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

