def day2_1():
    with open("inputday2.txt","r") as input_:
        passwords = []
        counter = 0
        for line in input_:
            t = line.split(":")
            t2 = t[0].split()
            passwords.append((t2[0],t2[1],t[1].replace("\n","")))
        for pass_ in passwords:
            total = 0
            for letter in pass_[2]:
                if letter == pass_[1]:
                    total += 1 
            if len(pass_[0].split("-")) > 1:
                t = pass_[0].split("-")
                if total >= int(t[0]) and total <= int(t[1]):
                    counter += 1
            else:
                if total < int(pass_[0]):
                    counter += 1

        return counter

def day2_2():
    with open("inputday2.txt","r") as input_:
        passwords = []
        counter = 0
        for line in input_:
            t = line.split(":")
            t2 = t[0].split()
            passwords.append((t2[0],t2[1],(t[1].replace("\n","")).strip()))
        for pass_ in passwords:
            t = pass_[0].split("-")
            lb = int(t[0])-1
            ub = int(t[1])-1
            if ub < len(pass_[2]):
                if (pass_[2][lb] == pass_[1] and not pass_[2][ub] == pass_[1]) or (pass_[2][ub] == pass_[1] and not pass_[2][lb] == pass_[1]):
                    print(pass_)
                    counter += 1

        return counter

print(day2_2())
