products=[["Surface Book Pro", "Microsoft", "Laptop", "Windows10",1699.99,5],
["MacBook","Apple","Laptop","Snow Leopard", 1299.00,3],
["MacBook Pro", "Apple", "Laptop", "Snow Leopard", 1399.99,5],
["Inspiron", "Dell", "Desktop", "Windows 8", 499.99,0]
]
for i in range(len(products)):
    if products[i][5] > 0:
        output = str(products[i]).replace("[" ,"").replace("]", "").replace("'", "")
        print(output)