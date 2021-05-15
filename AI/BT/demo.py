
a=float(input("canh a:"))
b=float(input("canh b:"))
c=float(input("canh c:"))
import math
if a<=0 or b<=0 or c<=0 or a+b<=c or b+c<=a or a+c<=b  :
   print("error")
   
else :
   cv=a+b+c
   p=cv/2
   import math
   dt=math.sqrt(p*(p-a)*(p-b)*(p-c))
   print("Chu vi",round(cv,2))
   print("Dien tich",round(dt,2))
    
