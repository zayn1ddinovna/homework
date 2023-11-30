nums = [5,8,2,6,4,0,-2]
n = len(nums)
for i in range(n):
    for j in range(n - i -1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(nums)
#Algoritm_1

num1 = int(input("Qiymat kiriting : "))
num2 = int(input("Qiymat kiriting : "))
num3 = int(input("Qiymat kiriting : "))
numbers = [num1+num2+num3]
print(f"{numbers}")

task
massiv = [1,2,3]
a = 0
for num in massiv:
    a+=num
print(f" Son yig'indisi {a}")

taask
a = int(input("Son:"))
b = int(input("Son:"))
if a ==b:
    s=a,b ** 2
    print("True")
    print(f"{a} sonlar yig'indisi {a}")
else:
    print("False")

2task
Target = int(input("Son kiriting : "))
Num = [2,3,4,5,6,6,7,7,7]

def find_occurrences (num,Target):
    occurrence_count = 0

    for num in Num:
        if num==Target:
            occurrence_count+=1

        return occurrence_count


print(find_occurrences(Num,Target))

num = int (input("Son kiriting : "))

def find_square(num,square):
    if num ** 0.5 == square:
        return True
    else:
        return False

print(find_square(num,square:5))