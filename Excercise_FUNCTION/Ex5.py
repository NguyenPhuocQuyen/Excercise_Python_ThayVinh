def called_discounted(price_orginal, percentage):
    value_percentage = percentage/100
    price_discounted = price_orginal * value_percentage
    return (price_discounted)
price_orginal = int(input("Please enter a price: "))
percentage = int(input("Please enter a percentage: "))
a = called_discounted(price_orginal, percentage)
print(f"Price_discounted is: {a}")

