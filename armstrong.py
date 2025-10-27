# armstrong njumber
num = int(input("num: "))
temp = num 
count = 0
while temp>0:
    temp = temp//10
    count += 1
temp = num
sum = 0
while temp > 0:
    digit = temp%10
    sum += digit**count
    temp = temp // 10
if sum == num :
    print("Armstrong")
else:
    print("Not Armstrong")