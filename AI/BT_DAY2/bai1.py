def is_palindrome(st):
   return (st == st[::-1])
str=input("Nhap 1 chuoi : ")
print(is_palindrome(str))