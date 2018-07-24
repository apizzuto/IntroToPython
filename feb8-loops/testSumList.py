"""Test sumList Exercise"""

def sumList(nums):
    '''Return the sum of the numbers in the list nums.'''
    sum = 0
    for num in nums:
        sum = sum + num
    return sum

def main():
    sum1=sumList([1,2,3,4,5,6])
    sum2=sumList([2,4,2,6,7])
    sum3=sumList([11,52,34,25,73])
    sum4=sumList([])
    print(sum1,sum2,sum3,sum4)

main()
