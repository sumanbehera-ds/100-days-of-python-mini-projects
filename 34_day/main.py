# Calculate Simple Interest
def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100

    total_amount = principal + interest

    return interest, total_amount


p = 10000
r = 5
t = 2

interest, amount = simple_interest(p, r, t)

print("Interest:", interest)
print("Total Amount:", amount)