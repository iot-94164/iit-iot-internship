def overlapping(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

list1 = input("Enter elements of first list : ")
list2 = input("Enter elements of second list : ")

result = overlapping(list1, list2)

print(result)
