def f(x):
    sq = int(x**0.5)+1
    d = set()

    for i in range(2, sq+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)

    if len(d) > 1:
        if (min(d)+max(d)) % 138 == 0:
            return (min(d)+max(d))


i, count = 800000+1, 0

while count < 5:
    if f(i):
        print(i, f(i))
        count += 1
        
    i += 1
