import pandas as pd

# Đọc file đã xử lý
file_path = "Expanded_Pizza_Sales.xlsx"
df = pd.read_excel(file_path)

# Tạo cột revenue_per_pizza
df['revenue_per_pizza'] = df['total_price'] / df['quantity']

# Tạo cột order_hour
df['order_hour'] = pd.to_datetime(df['order_time'], format='%H:%M:%S').dt.hour

# Lưu file mới
output_path = "Processed_Pizza_Sales_Updated.xlsx"
df.to_excel(output_path, index=False)

print(output_path)
