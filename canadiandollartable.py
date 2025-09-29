print(f"{'Canadian Dollar Table' : ^20}")
today = float(input("Enter current value of CAD against USD: "))
yesterday = float(input("Enter yesterday's value of CAD against USD: "))
change = today - yesterday

# Table
print("Date\t\tRate") # \t creates an indent, like the tab key
print("====\t\t====")
print(f"Yesterday\t{yesterday:+.4f}") # .4f formats to 4 decimal places
print(f"Today\t\t{today:+.4f}")
print(f"Change\t\t{change:+.4f}")

# Alternatively
#print("{:>9s} {:>9s}".format("Date", "Rate")) # I honestly don't know
#print("{:>9s} {:>9s}".format("====", "===="))
#print("{:>9s} {:+9.4f}".format("Yesterday", yesterday)) # 4f means four decimal places
#print("{:>9s} {:+9.4f}".format("Today", today))
#print("{:>9s} {:+9.4f}".format("Change", change))