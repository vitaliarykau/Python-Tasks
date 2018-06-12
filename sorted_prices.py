""" To find the most expensive goods and return a certain
number of entries """

def sorted_prices(limit, data):

    result = sorted(data, key=lambda x: x['price'], reverse=True)

    return result[:limit]


goods = [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "milk", "price": 31},
        {"name": "meat", "price": 15},
        {"name": "orange", "price": 147},
        {"name": "water", "price": 1}
    ]

print(sorted_prices(3, goods))