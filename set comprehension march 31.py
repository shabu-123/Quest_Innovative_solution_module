numbers={1,2,3,4,5,6,7,8,9}
multiple_of_3={i for i in numbers if i%3==0}
print(multiple_of_3)

even_or_odd={'even' if num%2==0 else 'odd' for num in numbers}
print(even_or_odd)

even_or_odd=['even' if num%2==0 else 'odd' for num in numbers]
print(even_or_odd)

check_num={0 if i<5 else 1 for i in numbers}
print(check_num)

check_num=[0 if i<5 else 1 for i in numbers]
print(check_num)

check_num1=[0 if i<5 else 1 if i>5 else 5 for i in numbers]
print(check_num1)





