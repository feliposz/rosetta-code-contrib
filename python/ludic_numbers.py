# http://rosettacode.org/wiki/Ludic_numbers

LIMIT = 25000
ludic = [1]
nums = list(range(2, LIMIT))
while len(nums) > 0:
    next = nums[0]
    ludic.append(next)
    #new_nums = []
    #for i in range(len(nums)):
    #    if i % next != 0:
    #        new_nums.append(nums[i])
    #nums = new_nums
    del nums[::next] # <-- Much better!
    
print('Generate and show here the first 25 ludic numbers.')
print(ludic[:25])

print('How many ludic numbers are there less than or equal to 1000?')
print(sum(1 for x in ludic if x <= 1000))

print("Show the 2000..2005'th ludic numbers.")
#print(len(ludic))
print(ludic[2000-1:2005])

print('A triplet is any three numbers x, x + 2, x + 6 where all three numbers are also ludic numbers. Show all triplets of ludic numbers < 250 (Stretch goal)')
print([(x, x+2, x+6) for x in ludic if x+6 < 250 and x+2 in ludic and x+6 in ludic])
