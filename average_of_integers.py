bigger_than_one = False
sum = 0
repeat_flag = True
while repeat_flag:
    N = int(input("Enter the amount of numbers you want to calculate: "))

    if (N > 1):
        bigger_than_one = True

    if bigger_than_one:
        for num in range(1, N+1):
            sum += num
            repeat_flag = False
    else:
        print("Enter a number greater than 1.")
print(f"The average of every integer from 1 to {N} is {sum/N}.")