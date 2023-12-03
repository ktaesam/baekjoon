

answer = [0] * 3

for i in range(10):
    for j in range(10):
        num1 = (20 + i) * j
        if len(str(num1)) == 3 and str(num1)[1] == '3':
            for k in range(1, 10):
                num2 = (20 + i) * k
                if len(str(num2)) == 2:
                    num3 = num1 + num2 * 10
                    if len(str(num3)) == 3 and str(num3)[1] == '4':
                        answer[0] = i
                        answer[1] = j
                        answer[2] = k

print(answer)
n1 = 20 + answer[0]
n2 = answer[2] * 10 + answer[1]
n3 = n1 * answer[1]
n4 = n1 * answer[2]
n5 = n4 * 10 + n3
print(n1, n2, n3, n4, n5)