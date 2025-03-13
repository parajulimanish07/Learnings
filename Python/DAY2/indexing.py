# indexing = accessing elements of a sequence using an index [].
# [start:end:step] 
#start = starting index 
#end = ending index
#step = how many elements to skip

credit_number = "1234-5678-9012-3456"

# print(credit_number[0]) # 1

# print(credit_number[:4])

# print(credit_number[5:9])

# print(credit_number[5:])


# print(credit_number[::2]) # 135790246

# print(credit_number[::-1]) # 6543-2109-8765-4321

credit_number = credit_number[::-1]

print(credit_number) # 3456