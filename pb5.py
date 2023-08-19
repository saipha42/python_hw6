
def reverse(num) :
    num = str(num)[::-1]
    return int(num)

input_num = int(input("Enter an integer : "))
result = reverse(input_num)

print(result)