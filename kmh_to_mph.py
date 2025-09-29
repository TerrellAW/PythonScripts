print("{:>9s} {:>9s}".format("MPH", "KPH"))
print("{:>9s} {:>9s}".format("====", "===="))
for mph in range(10, 80, 10): # to stop at 70, must put next step number (70 = 80 - 10)
    kph = mph * 1.61
    print(f"{mph} mph\t\t{kph:.0f} kph")
