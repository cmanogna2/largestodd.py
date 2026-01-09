nums = list(map(int, input("Enter sorted numbers: ").split()))
target = int(input("Enter target number: "))

left = 0
right = len(nums) - 1
index = -1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        index = mid
        break
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

print(index)
