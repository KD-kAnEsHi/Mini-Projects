# MOCK DATA
import pandas as pd

# MOCK DATAFRAMES
dataframes = {
    "Customers": pd.DataFrame({
        'CustomerID': [1, 2, 3],
        'FirstName': ['Alice', 'Bob', 'Charlie'],
        'LastName': ['Smith', 'Jones', 'Brown'],
        'Email': ['alice@example.com', 'bob@example.com', 'charlie@example.com'],
        'Phone': ['123-456-7890', '234-567-8901', '345-678-9012']
    }),
    "Orders": pd.DataFrame({
        'OrderID': [101, 102, 103],
        'CustomerID': [1, 2, 3],
        'OrderDate': ['2025-01-01', '2025-01-02', '2025-01-03'],
        'TotalAmount': [250.00, 450.50, 120.00]
    }),
    "OrderDetails": pd.DataFrame({
        'OrderDetailID': [1001, 1002, 1003],
        'OrderID': [101, 102, 103],
        'ProductID': [201, 202, 203],
        'Quantity': [2, 1, 4],
        'Price': [50.00, 450.50, 30.00]
    }),
    "Products": pd.DataFrame({
        'ProductID': [201, 202, 203],
        'ProductName': ['Laptop', 'Headphones', 'Mouse'],
        'Category': ['Electronics', 'Accessories', 'Accessories'],
        'Price': [1000.00, 450.50, 30.00]
    })
}

mock_data = {
    "dataframes": dataframes,
    "tables": {
        'Customers': [
            'CustomerID',
            'FirstName',
            'LastName',
            'Email',
            'Phone'
        ],
        'Orders': [
            'OrderID',
            'CustomerID',
            'OrderDate',
            'TotalAmount'
        ],
        'OrderDetails': [
            'OrderDetailID',
            'OrderID',
            'ProductID',
            'Quantity',
            'Price'
        ],
        'Products': [
            'ProductID',
            'ProductName',
            'Category',
            'Price'
        ]
    },
    # Tuples representing relational columns (Table1, Table2, Table1ColumnName, Table2ColumnName)
    "relationships": [
        ('Customers', 'Orders', 'CustomerID', 'CustomerID'),
        ('Orders', 'OrderDetails', 'OrderID', 'OrderID'),
        ('Products', 'OrderDetails', 'ProductID', 'ProductID'),
    ]
}
