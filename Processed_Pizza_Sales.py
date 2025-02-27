import pandas as pd

# Đọc dữ liệu từ file
df = pd.read_excel("Processed_Pizza_Sales_Updated.xlsx")

# Chuyển đổi cột order_date và feedback_date sang chỉ ngày tháng năm
df['order_date'] = pd.to_datetime(df['order_date']).dt.date
df['feedback_date'] = pd.to_datetime(df['feedback_date']).dt.date

# Lưu lại để kiểm tra kết quả
print(df[['order_date', 'feedback_date']].head())

# Lưu lại file mới (nếu cần)
df.to_excel("Processed_Pizza_Sales.xlsx", index=False)
