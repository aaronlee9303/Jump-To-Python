# Q1fffff
korean = 80
english = 75
mathematics = 55
total = korean + english + mathematics
average = total / 3
print(total, average)

# Q2
def odd_detector(i):
    if i % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

odd_detector(13)

# Q3
pin = "881120-1068234"
yyddmm = pin[:6]
num = pin[7:]
print(yyddmm)
print(num)

# Q4
def sex_detector(s):
    sex_num = int(s[7])
    if sex_num == 1 or sex_num == 3 or sex_num == 5 or sex_num == 7:
        print("Man")
    elif sex_num == 2 or sex_num == 4 or sex_num == 6 or sex_num == 8:
        print("Woman")
    else:
        print("Others")

sex_detector(pin)

# Q5
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

# Q6
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

# Q7
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)

# Q8
a = (1, 2, 3)
a = a + (4,)
print(a)

# Q9
# Answer is 3

# Q10
a = {'A': 90, 'B': 80, 'C': 70}
result = a.pop('B')
print(a)
print(result)

# Q11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)

# Q12
a = b = [1, 2, 3]
a[1] = 4
print(b)
print(id(a))
print(id(b))
