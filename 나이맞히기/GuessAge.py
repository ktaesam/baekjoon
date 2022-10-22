def Guess(target, candid):
    global cnt

    guess = (candid[-1] - candid[0]) / 2
    cnt += 1

    if len(candid) == 1:
        cnt -= 1
        return
    elif guess > target:
        return Guess(target, candid[:len(candid) // 2])
    else:
        return Guess(target, candid[len(candid) // 2:])


age_list = [i for i in range(20,36)]
max_cnt = 0
for age in age_list:
    cnt = 0
    Guess(age, age_list)

    max_cnt = max(max_cnt, cnt)

print(max_cnt)