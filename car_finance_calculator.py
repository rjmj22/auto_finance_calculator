import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns
# Make sure to update the path below as needed
engine = create_engine('sqlite:///D:\\coding\\test\\data.sqlite3')
# Make sure to update the path above as needed
df = pd.read_sql_table('credit', engine)

# getting rid of "NaN"
df = df.dropna()
# Getting csv data to lists

superprime = df.loc[1, :].values.tolist()

prime = df.loc[3, :].values.tolist()

nonprime = df.loc[5, :].values.tolist()

subprime = df.loc[7, :].values.tolist()

deep_subprime = df.loc[9, :].values.tolist()

# function to get rates from credit score and condition

def get_rate(credit_score, condition):
    if condition == 1:
        if credit_score >= 781:
            rate = superprime[2]
        elif credit_score >= 661:
            rate = prime[2]
        elif credit_score >= 601:
            rate = nonprime[2]
        elif credit_score >= 501:
            rate = subprime[2]
        elif credit_score <= 500:
            rate = deep_subprime[2]
    if condition == 2:
        if credit_score >= 781:
            rate = superprime[3]
        elif credit_score >= 661:
            rate = prime[3]
        elif credit_score >= 601:
            rate = nonprime[3]
        elif credit_score >= 501:
            rate = subprime[3]
        elif credit_score <= 500:
            rate = deep_subprime[3]
    return rate

def get_int(principal, rate):
    int3 = (principal * rate * 3)
    int4 = (principal * rate * 4)
    int5 = (principal * rate * 5)
    int6 = (principal * rate * 6)
    int7 = (principal * rate * 7)
    int_rates = (int3, int4, int5, int6, int7)
    return int_rates

def get_years(principal, int_rates):
    three_year = int((principal + int_rates[0]) / 36)
    four_year = int((principal + int_rates[1]) / 48)
    five_year = int((principal + int_rates[2]) / 60)
    six_year = int((principal + int_rates[3]) / 72)
    seven_year = int((principal + int_rates[4]) / 84)
    loan_years = (three_year, four_year, five_year, six_year, seven_year)
    return loan_years

def main():
    print("This is a Auto loan finance calculator. Please enter whole numbers only, no commas needed!")
    # new or used, trade in, down payment, credit score and overall car values:
    while True:
        try:
            condition = float(input("If vehicle is New, enter 1. If used enter 2: "))
            if (condition < 1) or (condition > 2):
                print("Invalid number: try again")
                continue
        except ValueError:
            print('1 or 2 only:')
            continue
        else:
            break
    while True:
        try:
            trade_in = float(input("If you have a trade in enter value, if not put 0: "))
        except ValueError:
            print('Numerics only')
            continue
        else:
            break
    while True:
        try:
            down_payment = float(input("If you have a down payment enter value, if not put 0: "))
        except ValueError:
            print('Numerics only')
            continue
        else:
            break
    while True:
        try:
            credit_score = float(input("Enter credit score number between 300-850: "))
            if (credit_score < 300) or (credit_score > 850):
                print("Invalid number: try again")
                continue
        except ValueError:
            print('Numerics only')
            continue
        else:
            break
    while True:
        try:
            auto_price = float(input("Enter the total price of the vehicle: "))
        except ValueError:
            print('Numerics only')
            continue
        else:
            break

# matching credit score to rate
    get_rate(credit_score, condition)
    rate = get_rate(credit_score, condition)

# figuring our principal and interest rate by year
    principal = (auto_price - (down_payment + trade_in))
    get_int(principal, rate)
    int_rates = get_int(principal, rate)

# getting monthly payments calculations
    get_years(principal, int_rates)
    loan_years = get_years(principal, int_rates)

# Making plot data

# Plot 1 data
    plt.figure(1)
    plot_data1 = {"Months": ["36", "48", "60", "72", "84"],
                 "Amounts": [loan_years[0], loan_years[1], loan_years[2], loan_years[3], loan_years[4]]}
    splot1=sns.barplot(x="Months",y="Amounts",data=plot_data1)
    for bar in splot1.patches:
        splot1.annotate(format(bar.get_height(), '.2f'),
                (bar.get_x() + bar.get_width() / 2,
                 bar.get_height()), ha='center', va='center',
                 size=15, xytext=(0, 8),
                 textcoords='offset points')
    plt.xlabel("Months", size=15)
    plt.ylabel("Monthly payment", size=15)

# Plot 2 data
    plt.figure(2)
    plot_data2 = {"Months": ["36", "48", "60", "72", "84"],
                 "Amounts": [int_rates[0], int_rates[1], int_rates[2], int_rates[3], int_rates[4]]}
    splot2=sns.barplot(x="Months",y="Amounts",data=plot_data2)
    for bar in splot2.patches:
        splot2.annotate(format(bar.get_height(), '.2f'),
                (bar.get_x() + bar.get_width() / 2,
                 bar.get_height()), ha='center', va='center',
                 size=15, xytext=(0, 8),
                 textcoords='offset points')
    plt.xlabel("Months", size=15)
    plt.ylabel("Interest paid", size=15)
    plt.show()

main()