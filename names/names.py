import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")

# ---------- TASK TWO -----------
from binary_search_tree import BinarySearchTree
bst = BinarySearchTree(names_1[0])

bst_duplicates = []

for i in range(0, len(names_1)):
    current_name = names_1[i]
    bst.insert(current_name)

for j in range(0,len(names_2)):
    current_name = names_2[j]
    if bst.contains(current_name):
        bst_duplicates.append(current_name)

end_time = time.time()
print (f"{len(bst_duplicates)} duplicates:\n\n{', '.join(bst_duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?

