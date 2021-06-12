# Happy Numbers in List Up to 500.

hnum = list()  # Happy_Numbers_List
num = list()   # Happy_Numbers_Count
s = 0          # Sum_Square
ln = 0         # Last_Number

for i in range(500):
    ln = i
    num.clear()                 # Happy_Numbers_Count Clear
    while True:
        if len(num) != 0:
            if num[-1] == 1:    # If Sum_Square = 1 (stop)
                hnum.append(i)
                break

        for n in str(ln):       # Loop for Sum_Square
            s += int(n)**2
        
        if s in num:            # If The Looped Terms (stop)
            break
        else:                   # Else Happy_Numbers_Count
            num.append(s)
        
        s = 0                   # Sum_Square Clear
        ln = num[-1]            # New Last Number

print("\n")
print("=" * 40)
print(f"{'HAPPY NUMBERS':^40}")
print("=" * 40)
print("\n")
for i in hnum:
    print(i, end = ", ")
