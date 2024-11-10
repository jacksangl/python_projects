import cs50

def main():
    card = []
    while True:
        card = input("Card: ")
        if card.isdigit():
            break
        else:
            pass
    num = [int(x) for x in card]
    length = len(num)
    total = calculate(num, length)
    validate(num, total, length)

def validate(num, total, length):
    if total % 10 == 0:
        if num[0] == 5 and num[1] <= 5 and length == 16:
            print("MASTERCARD")
        elif num[0] == 3 and num[1] == 4 and length == 15:
            print("AMEX")
        elif num[0] == 3 and num[1] == 7 and length == 15:
            print("AMEX")
        elif num[0] == 4 and length == 13:
            print("VISA")
        elif num[0] == 4 and length == 16:
            print("VISA")
        else:
            print("INVALID")
    else:
        print("INVALID")

def calculate(num, length):
    total = 0
    total += num[length-1]
    for i in range(len(num) - 2, -1, -1):
        if length % 2 == 0:
            if i % 2 == 0:
                if num[i]*2 >= 10:
                    num_string = str(num[i]*2)
                    digit_1 = num_string[0]
                    digit_2 = num_string[1]
                    total += int(digit_1)
                    total += int(digit_2)
                else:
                    total += (num[i] * 2)
            else:
                total += num[i]
        else:
            if i % 2 == 1:
                if num[i]*2 >= 10:
                    num_string = str(num[i]*2)
                    digit_1 = num_string[0]
                    digit_2 = num_string[1]
                    total += int(digit_1)
                    total += int(digit_2)
                else:
                    total += (num[i] * 2)
            else:
                total += num[i]
    return total


main()
#print(f"New card num: {num}")
 #   print(f"Total: {total}")
