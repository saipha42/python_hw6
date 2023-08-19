

base_num = [
    "one", "two", "three", "four", "five", 
    "six", "seven", "eight", "nine", "ten"
]

eleven_to_nineteen = [
    "eleven", "twelfth", "thirteen", "fourteen",
    "fifteen", "sixteen", "seventeen", "eighteen", "ninteen"
]

decimal_num = [
    "twenty", "thirty", "fourty", "fifty",
    "sixty", "seventy", "eighty", "ninety"
]

def extract_digit(num) :
     
    digit_one = int(str(num)[0])
    digit_two = int(str(num)[1])

    if num >= 100 :
         digit_three = int(str(num)[2])
         return digit_one, digit_two, digit_three
    return digit_one, digit_two

def convert_one_to_two_digit(num) :

    text = ""
    base_offset = 1
    dicimal_offset = 2

    if num == 0 :

        text = "zero"
    if num <= 10 and num > 0:
    
        text = base_num[num - base_offset]
    elif num > 10 and num < 20 :

            _, digit_two = extract_digit(num)
            text = f"{eleven_to_nineteen[digit_two - base_offset]}"
    elif num >= 20 and num <= 99 :
    
        digit_one, digit_two = extract_digit(num)

        if digit_two == 0 :
            text = f"{decimal_num[digit_one - dicimal_offset]}"
        else :
            text = f"{decimal_num[digit_one - dicimal_offset]}-{base_num[digit_two - 1]}"
    return text



def num_to_word(num) :

    if num > 999 :
        return "I don't know"
    
    if num >=0 and num < 100 :
        return convert_one_to_two_digit(num)
    
    text= None

    base_offset = 1
    digit_one, digit_two, digit_three = extract_digit(num)

    if digit_two ==0 and digit_three == 0 :
            
        text = f"{base_num[digit_one - base_offset]} hundred"
    else :
        rest_digit = int(str(digit_two) + str(digit_three))
        text = f"{base_num[digit_one - base_offset]} hundred and {convert_one_to_two_digit(rest_digit)} "
    return text


input_number = eval(input("Enter a number between 0 and 999 : "))

print(num_to_word(input_number))