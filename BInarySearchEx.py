pos = -1

def binarySearch(nums, target):
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            globals()['pos'] = mid
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    

nums = [1,2,3,4,5,6,7,8,9,12,12,24,34,54,657,686]
target = 30

if binarySearch(nums, target):
    print("Found at ", pos+1)
else:
    print("Not Found")
