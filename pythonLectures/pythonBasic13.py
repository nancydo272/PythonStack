#1.Print 1-255

def print255():
    for x in range(1,256):
        print(x)

# print255()

#2.Print sum 0-255, print integers from 0-255 and which interger print the sum so far
def printSum():
    sum = 0
    for x in range(0, 256, 1):
        print(x)
        sum += x
        print(sum)
    return sum

# printSum()

#3. Find and print Max, given a list, find its largest element
def findMax(list):
    max = list[0]
    for x in range(list[1], len(list)):
        if list[x] > max:
            max = list[x]
        return max

print(findMax([2, 3, 4, 9, 8]))