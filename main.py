def main():
    name = "Андрей"
    print(name)

    age = 20
    print("Мне", age, "лет")


    print(name * 5, "\n")

    print("Enter your name:\n")
    userName = input()
    # print(userName)
    print("Enter your age:\n")
    userAge = input()
    print("Hello", userName, userAge, "years old")

    userAgeInt = int(userAge)
    print(userAgeInt)
    if userAgeInt > 20:
        print("You are over 20")
    else:
        print("You are under 20")
    if userAgeInt == 20:
        print("You are 20 years old")

    print(userName[::-1])
    print(userName[1:-1])
    print(userName[-3:])
    print(userName[:5])

    nameLen = len(userName)
    print("nameLen =", nameLen)
    ageList = str(age).split()

    print(ageList[0])
    # i = 1
    # str = ""
    # while i < nameLen - 1:
    #     str = str + userName[i]
    #     i = i + 1
    # print(str)



if __name__ == '__main__':
    main()
