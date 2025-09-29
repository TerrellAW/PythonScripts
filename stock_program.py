# Greeting
print("Welcome to the Stock Value Calculator Program!")
# Input for purchasing stocks
stock_name = str(input("Enter stock's name: "))

shares_bought = float(input("Enter the total number of purchased shares: "))

if shares_bought <= 0:
    exit("Error: Number of purchased shares should be > 0")

price_bought = float(input("Enter the dollar amount paid per purchased share: "))

if price_bought <= 0:
    exit("Error: Price of shares should be > 0")

total_purchase = shares_bought * price_bought

# Input for selling stocks   
shares_sold = float(input("Enter the total number of sold shares: "))

if shares_sold <= 0:
    exit("Error: Number of sold shares should be > 0")

if shares_sold > shares_bought:
    exit("Error: Number of sold shares can't exceed bought shares")

price_sold = float(input("Enter the dollar amount paid per sold share: "))

if price_sold <= 0:
    exit("Error: Price of shares should be > 0")

total_sold = shares_sold * price_sold

# Commissions

comm_no = 0

comm_low = 50

comm_high = 100

# Purchase Commission

if shares_bought < 1000:
    purchase_comm = comm_high

else:
    purchase_comm = comm_no

# Sale Commission

if shares_sold < 1000:
    sold_comm = comm_high

elif 1000 <= shares_sold < 2000:
    sold_comm = comm_low

else:
    sold_comm = comm_no

# Purchasing report
print("Purchasing Report")
print(f"Stock Name: {stock_name}")
print(f"Total Purchase Amount: ${total_purchase:.1f}")
print(f"Purchase Commission: ${purchase_comm}")
print(f"Total Sold Amount: ${total_sold:.1f}")
print(f"Sold Commission: ${sold_comm}")

# Profit
