from random import randint as rd

def userBoolInput():
    valid = False
    while not valid:
        value_str = input("enter 1 for ascending , 0 for descending : ")
        try:
            value = int(value_str)
        except ValueError:
            print("enter 0 or 1")
            continue
        if value < 0 or value > 1:
            print("please enter 0 or 1")
            continue
        valid = True
    return value

def userSizeInput():
    valid = False
    while not valid:
        value_str = input("enter size of list: ")
        try:
            value = int(value_str)
        except ValueError:
            print("enter integers only")
            continue
        if value <= 1:
            print("please enter positive value and greater than 1")
            continue
        valid = True
    return value

def GenerateList(size):
    nums = []
    for i in range(size):
        nums.append(rd(0,100))
    return nums    

def Swap(nums,left,right):
    temp = nums[left]
    nums[left] = nums[right]
    nums[right]=temp

def printList(nums,ascending):
    for i in range(len(nums)):
        if i < len(nums)-1:
            print(nums[i],end =",")
        else:
            print(nums[i],end =" ")
    CheckSortResult(ascending,nums)
    

def partition(nums,left,right,ascending):
    i = left-1
    for j in range(left,right+1):
        if(ascending):
            if nums[j] < nums[right]:
                i+=1
                Swap(nums,i,j)
        else:
            if nums[j] > nums[right]:
                i+=1
                Swap(nums,i,j)
            
    Swap(nums,i+1,right)        
    return i+1

def CheckSortResult(ascending,nums):
    if(ascending):
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                print("the list not sorted")
                return
        print("The list has been sorted in a ascending order.")
    else:
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                print("the list not sorted")
                return
        print("The list has been sorted in a descending order.")
        
    
    
def QuickSort(nums,left,right,ascending):
    if right <=left:
        return
    p = partition(nums,left,right,ascending)
    QuickSort(nums,left,p-1,ascending)
    QuickSort(nums,p+1,right,ascending)
    
size = userSizeInput()
ascending = userBoolInput()
nums = GenerateList(size)
printList(nums,ascending)
QuickSort(nums,0,len(nums)-1,bool(ascending))
printList(nums,ascending)
