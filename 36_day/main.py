# Check Leap Year
def is_leap_year(year):
    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    if year % 4 == 0:
        return True

    return False


year = 2024

result = is_leap_year(year)

print("Year:", year)
print("Leap year:", result)