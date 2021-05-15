row=int(input("Enter the number of rows(columns) : "))
matrix=[]
count=0
for i in range(row):          # A for loop for row entries
    a =[]
    for j in range(row):      # A for loop for column entries
         count+=1
         a.append(count)
    matrix.append(a)
  
#  print the matrix
def print_matrix(matrix):
  for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(matrix[i][j], end = " ")
    print()
# rotate matrix 90
def rotate_matrix_90(matrix,row):
       return [[matrix[i][j] for i in range(row)]  for j in range(row-1,-1,-1)]   

#rotate matrix 180
def rotate_matrix_180(matrix,row):
     return [[matrix[i][j] for j in range(row-1,-1,-1)]  for i in range(row-1,-1,-1)]   
print_matrix(matrix)
print("\nrotate 90:")
print_matrix(rotate_matrix_90(matrix,row))
print("\nrotate 180:")
print_matrix(rotate_matrix_180(matrix,row))
