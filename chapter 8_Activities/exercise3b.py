# Step 1: Create the list
MYLIST = ["SAUDI", "UAE", "QATAR", "KUWAIT"]

# Step 2: Print MYLIST
print("Original List:", MYLIST)

# Step 3: Print MYLIST in reverse order
print("Reversed List:", MYLIST[::-1])

# Step 4: Print length of MYLIST
print("Length of List:", len(MYLIST))

# Step 5: Add OMAN using append()
MYLIST.append("OMAN")
print("After adding OMAN:", MYLIST)

index = MYLIST.index("QATAR")
MYLIST.pop(index)
print("After removing QATAR:", MYLIST)

# Step 7: Sort the list
MYLIST.sort()
print("Sorted List:", MYLIST)