import pandas as pd

# Load your CSV file
df = pd.read_csv('Video_Q19_Dataset_CSV_FILE.csv')

# Start building the SQL
sql = """INSERT INTO pizza_delivery (order_id, order_time, expected_delivery, actual_delivery, no_of_pizzas, price)\nVALUES\n"""

# Convert each row into a SQL value tuple
values = []
for _, row in df.iterrows():
    order_id = row['order_id']
    order_time = f"'{row['order_time']}'"
    expected_delivery = f"'{row['expected_delivery']}'"
    actual_delivery = f"'{row['actual_delivery']}'" if pd.notnull(row['actual_delivery']) else "NULL"
    no_of_pizzas = row['no_of_pizzas']
    price = row['price']
    values.append(f"({order_id}, {order_time}, {expected_delivery}, {actual_delivery}, {no_of_pizzas}, {price})")

# Join all values into one SQL statement
sql += ",\n".join(values) + ";"

# Save to file
with open('insert_pizza_delivery.sql', 'w') as f:
    f.write(sql)

print("SQL script generated: insert_pizza_delivery.sql")
