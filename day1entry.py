def startDayOne():
    with open("input.txt", "r") as input_:
        numbers = []
        for line in input_:
            numbers.append(int(line))
        for n in range(len(numbers)):
            for k in range(len(numbers)):
                if n != k:
                    j = numbers[n] + numbers[k]
                    if j == 2020:
                        print(n," ",k)
                        print(numbers[n]," ", numbers[k])
                        print(numbers[n] * numbers[k])


def startDayOne2():
    with open("input.txt", "r") as input_:
        numbers = []
        for line in input_:
            numbers.append(int(line))
        for n in range(len(numbers)):
            for k in range(len(numbers)):
                for h in range(len(numbers)):
                    if n != k and k != h:
                        j = numbers[n] + numbers[k] + numbers[h]
                        if j == 2020:
                            return numbers[n] * numbers[k] * numbers[h]
