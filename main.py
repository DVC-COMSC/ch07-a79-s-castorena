# Sarah Castorena
# SID: 2028049
numbers = [     [99, 11, 66, 86, 55],
               [44, 21, 65, 88, 24],
               [33, 77, 32, 33, 34]]


rnum = len(numbers)
cnum = len(numbers[0])

'''
print ('Sum of rows: ', end=' ')
for i in range(rnum):
	rsum = sum(numbers[i])
	print (rsum, end=' ')
print()
'''
# ******************************
# Make your Code
# ******************************
row_sum=[]
col_sum = []
rsum = 0
for i in range(rnum):
    rsum = sum(numbers[i])
    row_sum.append(rsum)
    max_rowidx = row_sum.index(max(row_sum))
    
for i in range(cnum):
    csum = 0
    for j in range(rnum):
        csum = csum + numbers[j][i]

    col_sum.append(csum)
max_num = max(max(x) for x in numbers)


print('Sum of rows: ', *row_sum, sep = ' ')
print('Sum of Columns: ',*col_sum, sep=' ')  
print('The row that has the greatest sum: ',max_rowidx)      
print('the greatest number: ',max_num)