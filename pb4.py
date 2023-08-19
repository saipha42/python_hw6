
notes_and_coins = [1000, 500, 100, 50, 20, 10, 5, 2, 1]

def divider(divident, divisor) :
    return int(divident/divisor) , int(divident % divisor)

def money_calculator(amount) :

    result = []
    for divisor in notes_and_coins :
        quotient, remainder = divider(amount, divisor)
        amount = remainder
        result.append(quotient)
    return result


input_money = int(input("Enter an amount of money : "))
result = money_calculator(input_money)
index = 0
while index < len(notes_and_coins) :
    bath_type = "Baht notes"
    if notes_and_coins[index] <= 2 :
        bath_type = "Baht coins"
    if result[index] != 0 :

        print(f"{notes_and_coins[index]}-{bath_type} : {result[index]}")
    index += 1
