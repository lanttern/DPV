def readinput(X="number"):
    while True:
        num = raw_input("Enter %s: " % (X))
        num = num.strip()
        if not num.isdigit():
            print ("Bad Input. Please try again..")
            continue
        num = int(num)
        if num < 0:
            print ("Bad Integer input - Please enter positive number")
            continue
        return num


def main():
    num = readinput()
    print ("Input number:", num)


if __name__ == '__main__':
    main()
