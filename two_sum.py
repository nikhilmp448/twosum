
def two_sum(arr , target):
    values = {}

    for index , element in enumerate(arr):
        comp = target - element
        if comp in values:
            return [values[comp],index]
        values[element] = index
    return values

"""
SAMPLE INPUT DATA

arr1 = [2,7,11,15]
target1 = 9

arr2 = [3,2,4]
target2 = 6

arr3 = [3,3]
target3 = 6

"""

List = two_sum(arr1,target1)
print(List)
