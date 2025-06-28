# TASK_2 
b="abc"
print("Task 2:")

# abc*abc*abc:                 
print(b, b, b, sep='*')

# abc	abc (The separator is a tab):
print(b, b,  sep='\t')

# abcabcabc (Without separator):
print(b, b, b, sep='')

# abc#abc#abc (Stay on the same line):
print(b, end='#')                     
print(b, end='#')
print(b)

# abc (The separator is a new lines):
# abc  
print(b, b, sep='\n')



# TASK_3
print("\nTask 3:")
A = "#\t#\n"    # It's: #       #\n
B = '#'*9 +'\n' # It's: #########\n

# Figure О:
print(B + A*3 + B, sep='')

# Figure Н:
print(A*2 + B + A*2, sep='')
