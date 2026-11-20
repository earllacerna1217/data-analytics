starting_bank_balance = 1000.00
savings_goal = 7500.00
weekly_savings = 350.00

while starting_bank_balance < savings_goal:
    starting_bank_balance += weekly_savings
    print(f"This week my balance increased to: ${starting_bank_balance:.2f}")
    if starting_bank_balance >= savings_goal / 2:
        print(f"Half way there! This week my balance is up to: ${starting_bank_balance:.2f}")
    elif starting_bank_balance < savings_goal / 4 * 3:
        print(f"So close! After treating myself, my balance is up to: ${starting_bank_balance:.2f}")
    else:
        print(f"Goal reached! My balance is now: ${starting_bank_balance:.2f}")