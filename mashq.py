
Target = int(input("Son kiriting : "))
Num = [2,3,4,5,6,6,7,7,7]

def find_occurrences (num,Target):
    occurrence_count = 0

    for num in Num:
        if num==Target:
            occurrence_count+=1

        return occurrence_count


print(find_occurrences(Num,Target))