This project will take input from a user, which is a trade in value if applicable, a down payment from the user if applicable, if the vehicle is new or used and the total amount of the vehicle cost, and give the monthly payment and total interest paid over the loan term.

Got the rates by credit score from:
https://www.nerdwallet.com/article/loans/auto-loans/average-car-loan-interest-rates-by-credit-score

*rates accurate as of 5/29/22

The install requirements are in the requirements.txt
Need to also download data.sqlite3

Will need to change: line 6 "df = pd.read_sql_table('D:/coding/project/data.sqlite3')" to the directory that data.sqlite3 is put into

The selections from the list are:

1st: Read in data from a database.
2nd: Use pandas to clean data
3rd: 5 basic calculations with python And custom functions
4th: 2 graphs
5th: readme

run file: "car_finance_calculator.py"