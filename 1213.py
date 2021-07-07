name = list(input())
count_even = list(set([(n,name.count(n)) for n in name if name.count(n) % 2 == 0 ]))
count_odd = list(set([(n,name.count(n)) for n in name if name.count(n) % 2 != 0 ]))
print(count_odd)
print(len(count_odd))

if len(count_odd) > 1:
    print("I'm Sorry Hansoo")
    exit()

count_even.sort(key = lambda x : x[0])
print(count_even)

str = ""
for alpha in count_even:
    str += alpha[0] * int(alpha[1]/2)
    print(str)

if count_odd:
    str += count_odd[0][0] * count_odd[0][1]

count_even.sort(reverse=True)
print(count_even)
for alpha in count_even:
    str += alpha[0] * int(alpha[1]/2)
    print(str)
