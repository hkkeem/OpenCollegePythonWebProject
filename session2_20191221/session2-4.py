numbers = [1, 2, 3, 4]
numbers_double = []

for a in numbers:
    numbers_double.append(a * 2)

for a in numbers_double:
    print(a)

numbers_double2 = [number * 2 for number in numbers]
print(numbers_double2)

# while보다 for을 더 많이 사용한다.(좀 더 오류를 방지할 수 있다.)