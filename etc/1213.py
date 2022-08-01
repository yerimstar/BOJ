name = list(input())

count_even = list(set([(n,name.count(n)) for n in name if name.count(n) % 2 == 0 ]))
count_odd = list(set([(n,name.count(n)) for n in name if name.count(n) % 2 != 0 ]))

if len(count_odd) > 1:
    print("I'm Sorry Hansoo")
    exit()

str = ""
if count_odd:
    if count_odd[0][1] > 1:
        count_even.append((count_odd[0][0],count_odd[0][1]-1))

count_even.sort(key = lambda x : x[0])

for alpha in count_even:
    str += alpha[0] * (int(alpha[1]/2))

tmp_str = "".join(reversed(str))

if count_odd:
    str += count_odd[0][0]
str += tmp_str

print(str)