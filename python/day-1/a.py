nums = [int(i) for i in open('in.txt')]
print(sum(a > b for a, b in zip(nums[1:], nums)))