#make list 0 -4 [0, 1]
nums = list(range(5)) 
print(nums)

#nums = [0, 1 ,2 , 3, 4]

nums[2:4] #[2,3]  Slice index 2 to 4 (exclusive)
nums[2:] #[2,3,4] everything from index 2 on
nums[:2] #[0,1] everything from beggining to index 2 (exclusive)
nums[:] #all of nums
nums[:-1] #[0, 1, 2, 3] from begging to end (-1) (exclusive)
nums[2:4]  = [8,9] #index 2 and 3 equal (4 not included) to [8,9]

#index numbers
animals = ['cat', 'dog', 'monkey']
#idx refers to index number
for idx, animal in enumerate(animals):
    print(f"{idx + 1}: {animal}")

#add to a list
squares = []
for x in nums:
    squares.append( x ** 2)

#for loop one line
squares = [x **2 for x in nums]
print(squares)

#for and if loop in one line 
even_squares = [x **2 for x in nums if x % 2 == 0]
print(even_squares)

