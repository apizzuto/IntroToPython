'''
TITLE: Final Exam Question 1a
AUTHOR: Alex Pizzuto
DATE: 5/1/17
DESCRIPTION: Computes Geometric Sums

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 5/1/17

'''

def geometricSum(x, n):
    total = 0
    for item in range(n+1):
        total = total + x**item
    return total

def main():
    print("geometricSum(5,2) returns "+str(geometricSum(5,2)))
    print("geometricSum(3,3) returns "+str(geometricSum(3,3)))
    print("geometricSum(4,2) returns "+str(geometricSum(4,2)))
    print("geometricSum(8,6) returns "+str(geometricSum(8,6)))
    print("geometricSum(2,4) returns "+str(geometricSum(2,4)))

main()
