def is_it_binary(num):
    if num.isdigit():
        temp = int(num)
        while temp > 0:
            if temp % 10 > 1:
                return False
            else:
                temp = int(temp / 10)
        return True
    else:
        return False
def b2d(num):
    num = str(num)
    if is_it_binary(num):
        num = int(num)
        temp = 0
        count = 0
        while num > 0:
            if num%10 == 1:
                
                temp += 2**count
            num = int(num / 10)
            count += 1
        return temp
    else:
        print("not binary")
        return None
def d2b(num):
    if str(num).isdigit():
        num = int(num)
        output = ""
        digit = 0
        while num >= 2**(digit+1):
            digit += 1
        while digit >= 0:
            if num >= 2**digit:
                output += "1"
                num -= 2**digit
            else:
                output += "0"
            digit -= 1
        return output
    else:
        print("Not a number!")
        return ""

def main():
    while True:
        num = raw_input("Enter a number: ")
        output = d2b(num)
        if output:
            print(num + " in binary is " + d2b(num))
        else:
            print("No funny business!")

if __name__ == "__main__":
    main()
