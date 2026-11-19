
print("====================================")
print("       💸 STOCK SMART ZONE 💸")
print("====================================")
print("Hey Investor! Welcome to your money zone.")
print("Let's see how much your stocks are worth!\n")

# Stock prices
stock_prices = {
    "apple": 180,
    "tesla": 250,
    "google": 150,
    "microsoft": 420,
    "amazon": 190
}

total_investment = 0

print("🔥 AVAILABLE STOCKS 🔥")
print("Apple | Tesla | Google | Microsoft | Amazon")

while True:
    stock = input("\nPick your stock (or type done to finish): ").lower()

    if stock == "done":
        break

    if stock in stock_prices:
        quantity = int(input("How many shares are you grabbing? "))

        if quantity > 0:
            investment = stock_prices[stock] * quantity
            total_investment = total_investment + investment

            print("✨ Nice pick!")
            print("Stock:", stock.capitalize())
            print("Price per share: ₹", stock_prices[stock])
            print("Your investment: ₹", investment)

        else:
            print("⚠️ Quantity must be greater than zero!")

    else:
        print("Oops! That stock isn't on our list. Try again!")

print("\n====================================")
print("          💰 YOUR MONEY REPORT 💰")
print("====================================")
print("Total Investment: ₹", total_investment)
print("Smart moves! Keep learning and investing.")
print("Thanks for hanging out with Stock Smart Zone!")
print("====================================")
