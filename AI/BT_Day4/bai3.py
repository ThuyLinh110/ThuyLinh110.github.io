import math
def is_palindrome(n):
  n1=n
  pal=0
  while(n!=0):
     pal=pal*10+ n%10
     n=n//10
  return (n1==pal) and (round(n1)==n1)
  
def is_super_palindrome(x):
    return (is_palindrome(x)) and (is_palindrome(math.sqrt(x)))
left=int(input("left: "))
right=int(input("right: "))
for i in range(left,right):
    if is_super_palindrome(i):
      print(i,end=" ")