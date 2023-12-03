def Test1(num):
    if len(str(num)) == 6 and str(num)[0] == '6' and str(num)[1] == '6':
        return 1
    return 0


def Test2(num):
    if len(str(num)) == 6 and str(num)[0] == '6':
        return 1
    return 0


def Test3(num):
    if len(str(num)) == 7:
        if str(num)[2] == '6' and str(num)[3] == '6' and str(num)[4] == '6':
            return 1
    return 0


def Test4(num):
    if len(str(num)) == 6:
        if str(num)[2] == '6' and str(num)[5] == '6':
            return 1
    return 0


def Test5(num):
    if len(str(num)) == 10:
        if str(num)[4] == '6' and str(num)[5] == '6':
            return 1
    return 0



for i in range(100000, 1000000):
    for j in range(1000, 10000):
        temp_num1 = i * int(str(j)[3])
        
        
        
        if Test1(temp_num1) == 1:
            temp_num2 = i * int(str(j)[2])
            if Test2(temp_num2) == 1:
                temp_num3 = i * int(str(j)[1])
                if Test3(temp_num3) == 1:
                    temp_num4 = i * int(str(j)[0])
                    if Test4(temp_num4) == 1:
                        final_num = temp_num1
                        final_num += temp_num2 * 10
                        final_num += temp_num3 * 100
                        final_num += temp_num4 * 1000
                        if Test5(final_num) == 1:
                            print(i)
                            print(j)