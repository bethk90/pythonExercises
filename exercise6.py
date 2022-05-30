count = 0
total = 0

while True:
    sval = input("Enter a number: ")

    if sval == 'Done':
        break

    try:
        fval = float(sval)
    except:
        print("Uh oh bad data")
        continue

    count = count + 1
    total = total + fval
    ave = total/count

print("All done!")
print(f"The total is {total} and the average is {ave}")