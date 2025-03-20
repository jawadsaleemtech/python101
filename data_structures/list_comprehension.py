nums = [10,20,30,40,50]

n2 = [n for n in nums if n >=30]
print(n2)


nums = [10,20,30,40,50]
n3 = [n *2 for n in nums]
print(n3)



nums1 = [10,20,30,40,50]
nums2 = [11,22,33,44,55]

nums3 = [[n1,n2] for n1 in nums1 for n2 in nums2 if n1 + n2 > 50 ]
print(nums3)

nums4 = [n1 + n2 for n1 in nums1 for n2 in nums2  ]
print(nums4)



nums = [1, 2, 3, 4, 5]
result = [x * x for x in nums if x % 2 == 0]
print(result)

