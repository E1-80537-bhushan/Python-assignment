"""6). Concatenate two lists in the following order by using list comprehension
Input:- list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
Output:- [’Hello Dear’, ’Hello Sir’, ’take Dear’, ’take Sir’]"""

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

result = []

for item1 in list1:
    for item2 in list2:
        concatenated = item1 + item2
        result.append(concatenated)

print(result)
