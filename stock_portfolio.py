stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 400
}

total_investment = 0

number_of_stocks = int(input("How many stocks do you want to enter? "))

for i in range(number_of_stocks):
    stock = input("Enter stock symbol: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stock_prices:
        price = stock_prices[stock]
        investment = price * quantity
        total_investment += investment
        print("Investment for", stock, ":", investment)
    else:
        print("Stock not available.")

print("\nTotal investment:", total_investment)