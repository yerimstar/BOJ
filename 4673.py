numbers = [i for i in range(1,10001)]
no_self_num = []
for number in numbers:
        a = number//1000
        b = (number-a*1000)//100
        c = (number-a*1000-b*100)//10
        d = number-a*1000-b*100-c*10
        x = number+a+b+c+d
        if x > 10000:
            pass
        else:
            no_self_num.append(number+a+b+c+d)
sort_difference = sorted(set(numbers).difference(set(no_self_num)))
for d in sort_difference:
    print(d)