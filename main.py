# insertion at End
def ins(ary, element):
    ary.append(element)


arr = [1, 2, 3, 4, 5, 6]
key = 9
n = len(arr)

print("Before insertion: ")
print(arr)

result = ins(arr, key)
print("After insertion: ")
print(arr)
