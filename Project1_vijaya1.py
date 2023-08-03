nums = input("Enter numbers:").split(",")

for a in nums:

    def check_9(num):

        if len(num) == 1:

            return num

        else:

            sm = 0

            for i in num:

                sm += int(i)

            return check_9(str(sm))

    def check_8(num):

        if len(num) == 1:

            return num

        else:

            new_num = int(num[-2])*2+int(num[-1])

            return check_8(str(new_num))

 

    def check_7(num):

        if len(num) == 1:

            return num

        elif len(num) > 1:

            units = num[-1]

            remaining_num = num[:-1]

            diff = abs(2*int(units) - int(remaining_num))

        return check_7(str(diff))

    def check_4(num):

        if(len(num) == 1) and (num == "4"):

            return True

        else:

            tens_digit = num[-2]

            ones_digit = num[-1]

            if tens_digit in ["2","4","6","8"] and ones_digit in ["0","4","8"]:

                return True

            elif tens_digit in ["1","3","5","7","9"] and ones_digit in ["2","6"]:

                return True

 

    def check_3(num):

        if len(num) == 1:

            return int(num)

        else:

            sm = 0

            for i in num:

                sm += int(i)

            return check_3(str(sm))


    factors = []

    if a[-1] in ["0","2","4","6","8"]:

        factors.append(2)

    if check_3(a) in [3,6,9]:

        factors.append(3)


    if len(a) == 1 and a in ["4","8"]:

        factors.append(4)

    elif len(a) > 1 and a[-2] in ["0","2","4","6","8"] and a[-1] in ["0","4","8"]:

        factors.append(4)

    elif len(a) > 1 and a[-2] in ["1","3","5","7","9"] and a[-1] in ["2","6"]:

        factors.append(4)

 
    if a[-1] in ["0","5"]:

        factors.append(5)


    if 2 in factors and 3 in factors:

        factors.append(6)


    if check_7(a) in ["7","0"]:

        factors.append(7)


    if check_8(a) in ["8","0"]:

        factors.append(8)


    if check_9(a) == "9":

        factors.append(9)

    facts = ",".join(map(str,factors))

    print("{0} is divisible by {1}".format(a,str(facts)))
