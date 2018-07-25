roman_num = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', "I"]
int_num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]


# roman_and_num_dict = {'M': 1000,
#                       'CM': 900,
#                       'D': 500,
#                       'CD': 400,
#                       'C': 100,
#                       'XC': 90,
#                       'L': 50,
#                       'XL': 40,
#                       'X': 10,
#                       'IX': 9,
#                       'V': 5,
#                       'IV': 4,
#                       'I': 1}


def roman_to_int(num):
    result = 0
    for i in range(len(roman_num)):
        while not num.find(roman_num[i]):  # roman_num1.find(i)==0
            result += int_num[i]
            num = num[len(roman_num[i]):]
    return result


def two_roman_num_diff(num1, num2):
    result = ''
    diff = abs(roman_to_int(num1) - roman_to_int(num2))

    if not diff:  # diff==0
        return 'ZERO'
    else:
        for i in range(len(int_num)):
            while diff >= int_num[i]:
                result += roman_num[i]
                diff -= int_num[i]

    return result


while 1:  # True
    line = input()

    if line is '#':
        break
    else:
        roman_num1, roman_num2 = line.split()
        print(two_roman_num_diff(roman_num1, roman_num2))
