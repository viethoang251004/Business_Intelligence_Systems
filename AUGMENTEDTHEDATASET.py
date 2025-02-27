# Reimport necessary libraries
import pandas as pd
import random
import numpy as np
from datetime import datetime, timedelta

# Reload the uploaded file
file_path = "Pizza_Sales.xlsx"
data = pd.ExcelFile(file_path)

# Load the content of the first sheet to inspect the data structure
pizza_sales_df = data.parse('pizza_sales')

# Display the first few rows and dataset info
pizza_sales_df.head(), pizza_sales_df.info()

# Helper functions for generating synthetic data
def random_name():
    first_names = ["Alice", "Bob", "Charlie", "Diana", "Edward", "Fiona", "George", "Hannah"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def random_gender():
    return random.choice(["Male", "Female", "Other"])

def random_dob(start_year=1950, end_year=2005):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    return start_date + (end_date - start_date) * random.random()

def random_feedback():
    feedback_list = [
        "Excellent service!", "Good quality food.", "Could be better.", 
        "Service was slow.", "Loved the ambiance.", "Not satisfied.", 
        "Highly recommended!", "Average experience."
    ]
    return random.choice(feedback_list)

def random_feedback_platform():
    platforms = ["Google Review", "Yelp", "Zomato", "Internal Survey"]
    return random.choice(platforms)

def random_feedback_date(order_date):
    return order_date + timedelta(days=random.randint(1, 30))

def random_employee_id():
    return random.randint(1000, 9999)

def random_employee_activity():
    activities = ["Order Taken", "Prepared Food", "Delivered Order", "Customer Service"]
    return random.choice(activities)

# Populate existing rows with synthetic data
rows = pizza_sales_df.shape[0]
pizza_sales_df["customer_name"] = [random_name() for _ in range(rows)]
pizza_sales_df["customer_gender"] = [random_gender() for _ in range(rows)]
pizza_sales_df["customer_dob"] = [random_dob() for _ in range(rows)]
pizza_sales_df["customer_feedback"] = [random_feedback() for _ in range(rows)]
pizza_sales_df["feedback_platform"] = [random_feedback_platform() for _ in range(rows)]
pizza_sales_df["feedback_date"] = [random_feedback_date(order_date) for order_date in pizza_sales_df["order_date"]]
pizza_sales_df["employee_id"] = [random_employee_id() for _ in range(rows)]
pizza_sales_df["employee_activity"] = [random_employee_activity() for _ in range(rows)]

# Generate an additional 48,620 rows
additional_rows = 48620
new_data = pd.DataFrame({
    "order_details_id": [None] * additional_rows,  # Placeholder
    "order_id": [None] * additional_rows,  # Placeholder
    "pizza_id": [random.choice(pizza_sales_df["pizza_id"]) for _ in range(additional_rows)],
    "quantity": [random.randint(1, 5) for _ in range(additional_rows)],
    "order_date": [random.choice(pizza_sales_df["order_date"]) for _ in range(additional_rows)],
    "order_time": [f"{random.randint(10, 23)}:{random.randint(0, 59):02}:{random.randint(0, 59):02}" for _ in range(additional_rows)],
    "unit_price": [random.uniform(10.0, 25.0) for _ in range(additional_rows)],
    "total_price": [random.uniform(15.0, 100.0) for _ in range(additional_rows)],
    "pizza_size": [random.choice(pizza_sales_df["pizza_size"]) for _ in range(additional_rows)],
    "pizza_category": [random.choice(pizza_sales_df["pizza_category"]) for _ in range(additional_rows)],
    "pizza_ingredients": [random.choice(pizza_sales_df["pizza_ingredients"]) for _ in range(additional_rows)],
    "pizza_name": [random.choice(pizza_sales_df["pizza_name"]) for _ in range(additional_rows)],
    "customer_name": [random_name() for _ in range(additional_rows)],
    "customer_gender": [random_gender() for _ in range(additional_rows)],
    "customer_dob": [random_dob() for _ in range(additional_rows)],
    "customer_feedback": [random_feedback() for _ in range(additional_rows)],
    "feedback_platform": [random_feedback_platform() for _ in range(additional_rows)],
    "feedback_date": [random_feedback_date(random.choice(pizza_sales_df["order_date"])) for _ in range(additional_rows)],
    "employee_id": [random_employee_id() for _ in range(additional_rows)],
    "employee_activity": [random_employee_activity() for _ in range(additional_rows)]
})

# Concatenate the new data with the original dataset
expanded_pizza_sales_df = pd.concat([pizza_sales_df, new_data], ignore_index=True)

# # Save the extended dataset to a new file
# output_path = "Expanded_Pizza_Sales.xlsx"
# expanded_pizza_sales_df.to_excel(output_path, index=False)
# print(output_path)

# Remove rows starting from index 48620 onward
cleaned_pizza_sales_df = expanded_pizza_sales_df.iloc[:48620]

# Save the cleaned dataset to a new file
cleaned_output_path = "Expanded_Pizza_Sales.xlsx"
cleaned_pizza_sales_df.to_excel(cleaned_output_path, index=False)

print(cleaned_output_path)
