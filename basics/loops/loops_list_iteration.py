students = ["Harry", "Hermione", "Ron"]

# Direct iteration
for student in students:
    print(student)

# index and value together
for i in range(len(students)):
    print(i, students[i])

# BUG: mutating a list while iterating skips elements
nums = [2, 4, 6, 8, 10]
for n in nums:
    if n % 2 == 0:
        nums.remove(n)
print(nums)  # not [] as expected — demonstrates why this is dangerous

# Correct fix: iterate over a copy
nums2 = [2, 4, 6, 8, 10]
for n in nums2[:]:
    if n % 2 == 0:
        nums2.remove(n)
print(nums2)  # correctly []
