markdown
# IBM Data Scientist HackerRank Test

This repository contains my solutions for the **IBM Data Scientist** assessment on HackerRank. The test focused on applying SQL for data analysis and Python for algorithmic problem-solving, using real-world scenarios.

## 📁 Repository Structure

- **`Problem_Statement_1.pdf`** – A finance-focused SQL problem requiring transaction aggregation.
- **`Problem_Statement_2.pdf`** – A Python problem on identifying the most frequent product with a specific tie-breaking rule.
- **`Solution_1.txt`** – SQL query solving Problem 1.
- **`Solution_2.py`** – Python function solving Problem 2.

## 🧠 Problem Overview

### Problem 1: September Account Performance Analytics (SQL)

Write a SQL query to join an `account` and a `transaction` table, calculating key metrics (minimum, maximum, average, and total transaction amount) for each active account in **September 2022**. Results must be sorted by `ibmn`.

- **Key skills**: SQL aggregation (`MIN`, `MAX`, `AVG`, `SUM`), filtering, joining, grouping, rounding.
- **Provided Solution**: See `Solution_1.txt`.

### Problem 2: Most Popular Product (Python)

Given a list of product names, find the product with the highest frequency. In case of a tie, return the lexicographically last product among those with the maximum frequency.

- **Key skills**: Frequency counting, dictionary operations, sorting, list manipulation.
- **Provided Solution**: See `Solution_2.py`.

## 🚀 How to Use

### SQL Solution

1. Open `Solution_1.txt` to view the SQL query.
2. Run the query against your database containing `account` and `transaction` tables.

### Python Solution

1. Ensure you have Python 3 installed.
2. Run the script or import the function:
   ```python
   from solution_2 import solve_product_twist

   products = ["apple", "banana", "cherry", "apple", "cherry", "banana"]
   result = solve_product_twist(products)
   print(result)  # Output: "cherry"
⚠️ Disclaimer

This code is my personal solution to the HackerRank challenge and is shared for educational and portfolio purposes. It is not the official IBM solution, nor is it endorsed by IBM or HackerRank.
