# main.py

import datetime
import json
import os
from sklearn.linear_model import LinearRegression
import numpy as np

DATA_FILE = "expenses.json"

def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2)

def add_expense(expenses, category, amount, date):
    expenses.append({
        "category": category,
        "amount": amount,
        "date": date.isoformat()
    })
    save_expenses(expenses)

def summarize_monthly(expenses):
    summary = {}
    for e in expenses:
        date = datetime.datetime.fromisoformat(e["date"])
        key = f"{date.year}-{date.month:02d}"
        summary.setdefault(key, 0)
        summary[key] += e["amount"]
    return summary

def predict_next_month(expenses):
    monthly = summarize_monthly(expenses)

    if len(monthly) < 2:
        return "Not enough data to predict."

    # Prepare data for prediction
    months = sorted(monthly.keys())
    X = []
    y = []
    for i, m in enumerate(months):
        X.append([i])
        y.append(monthly[m])
    X = np.array(X)
    y = np.array(y)

    model = LinearRegression()
    model.fit(X, y)

    next_month_idx = len(monthly)
    prediction = model.predict(np.array([[next_month_idx]]))[0]
    return max(prediction, 0)  # avoid negative prediction

def main():
    expenses = load_expenses()

    # Add default demo expense
    category = "Food"
    amount = 15.0
    date = datetime.datetime.now()
    
    add_expense(expenses, category, amount, date)
    print(f"Added expense: {category} - ${amount} on {date.date()}")

    monthly_summary = summarize_monthly(expenses)
    print("Monthly total expenses:")
    for month, total in monthly_summary.items():
        print(f"{month}: ${total:.2f}")

    prediction = predict_next_month(expenses)
    print(f"Predicted total expenses for next month: ${prediction:.2f}" if isinstance(prediction, float) else prediction)

if __name__ == "__main__":
    main()
