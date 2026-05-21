import random
from datetime import datetime

sales = []

for i in range(1, 101):

    sale = {
        "order_id": i,
        "customer_id": random.randint(1, 20),
        "amount": round(random.uniform(50, 500), 2),
        "purchase_date": datetime.now()
    }

    sales.append(sale)

print(sales[:5])