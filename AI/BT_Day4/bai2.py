inp=input("Nhap day so")
value=[int(x) for x in inp.split(" ")]
outp=value[::]
for i in range(len(value)):
     for j in range(i):
       outp[i]+=value[j]
print(outp) 