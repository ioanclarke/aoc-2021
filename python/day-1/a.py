nums = [int(i) for i in open('input.txt').read().split()]
print(sum(a > b for a, b in zip(nums[1:], nums)))