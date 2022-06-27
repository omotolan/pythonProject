def calculate_interest(principal, rate, number_of_years):
    i = 1
    interest_rate = 0
    while(i <= number_of_years):
        interest_rate += principal * rate
        print(f"{principal} with {rate} is {interest_rate + principal} ")
        i += 1

calculate_interest(1000, 0.05, 5)