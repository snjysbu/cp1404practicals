import random

# Initial stock price
stock_price = 10.00

# Simulation loop
while 0.01 <= stock_price <= 1000.00:
    # Determine whether the price increases or decreases
    if random.randint(0, 1) == 0:  # 50% chance of decrease
        decrease_percentage = random.uniform(0, 0.05)
        stock_price -= stock_price * decrease_percentage
    else:  # 50% chance of increase
        increase_percentage = random.uniform(0, 0.10)
        stock_price += stock_price * increase_percentage

    # Display the stock price to the nearest cent
    stock_price = round(stock_price, 2)
    print(f"Stock price: ${stock_price}")

# Simulation ends if the price goes below $0.01 or above $1000
