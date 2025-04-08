import timeit
import random 
import math

# setup with 100 preadded elements for Hash Table and Array 
intList = [random.randint(1, 10000) for _ in range(100)] # Array 
intDict = {key: random.randint(1, 10000) for key in range(100)} # Hash Table 

# This is the setup code for timeit() function , use for extracting the running time 
setupCode = """
import random 
intList = [random.randint(1, 10000) for _ in range(100)]
intDict = {key: random.randint(1, 10000) for key in range(100)} """


# NOTE: Task 1 Look up 
list_lookup = timeit.timeit(
    stmt='9999 in intList',
    setup=setupCode,
    number=10000
)


dict_lookup = timeit.timeit(
    stmt='99 in intDict',
    setup=setupCode,
    number=10000
)

# NOTE: Task 2 Update value 
list_update = timeit.timeit(
    stmt='intList[99] = 1234',
    setup=setupCode,
    number=10000
)

dict_update = timeit.timeit(
    stmt='intDict[99] = 1234',
    setup=setupCode,
    number=10000
)

# NOTE: Task 3 Count occurances of a value 
# def dictCount(data: dict, element: int) -> int: 
#     count =  0 
#     for i in range(len(data)): 
#          if data[i] == element: count += 1 
#     return count
# dict_count = timeit.timeit(
#     stmt='dictCount(intList,1234)',
#     number=10000,
#     globals=globals()
# )

list_count = timeit.timeit(
    stmt='intList.count(1234)',
    setup=setupCode,
    number=10000
)


dict_count = timeit.timeit(
    stmt='list(intDict.values()).count(1234)',
    setup=setupCode,
    number=10000
)

# NOTE: Task 4 Reverse Elements 
list_reverse = timeit.timeit(
    stmt='newList = intList[::-1]',
    setup=setupCode,
    number=10000
)

dict_reverse = timeit.timeit(
    stmt="newDict = {value:key for (key,value) in intDict.items()}",
    setup=setupCode,
    number=10000
)

#NOTE: Task 5 remove last the item  
def popList():
    newList =  [random.randint(1, 10000) for _ in range(100)]
    for _ in range(100):
        newList.pop()
        
def popDict(): 
    newDict = {key:random.randint(1,10000) for key in range(100)}
    for _ in range(100): 
        newDict.popitem()
        
        
list_remove = timeit.timeit(
    popList,
    number=10000
)

dict_remove = timeit.timeit(
    popDict,
    number=10000
) 

# NOTE: Task 6 Find mean  
def listMean(list: list) -> float:
    total = 0
    for i in range(len(list)): 
        total += list[i]
    total /= len(list)
    return total 

def dictMean(dict: dict) -> float: 
    total = 0 
    for value in dict.values():
        total += value
    total /= len(dict)
    return total
    
list_mean = timeit.timeit(
    stmt="listMean(intList)",
    number=10000,
    globals=globals()
)

dict_mean = timeit.timeit(
    stmt="dictMean(intDict)",
    number=10000,
    globals=globals()
)

# NOTE: Task 7 Find Variance
def listVariance(list: list) -> float:
    mean = listMean(list)
    total = 0
    for i in range(len(list)): 
        total += (list[i]-mean) ** 2 
    return total / len(list)

def dictVariance(dict: dict) -> float: 
    mean = dictMean(dict)
    total = 0 
    for value in dict.values():
        total += (value - mean) ** 2 
    return total / len(dict.values())

list_variance = timeit.timeit(
    stmt="listVariance(intList)",
    number= 10000,
    globals=globals()
)
 
dict_variance = timeit.timeit(
    stmt="dictVariance(intDict)",
    number= 10000,
    globals=globals()
)

# NOTE: Task 8 Find Standard Deviation
def listStdDev(data: list) -> float: 
    return math.sqrt(listVariance(data))

def dictStdDev(data: dict) -> float: 
    return math.sqrt(dictVariance(data))

list_stdDev = timeit.timeit(
    stmt="listStdDev(intList)",
    number=10000,
    globals=globals()
)

dict_stdDev = timeit.timeit(
    stmt="dictStdDev(intDict)",
    number=10000,
    globals=globals()
)

# NOTE: Task 9 Group Items with condition 
def dictGroup(data: dict) -> dict: 
    newDict = {i:[] for i in range(10)}
    for num in data: # looks at the key 
        key = data[num] % 10
        newDict[key].append(data[num])
    return newDict

def listGroup(data: list) -> list: 
    newList = [[]*i for i in range(10)]
    for num in data: 
        key = num % 10 
        newList[key].append(num)
    return newList
    
list_group = timeit.timeit(
    stmt="listGroup(intList)",
    number=10000,
    globals=globals()
)

dict_group = timeit.timeit(
    stmt="dictGroup(intDict)", 
    number=10000,
    globals=globals()
)

# NOTE: Task 10 
def listRemoveDup(data: list) -> list: 
    aSet = set() 
    for num in data: 
        if num not in aSet: aSet.add(num)
    return list(aSet)

def dictRemoveDup(data: dict) -> dict: 
    aSet = set() # membership property in set is much faster
    newDict = {}
    for key,value in data.items(): 
        # if data[key] not in aList:  # using list will be much slower, as O(n^2)
        #     aList.append(data[key])
        if value not in aSet: 
            aSet.add(value)
            newDict[key] = value
    # return {i:aList[i] for i in range(len(aList))}
    return newDict

dict_remove_dup = timeit.timeit(
    stmt="dictRemoveDup(intDict)",
    number=10000,
    globals=globals()
)

list_remove_dup = timeit.timeit(
    stmt="listRemoveDup(intList)",
    number=10000,
    globals=globals()
)
      
# Print results
print("Tasks         Hash Table      Array       Diff")
print(f"Lookup         {dict_lookup:.6f}     {list_lookup:.6f}    {(dict_lookup - list_lookup):.6f}   seconds")
print(f"Update         {dict_update:.6f}     {list_update:.6f}    {(dict_update - list_update):.6f}   seconds")
print(f"Count Dup      {dict_count:.6f}     {list_count:.6f}    {(dict_count - list_count):.6f}   seconds")
print(f"Reverse        {dict_reverse:.6f}     {list_reverse:.6f}    {(dict_reverse - list_reverse):.6f}   seconds")
print(f"RemoveLast     {dict_remove:.6f}     {list_remove:.6f}    {(dict_remove - list_remove):.6f}   seconds ")
print(f"Find Mean      {dict_mean:.6f}     {list_mean:.6f}    {(dict_mean - list_mean):.6f}   seconds")
print(f"Find Variance  {dict_variance:.6f}     {list_variance:.6f}    {(dict_variance - list_variance):.6f}   seconds")
print(f"Find StdDev    {dict_stdDev:.6f}     {list_stdDev:.6f}    {(dict_stdDev - list_stdDev):.6f}   seconds")
print(f"GroupItem      {dict_group:.6f}     {list_group:.6f}    {(dict_group - list_group):.6f}   seconds")
print(f"RemoveDup      {dict_remove_dup:.6f}     {list_remove_dup:.6f}    {(dict_remove_dup - list_remove_dup):.6f}   seconds")