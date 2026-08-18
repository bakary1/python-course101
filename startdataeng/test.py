customer_data = [
    {"name": "customer_1", "id": 1, "age": 100},
    {"name": "customer_2", "id": 2, "age": 42},
    {"name": "customer_3", "id": 3, "age": 25},
    {"name": "customer_4", "id": 4, "age": 19},
]

for item in customer_data:
    for k, v in item.items():
        print(f"key:{k}: value:{v}")
